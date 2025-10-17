With the definitions:
$$
\xi=x^0+ix^1,~\partial_\xi=\frac{1}{2}(\partial_0-i\partial_1)
$$
and $z=e^\xi$, the actions can be written as:
$$
S=\int d^2x{\cal L}=
\frac{1}{8\pi}\int d^2x\partial_\nu\hat X\partial^\nu\hat X=
\frac{1}{4\pi}\int d^2\xi\partial_\xi\hat X\partial_{\bar \xi}\hat X=
\frac{1}{4\pi}\int d^2z\partial_z\hat X\partial_{\bar z}\hat X,
$$
where
$$
d^2\xi=\frac{i}{2}d\xi\wedge d\bar\xi,~d^2\z=\frac{i}{2}dz\wedge d\barz
$$
The Euler-Lagrange equation:
$$
\partial\bar\partial\hat X=0
$$
has the most general solution:
$$
\hat X(z,\bar z)=X(z) + \bar X(\bar z).
$$
It is invariant under translations, SO(2) rotations:
$$
\delta z=-i\epsilon z,~\delta\bar z =i\epsilon\bar z,
$$
and affine current algebra transformations:
$$
\hat X(z,\bar z)\rightarrow \hat X(z,\bar z)+A(z),~
\hat X(z,\bar z)\rightarrow \hat X(z,\bar z)+\bar A(\bar z),
$$
where $A(z)$, $\bar A(\bar z)$ are arbitrary holomorphic and anti-holomorphic functions.
(N.B., anti-holomorphic is a function whose complex conjugate is holomorphic).
The currents obtained from infinitesimal affine current algebra transformations:
$$
J=\partial X,~\bar J=\bar\partial\bar X
$$
are holomorphic and anti-holomorphic conserved:
$$
\bar\partial J=0=\partial\bar J.
$$
Space-time translations can be elevated to holomorphic and anti-holomorphic transformations:
$$
z\rightarrow f(z),~\bar z\rightarrow\bar f(\bar z).
$$
The infinitesimal version gives rise to holomorphic and anti-holomorphic conserved **energy-momentum tensor**:
$$
T=-\frac{1}{2}\partial X\partial X,~
\bar T=-\frac{1}{2}\bar\partial\bar X\bar\partial\bar X.
$$
#### Mode expansion
In the case of infinite plane, it is:
$$
\hat X(x^0,x^1)=\int\frac{dk^1}{\sqrt{2\pi}\sqrt{k^0}}
[a(k^1)e^{-ikx}+a^\dagger(k^1)e^{ikx}].
$$
For closed strings, periodic boundary conditions, $\hat X(x^0,x^1)=\hat X(x^0,x^1+2\pi)$ , are automatically obeyed, therefore one can write a Laurent series:
$$
\partial X=-i\sum_{n=-\infty}^\infty\frac{\alpha_n}{z^{n+1}},~
\bar\partial \bar X=-i\sum_{n=-\infty}^\infty\frac{\bar\alpha_n}{\bar z^{n+1}},
$$
whch can be integrated to get:
$$
\hat X(z,\bar z)={\cal X}-i{\cal P}\ln(z\bar z)+
i\sum_{m--\infty,m\neq 0}^\infty\left(
\frac{\alpha_m}{m}z^{-m}+\frac{\bar\alpha_m}{m}\bar z^{-m}
\right),
$$
where $\cal X$ is a constant and ${\cal P}=a_0=\bar a_0$.

For open strings, there are Neumann type boundary conditions:
$$
\partial_1\hat X(x^0,x^1=0)=\partial_1\hat X(x^0,x^1=\pi)=0\Rightarrow
\partial\hat X(z,\bar z=z)=\bar\partial\hat X(z,\bar z=z).
$$
and the corresponding mode expansion is:
$$
\hat X(z,\bar z)=
{\cal X}-i{\cal P}\ln(z\bar z)+
i\sum_{m--\infty,m\neq 0}^\infty\frac{\alpha_m}{m}\left(
z^{-m}+\bar z^{-m}
\right),
$$
#### Canonical quanization
Momentum conjugate to $\bar X(z,\bar z)$ is
$$
\Pi=\frac{1}{4\pi}\partial_0\bar X.
$$
Quantization conditions are:
$$
[\bar X(x^0,x^1),\Pi(y^0,y^1)]_{x^0=y^0}=i\delta(x^1-y^1)
$$
and other equal time commutators are 0.
This gives the algebra of creation and annihilation operators:
$$
[a(k^1),a^\dagger(p^1)]=\delta(k^1-p^1)
$$
with other commutators equal 0.
Thus, energy-momentum operators are proportional to $a^\dagger(k)a(k)+a(k)a^\dagger(k)$, and their vacuum expectation values are proportional to $\delta(0)~L$, where $L$ is the extent of the space direction, which diverges for infinite Minkowski or Euclidean space. Therefore one defines a normal ordered operators as:
$$
:{\cal O}:={\cal O}-\langle 0|{\cal O}|0\rangle.
$$
For $\alpha_n$ operators on open string and for $\alpha_n$ and $\bar \alpha_n$ operators on closed strings the algebra is as follows:
$$
[\alpha_m,\alpha_n]=m\delta_{m+n},
$$
$$
[\bar\alpha_m,\bar\alpha_n]=m\delta_{m+n},
$$
$$
[\alpha_m,\bar\alpha_n]=0.
$$
One can infer that:
$$
\alpha_m=\sqrt{m}a(m),~m>0;~~\alpha_{-m}=\sqrt{m}a^\dagger(m),~m>0.
$$