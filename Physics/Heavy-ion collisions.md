# Quantum Hadro-Dynamics (QHD):
$$
{\cal L}={\cal L}_B+{\cal L}_M+{\cal L}_I,
$$
where baryonic part:
$$
{\cal L}_B=\bar \Phi(i\partial\!\!\!/-M)\Psi,
$$
meson part (which ia a gauge field):
$$
{\cal L}_M=\frac{1}{2}\partial_\mu\sigma\partial^\mu\sigma
-U(\sigma)-\frac{1}{4}F_{\mu\nu}F^{\mu\nu}+O(\omega^\mu\omega_\mu),
$$
and interaction part:
$$
{\cal L}_I=\Gamma_\sigma(\hat \rho_0)\bar \Psi\sigma\Psi-
\Gamma_\omega(\hat\rho_0)\bar\Psi\omega\!\!\!/\Psi.
$$
We have $F^{\mu\nu}=\partial^\mu\omega^\nu-\partial^\nu\omega^\mu$, and when self-interactions are neglected:
$$
U(\sigma)=\frac{1}{2}m^2_\sigma\sigma^2,~~~
O(\omega^\mu\omega_\mu)=\frac{1}2m^2_\omega\omega^\mu\omega_\mu.
$$
# Free spectral functions
We use commutator/anitcommutator:
$$
\Delta_{ll'}=[\psi_l(x),\psi^\dagger_{l'}(x')]_\pm,
$$
and the **Feynman propagator**:
$$
\Delta^F_{ll'}=i\langle0|T\{\psi_l(x)\psi^\dagger_{l'}(x')\}|0\rangle.
$$
For a general field:
$$
\psi_l(x)=
\int\frac{d^3q}{(2\pi)^3 2\omega}\sum_\sigma
\left(
u_l({\bf q,\sigma})e^{-iq\cdot x}a({\bf q,\sigma})+
v_l({\bf q,\sigma})e^{iq\cdot x}b^\dagger({\bf q,\sigma})
\right).
$$
One gets:
$$
\Delta_{ll'}(x,x')=
\int\frac{d^3q}{(2\pi)^3 2\omega}
\left(
e^{-iq\cdot (x-x')}\sum_\sigma u_l({\bf q,\sigma})u^*_{l'}({\bf q,\sigma})\mp
e^{iq\cdot (x-x')}\sum_\sigma v_l({\bf q,\sigma})v^*_{l'}({\bf q,\sigma})
\right),
$$
and:
$$
-i\Delta^F_{ll'}(x,x')=
\int\frac{d^3q}{(2\pi)^3 2\omega}
\left(
\theta(t-t')e^{-iq\cdot (x-x')}\sum_\sigma u_l({\bf q,\sigma})u^*_{l'}({\bf q,\sigma})\pm
\theta(t'-t)e^{iq\cdot (x-x')}\sum_\sigma v_l({\bf q,\sigma})v^*_{l'}({\bf q,\sigma})
\right).
$$
For the free real scalar field:
$$
\Delta(x-x')=\int\frac{d^3k}{(2\pi)^3 2\omega}
\left(
e^{-ik(x-x')}-e^{ik(x-x')}
\right)\equiv\Delta_+(x-x')-\Delta_+(x'-x),
$$
where a *standard function was defined*:
$$
\Delta_+(x-x')=\int\frac{d^3k}{(2\pi)^3 2\omega}e^{-ik(x-x')}.
$$
It can be written as a Fourier transform:
$$
\Delta_+(x-x')=\int\frac{d^4k}{(2\pi)^4}e^{-ik(x-x')}2\pi\theta(k_0)\delta(k^2-m^2)
$$
Using a formula:
$$
\delta(k^2-m^2)=\frac{1}{2\omega}[\delta(k_0-\omega)+\delta(k_0+\omega)],
$$
The commutator takes the form:
$$
\Delta(x-x')=\int\frac{d^4k}{(2\pi)^4}e^{-ik(x-x')}\rho_0(k),
$$
where the **free spectral function** is
$$
\rho_0(k)=2\pi\epsilon(k_0)\delta(k^2-m^2),
$$
where $\epsilon(k_0)\equiv\theta(k_0)-\theta(-k_0)$.
The Fourier transform of the Feynman propagator is
$$
\Delta_F(k)=\frac{-1}{k^2-m^2+i\eta}.
$$
It can be put into spectral representation:
$$
\Delta_F(k)=\int_{-\infty}^\infty\frac{dk'_0}{2\pi}
\frac{\rho_0(k_0,{\bf k})}{k'_0-k_0-i\eta\epsilon(k_0)}.
$$
For the Dirac field the anticommutator is:
$$
\{\psi(x),\bar\psi(x')\}=
\int\frac{d^3p}{(2\pi)^32\omega}
\left(
(p\!\!\!/+m)e^{-ip(x-x')}+
(p\!\!\!/-m)e^{ip(x-x')}
\right)=
\int\frac{d^4p}{(2\pi)^4}e^{-ip(x-x')\sigma_0(p)}
$$
with the free spectral function:
$$
\sigma_0(p)=2\pi\epsilon(p_0)(p\!\!\!/+m)\delta(p^2-m^2).
$$
The Fourier transform of the Feynman propagator:
$$
S_F(p)=\frac{-(p\!\!\!/+m)}{p^2-m^2+i\eta}.
$$
Its spectral representation:
$$
S_F(p)=\int_{-\infty}^\infty\frac{dp'_0}{2\pi}
\frac{\sigma_0(p'_0,{\bf p})}{p'_0-p_0-i\eta\epsilon(p_0)}.
$$
For the vector field the commutator is
$$
\Delta^{\mu\nu}(x-x')=\int\frac{d^4k}{(2\pi)^4}e^{-ik(x-x')}\rho_0^{\mu\nu}(k),
$$
where the free spectral function is
$$
\rho_0^{\mu\nu}(k)=
\left(
-g^{\mu\nu}+\frac{k^\mu k^\nu}{m^2}
\right)
2\pi\epsilon(k_0)\delta(k^2-m^2).
$$
The Fourier transform of the Feynman propagator:
$$
\Delta_F^{\mu\nu}(k)=
\left(
-g^{\mu\nu}+\frac{k^\mu k^\nu}{m^2}
\right)
\frac{-1}{k^2-m^2+i\eta}.
$$
# Spontaneous symmetry breaking
## First derivation of the Goldstone theorem, effective potential
If the S-matrix element is:
$$
S_{\alpha\beta}=
\langle\beta|T\exp\left(
i\int d^4x{\cal L}_\mathrm{int}(\phi_n)
\right)
|\alpha\rangle,
$$
then the generating functional in the presence of an external classical field,
$$
Z[h]=\langle 0|T\exp\left(
i\int d^4x\h_n(x)\phi_n(x)
\right)|0\rangle,
$$
is the vaccum-to-vacuum amplitude in the presence of the field:
$$
Z[h]=\langle 0,\mathrm{out}|0,\mathrm{in}\rangle_h.
$$
We can expand the exponential:
$$
Z[h]=\sum_{r=0}^\infty\frac{1}{r!}
\int d^4x_1....d^4x_rh_{n_1}(x_1)h_{n_2}(x_2)...h_{n_r}(x_r)
\langle 0|T\phi_{n_2}(x_2)\phi_{n_1}(x_1)...\phi_{n_r}(x_r)|0\rangle.
$$
The fields are in the Heisenberg representation, the full original Hamiltonian gives their time evolution. The coefficients can be expressed in the interaction representation:
$$
\langle 0|T\phi_{n_2}(x_2)\phi_{n_1}(x_1)...\phi_{n_r}(x_r)|0\rangle=
\langle 0|T\phi^I_{n_2}(x_2)\phi^I_{n_1}(x_1)...\phi^I_{n_r}(x_r)
\exp\left(
i\int d^4x{\cal L}_\mathrm{int}(x)
\right)|0\rangle.
$$
If we write
$$
Z[h]=e^{iW[h]},
$$
then $W[h]$ generates only connected diagrams.
We define the classical field $\phi^c_n(x)$ as the vacuum expectation value of the quantum field in the presence of external fields:
$$
\phi^c_n(x)=
\frac{\langle 0,\mathrm{out}|\phi_n(x)|0,\mathrm{in}\rangle_h}
{\langle 0,\mathrm{out}|0,\mathrm{in}\rangle_h}=
\frac{-i}{Z[h]}\frac{\delta Z[h]}{\delta h_n(x)}=
\frac{\delta W[h]}{\delta h_n(x)}
$$
The effective action is the Legendre transform of $W[h]$:
$$
\Gamma[\phi^c]=W[h]-\int d^4x\phi^c_n(x)h_n(x).
$$
It generates **one-particle irreducible** diagrams,
$$
\Gamma[\psi^c]=\sum_r\frac{1}{r!}
\int d^4x_1....d^4x_r\Gamma^{(r)}_{n_1...n_r}(x_1...x_r)
\phi^c_{n_1}(x_1)...\phi^c_{n_r}(x_r),
$$
with $r$ external lines, from which propagators were removed. In particular, $\Gamma^{(2)}(x_1,x^2)$ *is the inverse propagator*.
The effective action fulfills the relation:
$$
\frac{\delta\Gamma}{\delta\phi^c_n(x)}=-h_n(x).
$$
Alternatively to 1PI diagrams, one can also expand $\Gamma[\psi^c]$ in powers of external momenta:
$$
\Gamma[\phi^c]=
\int d^4x\{-V(\phi^c)+Z_{n_1n_2}\partial_\mu\phi^c_{n_1}\partial_\mu\phi^c_{n_2}+...\},
$$
where the ordinary function $V(\phi^c)$ is called **effective potential**, and a the tree level it is equal the usual potential.
When to the 1PI expansion one inserts Fourier transform $\tilde \Gamma^{(r)}(p_1,...,p_r)$ of  $\Gamma^{(r)}(x_1,...,x_r)$, and then specializes to constant $\phi^c(x)$, then the position integrals give $\delta(p)$, which remove the momentum integrals and give:
$$
\Gamma[\phi^c]=\sum_r\frac{1}{r!}\tilde\Gamma^{(r)}_{n_1...n_r}
(p_1=0,...,p_r=0)\phi^c_{n_1}(0)...\phi^c_{n_r}(0).
$$
Comparing the last two expressions for $\Gamma[\phi^c]$, we can see that the n-th derivative of $V$ (coefficient in its expansion in powers of $\phi^c$) is a sum of all 1PI diagrams with n external momenta equal zero, up to a multiplicative factor dependent on four-dimensional volume. In particular, the second derivative is the **mass matrix**.

If the symmetry is spontaneously broken, $\phi^c$ has a non-zero expectation value for vanishing external field, which in addition is constant, so
$$
0=\frac{\delta\Gamma}{\delta\phi^c_n}\rightarrow
\left.\frac{\partial V}{\partial\phi^c_n}\right|_{\phi^c=\bar\phi\neq0}.
$$

An infinitesimal symmetry transformation can be written as:
$$
\delta\phi_n=i\epsilon_\alpha[l_\alpha]_{mn}\phi_n.
$$
The group is also a symmetry group of the effective potential, so
$$
0=\delta V=\frac{\partial V}{\partial \phi_m}\delta\phi_m=
i\frac{\partial V}{\partial \phi_m}\epsilon_\alpha[l_\alpha]_{mn}\phi_n.
$$
Since $\epsilon_\alpha$ are arbitrary, this must hold separately for each generator:
$$
\frac{\partial V}{\partial\phi_n}[l_\alpha]_{mn}\phi_n=0.
$$
Taking the second derivative at minimum ($\partial V/\partial\phi^c_n|_{\phi^c=\bar\phi}=0$) one gets:
$$
\left.\frac{\partial^2V}{\partial\phi^c_n\partial\phi^c_m}\right|(l_\alpha\bar\phi_\alpha)_n=0.
$$
If $l_\alpha$ is a generator of the unbroken symmetry subgroup, then $(l_\alpha\bar\phi_\alpha)_n=0$, because in this case:
$$
g(\theta_\alpha)=\exp(i\theta_\alpha l_\alpha) = 1.
$$
Otherwise, if it is a generator of a broken symmetry, then $(l_\alpha\bar\phi_\alpha)_n=0$ is an eigenvector of the mass matrix with eigenvalue zero. For every independent broken generator of a symmetry group of the Lagrangian, there is one massless boson - a **Goldstone boson**.
## Second derivation of the Goldstone theorem
A $g\in G$ is represented by an unitary transformation:
$$
|\psi\rangle\rightarrow|\psi'\rangle={\cal U}(g)|\psi\rangle.
$$
Let the matrix elements of the field multiplet transform according to a representation $D(g)$ of $G$:
$$
\langle\psi|\phi_n(x)|\chi\rangle\rightarrow
\langle\psi'|\phi_n(x)|\chi'\rangle=
D_{nm}(g)\langle\psi|\phi_m(x)|\chi\rangle.
$$
Therefore:
$$
{\cal U}^\dagger(g)\phi_n(x){\cal U}(g)=D_{nm}(g)\phi_m(x).
$$
For group elements with coordinates $\omega_1,\omega_2,...$ infinitisemally close to unity:
$$
\begin{split}
{\cal U}(1+\omega)=&1+i\omega_\alpha Q_\alpha+{\cal O}(omega^2)\\
D(1+\omega)=&1+i\omega_\alpha l_\alpha + {\cal O}(\omega^2).
\end{split}
$$
Here the charges $Q_\alpha$ are quantum generators and matrices $l_\alpha$ are group generators. Now, the commutator is:
$$
[Q_\alpha,\phi_n(x)]=-[l_\alpha]_{nm}\phi_m(x).
$$
One can compute:
$$
\langle 0|J^\mu_\alpha(y)\phi_n(x)|0\rangle=
\int\frac{d^4p}{(2\pi)^3}e^{-ip(y-x)}i\rho^\mu_{\alpha,n}(p)
$$
with the spectral density of the form:
$$
(2\pi)^3\sum_N\langle 0|J^\mu_\alpha(0)|N\rangle\langle N|\phi_n(0)|0\rangle
\delta^4(p-p_N)=
i\rho^\mu_{\alpha,n}(p)=ip^\mu\rho_{\alpha,n}(p^2)\theta(p_0),
$$
where the sum is over complete set of states chosen to be eigenstates of momenta, and the last equality takes into account the Lorentz invariance (four-vector depending only on momentum must be proportional to it) and the fact that energy is positive.
Introducing $1=\int ds\delta(s-p^2)$, one gets:
$$
\langle 0|J^\mu_\alpha(y)\phi_n(x)|0\rangle=
-\frac{\partial}{\partial y_\mu}\int ds \rho_{alpha,n}(s)\Delta_+(y-x,s)
$$
Calculating similarly and defining:
$$
(2\pi)^3\sum_N\langle 0|\phi_n(0)|N\rangle\langle N|J^\mu_\alpha(0)|0\rangle
\delta^4(p-p_N)=
i\tilde\rho^\mu_{\alpha,n}(p)=ip^\mu\tilde\rho_{\alpha,n}(p^2)\theta(p_0),
$$
we get for the commutator:
$$
\langle 0|[J^\mu_\alpha(y),\phi_n(x)]|0\rangle=
-\frac{\partial}{\partial y_\mu}\int ds[\rho_{\alpha,n}(s)\Delta_+(y-x,s)+
\tilde\rho_{\alpha,n}(s)\Delta_+(x-y,s)].
$$
The two spectral functions are not independent, for the spacelike separations $\Delta_+(x-y,s)$ becomes an even function of $x-y$, and the commutator vanishes in this region. Therefore
$$
\rho_{\alpha,n}(s)+\tilde\rho_{\alpha,n}(s)=0,
$$
and for general $x-y$:
$$
\langle 0|[J^\mu_\alpha(y),\phi_n(x)]|0\rangle=-\frac{\partial}{\partial y_\mu}
\int ds \rho_{\alpha,n}(s)\Delta(y-x,s).
$$
Taking $\partial/\partial y_\mu$ on both sides, using the fact that $J^\mu_\alpha(y)$ is conserved, and that $\Delta(y-x,s)$ is a Green function, one gets for any $x-y$:
$$
0=\int dss\rho_{\alpha,n}(s)\Delta(x-y,s)
$$
which leads to 
$$
s\rho_{\alpha,n}(s)=0.
$$
The general solution is
$$
\rho_{\alpha,n}(s)=c_{\alpha,n}\delta(s)
$$
with $c_{\alpha, n}$ being constants. Inserting this solution, choosing $\mu=0$, and using the equality:
$$
\partial_l\Delta(x-x')|_{t=t'}=-i\delta^3({\bf x}-{\bf x}'),
$$
one arrives at
$$
\langle 0|[J^\mu_\alpha({\bf y},y),\phi_n({\bf x},t)]|0\rangle=
ic_{\alpha,n}\delta^3({\bf x}-{\bf y}).
$$
Integrating over $\bf y$ and using the commutator derived above, one gets:
$$
-[l_\alpha]_{nm}\langle 0|\phi_m|0\rangle=ic_{\alpha,n},
$$
so the *constants are indeed non-vanishing in theories with spontaneous symmetry breaking*. Finally, for the broken generators $s_\alpha$:
$$
\rho_{\alpha,n}=i\delta(s)(s_\alpha\bar\phi)_n\neq0.
$$
The delta function means that the modes are massless and are again **Goldstone bosons**.
# Effective field theories
If the symmetry group $G$ Is broken spontaneously to some subgroup $H$, elements of which leave the VEV of the field $\psi_m(x)$, that is, $\bar\psi_m=\langle 0|\psi_m|0\rangle$, invariant:
$$
h_{nm}\bar\psi_m=\psi_n,~~~h\in H.
$$
One expresses $\psi$ as a position-dependent transformation of fields $\tilde\psi$, *from which Goldstone fields were removed*:
$$
\psi_n(x)=\gamma_{nm}(x)\tilde\psi_m(x),~~~\gamma\in G.
$$
At the end of the first derivation of the Goldstone theorem, it was stated, that the Goldstone modes are represented by vectors $s_\alpha\bar\phi$, with broken generators $s_\alpha$. That "Goldstone fields were removed" means the orthogonality between the states:
$$
\tilde\psi_n[s_\alpha]_{nm}\bar\phi_m=0.
$$
Matrices $\gamma$ can always be chosen to satisfy this condition. Define namely in a real representation of a compact group $G$:
$$
V_\psi(g)=\psi_ng_{nm}\bar\phi_m.
$$
$V(g)$ is real and continuous function of $g$, so it is bounded and at each $x$ reaches a maximum for some $g=\gamma(x)$.  If $g$ is written as:
$$
g=\exp(il_\alpha\theta_\alpha),
$$
then an infinitesimal change is:
$$
\delta g=i\epsilon_\alpha gl_\alpha.
$$
Close to the maximum, $V$ is stationary, so:
$$
0=\delta V(\gamma(x))=
i\epsilon_\alpha\psi_n(x)[\gamma(x)]_{np}[s_\alpha]_{pm}\bar\phi_m.
$$
It must be fulfilled for every $\epsilon_\alpha$. Furthermore, for a compact group we can choose a unitary representation, which in real case is orthogonal, that is, $\gamma\gamma^T=1$, so $[\gamma]_{np}=[\gamma^{-1}]_{pn}$, so:
$$
[\gamma^{-1}(x)\psi(x)]_pi(s_\alpha\bar\phi)_p=0.
$$
This shows that $\gamma$ indeed fulfills the orthogonality relation.
But because $h_{nm}\bar\psi_m=\psi_n$, if $\gamma$ maximizes $V(g)$, so does $\gamma h$. The set of all such elements defines an equivalence class - **a right coset of $G$ with respect to $H$**. The space of right cosets is the **quotient space** $G/H$.
All elements $g\in G$ can be sorted into right cosets. If we choose one $\gamma$ from each coset, we can parametrize each group element:
$$
g=\gamma h\equiv\exp(i\xi_\alpha s_\alpha)\exp(i\theta_it_i),
$$
where we take $\xi_\alpha=\xi_\alpha(x)$ as *fields proportional to Goldstone bosons*.
Now, under the action of general $g\in G$ the field transforms as:
$$
\psi(x)\rightarrow\psi'(x)=g\psi(x)=g\gamma(\xi(x))\tilde\psi(x).
$$
But $g\gamma(\xi(x))$ is another group elements, so it must belong to some coset represented by another $\gamma(\xi'(x))$. Then:
$$
g\gamma(\xi(x))=\gamma(\xi'(x))h(x,g).
$$
This gives the transformation rule $\xi(x)\rightarrow\xi'(x)$ for Goldstone fields under the action of $g$. Inserting this decomposition into the transformation $\psi\rightarrow\psi'$ we get:
$$
\psi'(x)=\gamma(\xi'(x))\tilde\psi'(x),
$$
where
$$
\tilde\psi'(x)=h(\xi,g)\tilde\psi(x).
$$
This gives the transformation rule for non-Goldstone fields.