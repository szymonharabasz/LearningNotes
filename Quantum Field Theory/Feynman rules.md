#### Scalar field
Assuming the interaction term:
$$
{\cal H}_\mathrm{int}=\frac{\lambda}{n!}\phi^n
$$
one has to draw all connected graphs corresponding to given initial and final states and with $n$ lines meeting at each vertex. For each graph:
1. Neglect external legs
2. Energy-momentum conservation is imposed on each internal vertex
3. To each vertex associate a factor $-i\lambda$
4. To each internal line with momentum $p$ associate a propagator:
   $$
   D(p)=\frac{i}{p^2-m^2+i\epsilon}
   $$
5. Integrate over momenta that are not fixed by energy-momentum conservation, with a measure $d^4k_i/(2\pi)^4$.
6. Include a combinatorial factor from $1/N!$ of the exponential expansion, the number of equivalent contractions, and $1/n!$ from the hamiltonian.
The sum of all contributions gives $i{\cal M}_{fi}$, related to the matrix element of the $T$ operator by:
$$
\langle{\bf p}_1,...,{\bf p}_n|T|{\bf k}_1,...,{\bf k}_m\rangle=
(2\pi)^4\delta^{(4)}\left(
\sum_i{\bf p}_i-\sum_j{\bf k}_ji{\cal M}_{fi}
\right),
$$
which in turn is related to the S-matrix by:
$$
S=1+iT.
$$
#### QED
$\Psi$ has a mode expansion with destruction of electron and creation of positron:
$$
\Psi(x)=\int\frac{d^3p}{(2\pi)^3\sqrt{2E_{\bf p}}}\sum_{s=1,2}
(a_{{\bf p},s}u^s(p)e^{-ipx}+
b^\dagger_{{\bf p},s}v^s(p)e^{ipx}).
$$
$\bar\Psi$ has a mode expansion with creation of electron and destruction of positron:
$$
\bar\Psi(x)=\int\frac{d^3p}{(2\pi)^3\sqrt{2E_{\bf p}}}\sum_{s=1,2}
(b_{{\bf p},s}\bar v^s(p)e^{-ipx}+
a^\dagger_{{\bf p},s}\bar u^s(p)e^{ipx}).
$$

$A_\mu$ has a mode expansion with various polarization tensors:
$$
A_\mu(x)=\int\frac{d^3p}{(2\pi)^3\sqrt{2\omega_{\bf p}}}\sum_{\;ambda=0}^3\left(
\epsilon_\mu({\bf p},\lambda)a_{{\bf p},\lambda}e^{-ipx}+
\epsilon^*_\mu({\bf p},\lambda)a^\dagger_{{\bf p},\lambda}e^{ipx}
\right)
$$
Fermion propagator:
$$
\frac{i}{p\!\!\!/-m}.
$$
Photon propagator:
$$
D_{\mu\nu}=\frac{-i}{k^2+i\epsilon}\eta_{\mu\nu}.
$$
Interaction vertex:
$$
-ie\gamma^\mu.
$$
External lines:
1. Final photon: $\epsilon^*_\mu(k)$
2. Initial photon: $\epsilon_\mu(k)$
3. Initial electron: $u^s(p)$
4. Final positron: $v^s(p)$
5. Final electron: $\bar u^s(p)$
6. Initial positron: $\bar v^s(p)$
There is an additional minus sign for each closed fermion loop