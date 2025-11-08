For a free particle:
$$
\psi_E({\bf r})=\frac{e^{i{\bf p\cdot r}/\hbar}}{(2\pi\hbar)^{3/2}}.
$$
If a particle moves along $z$ axis and has momentum $p$:
$$
{\bf p\cdot r}/\hbar=(pr\cos\theta)/\hbar=kr\cos\theta.
$$
Therefore:
$$
\psi_E({\bf r})=\frac{e^{ikr\cos\theta}}{(2\pi\hbar)^{3/2}},~~~
E=\frac{\hbar^2k^2}{2m}.
$$
It should be possible to expand this as a linear combination of $\psi_{Elm}$ with the same $E$, that is, the same $k$:
$$
e^{ikr\cos\theta}=\sum_{l=0}^{\infty}\sum_{m=-l}^{l}C_l^m
j_l(kr)Y_l^m(\theta,\phi).
$$
Left-hand side does not depend of $\phi$ (moves along $z$ and does not have angular momentum along this axis), so only $m=0$ contributes. It is known that:
$$
Y_l^0=\left(\frac{2l+1}{4\pi}\right)^{1/2}P_l(\cos\theta),
$$
so:
$$
e^{ikr\cos\theta}=\sum_{l=0}^{\infty}C_lj_l(kr)P_l(cos\theta),~~~
C_l=C_l^0\left(\frac{2l+1}{4\pi}\right)^{1/2}.
$$
It can be shown that $C_l=i^l(2l+1)$, therefore:
$$
e^{ikz}=e^{ikr\cos\theta}=\sum_{l=0}^{\infty}i^l(2l+1)j_l(kr)P_l(cos\theta).
$$
It holds that
$$
j_l(kr)\xrightarrow[r\rightarrow\infty]{}\frac{\sin(kr-l\pi/2)}{kr}.
$$
from which it follows:
$$
e^{ikz}\xrightarrow[r\rightarrow\infty]{}
\frac{1}{2ik}\sum_{l=0}^{\infty}i^l(2l+1)
\left(
\frac{e^{i(kr-l\pi/2)}}{r}-\frac{e^{-i(kr-l\pi/2)}}{r}
\right)
P_l(cos\theta)=
\frac{1}{2ik}\sum_{l=0}^{\infty}(2l+1)
\left(
\frac{e^{ikr}}{r}-\frac{e^{-i(kr-l\pi)}}{r}
\right)
P_l(cos\theta),
$$
which uses the fact that $e^{i\pi/2}=i$.

When a **particle is not free**, radial wave function should asymptotically approach the free one, with possible **phase shift**, due to the potential:
$$
R_l(r)=\frac{U_l(r)}{r}\xrightarrow[r\rightarrow\infty]{}
A_l\frac{\sin(kr-l\pi/2+\delta_l(k))}{r}.
$$
Consequently:
$$
\psi_{\bf k}({\bf k})
\xrightarrow[r\rightarrow\infty]{}
\sum_{l=0}^{\infty}A_l
\frac{e^{i(ik-l\pi/2+\delta_l)}-e^{-i(ik-l\pi/2+\delta_l)}}{r}
P_l(cos\theta),
$$
The potential is a source of the outgoing wave, the incoming wave must be the same as in the free case. this allows to fix:
$$
A_l=\frac{2l+1}{2ik}e^{i(l\pi/2+\delta_l)}.
$$
Inserting this, one gets:
$$
\psi_{\bf k}({\bf k})
\xrightarrow[r\rightarrow\infty]{}
e^{ikz}+
\left[\sum_{l=0}^{\infty}
(2l+1)\left(
\frac{e^{2i\delta_l}-1}{2ik}
\right)
P_l(cos\theta)\right]\frac{e^{ikr}}{r},
$$
Then the **amplitude of $l$-th partial wave** is:
$$
a_l(k)=\frac{e^{2i\delta_l}-1}{2ik}=\frac{e^{i\delta_k}\sin\delta_l}{k}.
$$
S-matrix element for a partial wave or angular momentum $l$ is equal:
$$
S_l(k)=e^{2o\delta_l(k)}.
$$
But $S$ is just $\lim_{t\rightarrow\infty}U(-t,t)$, so it is unitary and is a function of the hamiltonian. If $\bf L$ is conserved, then $S$ is diagonal in the basis of $(E,l,m)$ and being unitary, it has eigenvalues of the form $e^{i\vartheta}$, so $\vartheta=2\delta_l$.
When particle absorption is possible,
$$
S_l(k)=\eta_l(k)e^{2i\delta_l},
$$
where $\eta<1$ is called **inelasticity coefficient**.

