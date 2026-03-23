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
#### WIghtman funcions
They are VEV of products of local operators,
$$
\langle 0|\phi_1(x_1)...\phi_n(x_n)|0\rangle.
$$
Their symmetry is expressed in Ward identities. For a conserved charge that annihilates vacuum, $G|0\rangle=0$ (which could be $P^\mu$ or $M^{\mu\nu}$),
$$
\begin{split}
\langle 0|[G,phi_1(x_1)]\phi_2(x_2)...\phi_n(x_n)|0\rangle+&\\
\langle 0|\phi_1(x_1)[G,\phi_2(x_2)]...\phi_n(x_n)|0\rangle+&\\
...+\\
\langle 0|phi_1(x_1)\phi_2(x_2)...[G,\phi_n(x_n)]|0\rangle =& 0.
\end{split}
$$
Examples are:
$$
\partial_\mu\langle 0|\phi(x)|0\rangle=0,
$$
$$
\left(\frac{\partial}{\partial x^\mu}+\frac{\partial}{\partial x^\mu}\right)
\langle0|\phi(x)\phi(y)|0\rangle=0.
$$
which establishes that this correlator depends only on $x-y$ and not $x+y$,
$$
\langle0|\phi(x)\phi(y)|0\rangle=W(x-y).
$$
Taking a Fourier transform,
$$
(p^\mu+q^\mu)\langle0|\tilde\phi(p)\tilde\phi(q)|0\rangle=0,
$$
which gives
$$
\langle0|\tilde\phi(p)\tilde\phi(q)|0\rangle=(2\pi)^d\delta^d(p+q)\tilde W(q),
$$
where $\tilde W$ is indeed a Fourier transform of $W$.
By Lorentz invariance and requiring the momentum to be timelike, we can get:
$$
\tilde W(q)=2\pi\theta(q^0-|\vec q|)\rho(-q^2).
$$
Note that Wightman functions are actually **tempered distributions**. In order for the norm to be positive *for any test function*, the function $\rho$ must be positive,
$$
\rho(\mu^2)\geq0,~~~\forall\mu^2>0.
$$
It is called **spectral density**.
In the standard QFT it is often used in the Källen-Lehmann representation of the time-ordered 2-point function (which, by the way, is not a tempered distribution),
$$
\langle\phi(x\phi(y))\rangle_T=
\int\frac{d^dk}{(2\pi)^d}\int_0^\infty d\mu^2e^{ik\cdot(x-y)}
\frac{i}{-k^2-\mu^2+i\epsilon}\rho(\mu^2).
$$
For a massive scalar field,
$$
\rho(\mu^2)=\delta(\mu^2-m^2),
$$
and the above expression gives the familiar massive propagator.
#### Scaling symmetry in QFT
The symmetry amounts to assuming the existence of a conserved charge $D$. Since it commutes with $M^{\mu\nu}$, any local operator inserted at 0 can be decomposed into irreducible representations of the group of scale transformations, which then means, that the commutator is
$$
[D,\phi(0)]=-i\Delta\phi(0),
$$
where $\Delta$ is the **scaling dimension** of the operator $\phi$. One can obtain at any other point
$$
[D,\phi(x)]=-i(x^\mu\partial_\mu+\Delta)\phi(x),
$$
the scaling dimension coincides with the mass dimension of the *free field*. Using this commutator, one gets new Ward identities
$$
\left(x^\mu\frac{\partial}{\partial x^\mu}+
y^\mu\frac{\partial}{\partial y^\mu}+
2\Delta\right)
\langle0|phi(x)\phi(y)|0\rangle=0,
$$
equivalently,
$$
\left(
x^\mu\frac{\partial}{\partial x^\mu}+2\Delta
\right)
W(x)=0.
$$
After Fourier transformation,
$$
\left(
-q^\mu\frac{\partial}{\partial q^\mu}+2\Delta-d
\right)
\tilde W(q)=0,
$$
Which is solved by
$$
\tilde W(q)=2\pi C\theta(q^0-|\vec q|)(-q^2)^{\delta-d/2}
$$
and implies the spectral density
$$
\rho(\mu^2=C(\mu^2)^{\Delta-d/2}.
$$
The time-ordered function takes the form
$$
\langle\phi(x)\phi(y)\rangle_T=
\frac{i\pi C}{\sin[\pi(\Delta-\frac{c}{2})]}
\int\frac{d^dk}{(2\pi)^d}e^{ik\cdot(x-y)}
(k^2-ie)^{\Delta-d/2}.
$$
It looks like an integral of a propagator raised to a non-integral power. This happens in the perturbation theory when the $\beta$-function has a non-trivial fixed point. The renormalized 2-point function obtains then logarithms what can be resummed into a power,
$$
-\frac{i}{q^2}[1+\gamma\log(-q^2)+...]\approx-i(q^2)^{1+\gamma},
$$
where $\gamma$ is the **anomalous dimension** of field $\phi$.
In this case, the scaling dimension of the renormalized field becomes
$$
\Delta=\frac{d-2}{2}+\gamma.
$$
In the limit $\gamma\rightarrow0$, one recovers the free propagator, but the factor in front of the integral diverges, unless $C\propto\gamma$. The spectral density becomes
$$
\rho(\mu^2)\propto\gamma(\mu^2)^{-1+\gamma}
\xrightarrow[\gamma\rightarrow0]{} \delta(\mu^2).
$$
The so-called **unitarity bound**,
$$
\Delta\geq\frac{d-2}{d}
$$
must be satisfied, otherwise the spectral density would be non-integrable in the limit $\mu^2\rightarrow0$.
For any operator that *saturates* it, one has
$$
\langle0|\tilde\phi(p)\tilde\phi(x)|0\rangle\propto\delta(q^2),
$$
meaning
$$
q^2\langle0|\tilde\phi(p)\tilde\phi(x)|0\rangle=0,
$$
or in position space
$$
\langle0|\phi(x)\partial^2q(y)|0\rangle=0,
$$
which implies
$$
\partial^2\phi(x)=0.
$$
So the theory in which $\Delta=\frac{d-2}{2}$ is a free field theory.
Using inverse Fourier transform, one can write
$$
W(x)=\frac{C'}{[-(c^0+i\epsilon)^2+\vec x^2]^\Delta}
$$
with
$$
C'=\frac{(4\pi)^{d/2}}{2^{2\Delta}\Gamma(\Delta)\Gamma(\Delta-\frac{d-2}{2})}C,
$$
and the limit $\epsilon\rightarrow0_+$ is understood in a sense that
$$
W(x)=\frac{C'}{|x^2|^\Delta}\times\left\{
\begin{split}
&e^{-i\pi\Delta},&x^0<-|\vec x|,\\
&1, &-|\vec x| < x^0 < |\vec x|,\\
&e^{i\pi\Delta},&x^0>|\vec x|.
\end{split}
\right.
$$

For one-point functions the constant VEV was consistent with the Poincare symmetry. But in this case, the commutator $[D,\phi(x)]$ requires that $\Delta=0$ which violates the unitarity bound. Therefore, *one-point VEV must vanish in a scale-invariant theory*.

#### Special conformal symmetry
$K^\mu$ does not commute with $M^{\mu\nu}$, so $\phi$ cannot be split into irreducible representation of the Poincare group at $x=0$. One can calculate that if $\phi$ has scaling dimension $\Delta$, then $[K^\mu,\phi]$ has scaling dimension $\Delta-1$,
$$
[D,[K^\mu,\phi(0)]]=-i(\Delta-1)[K^\mu,\phi(0)].
$$
Similarly, $[P^\mu,\phi]$ has scaling dimension $\Delta+1$,
$$
[D,[P^\mu,\phi(0)]]=-i(\Delta+1)[P^\mu,\phi(0)],
$$
which is consistent with the fact that $\partial^\mu$ has mass dimension $+1$. 

Lowering the scaling dimension indefinitely would violate the unitarity bound, so one has to assume that at some point $K^\mu$ annihilates the operator, so there must exist a local operator such that
$$
[K^\mu,\phi(0)]=0.
$$
This is called a **primary operator**. Any other operator obtained by the action of $P^\mu$ is called **descendant**. Thus the primary operator cannot be obtained by acting with derivative on some other operator.

Away from the origin
$$
[K^\mu,\phi(x)]=
-i(2x^\mu x^\nu \partial_\nu-x^2\partial^\mu+2\Delta x^\mu-2S^{\mu\nu}x_\nu)
\phi(x).
$$
In momentum space
$$
\begin{split}
[K^\mu,\tilde\phi(q)]=&
\left[
2\frac{\partial^2}{\partial q_\mu\partial q_\nu}q_\nu-
\frac{\partial^2}{\partial q_\nu\partial q^\nu}q^\mu-
2\Delta\frac{\partial}{\partial q_\mu}+
2S^{\mu\nu}\frac{\partial}{\partial q^\nu}
\right]\tilde\phi(q)=\\
&\left[
2q_\nu\frac{\partial^2}{\partial q_\mu\partial q_\nu}-
q^\mu\frac{\partial^2}{\partial q_\nu\partial q^\nu}+
2(d-\Delta)\frac{\partial}{\partial q_\mu}+
2S^{\mu\nu}\frac{\partial}{\partial q^\nu}
\right]\tilde\phi(q)
\end{split}
$$
For *distinct operators*, their two-point function is non-vanishing only if they have identical scaling dimensions.

#### FIelds with spin
For example of vector fields, one defines
$$
W^{\mu\nu}=\langle0|A^\mu(0)A^\nu(x)|0\rangle,
$$
a Fourier transform,
$$
\tilde W^{\mu\nu}(p)=\langle0|A^\mu(0)\tilde A^\nu(p)|0\rangle,
$$
which represents a two-point correlation function without the momentum conservation delta, 
$$
\langle0|\tilde A^\mu(p)\tilde A^\nu(q)|0\rangle=
(2\pi)^d\delta^d(p+q)\tilde W^{\mu\nu}(q).
$$
It can be decomposed using Lorentz symmetry,
$$
\tilde W^{\mu\nu}(p)=
(p^\mu p^\nu-p^2\eta^{\mu\nu})\tilde W_1(p)+p^\mu p^\nu\tilde W(p).
$$
By scale invariance and energy positivity. one can get
$$
\tilde W_{1,0}(p)=\theta(p^0-|\vec p|)(-p^2)^{\Delta-d/2-1}C_{1,0}.
$$
In the rest frame, $\vec q=0$, the momentum is invariant under the group $SO(d-1)$ of spatial rotations. The part proportional to $C_0$ appears only in $\tilde W^{00}$, and it transforms as a scalar under rotations. The part proportional to $C_1$ has non-zero entries only in $\tilde W^{ij}$ (in fact it is proportional to the identity in the $SO(d-1)$ subspace) and is an invariant tensor. These two parts are called **longitudinal** and **transverse**.

From the Ward identity one can obtain
$$
C_0=\frac{\Delta-d+1}{\Delta-1}C_1.
$$
Therefore, in the *conformal theory the two polarizations are not independent*.

For the intrgrability in $p^2\rightarrow0$, one has to require $\Delta>d/2$. As both $C_1$ and $C_2$ must be positive ($\tilde W$ must be positive definite), $\Delta-1$ and $\Delta-d+1$ must have the same sign. This implies the **unitarity bound for the vector field**
$$
\Delta\geq d+1.
$$
If the bound is *saturated*, $C_0=0$ and there is only a transverse part. So contraction with $p^\mu$ annihilates the state,
$$
p_\mu\tilde A^\mu(p)|0\rangle=0.
$$
In position space,
$$
\partial_\mu A^\mu(x)|0\rangle=0,
$$
This means that *primary fields are conserved currents*.
#### Correlation functions
The conformal algebra in $d$ is isomorphic to $SO(d+1,1)$ in the Euclidean metric case and $SO(d,2)$ in the Minkowski metric. This is checked explicitly after defining the coordinates
$$
X^\mu, X^{d+1}, X^{d+2}
$$
and the line element
$$
ds^2=g_{\mu\nu}dX^\mu dX^\nu+dX^{d+1}dX^{d+1}-dX^{d+2}dX^{d+2}\equiv\
\eta_{MN}dX^{M}dX^{N}.
$$

From the explicit form of $W(x)$, one can get by Wick rotation in the upper-half complex plane (where it is analytical),
$$
x^0=i\tau,~~~\tau>0,
$$
a **Schwinger function**,
$$
\langle\phi(0)\phi(x_E)\rangle=\frac{1}{(x^2_E)^\Delta}.
$$
The function is invariant under the Euclidean conformal group $SO(d+1,1)$, and so under translations and rotations. Then one can show
$$
\langle\phi(0)\phi(x)\rangle=\langle\phi(x)\phi(0)\rangle.
$$
An $n$-point Wightman function
$$
\langle0|\phi_n(x_n-n_{n-1})\phi_{n-1}(x_{n-1}-x_{n-2})...
\phi_2(x_2-x_1)\phi_1(x_1)|0\rangle,
$$
can be Wick rotated to the $n$-point Schwinger function (using the "average" notation instead of the "VEV" one implies using Euclidean metric),
$$
\langle\phi_n(x_n-n_{n-1})\phi_{n-1}(x_{n-1}-x_{n-2})...
\phi_2(x_2-x_1)\phi_1(x_1)\rangle,
$$
where all the arguments have positive $\tau$, so the product is time-ordered. One can state that:
- Schwinger functions are symmetric under exchange of operators,
- They transform covariantly under Euclidean $SO(d+1,d)$ transformations,
- They are not defined at coincident points
- Are **reflection positive**, if they are arranged in a configuration that is symmetric under reflection across some plane, then they are positive.