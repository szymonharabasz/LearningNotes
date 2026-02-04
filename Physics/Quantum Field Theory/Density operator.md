For a pure state, represented by $|\psi\rangle$, it is defined as:
$$
\rho=|\phi\rangle\langle\psi|.
$$
It projects to one-dimensional subspace of a Hilbert space.

A mixed state is a statistical mixture of pure states that do not interfere with each other. They can be described by a density operator:
$$
\rho=\sum_i\lambda_i|\psi\rangle\langle\psi_i|.
$$
The operator is self-adjoint, positive-definite, has $\mathrm{Tr}(\rho)=1$ and $\mathrm{Tr}(\rho^2)\leq 1$, where equality holds only for a pure state. It satisfies the von Neumann equation:
$$
i\hbar\frac{\partial\rho}{\partial t}=[H,\rho].
$$
Expectation value of an observable is:
$$
\langle A\rangle=\sum_i\lambda_i\langle\psi_i|A|\psi_i\rangle=\mathrm{Tr}(A\rho).
$$