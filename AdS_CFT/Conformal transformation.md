Since all observers must agree on distances,
$$
g'_{\mu\nu}(x')dx'^\mu dx'^\nu=g_{\mu\nu}(x)dx^\mu dx^\nu.
$$
For the flat metric $\partial_\alpha g_{\mu\nu}=0$, and infinitesimal transformation $x'^\mu=x^\mu+\epsilon^\mu(x)$,
$$
g'_{\mu\nu}=g_{\alpha\beta}
\frac{\partial x^\alpha}{\partial x'^\mu}
\frac{\partial x^\beta}{\partial x'^\nu}=
g_{\mu\nu}-(\partial_\mu\epsilon_\nu+\partial_\nu\epsilon_\nu).
$$
If all the observers are also required to agree on metric, then
$$
\partial_\mu\epsilon_\nu+\partial_\nu\epsilon_\nu=0.
$$
The most general solution involves translations and Lorentz transformations:
$$
\epsilon^\mu=a^\mu+{\omega^\mu}_\nux^\nu.
$$
But if the observers are allowed to disagree on an overall definition of scale, but agree that the metric is flat, then $g'_{\mu\nu}\propto g_{\mu\nu}$, and the constraint becomes
$$
\partial_\mu\epsilon_\nu+\partial_\nu\epsilon_\nu=2\lambda g_{\mu\nu}.
$$
The most general solution is
$$
\epsilon^\mu=a^\mu+{\omega^\mu}_\nu x^\nu+\lambda x^\nu
$$
with the scale transformation called **dilatation**,
$$
x'^\mu=(1+\lambda)x^\mu.
$$
As a final generalization, if the definition of scale may depend on $x$,
$$
g'_{\mu\nu}(x)=\Omega(x)g_{\mu\nu}.
$$
The condition becomes the so-called **conformal Killing equation**:
$$
\partial_\mu\epsilon_\nu+\partial_\nu\epsilon_\nu=2\sigma g_{\mu\nu},
$$
where $\sigma$ is an infinitesimal version of $\Omega$, 
$$
\Omega(x)=e^{-2\sigma(x)}\approx1-2\sigma(x).
$$
One can derive two conditions:
$$
\begin{split}
(d-1)\partial^2\sigma=&0,\\
(2-d)\partial_\mu\partial_\nu\sigma=&g_\mu\nu\partial^2\sigma.
\end{split}
$$
For $d>2$ this means the condition $\partial_\mu\partial_\nu\sigma=0$ which is solved by
$$
\sigma(x)=\lambda+2b\cdot x,
$$
and the solution for $\epsilon$ is
$$
\epsilon^\mu=a^\mu+{\omega^\mu}_\nu x^\nu+\lambda x^\nu+
2(b\cdot x)x^\mu-x^2b^\mu.
$$
These solutions are called **Killing vectors**.
The new part is the **special conformal transformation**.
$$
x'^\mu=x^\mu+2(b\cdot x)x^\mu-x^2b^\mu.
$$
Its Jacobian as
$$
\frac{\partial x'^\mu}{\partial x^\nu}\approx(1+2b\cdot x){R^\mu}_\nu(x),
$$
which is a product of a position-dependent scale factor and an orthogonal matrix
$$
{R^\mu}_\nu(x)=\delta^\mu_\nu+2(b_\nu x^\mu-x_\nub^\mu).
$$
This means that conformal transformations *preserve angles*.

For $d=2$, we can define light-cone coordinates in Minkowski space:
$$
x^+=\frac{x^0+x^1}{2},~~~x^-=\frac{x^0-x^1}{2}
$$
or complex coordinates in Euclidean space:
$$
z=\frac{x^1+ix^2}{2},~~~\bar z=\frac{x^1-ix^2}{2}.
$$
In the former case, if we define
$$
\epsilon^\pm=\epsilon^0\pm\epsilon^1,
$$
then we can take arbitrary functions $\epsilon^+(x^+)$ and $\epsilon^-(x^-)$ and the condition $\partial_\mu\epsilon_\nu+\partial_\nu\epsilon_\nu=2\sigma g_{\mu\nu}$ is automatically satisfied by
$$
\sigma=\frac{1}{2}(\partial_+\epsilon_++\partial_-\epsilon_-).
$$
The same logic applies in the latter case. Thus there are infinitely more conformal transformations in $d=2$ than in higher dimensions.
#### Generators
There are **15** generators:
- Translations: $P_\mu=i\partial_\mu$.
- Lorentz Transformations: $M^{\mu\nu}=i(x^\mu\partial^\nu-x^\nu\partial^\mu)$.
- Scale transformations: $D=ix^\mu\partial_\mu$.
- Special conformal transformations: $K^\mu=i(2x^\mu x^\nu\partial_\nu-x^2\partial^\mu)$.
Commutation relations are
$$
\begin{split}
[M^{\mu\nu},M^{\rho\sigma}]=&-i(g^{\mu\rho}M^{\nu\sigma}-g^{\mu\sigma}M^{\nu\rho}+
g^{\nu\rho}M^{\mu\sigma}+g^{\nu\sigma}M^{\mu\rho}), \\
[M^{mu\nu},P^\rho]=&-i(g^{\mu\rho}P^\nu-g^{\nu\rho}P^\mu), \\
[M^{mu\nu},K^\rho]=&-i(g^{\mu\rho}K^\nu-g^{\nu\rho}K^\mu), \\
[D,P^\mu]=&-iP^\mu, \\
[D,K^\mu]=&~ ~iK^\mu, \\
[P^\mu,K^\nu]=&~2i(g^{\mu\nu}D-M^{\mu\nu}).
\end{split}
$$
This algebra is isomorphic to that of $SO(d+1,1)$ or $SO(d,2)$.

Finite special conformal transformation can be interpreted as coordinate inversion,
$$
x'^\mu=\frac{x^\mu}{x^2},
$$
translation, and inversion again. It is proven by calculating the transformation of $x^2$, neglecting terms of order $b^2$ and writing
$$
\frac{x'^\mu}{x'^2}=\frac{x^\mu}{x^2}-b^\nu.
$$It can be written as
$$
x^\mu=\frac{x^\mu-x^2b^\mu}{1-2b\cdot x+b^2x^2}.
$$

###### Generic recursion relation for solid angle
$$
d\Omega^2_n=d\theta^2+\sin^2\theta d\Omega^2_{n-1}.
$$
#### Compactifications
Inverse stereographic projection is a change of variables:
$$
r=\frac{\sin\psi}{1-\cos\psi},
$$
where $\psi$ is the zenith angle on the sphere with $\psi=0$ being the north pole, and $\psi=\pi$ the south pole. But if one chooses $\psi$ as the Euclidean "time" on the sphere, then the "space" direction is the sphere $S^{d-1}$, whose volume depends on $\psi$. Therefore, the generator of "time" translations is not a symmetry of the system. It is inconvenient in quantum theory.

Another compactification is in Euclidean space is:
$$
\tau=\log(r),~~~r=e^\tau.
$$
The interval becomes
$$
ds^2=e^{2\tau}(d\tau^2+d\Omega^2_{d-1}).
$$
It is flat, the rescaled metric is independent of $\tau$, but it is not fully compact, it represents the geometry of a cylinder instead of a sphere.
#### Classical fields
The conformal transformation can be viewed as acting on fields and the metric:
$$
\begin{split}
\phi(x)\rightarrow &e^{\Delta\sigma(x)}\phi(x),\\
g_{\mu\nu}(x)\rightarrow&e^{2\sigma(x)}g_{\mu\nu}(x),
\end{split}
$$
where $\Delta$ is the **scaling dimension** that for the free fields coincides with units of energy,
$$
\Delta=\frac{d-2}{2}.
$$
In this approach the space-time is curved, so the action must include metric explicitly and can be supplemented with a term depending on the scalar curvature $R$,
$$
S=\int d^dx\sqrt{|g|}\left[
-\frac{1}{2}g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi+\alpha R\phi^2
\right].
$$
The value of $\alpha$ is uniquely defined if the action is to be invariant under the above transformation.

Another view is to assume that the transformation changes fields and coordinates, but not the metric,
$$
\phi(x)\rightarrow e^{\Delta\sigma(x)}\phi(x+\epsilon),
$$
where $\sigma$ and $\epsilon$ are related by the conformal Killing equation,
$$
\sigma=\frac{1}{d}\partial_\mu\epsilon^\mu.
$$
Infinitisemaly,
$$
\phi(x)\rightarrow\left[
1+\frac{d-2}{2d}(\partial_\nu\epsilon^\nu)+e^\nu\partial_\nu
\right]\phi(x).
$$
When the change of the Lagrangian under the transformation $\phi\rightarrow \phi+\delta_\epsilon\phi$ is
$$
{\cal L}\rightarrow {\cal L}+\partial_\mu\Lambda^\mu_\epsilon,
$$
then the Noether current is
$$
J^\mu_\epsilon=\Lambda^\mu_\epsilon-
\frac{\partial{\cal L}}{\partial(\partial_\mu\phi)}\delta_\epsilon\phi.
$$
In this example,
$$
J^\mu_\epsilon=\epsilon_\nu\left(
\partial_\mu\phi\partial^\nu\phi-
\frac{1}{2}g^{\mu\nu}\partial_\rho\phi\partial^\rho\phi
\right) \equiv \epsilon_\mu T^{\mu\nu}_c,
$$
where $T^{\mu\nu}_c$ is the canonical **energy-momentum tensor**, whose divergence is
$$
\partial_\nu T^{\mu\nu}_c=\partial^\mu\phi\partial^2\phi.
$$
It vanishes by equations of motion $\partial^2\phi=0$. For constant $\epsilon$ the current is then conserved, but for $\epsilon$ depending on the space-time, one has:
$$
\partial_\mu J^\mu_\epsilon=(\partial_\nu\epsilon_\mu)T^{\mu\nu}_c.
$$
Because the tensor is symmetric, one can write
$$
\partial_\mu J^\mu_\epsilon=
\frac{1}{2}(\partial_\nu\epsilon_\mu+\partial_\mu\epsilon_\nu)T^{\mu\nu}_c=
\sigma g_{\mu\nu}T^{\mu\nu}_c=
-\frac{d-2}{2}\sigma\partial_\mu\phi\partial^\mu\phi.
$$
For $d>2$ the current is only conserved if $\sigma=0$. This is because the above version of Noether's theorem does not directly apply to the case of a space-dependent parameter. In fact, the energy-momentum tensor is not unique, one can always add a term proportional to
$$
(\partial^\mu\partial^\nu-g^{\mu\nu}\partial^2)\phi^2,
$$
and the tensor conservation is not affected. For example, the combination
$$
T^{\mu\nu}=T^{\mu\nu}_c+\frac{d-2}{2(d-1)}(\partial^\mu\partial^\nu-g^{\mu\nu}\partial^2)\phi^2
$$
is traceless for every $d$. In a field theory with conformal symmetry one can always construct a symmetric, traceless energy-momentum tensor that is conserved when imposing equations of motion. The Noether's theorem only applies to theories with Lagrangian desrciption, but the existence of such a tensor will be always assumed in conformal field theories and will be treated, in a sense, as their "axiom". From this one will deduce a charge conservation
$$
J^\mu=\epsilon_\nu T^{\mu\nu} \Rightarrow 
\partial_\mu J^\mu=\epsilon_\nu\partial_\mu T^{\mu\nu}=0
$$
if equations of motion are obeyed.

The conserved charges are:
$$
\begin{split}
P^\mu=&-i\int d^{d-1}\vec xT^{0\mu}(x),\\
M^{\mu\nu}=&-i\int d^{d-1}\vec x[x^\mu T^{0\nu}(x)x^\nu T^{0\mu}(x)], \\
D=&-i\int d^{d-1}\vec xx_\mu T^{0\mu}(x),\\
K^\mu=&-i\int d^{d-1}\vec x[2x^\mu x_\nu T^{0\nu}(x)-x^2T^{0\mu}(x)].
\end{split}
$$