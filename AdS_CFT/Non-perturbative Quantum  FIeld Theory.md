Non-perturbative QFT is defined based on:
- Hilbert space: on every slice of constant time we define a Hilbert space of quantum states. Because the time translation operator is unitary, they are actually equivalent.
- Local operators: they (anti-)commute with every other local operator inserted at a different point $\vec x'\neq\vec x$ on the same time slice,
  $$
	  [\phi_a(x),\phi_b(x')]=0,~~~x'^0=x^0,~~~\vec x'\neq\vec x. 
   $$
  This condition is often expressed in Lorentz-invariant way,
  $$
	  [\phi_a(x),\phi_b(x')]=0,~~~(x-x')^2>0, 
   $$
   which is then called *micro-causality condition*.
   
- Symmetries: the energy-momentum tensor is a local operator, from which one can get conserved charges $P^\mu$, $M^{\mu\nu}$. In a *generic QFT*, the energy-momentum tensor needs not be traceless, *so* the charges $D$, $K^\mu$ cannot be considered.
In analogy to $P^\mu_\odot=i\partial^\mu\phi(x)$, we require
$$
[P^\mu,\phi(x)]=i\partial^\mu\phi(x).
$$
This is solved by
$$
\phi(x)=e^{-ix\cdot P}\phi(0)e^{ix\cdot P},
$$
so $P^\mu$ generate translations that act as unitary transformations.
For Lorentz transformation, we can choose to decompose local operators inserted at $x=0$ into irreducible representations $\phi^a(0)$ of the Lorentz group, where $a$ stands for a collection of Lorentz indices. In this case:
$$
[M^{\mu\nu},\phi^a(0)]=i{(S^{\mu\nu})^a}_b\phi^b(0),
$$
where the matrix ${(S^{\mu\nu})^a}_b$ satisfies the Lorentz algebra. For a scalar operator, $S^{\mu\nu}=0$, for a vector operator with a Lorentz index it is given by
$$
{(S^{\mu\nu})^a}_b=\delta^\mu_a\delta^\nu_b-\delta^\mu_b\delta^\nu_a.
$$
Combining with Poincare algebra for $P^\mu$ and $M^{\mu\nu}$, one gets:
$$
[M^{\mu\nu},\phi^a(x)]=
-i(x^\mu\partial^\nu-x^\nu\partial^\mu)\phi^a(x)+
i{(S^{\mu\nu})^a}_b\phi^b(0).
$$
Note that $P^\mu$ and $M^{\mu\nu}$ are good operators in Hilbert space, but they are not local, but their commutator with any local operator is again local. Later in CFT, it will be also valid for $D$ and $K^\mu$.
- The Hilbert space includes a vacuum state that is invariant under Poincare (and later also conformal) transformations:
  $$
	  P^\mu|0\rangle=M^{\mu\nu}|0\rangle=0.
   $$
   It is assumed to have the lowest energy. Other states are created by acting with local operators on this state. It is also assumed that if the four momentum is timelike, then for the Fourier transform of a local operator:
   $$
   \tilde\phi(p)|0\rangle=0,~~~p^0<|\vec p|,
   $$
   which generalized to the product of multiple operators,
   $$
   \tilde\phi_1(p_1)...\tilde\phi_n(p_n)|0\rangle=0,~~~
   p^0_1+...+p^0_n<|\vec p_1+...+\vec p_n|,
   $$
   and called the **spectral condition**.