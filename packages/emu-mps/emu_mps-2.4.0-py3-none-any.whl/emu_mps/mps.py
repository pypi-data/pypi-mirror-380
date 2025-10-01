from __future__ import annotations

import math
from collections import Counter
from typing import List, Optional, Sequence, TypeVar, Mapping

import torch

from pulser.backend.state import State, Eigenstate
from emu_base import DEVICE_COUNT, apply_measurement_errors
from emu_mps import MPSConfig
from emu_mps.algebra import add_factors, scale_factors
from emu_mps.utils import (
    assign_devices,
    truncate_impl,
    tensor_trace,
    n_operator,
)

ArgScalarType = TypeVar("ArgScalarType")


class MPS(State[complex, torch.Tensor]):
    """
    Matrix Product State, aka tensor train.

    Each tensor has 3 dimensions ordered as such: (left bond, site, right bond).

    Only qubits are supported.
    """

    def __init__(
        self,
        factors: List[torch.Tensor],
        /,
        *,
        orthogonality_center: Optional[int] = None,
        config: Optional[MPSConfig] = None,
        num_gpus_to_use: Optional[int] = DEVICE_COUNT,
        eigenstates: Sequence[Eigenstate] = ("r", "g"),
    ):
        """
        This constructor creates a MPS directly from a list of tensors. It is for internal use only.

        Args:
            factors: the tensors for each site
                WARNING: for efficiency in a lot of use cases, this list of tensors
                IS NOT DEEP-COPIED. Therefore, the new MPS object is not necessarily
                the exclusive owner of the list and its tensors. As a consequence,
                beware of potential external modifications affecting the list or the tensors.
                You are responsible for deciding whether to pass its own exclusive copy
                of the data to this constructor, or some shared objects.
            orthogonality_center: the orthogonality center of the MPS, or None (in which case
                it will be orthogonalized when needed)
            config: the emu-mps config object passed to the run method
            num_gpus_to_use: distribute the factors over this many GPUs
                0=all factors to cpu, None=keep the existing device assignment.
        """
        super().__init__(eigenstates=eigenstates)
        self.config = config if config is not None else MPSConfig()
        assert all(
            factors[i - 1].shape[2] == factors[i].shape[0] for i in range(1, len(factors))
        ), "The dimensions of consecutive tensors should match"
        assert (
            factors[0].shape[0] == 1 and factors[-1].shape[2] == 1
        ), "The dimension of the left (right) link of the first (last) tensor should be 1"

        self.factors = factors
        self.num_sites = len(factors)
        assert self.num_sites > 1  # otherwise, do state vector

        assert (orthogonality_center is None) or (
            0 <= orthogonality_center < self.num_sites
        ), "Invalid orthogonality center provided"
        self.orthogonality_center = orthogonality_center

        if num_gpus_to_use is not None:
            assign_devices(self.factors, min(DEVICE_COUNT, num_gpus_to_use))

    @property
    def n_qudits(self) -> int:
        """The number of qudits in the state."""
        return self.num_sites

    @classmethod
    def make(
        cls,
        num_sites: int,
        config: Optional[MPSConfig] = None,
        num_gpus_to_use: int = DEVICE_COUNT,
        eigenstates: Sequence[Eigenstate] = ["0", "1"],
    ) -> MPS:
        """
        Returns a MPS in ground state |000..0>.

        Args:
            num_sites: the number of qubits
            config: the MPSConfig
            num_gpus_to_use: distribute the factors over this many GPUs
                0=all factors to cpu
        """
        config = config if config is not None else MPSConfig()

        if num_sites <= 1:
            raise ValueError("For 1 qubit states, do state vector")

        return cls(
            [
                torch.tensor([[[1.0], [0.0]]], dtype=torch.complex128)
                for _ in range(num_sites)
            ],
            config=config,
            num_gpus_to_use=num_gpus_to_use,
            orthogonality_center=0,  # Arbitrary: every qubit is an orthogonality center.
            eigenstates=eigenstates,
        )

    def __repr__(self) -> str:
        result = "["
        for fac in self.factors:
            result += repr(fac)
            result += ", "
        result += "]"
        return result

    def orthogonalize(self, desired_orthogonality_center: int = 0) -> int:
        """
        Orthogonalize the state on the given orthogonality center.

        Returns the new orthogonality center index as an integer,
        this is convenient for type-checking purposes.
        """
        assert (
            0 <= desired_orthogonality_center < self.num_sites
        ), f"Cannot move orthogonality center to nonexistent qubit #{desired_orthogonality_center}"

        lr_swipe_start = (
            self.orthogonality_center if self.orthogonality_center is not None else 0
        )

        for i in range(lr_swipe_start, desired_orthogonality_center):
            q, r = torch.linalg.qr(self.factors[i].view(-1, self.factors[i].shape[2]))
            self.factors[i] = q.view(self.factors[i].shape[0], 2, -1)
            self.factors[i + 1] = torch.tensordot(
                r.to(self.factors[i + 1].device), self.factors[i + 1], dims=1
            )

        rl_swipe_start = (
            self.orthogonality_center
            if self.orthogonality_center is not None
            else (self.num_sites - 1)
        )

        for i in range(rl_swipe_start, desired_orthogonality_center, -1):
            q, r = torch.linalg.qr(
                self.factors[i].contiguous().view(self.factors[i].shape[0], -1).mT,
            )
            self.factors[i] = q.mT.view(-1, 2, self.factors[i].shape[2])
            self.factors[i - 1] = torch.tensordot(
                self.factors[i - 1], r.to(self.factors[i - 1].device), ([2], [1])
            )

        self.orthogonality_center = desired_orthogonality_center

        return desired_orthogonality_center

    def truncate(self) -> None:
        """
        SVD based truncation of the state. Puts the orthogonality center at the first qubit.
        Calls orthogonalize on the last qubit, and then sweeps a series of SVDs right-left.
        Uses self.config for determining accuracy.
        An in-place operation.
        """
        self.orthogonalize(self.num_sites - 1)
        truncate_impl(self.factors, config=self.config)
        self.orthogonality_center = 0

    def get_max_bond_dim(self) -> int:
        """
        Return the max bond dimension of this MPS.

        Returns:
            the largest bond dimension in the state
        """
        return max((x.shape[2] for x in self.factors), default=0)

    def sample(
        self,
        *,
        num_shots: int,
        one_state: Eigenstate | None = None,
        p_false_pos: float = 0.0,
        p_false_neg: float = 0.0,
    ) -> Counter[str]:
        """
        Samples bitstrings, taking into account the specified error rates.

        Args:
            num_shots: how many bitstrings to sample
            p_false_pos: the rate at which a 0 is read as a 1
            p_false_neg: the rate at which a 1 is read as a 0

        Returns:
            the measured bitstrings, by count
        """
        assert one_state in {None, "r", "1"}
        self.orthogonalize(0)

        rnd_matrix = torch.rand(num_shots, self.num_sites).to(self.factors[0].device)

        bitstrings: Counter[str] = Counter()

        # Shots are performed in batches.
        # Larger max_batch_size is faster but uses more memory.
        max_batch_size = 32

        shots_done = 0
        while shots_done < num_shots:
            batch_size = min(max_batch_size, num_shots - shots_done)
            batched_accumulator = torch.ones(
                batch_size, 1, dtype=torch.complex128, device=self.factors[0].device
            )

            batch_outcomes = torch.empty(batch_size, self.num_sites, dtype=torch.bool)

            for qubit, factor in enumerate(self.factors):
                batched_accumulator = torch.tensordot(
                    batched_accumulator.to(factor.device), factor, dims=1
                )

                # Probability of measuring qubit == 0 for each shot in the batch
                probas = (
                    torch.linalg.vector_norm(batched_accumulator[:, 0, :], dim=1) ** 2
                )

                outcomes = (
                    rnd_matrix[shots_done : shots_done + batch_size, qubit].to(
                        factor.device
                    )
                    > probas
                )
                batch_outcomes[:, qubit] = outcomes

                # Batch collapse qubit
                tmp = torch.stack((~outcomes, outcomes), dim=1).to(dtype=torch.complex128)

                batched_accumulator = (
                    torch.tensordot(batched_accumulator, tmp, dims=([1], [1]))
                    .diagonal(dim1=0, dim2=2)
                    .transpose(1, 0)
                )
                batched_accumulator /= torch.sqrt(
                    (~outcomes) * probas + outcomes * (1 - probas)
                ).unsqueeze(1)

            shots_done += batch_size

            for outcome in batch_outcomes:
                bitstrings.update(["".join("0" if x == 0 else "1" for x in outcome)])

        if p_false_neg > 0 or p_false_pos > 0:
            bitstrings = apply_measurement_errors(
                bitstrings,
                p_false_pos=p_false_pos,
                p_false_neg=p_false_neg,
            )
        return bitstrings

    def norm(self) -> torch.Tensor:
        """Computes the norm of the MPS."""
        orthogonality_center = (
            self.orthogonality_center
            if self.orthogonality_center is not None
            else self.orthogonalize(0)
        )
        # the torch.norm function is not properly typed.
        return self.factors[orthogonality_center].norm().cpu()  # type: ignore[no-any-return]

    def inner(self, other: State) -> torch.Tensor:
        """
        Compute the inner product between this state and other.
        Note that self is the left state in the inner product,
        so this function is linear in other, and anti-linear in self

        Args:
            other: the other state

        Returns:
            inner product
        """
        assert isinstance(other, MPS), "Other state also needs to be an MPS"
        assert (
            self.num_sites == other.num_sites
        ), "States do not have the same number of sites"

        acc = torch.ones(1, 1, dtype=self.factors[0].dtype, device=self.factors[0].device)

        for i in range(self.num_sites):
            acc = acc.to(self.factors[i].device)
            acc = torch.tensordot(acc, other.factors[i].to(acc.device), dims=1)
            acc = torch.tensordot(self.factors[i].conj(), acc, dims=([0, 1], [0, 1]))

        return acc.view(1)[0].cpu()

    def overlap(self, other: State, /) -> torch.Tensor:
        """
        Compute the overlap of this state and other. This is defined as
        $|\\langle self | other \\rangle |^2$
        """
        return torch.abs(self.inner(other)) ** 2  # type: ignore[no-any-return]

    def entanglement_entropy(self, mps_site: int) -> torch.Tensor:
        """
        Returns
        the Von Neumann entanglement entropy of the state `mps` at the bond between sites b and b+1
        S = -Σᵢsᵢ² log(sᵢ²)),
        where sᵢ are the singular values at the chosen bond.
        """
        self.orthogonalize(mps_site)

        # perform svd on reshaped matrix at site b
        matrix = self.factors[mps_site].flatten(end_dim=1)
        s = torch.linalg.svdvals(matrix)

        s_e = torch.Tensor(torch.special.entr(s**2))
        s_e = torch.sum(s_e)

        self.orthogonalize(0)
        return s_e.cpu()

    def get_memory_footprint(self) -> float:
        """
        Returns the number of MBs of memory occupied to store the state

        Returns:
            the memory in MBs
        """
        return (  # type: ignore[no-any-return]
            sum(factor.element_size() * factor.numel() for factor in self.factors) * 1e-6
        )

    def __add__(self, other: State) -> MPS:
        """
        Returns the sum of two MPSs, computed with a direct algorithm.
        The resulting MPS is orthogonalized on the first site and truncated
        up to `self.config.precision`.

        Args:
            other: the other state

        Returns:
            the summed state
        """
        assert isinstance(other, MPS), "Other state also needs to be an MPS"
        assert (
            self.eigenstates == other.eigenstates
        ), f"`Other` state has basis {other.eigenstates} != {self.eigenstates}"
        new_tt = add_factors(self.factors, other.factors)
        result = MPS(
            new_tt,
            config=self.config,
            num_gpus_to_use=None,
            orthogonality_center=None,  # Orthogonality is lost.
            eigenstates=self.eigenstates,
        )
        result.truncate()
        return result

    def __rmul__(self, scalar: complex) -> MPS:
        """
        Multiply an MPS by a scalar.

        Args:
            scalar: the scale factor

        Returns:
            the scaled MPS
        """
        which = (
            self.orthogonality_center
            if self.orthogonality_center is not None
            else 0  # No need to orthogonalize for scaling.
        )
        factors = scale_factors(self.factors, scalar, which=which)
        return MPS(
            factors,
            config=self.config,
            num_gpus_to_use=None,
            orthogonality_center=self.orthogonality_center,
            eigenstates=self.eigenstates,
        )

    def __imul__(self, scalar: complex) -> MPS:
        return self.__rmul__(scalar)

    @classmethod
    def _from_state_amplitudes(
        cls,
        *,
        eigenstates: Sequence[Eigenstate],
        n_qudits: int,
        amplitudes: Mapping[str, complex],
    ) -> tuple[MPS, Mapping[str, complex]]:
        """
        See the base class.

        Args:
            basis: A tuple containing the basis states (e.g., ('r', 'g')).
            nqubits: the number of qubits.
            strings: A dictionary mapping state strings to complex or floats amplitudes.

        Returns:
            The resulting MPS representation of the state.s
        """
        basis = set(eigenstates)
        if basis == {"r", "g"}:
            one = "r"
        elif basis == {"0", "1"}:
            one = "1"
        else:
            raise ValueError("Unsupported basis provided")

        basis_0 = torch.tensor([[[1.0], [0.0]]], dtype=torch.complex128)  # ground state
        basis_1 = torch.tensor([[[0.0], [1.0]]], dtype=torch.complex128)  # excited state

        accum_mps = MPS(
            [torch.zeros((1, 2, 1), dtype=torch.complex128)] * n_qudits,
            orthogonality_center=0,
            eigenstates=eigenstates,
        )

        for state, amplitude in amplitudes.items():
            factors = [basis_1 if ch == one else basis_0 for ch in state]
            accum_mps += amplitude * MPS(factors, eigenstates=eigenstates)
        norm = accum_mps.norm()
        if not math.isclose(1.0, norm, rel_tol=1e-5, abs_tol=0.0):
            print("\nThe state is not normalized, normalizing it for you.")
            accum_mps *= 1 / norm

        return accum_mps, amplitudes

    def expect_batch(self, single_qubit_operators: torch.Tensor) -> torch.Tensor:
        """
        Computes expectation values for each qubit and each single qubit operator in
        the batched input tensor.

        Returns a tensor T such that T[q, i] is the expectation value for qubit #q
        and operator single_qubit_operators[i].
        """
        orthogonality_center = (
            self.orthogonality_center
            if self.orthogonality_center is not None
            else self.orthogonalize(0)
        )

        result = torch.zeros(
            self.num_sites, single_qubit_operators.shape[0], dtype=torch.complex128
        )

        center_factor = self.factors[orthogonality_center]
        for qubit_index in range(orthogonality_center, self.num_sites):
            temp = torch.tensordot(center_factor.conj(), center_factor, ([0, 2], [0, 2]))

            result[qubit_index] = torch.tensordot(
                single_qubit_operators.to(temp.device), temp, dims=2
            )

            if qubit_index < self.num_sites - 1:
                _, r = torch.linalg.qr(center_factor.view(-1, center_factor.shape[2]))
                center_factor = torch.tensordot(
                    r, self.factors[qubit_index + 1].to(r.device), dims=1
                )

        center_factor = self.factors[orthogonality_center]
        for qubit_index in range(orthogonality_center - 1, -1, -1):
            _, r = torch.linalg.qr(
                center_factor.view(center_factor.shape[0], -1).mT,
            )
            center_factor = torch.tensordot(
                self.factors[qubit_index],
                r.to(self.factors[qubit_index].device),
                ([2], [1]),
            )

            temp = torch.tensordot(center_factor.conj(), center_factor, ([0, 2], [0, 2]))

            result[qubit_index] = torch.tensordot(
                single_qubit_operators.to(temp.device), temp, dims=2
            )

        return result

    def apply(self, qubit_index: int, single_qubit_operator: torch.Tensor) -> None:
        """
        Apply given single qubit operator to qubit qubit_index, leaving the MPS
        orthogonalized on that qubit.
        """
        self.orthogonalize(qubit_index)

        self.factors[qubit_index] = (
            single_qubit_operator.to(self.factors[qubit_index].device)
            @ self.factors[qubit_index]
        )

    def get_correlation_matrix(
        self, *, operator: torch.Tensor = n_operator
    ) -> torch.Tensor:
        """
        Efficiently compute the symmetric correlation matrix
            C_ij = <self|operator_i operator_j|self>
        in basis ("r", "g").

        Args:
            operator: a 2x2 Torch tensor to use

        Returns:
            the corresponding correlation matrix
        """
        assert operator.shape == (2, 2)

        result = torch.zeros(self.num_sites, self.num_sites, dtype=torch.complex128)

        for left in range(0, self.num_sites):
            self.orthogonalize(left)
            accumulator = torch.tensordot(
                self.factors[left],
                operator.to(self.factors[left].device),
                dims=([1], [0]),
            )
            accumulator = torch.tensordot(
                accumulator, self.factors[left].conj(), dims=([0, 2], [0, 1])
            )
            result[left, left] = accumulator.trace().item().real
            for right in range(left + 1, self.num_sites):
                partial = torch.tensordot(
                    accumulator.to(self.factors[right].device),
                    self.factors[right],
                    dims=([0], [0]),
                )
                partial = torch.tensordot(
                    partial, self.factors[right].conj(), dims=([0], [0])
                )

                result[left, right] = (
                    torch.tensordot(
                        partial, operator.to(partial.device), dims=([0, 2], [0, 1])
                    )
                    .trace()
                    .item()
                    .real
                )
                result[right, left] = result[left, right]
                accumulator = tensor_trace(partial, 0, 2)

        return result


def inner(left: MPS, right: MPS) -> torch.Tensor:
    """
    Wrapper around MPS.inner.

    Args:
        left: the anti-linear argument
        right: the linear argument

    Returns:
        the inner product
    """
    return left.inner(right)
