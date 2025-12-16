#### In quantum mechanics of one particle
We define the amplitude:
$$
G(x,y,t)=\langle y|\exp(-i\hat H t)|x\rangle=\sum_n\psi_n(x)\psi_n^*(y)\exp(-iE_nt)
$$
Written as a path integral:
$$
G(x,y,t)=\int_{x(0)=0}^{x(t)=y}Dx(t)\exp(-iS[x(t)]).
$$
After Wick rotation, $\tau=it$:
$$
S(x,y,\tau)=\sum_n\psi_n(x)\psi_n^*(y)\exp(-E_n\tau).
$$
If we choose periodic paths with the period $\beta=\hbar/T$, and the states are normalized as 
$$
\int dx|\psi_n(x)|^2=1,
$$
then the path integral gives the statistical sum:
$$
Z=\sum_n\exp(-E_n/T)=\int Dx(\tau)\exp(-S_E[x(\tau)])
$$
#### Harmonic oscillator
For the potential written as:
$$
V=\frac{1}{2}m^2\Omega^2x^2,
$$
The amplitude has the form:
$$
S(x,y,\tau)=
\left(\frac{m\Omega}{2\pi\hbar\sinh(\Omega\tau)}\right)^{1\2}
\exp\left[-\left(\frac{m\Omega}{2\pi\hbar\sinh(\Omega\tau)}\right)
((x^2+y^2)\cosh(\Omega\tau)-2xy)
\right].
$$
The diagonal elements of the amplitude give the probability of finding a particle at $x$, so setting $x=y$ and $\tau=\beta$, one gets this probability equal:
$$
P(x)=\left(\frac{m\Omega}{2\pi\hbar\sinh(\Omega\tau)}\right)^{1/2}
\exp\left(-\frac{x^2}{2\langle x^2\rangle}\right),
$$
where the widths is:
$$
\langle x^2\rangle=\frac{1}{2m\Omega}\coth\left(\frac{\Omega}{2T}\right).
$$
Correlator of two coordinates, defined as:
$$
\langle x_ix_j\rangle=
\frac{
\int_{-\infty}^\infty(\prod_{n=1}^Ndx^n)~x_ix_je^{-\sum_{ij}x^iA_{ij}x^j}
}{
\int_{-\infty}^\infty(\prod_{n=1}^Ndx^n)~e^{-\sum_{ij}x^iA_{ij}x^j}
},
$$
is a ratio of integrals that factorize in the diagonal basis,
$$
A_{nj}y_j=\lambda_ny_n
$$
and it takes the form:
$$
\langle y_iy_j\rangle=\frac{1}{2}\frac{\delta_{ij}}{\lambda_i}.
$$
Coming back to the original basis with $x_i=\sum_jC_{ij}x_j$,
$$
\langle x_ix_j\rangle=\frac{1}{2}\sum_{ii'j}\frac{C_{ij}C_{i'j}}{\lambda_j}=\frac{1}{2}\left(A^{-1}\right)_{ij}.
$$
In the case of the harmonic oscillator, the operator is:
$$
\hat A=-m\frac{d^2}{d\tau^2}+m\Omega^2,
$$
 so eigenfunctions and eigenvalues are
$$
y_n=\exp(i\omega_n\tau),~~~\lambda_n=\frac{1}{2}m(\omega_n^2+\Omega^2).
$$
with the Matsubara frequencies
$$
\omega_n=2\pi n/\beta=2\pi nT.
$$
Therefore, the correlator at different times is:
$$
\langle x(\tau)x(\tau')\rangle=\frac{T}{m}\sum_n\frac{\exp[i\omega_n(\tau-\tau')]}
{\omega_n^2+\Omega^2}.
$$
The explicit form can be calculated as:
$$
G(\tau)=\frac{\cosh(\Omega(\tau-\beta/2))}{2m\Omega\sinh(\Omega\beta/2)}
\xrightarrow[T\rightarrow 0]{}\frac{1}{2m\Omega}e^{-\Omega|\tau|}.
$$
#### Quantum field theory
State vector is normalized as:
$$
\langle{\bf q}', \sigma'|{\bf q}, \sigma\rangle=
(2\pi)^32\omega\delta_{\sigma\sigma'}\delta({\bf q}'-{\bf q}).
$$
The field is expanded in terms of creation and annihilation operators:
$$
\psi_l(x)=\int\frac{d^3q}{(2\pi)^32\omega}
\sum_\sigma u_l({\bf q},\sigma)e^{-iqx}a({\bf q},\sigma)+
v_l({\bf q},\sigma)e^{iqx}b^\dagger({\bf q},\sigma).
$$
One can denote commutator/anicommutator:
$$
\Delta_{ll'}(x,x')=\left[
\psi_l(x),\psi^\dagger_{l'}(x')
\right]_\mp
$$
and the Feynman propagator:
$$
\Delta^F_{ll'}(x,x')=i\langle
0|T{\psi_l(x)\psi^\dagger_{l'}(x')}|0
\rangle.
$$
There is also a definition of a standard function:
$$
\Delta_+(x)=\int\frac{d^3k}{(2\pi)^32\omega}e^{-ikx}.
$$
In the case of vector fields, the spin sum that enters these quantities:
$$
E^{\mu\nu}(k)=\sum_\sigma\epsilon^\mu({\bf k},\sigma)\epsilon^{\nu*}({\bf k},\sigma)
$$
must be a linear combination of the two available second-rank tensors, $g^{\mu\nu}$ and $k^\mu k^\nu$. The gauge condition $\partial_\mu B^\mu=0$ gives $k_\mu\epsilon^\mu=0$, which fixes a relative coefficient between these two tensors. By fixing normalization, one obtains:
$$
E^{\mu\nu}(k)=-g^{\mu\nu}+\frac{k^\mu k^\nu}{m^2}.
$$