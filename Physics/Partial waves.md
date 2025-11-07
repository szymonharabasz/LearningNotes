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
a_l(k)=\frac{e^{2i\delta_l}-1}{2ik}.
$$