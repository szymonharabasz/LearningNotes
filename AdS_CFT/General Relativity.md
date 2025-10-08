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