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
It generates **one-particle irreducible** diagrams. It fulfills the relation:
$$
\frac{\delta\Gamma}{\delta\phi^c_n(x)}=-h_n(x).
$$