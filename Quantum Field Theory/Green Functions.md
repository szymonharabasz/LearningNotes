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