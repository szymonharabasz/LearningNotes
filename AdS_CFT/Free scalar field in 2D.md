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
[\bar X(x^0,x^1),\Pi(y^0,y^1)]_{x^0=y^0}=-i\delta(x^1-y^1)
$$
and other equal time commutators are 0.
This gives the algebra of creation and annihilation operators:
$$
[a(k^1),a^\dagger(p^1)]=2\pi\delta(k^1-p^1)
$$
with other commutators equal 0.
N.B., in the book "Non-Perturbative Field Theory" there is no minus sign in field commutator nor $2\pi$ in creation and annihilation operators commutator, but they seem necessary from own calculation.
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
#### Operator Product Expansion
From mode expansion and using a tabulated Fourier transform of $1/|x|$, one gets:
$$
\langle \hat X(z,\bar z)\hat X(w,\bar w)\rangle=-\log|z-w|^2
$$
which can be split into holomorphic and anti-holomorphic parts:
$$
\langle X(z) X(w)\rangle=-\log|z-w|,~~
\langle \bar X(\bar z)\bar X(\bar w)\rangle=-\log|z-w|
$$
Differentiating gives an expression for currents:
$$
J(z)J(w)=-\frac{1}{(z-w)^2}+\mathrm{finite~terms}.
$$
In the case of cylinder-like manifold, one can use $z=e^{x^0+ix^1}$. Space translations take the form of multiplying by a phase $z\rightarrow e^{ia}z$ and time translations are dilatations $z\rightarrow e^{a}z$. Noether currents are written as contour integrals:
$$
Q=\frac{1}{2\pi i}\oint[dz~J(z)+d\bar z~\bar J(\bar z)].
$$
Infinitesimal transformation is a commutator of a generator with an operator. By specific selection of integration contours in the commutator, the difference of two integral can be turned into integral of radial ordered product around the location $w$ of the operator ${\cal O}(w)$:
$$
\delta_{\epsilon,\bar\epsilon}{\cal O}=
\frac{1}{2\pi i}\oint[
dx\epsilon(z)R(J(z){\cal O}(w,\bar w)+
d\bar x\epsilon(\bar z)R(J(\bar z){\cal O}(w,\bar w))
].
$$
The infinitesimal translation is generated by the current $J=\partial X$ as
$$
\delta_\epsilon\bar X(x,\bar w)=
\frac{1}{2\pi i}\oint dz \epsilon(z)R(\partial X(z)\bar X(w,\bar w))=
\frac{1}{2\pi i}\oint dz \frac{-1}{z-w}\epsilon(z)=-\epsilon(w).
$$
When energy-momentum tensor is normal ordered as
$$
:W(w):=-\frac{1}{2}\lim_{z\rightarrow w}\left[
\partial X(z)\partial X(w)+\frac{1}{(z-w)^2},
\right]
$$
the infinitesimal transformation of the current $J=\partial X$, generated by it, becomes:
$$
\delta_\epsilon\partial X(w)=\partial\epsilon(w)X(w)+\epsilon(w)\partial^2X(w).
$$
Another useful OPEs are:
$$
:T(z)::e^{i\alpha X(w)}=
\frac{\alpha^2}{2(z-w)^2}e^{i\alpha X(w)}+
\frac{1}{z-w}\partial e^{i\alpha X(w)}
$$
and
$$
:e^{i\alpha X(z)}::e^{-i\beta X(w)}:=
\frac{:e^{i\alpha X(z)}e^{-i\beta X(w)}:}{(z-w)^{\alpha\beta}}.
$$
There is a rule:
$$
\partial\left(\frac{1}{z}\right)=
\bar\partial\left(\frac{1}{\bar z}\right)=2\pi\delta(z,\bar z).
$$
This can be use together with the fact that the path integral of total derivative is zero:
$$
0=\int{\cal D}\hat X(z,\bar z)
\frac{\delta}{\delta\hat X(z,\bar z)}[e^{-S]\hat X(w,\bar w)}=
\int{\cal D}\hat X(z,\bar z)e^{-S}\left[
-\frac{\delta S}{\delta\hat X(z,\bar z)}\hat X(w,\bar w)+
\delta^2(z-w,\bar z-\bar w)
\right]=
\frac{1}{2\pi}\langle\partial\bar\partial\hat X(z,\bar z)\hat X(w,\bar w)\rangle+
\langle\delta^2(z-w,\bar z-\bar w)\rangle.
$$
From which one deduces that correlation functions obey the equation:
$$
\partial\bar\partial\langle\hat X(z,\bar z)\hat X(w,\bar w)\rangle=
-2\pi\delta^2(z-w,\bar z-\bar w).
$$
By comparing currents related to affine current algebra transformations, $J\partial X$, expanded in Laurent series: 
$$
J=-i\sum_{n=-\infty}^\infty\frac{J_n}{z^{n+1}},
$$
with the mode expansion
$$
\partial X=-i\sum_{n=-\infty}^\infty\frac{\alpha_n}{z^{n+1}}
$$
It is clear that the algebra of generators is that of $\alpha_n$ operators:
$$
[J_m,J_n]=-m\delta_{m+n},~~[\bar J_m,\bar J_n]=-m\delta_{m+n}
$$
Similarly, for hte energy-momentum tensor:
$$
:T:=\sum_{n=-\infty}^\infty\frac{L_n}{z^{n+1}},
$$
one can find:
$$
L_n=\frac{1}{2}\sum_{m=-\infty}^\infty:\alpha_{n-m}\alpha_m:.
$$
and
$$
L_0=\frac{1}{2}{\cal P}^2+\sum_m=1^\infty\alpha_{-m}\alpha_m.
$$
Naively calculating the algebra:
$$
[L_m,L_n]=(m-n)L_{m+n},
$$
which is correct classically and for $m\neq-n$.
One can derive the corrections that are necessary due to normal ordering to get the full
Virasoro algebra:
$$
[L_m,L_n]=(m-n)L_{m+n}+\frac{1}{12}m(m^2-1)\delta_{m+1}.
$$
