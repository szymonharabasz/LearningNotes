Vector components in tangent space:
$$
V=V^\mu\partial_\mu.
$$
Cotangent space - linear maps from $T_p(M)$ to $\mathbb R$. The basis in the cotangent space dual to $\partial_\mu$:
$$
W=W_\nu dx^\nu
$$
with
$$
dx^\nu(\partial_\mu)=\delta^\nu_\mu.
$$
General tensor is a mapping:
$$
T^{(r,s)}:\underbrace{T^*_p(M)\times...\times T^*_p(M)}_{r~\mathrm{times}}\times
\underbrace{T_p(M)\times...\times T_p(M)}_{s~\mathrm{times}}\rightarrow\mathbb{R}.
$$
and has components:
$$
T^{(r,s)}={T^{\mu_1...\mu_r}}_{\nu_1...\nu_s}
\partial_{\mu_1}\otimes...\otimes\partial_{\mu_r}\otimes
dx^{\nu_1}\otimes...\otimes dx^{\nu_s}.
$$
Sometimes it is convenient to define a **non-coordinate basis** $e_a$ by
$$
g(e_a,e_b)=\eta_{ab}
$$
or, in components,
$$
g_{\mu\nu}e^\mu_ae^\nu_b=\eta_{ab}.
$$
The set of such basis vectors is called **vielbein** and can be seen as a square-root of the metric.
This condition can be satisfied by different orthonormal sets that are connectd by **local Lorentz transformations**,
$$
e'_a(x)={\Lambda_a}^b e_b(x)
$$
with matrices $\Lambda$ that satisfy
$$
{\Lambda_a}^c(x){\Lambda_b}^d(x)\eta^{ab}=\eta^{cd}.
$$
Vector components, $V=V^ae_a$, transform as
$$
V'^a={\Lambda^a}_b(x)V^b.
$$
Action of a relativistic particle:
$$
S=-m\int d\tau
$$
One that allows also massless particles:
$$
S=\frac{1}{2}\int d\lambda\left\lbrace 
e^{-1}\eta_{\mu\nu}\dot{x}^\mu\dot{x}^\nu-em^2
\right\rbrace
$$
It reduces to the previous one using the equation of motion for $e$:
$$
\dot{x}^2+e^2m^2=0
$$
In curved spacetime, $\eta_{\mu\nu}$ is replaced with $g_{\mu\nu}(x)$. Then, equations of motion of a particle are *geodesic equatiobns*:
$$
\frac{d^2x^\mu}{d\tau}+
{\Gamma^\mu}_{\rho\sigma}
\frac{d^2x^\rho}{d\tau}
\frac{d^2x^\sigma}{d\tau},
$$
where *Christoffel symbols* are:
$$
{\Gamma^\alpha}_{\mu\nu}=\frac{1}{2}g^{\alpha\beta}\left(
\partial_\nu g_{\beta\mu}+
\partial_\mu g_{\beta\nu}-
\partial_\beta g_{\mu\nu}
\right).
$$
They allow to define covariant derivatives of vectors and forms:
$$
\nabla_\mu V^\nu=\partial_\mu V^\nu+V^\alpha{\Gamma^\nu}_{\alpha\mu},
$$
$$
\nabla_\mu V_\nu=\partial_\mu V_\nu-V_\alpha{\Gamma^\alpha}_{\mu\nu}.
$$
For Latin indices:
$$
\nabla_\mu V^a=\partial_\mu V^a+V^\nu{{\omega_\mu}^a}_\nu,
$$
$$
\nabla_\mu V_a=\partial_\mu V_a-V_b{{\omega_\mu}^b}_a.
$$
The condition $\nabla_\mu e^\mu_a=0$ leads to an equation for the spin connection,
$$
{{\omega_\mu}^a}_b=e^a_\lambda e^\nu_b\Gamma^\lambda_{\mu\nu}-e^\nu_b\partial_\mu e^a_\nu.
$$
A useful formula for covariant divergence:
$$
\nabla_\mu V^\mu=\frac{1}{\sqrt{-g}}\partial_\mu\left(\sqrt{-g}V^\mu\right),
$$
where $g=\det g_{\mu\nu}$.
Einstein equation is:
$$
R_{\mu\nu}-\frac{1}{2}g_{\mu\nu}R=8\pi GT_{\mu\nu}.
$$
Energy-momentum tensor is:
$$
T_{\mu\nu}=-\frac{2}{\sqrt{-g}}\frac{\delta S_\mathrm{matter}}{\partial g^{\mu\nu}}.
$$
Term of the energy-momentum tensor with *cosmological constant* $\Lambda$:
$$
T_{\mu\nu}=-\frac{\Lambda}{8\pi G}g_{\mu\nu}.
$$
The Riemann curvature tensor can be defined with:
$$
{R^\lambda}_{\mu\nu\rho}=
\partial_\nu{\Gamma^\lambda}_{\mu\rho}-
\partial_\rho{\Gamma^\lambda}_{\mu\nu}+
{\Gamma^\sigma}_{\mu\rho}{\Gamma^\lambda}_{\sigma\nu}-
{\Gamma^\sigma}_{\mu\\nu}{\Gamma^\lambda}_{\sigma\rho}.
$$
Its contractioon is the Ricci tensor:
$$
R_{\mu\nu}={R^\lambda}_{\mu\lambda\nu}.
$$
The vacuum Einstein equation is derived from the action:
$$
S=\frac{1}{16\pi G}\int d^4x\sqrt{-g}R.
$$
The simplest solution of the Einstein equation without cosmological constant and without matter fields is the *Schwarzschild black hole*:
$$
ds^2=-\left(1-\frac{2GM}{r}\right)dt^2+
\frac{dr^2}{1-\frac{2GM}{r}}+r^2d\Omega^2_2,
$$
where the line element of the unit 2D sphere is: $d\Omega^2_2=d\theta^2+\sin^2\theta d\phi^2$.
###### Gravitational redshift
Is given by
$$
\frac{E(A)}{E(B)}=\sqrt{\frac{g_{00}(B)}{g_{00}(A)}}.
$$
###### Surface gravity
Can be naively calculated from the Newton's law, the result coincides with the one measured by the asymptotic (at infinity) observer in General Relativity:
$$
\kappa=a(r=r_0)=\frac{c^4}{4GM}.
$$
Black body temperature of Hawking radiation is
$$
k_\mathrm{B}T=\frac{\hbar\kappa}{2\pi c}.
$$
This also allows to write the black hole entropy as
$$
S=\frac{A}{4G\hbar}k_\mathrm{B}c^3=\frac{1}{4}\frac{A}{l^2_\mathrm{Planck}}k_\mathrm{B},
$$
where the Planck length $l_\mathrm{Planck}=\sqrt{G\hbar/c^3}\approx10^{-35}~\mathrm{m}$. 
###### de Sitter metric 
Describes accelerated expansion of the Universe in the inflationary phase
$$
ds^2=-dt^2+e^{2Ht}(dx^2+dy^2+dx^2).
$$
#### Lie derivative
The Lie derivative along the vector field $V=V^\mu(x)\partial_\mu$ acts on a scalar as follows:
$$
L_V\phi(x)=V^\rho(x)\partial_\rho\phi(x),
$$on vectors or one forms as follows:
$$
L_VU^\mu=V^\rho\partial_\rho U^\mu-(\partial_\rho V^\mu)U^\rho\equiv[V,U]^\mu
$$
$$
L_VW_\mu=V^\rho\partial_\rho W_\mu+(\partial_\mu V^\rho)W_\rho.
$$
For an infinitesimal transformation, $x^\mu\rightarrow x'^\mu=x^\mu+\xi^\mu$, an arbitrary tensor transforms as, up to terms linear in $\xi$, 
$$
\delta {T^{\mu_1...\mu_r}}_{\nu_1...\nu_s}\equiv
{T'^{\mu_1...\mu_r}}_{\nu_1...\nu_s} - {T^{\mu_1...\mu_r}}_{\nu_1...\nu_s}
=L_\xi{T^{\mu_1...\mu_r}}_{\nu_1...\nu_s}
$$
Vectors for which
$$
L_Vg_{\mu\nu}=\nabla_\mu V_\nu+\nabla_\nu V_\mu=0
$$
are called **Killing vectors**. A spacetime is **stationary** if it has a timelike Killing vector field, at least asymptotically at large distances.
#### DIfferential forms
They are antisymmetric $(0,p)$ tensors and can be written as
$$
\omega^{(p)}=
\frac{1}{p!}\omega_{\mu_1...\mu_p}dx^{\mu_1}~\wedge...\wedge~dx^{\mu_p},
$$
where the wedge product is defined as
$$
dx^{\mu_1}~\wedge...\wedge~dx^{\mu_p}=\sum_{\sigma\in S_p}\mathrm{sgn}(\sigma)
dx^{\mu_{\sigma(1)}}~\otimes...\otimes~dx^{\mu_{\sigma(p)}}.
$$
In the non-coordinate basis:
$$
\omega^{(p)}=
\frac{1}{p!}\omega_{a_1...a_p}e^{a_1}~\wedge...\wedge~e^{a_p},
$$
**Exterior derivative** acts as:
$$
\mathrm{d}\omega^{(p)}=\frac{1}{p!}(\partial_\mu\omega_{\mu_1...\mu_p})
dx^\mu\wedge dx^{\mu_1}\wedge...\wedge dx^{\mu_p}.
$$
One can write
$$
\mathrm{d}e^a+{\omega^a}_b\wedge e^b=0,
$$
where
$$
{\omega^a}_b={{\omega_\mu}^a}_bdx^\mu.
$$
This allows to calculate the spin connection in the torsion-free case without calculating first $\Gamma^\lambda_{\mu\nu}$.

**Canonical volume form** is a 1-form and is unique up to a multiplication by arbitray function. It is defined as
$$
\mathrm{dVol}=e^0\wedge...\wedge e^{d-1}
$$
The totally antisymmetric Levi-Civita symbol in the local frame basis is defined as:
$$
\epsilon_{a_1...a_d}=\left\{
\begin{split}
+1~:&~(a_1...a_d)~\mathrm{is~an~even~permutation~of}~(1,0,...,d-1)\\
-1~:&~(a_1...a_d)~\mathrm{is~an~odd~permutation~of}~(1,0,...,d-1)\\
0~:&~\mathrm{otherwise}
\end{split}
\right.
$$
For consistency, to define the symbol in the coordinate basis, one has to insert factors of $e\equiv\det(e^a_\mu)=\sqrt{-\det g}$:
$$
\epsilon_{\mu_1...\mu_d}=\frac{1}{e}\epsilon_{a_1...a_d}e^{a_1}_{\mu_1}...e^{a_d}_{\mu_d},
$$
$$
\epsilon^{\mu_1...\mu_d}=e\epsilon^{a_1...a_d}e_{a_1}^{\mu_1}...e_{a_d}^{\mu_d}.
$$
Then the canonical volume can be written as
$$
\mathrm{dVol}=
\frac{1}{d!}\epsilon_{a_1...a_d}e^{a_1}\wedge...\wedge e^{a_d}=
\frac{1}{d!}e\epsilon_{\mu_1...\mu_d}dx^{\mu_1}\wedge...\wedge e^{\mu_d}=edx^0\wedge...\wedge dx^{d-1}\equiv d^dx\sqrt{-g}.
$$