Writing the scattering amplitude:
$$
f(\theta)=\frac{1}{k}\sum_{l=0}^\infty(2l+1)e^{i\delta_l}\sin\delta_lP_l(\cos\theta).
$$
The total cross-section:
$$
\sigma=\int|f|^2d\Omega=\frac{4\pi}{k^2}\sum_{l=0}^\infty(2l+1)\sin^2\delta_l,
$$
which makes use of the orthogonality of Legendre polynomials:
$$
\int P_l(x)P_{l'}(x)dx=\frac{2}{2l+1}\delta_{ll'}.
$$
The total cross-section is a sum of cross-sections for different partial waves:
$$
\sigma=\sum_{l=0}^\infty\sigma_l,~~~\sigma_l=\frac{4\pi}{k^2}(2l+1)\sin^2\delta_l.
$$
The limiting value:
$$
\sigma_l\leq\sigma_l^\mathrm{max}=\frac{4\pi}{k}(2l+1)
$$
is called **unitarity limit**.

Using $P_l(\cos 0)=1$, one also gets **optical theorem**:
$$
\sigma=\frac{4\pi}{k}\mathrm{Im}f(0).
$$
For the potential of hard-sphere potential with radius $r_0$:
$$
\tan\delta_l\xrightarrow[k\rightarrow 0]{}\delta_l\propto(kr_0)^{2l+1}.
$$
This can be also interpreted as the definition of $r_0$ for *any* potential.
For a square well potential of range $r_0$, the phase shift is:
$$
\delta_0=-kr_0+\arctan\left(
\frac{k}{k'}\tan k'r_0
\right),
$$
where $k$ and $k'$ are wave numbers inside and outside of the well.

If the phase shift grows very quickly from 0 to $\pi$ in a narrow range of $k$ or $E$, then it can be written in that region as:
$$
\delta_l=\delta_\mathrm{bg}+\arctan\left(
\frac{\Gamma/2}{E_0-E}\right),
$$
where $\delta_\mathrm{bg}\approx n\pi$ is called **background phase**. Then the cross-section can be written as:
$$
\sigma_l=\frac{4\pi}{k^2}(2l+1)\sin^2\delta_l\approx
\frac{4\pi}{k^2}(2l+1)\frac{(\Gamma/2)^2}{(E_0-E)^2+(\Gamma/2)^2}
$$
which is the **Breit-Wigner distribution**. Around $E=E_0$ there is a **resonance**.

In a bit wider range, the width can be considered energy-dependent, from $\delta_i\propto(kr_0)^{2l+1}$:
$$
\Gamma/2=(kr_0)^{2l+1}\gamma,
$$
where $\gamma$ is a constant.

The S-matrix can be written as:
$$
S_l(k)=e^{2i\delta_l}=\frac{e^{i\delta_l}}{e^{-i\delta_l}}=
\frac{1+i\tan\delta_l}{1-t\tan\delta_l}=
\frac{E-E_0-i\Gamma/2}{E-E_0+i\Gamma/2}.
$$
Therefore resonance manifests itself in the pole of S-matrix at
$$
E=E_0-i\Gamma/2
$$
or
$$
k=k_0-i\eta/2,
$$
where $E_0=\hbar^2k_0^2/2m$ and $\Gamma=\eta\hbar^2k_0/m$. The S-matrix is also equal the ratio of the outgoing to incoming wave amplitude. 

For real negative $E$ there is $k=i\kappa$, so the bound state corresponds to poles at the imaginary $k$ axis. Resonances correspond to metastable states with poles close to real $k$ axis