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