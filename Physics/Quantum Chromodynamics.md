Pauli matrices:
$$
\sigma_1=\left(
\begin{matrix}
0 & 1 \\
1 & 0
\end{matrix}
\right),\;
\sigma_2=\left(
\begin{matrix}
0 & -i \\
i & 0
\end{matrix}
\right),\;
\sigma_3=\left(
\begin{matrix}
1 & 0 \\
0 & -1
\end{matrix}
\right).
$$
Dirac matrices, which anticommute:
$$
\gamma^0=\sigma^3\otimes I_2,\;\gamma^j=i\sigma^2\otimes\sigma^j
$$
$\gamma_5=\gamma_0\gamma_1\gamma_2\gamma_3\gamma_4$ anticommutes with all of them, $\gamma_5^2=1$.
Gell-Mann matrices:
$$
\begin{eqnarray}
\lambda_1=\left(
\begin{matrix}
0 & 1 & 0\\
1 & 0 & 0\\
0 & 0 & 0
\end{matrix}
\right),\;

\lambda_2=\left(
\begin{matrix}
0 & -i & 0\\
i & 0 & 0\\
0 & 0 & 0
\end{matrix}
\right),\;

\lambda_3=\left(
\begin{matrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 0
\end{matrix}
\right),\;

\lambda_4=\left(
\begin{matrix}
0 & 0 & 1\\
0 & 0 & 0\\
1 & 0 & 0
\end{matrix}
\right),\;

\\

\lambda_5=\left(
\begin{matrix}
0 & 0 & -i\\
0 & 0 & 0\\
i & 0 & 0
\end{matrix}
\right),\;

\lambda_6=\left(
\begin{matrix}
0 & 0 & 0\\
0 & 0 & 1\\
0 & 1 & 0
\end{matrix}
\right),\;

\lambda_7=\left(
\begin{matrix}
0 & 0 & 0\\
0 & 0 & -i\\
0 & i & 0
\end{matrix}
\right),\;

\lambda_8=\sqrt{\frac{1}{3}}
\left(
\begin{matrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & -2
\end{matrix}
\right),\;
\end{eqnarray}
$$
$\Gamma$ matrices:
$$
1, \gamma^\mu, \gamma_5, \gamma^\mu\gamma^5, 
\mathrm{six\ matrices\ }\sigma^{\mu\nu}=\frac{i}{2}\left[\gamma^\mu,\gamma^\nu\right].
$$

#### Center symmetry
Color gauge transformation:
$$
U(x)=\exp\left(
-i\Theta_a(x)\frac{\lambda^c_a}{2}
\right),
$$
Gluon field transformation:
$$
\mathcal{A}_\mu=\mathcal{A}_{a\mu}\frac{\lambda^c_a}{2}\rightarrow U\mathcal{A}_\mu U^\dagger+\frac{i}{g_3}\partial_\mu UU^\dagger.
$$
Covariant derivative:
$$
D_\mu=\partial_\mu+ig_3\mathcal{A_\mu}
$$
Full Lagrangian:
$$
\mathcal{L}_{QCD}=\sum_{f\in\langle u,d,s,c,b,t\rangle}
\bar q_f\left(iD\!\!\!\!/\;-m_f\right)q_f
-\frac{1}{4}\mathcal{G}_{a\mu\nu}G_a^{\mu\nu}
\bar q_f\left(iD\!\!\!\!/\;-m_f\right)q_f
-\frac{1}{2}\mathrm{Tr}_c(\mathcal{G}_{\mu\nu}G^{\mu\nu}).
$$
Gauge invariance allows also for a $\theta$ term that would be responsible for explicit P and CP violation that would imply, e.g., electric dipole moment of the neutron:
$$
\mathcal{L}_\theta=\frac{g_3^2\bar\theta}{64\pi^2}
\epsilon_{\mu\nu\rho\sigma}\mathcal{G}_a^{\mu\nu}\mathcal{G}_a^{\rho\sigma},\;\epsilon_{0123}=1.
$$
Inside the color $SU(3)$ symmetry there is a hidden center symmetry $Z(3)$ which is valid in. pure gauge theory and approximate in QCD:
$$
\Omega_1=e^{2\pi i/3}\mathbb{1},\ \ \ 
\Omega_2=e^{-2\pi i/3}\mathbb{1},\ \ \ 
\Omega_3=\mathbb{1}.\ \ \  
$$
It is a group, made by constant and diagonal matrices, so gauge fields are invariant under these transformations, because $e^{\pm2\pi i/3}=1$, $\det\Omega_i=1$, so this group is a subgroup of $SU(3)$.
A Wilson line:
$$
L(\vec x)=\mathcal{P}\exp\left(ig\int_0^{1/T}A_0(\tau,\vec x)d\tau\right),
$$
with $A_0(\tau,\vec x)$ acting as effective potential, can be understood as a propagator of an infinitely heavy (no kinetic term in $\exp$) *test quark*. It transform under gauge transformation like:
$$
L(\vec x)\rightarrow U^\dagger(1/T,\vec x)L(\vec x)U(0,\vec x).
$$
Now the gauge transformation of gluons depend on time, we can chose it to be periodic up to $Z(3)$:
$$
U(1/T,\vec x)=e^{2\pi i\nu/3}U(0,\vec x),\ \ \ \nu\in\lbrace -1,0,1\rbrace.
$$
Gluons do not change, because they are invariant under $Z(3)$, but the $L(\vec x)$, propagator can get some phase.
If the vacuum consists of domains where different phases apply, then the propagating *test quark* will pick up phases at random. Random phases add to 0, and the propagator vanishes, the quark does not propagate and is **confined**.
At high temperature $g(T)\sim 1/\log(T)$, so the propagator $\rightarrow 1$ and the quark is **deconfined**.
Closed Wilson line becomes **Wilson loop**:
$$
W(C)=\mathrm{tr}\mathcal{P}\exp\left(ig\oint_CA_\mu(x)dx^\mu\right),
$$
which can be interpreted as creation of quark-antiquark pair, its propagation for some time, and annihilation. It is related to the potential and the time interval over which it is considered. 

In the confined case, the potential is linear, $V\sim\sigma R$, where $\sigma$ - string tension, so the expectation value of the loop behaves as exponential of a quantity proportional to the area enclosed by the loop (**area law**).
In the deconfined case, the expectation value behaves as an exponential of a quantity proportional to the perimeter of the loop (**perimeter law**).

We can write a partition function as an Euclidean path integral:
$$
\mathcal{Z}=\mathrm{Tr}\exp(-\beta H)=\int DA_\mu\exp(-S_E),\ \ \ 
S_E=\frac{1}{4}\int_0^\beta d\tau\int d^3x F_{\mu\nu}F_{\mu\nu},
$$
where periodic boundary conditions are imposed on fields:
$$
A_\mu(\beta, \vec x)=A_\mu(0, \vec x).
$$
This corresponds to quantum field theory with *compactified* Euclidean time.
Now the temporal Wilson loop in Euclidean space that extends over the whole time axis, after compactification becomes a **Polyakov loop** and its charge conjugate:
$$
W(C)\rightarrow P(\vec x)P^\dagger(\vec x +\vec R).
$$
Polyakov loop is a loop that encircles the whole compactified Euclidean time:
$$
P[A_0](\vec x)=\exp\left(ig\int_0^\beta A_0(x_0,\vec x)dx_0\right).
$$
A single loop, as opposed to loop pair, is related to the free energy of single quark:
$$
\langle P(\vec x)\rangle = \exp[-\beta(F_q-F_0)],
$$
In the confined phase, where there are no free quarks, this free energy goes to infinity, so $\langle P(\vec x)\rangle=0$, In the deconfined phase, the free energy is finite, so $\langle P(\vec x)\rangle\neq0$. 

Let there be a gauge field localized on a closed curve $C_1$ in three dimensions. The field corms a **center vortex** if a Wilson loop calculated over a curve $C_2$ gets a non-trivial center element of the gauge group once the curves $C_1$ and $C_2$ are linked in a non-trivial way, that us:
$$
W[A(C_1)](C_2)=z^{L(C_1,C_2)},
$$
where $L(C_1,C_2)$ is the Gauss linking number.

**Lattice data suggest that center vortices are dominant field configurations in the infrared region and are responsible both for deconfinement and chiral symmetry.**
#### Chiral symmetry
Chiral left- and right-handed projectors:
$$
P_{L,R}=\frac{1}{2}\left(1\pm\gamma_5\right).
$$
Chiral fields:
$$
q_{L,R}=P_{L,R}q.
$$
In Minkowski space, because of Lorentz symmetry, $\bar q=q^\dagger\gamma^0$, therefore
$$
\bar q_{L,R} = \bar qP_{R,L}.
$$
*Chiral field is the one, which under parity does not transform into itself or its negative.* Chiral Quarks transform into their parity conjugates:
$$
\begin{eqnarray}
q_R(t,\vec x)\rightarrow \gamma_0 q_L(t,-\vec x)\neq\pm q_R(t,\vec x),\\
q_L(t,\vec x)\rightarrow \gamma_0 q_R(t,-\vec x)\neq\pm q_L(t,\vec x).
\end{eqnarray}
$$
In the ultrarelativistic (or zero-mass) limit chirality equals helicity, i.e., the eigenvalue of:
$$
\vec \sigma\cdot\vec p\chi_\pm=\pm\chi_\pm.
$$

Kinetic term of the free quark Lagrangian (which is the only term in the *chiral limit*):
$$
\bar qD\!\!\!\!/\;q = \bar q_LD\!\!\!\!/\;q_L + \bar q_RD\!\!\!\!/\;q_R
$$
is invariant under the **chiral symmetry** $SU(3)_L\times SU(3)_R$:
$$
\begin{eqnarray}
\left(\begin{matrix}
u_L\\d_L\\s_L
\end{matrix}\right)\rightarrow
U_L\left(\begin{matrix}
u_L\\d_L\\s_L
\end{matrix}\right)
=\exp\left(
-i\sum_{a=1}^8\Theta_{La}\frac{\lambda_a}{2}
\right)
\exp\left(
-i\Theta_L
\right)
\left(\begin{matrix}
u_L\\d_L\\s_L
\end{matrix}\right),
\\
\left(\begin{matrix}
u_R\\d_R\\s_R
\end{matrix}\right)\rightarrow
U_R\left(\begin{matrix}
u_R\\d_R\\s_R
\end{matrix}\right)
=\exp\left(
-i\sum_{a=1}^8\Theta_{Ra}\frac{\lambda_a}{2}
\right)
\exp\left(
-i\Theta_R
\right)
\left(\begin{matrix}
u_R\\d_R\\s_R
\end{matrix}\right)
\end{eqnarray}
$$

From group theory $U(N)=SU(N)\times U(1)$.
Noether currents in the light quark sector for the massless case:
$$
\begin{eqnarray}
L_a^\mu=\bar q_L\gamma^\mu\frac{\lambda_a}{2}q_L,\ 
L^\mu=\bar q_L\gamma^\mu q_L,\\
R_a^\mu=\bar q_R\gamma^\mu\frac{\lambda_a}{2}q_R,\ 
R^\mu=\bar q_R\gamma^\mu q_R.
\end{eqnarray}
$$
One often uses vector and axial-vector currents instead:
$$
\begin{eqnarray}
V_a^\mu&=&R_a^\mu+L_a^\mu=\bar q\gamma^\mu\frac{\lambda_a}{2}q,\\
A_a^\mu&=&R_a^\mu-L_a^\mu=\bar q\gamma^\mu\gamma_5\frac{\lambda_a}{2}q,\\
V^\mu&=&R^\mu+L^\mu = \bar q\gamma^\mu q,\\
A^\mu&=&R^\mu-L^\mu = \bar q\gamma^\mu\gamma_5 g
\end{eqnarray}
$$
They transform like vectors and axial-vectors under parity:
$$
\begin{eqnarray}
P:V_a^\mu(t,\vec x)&\rightarrow& V_a^\mu(t,-\vec x),\\
P:A_a^\mu(t,\vec x)&\rightarrow&-A_a^\mu(t,-\vec x).
\end{eqnarray}
$$
But the singlet axial-vector current is conserved only on the classical level. Quantum corrections destroy the conservation and extra term in the divergence is called **axial anomaly:**
$$
\partial_\mu A^\mu=\frac{3g_3^2}{32\pi^2}
\epsilon_{\mu\nu\rho\sigma}\mathcal{G}_a^{\mu\nu}\mathcal{G}_a^{\rho\sigma},\;\epsilon_{0123}=1.
$$
Factor of 3 comes from the number of flavors, In the $N_c\rightarrow\infty$ limit, the current is again conserved, because $g_3^2\sim N_c^{-1}$.
The $U(1)_A$ symmetry is also broken by topological fluctuations. The effects that break this symmetry are suppressed like $T^{-7}$ in pure gauge or $T^{-8}, T^{-9}$ in QCD. Lattice simulations are needed to know if it happens before the chiral transition.

With the finite quark masses, $\mathcal{M}=\mathrm{diag}(m_u, m_d, m_s)$, the divergences are (not considering anomalies):
$$
\begin{eqnarray}
\partial_\mu L_a^\mu=&
-&i\left(
\bar q_L \frac{\lambda_a}{2}\mathcal{M}q_R-
\bar q_R \mathcal{M}\frac{\lambda_a}{2}q_L
\right),
\\
\partial_\mu R_a^\mu=&
-&i\left(
\bar q_R \frac{\lambda_a}{2}\mathcal{M}q_L-
\bar q_L \mathcal{M}\frac{\lambda_a}{2}q_R
\right),
\\
\partial_\mu L^\mu=&
-&i\left(
\bar q_L \mathcal{M}q_R-
\bar q_R \mathcal{M}q_L
\right),
\\
\partial_\mu R^\mu=&
-&i\left(
\bar q_R \mathcal{M}q_L-
\bar q_L \mathcal{M}q_R
\right).
\end{eqnarray}
$$
This is the origin of the expression ***current-quark masses***. For vector and axial-vector (including anomaly):
$$
\begin{eqnarray}
\partial_\mu V_a^\mu&=&i\bar q\left[\mathcal{M},\frac{\lambda_a}{2}\right],\\
\partial_\mu A_a^\mu&=&
i\bar q\gamma_5\left\lbrace\mathcal{M},\frac{\lambda_a}{2}\right\rbrace,\\
\partial_\mu V^\mu&=&0,\\
\partial_\mu A^\mu&=&2i\bar q\gamma_5\mathcal{M}q+
\epsilon_{\mu\nu\rho\sigma}\mathcal{G}_a^{\mu\nu}\mathcal{G}_a^{\rho\sigma},\;\epsilon_{0123}=1.
\end{eqnarray}
$$
The $U(1)_V$ symmetry leads to **baryon number conservation**.

Noether charges commute with the Hamiltonian:
$$
\left[Q_{La},H_\mathrm{QCD}^0\right]=
\left[Q_{Ra},H_\mathrm{QCD}^0\right]=
\left[Q_{V},H_\mathrm{QCD}^0\right]=0
$$
and their commutation relations are:
$$
\begin{align}
\left[Q_{La},Q_{Lb}\right]&=if_{abc}Q_{Lc}, \\
\left[Q_{La},Q_{Lb}\right]&=if_{abc}R_{Lc}, \\
\left[Q_{La},Q_{Rb}\right]&=0, \\
\left[Q_{La},Q_{V}\right]&=\left[Q_{Ra},Q_{V}\right]=0. \\
\end{align}
$$
So, from the symmetry of the Lagrangian and from the equal time commutation relations *they are generators* of infinitesimal transformations of the Hilbert space associated with $H_\mathrm{QCD}^0$.
###### Ward identities
Generating functional is defined as:
$$
W[\mathcal{J}]=\exp\left(
iZ[\mathcal{J}]
\right)=\langle0|T\left(\exp\left\lbrace
i\int d^4x \mathcal{J}(x)\phi(x)
\right\rbrace\right)|0\rangle,
$$
where there could be as many external currents $\mathcal{J}$ as there are fields and one can have also external currents $\mathcal{J}_\mu$ coupled to conserved gauge currents $J_\mu$ giving a term $\mathcal{J}_\mu J^\mu$.

Green functions are obtained from functional derivatives of the generating functional, for example, for the complex scalar field $\Phi, \Phi^\dagger$ (coupled to $j^*,j$, respectively) with Lagrangian invariant under U(1) symmetry having the current $J^\mu$ (coupled to $j_\mu$):
$$
G^\mu(x,y,z)=\langle0|T[\Phi(x)J^\mu(y)\Phi^\dagger(z)]|0\rangle=
(-i)^3\left.
\frac{\delta^3W[j,j^*,j_\mu]}{\delta j^*(x),\delta j_\mu(y),j(z)}
\right|_{j=0,j^*=0,j_\mu=0}
$$
It can be shown that given that Lagrangian is invariant under *global* symmetry transformations, the generating functional becomes invariant under corresponding *local* transformations.

One can also obtain master equations for deriving Ward identities. In the example above it is:
$$
\left[
j(x)\frac{\delta}{\delta j(x)}-
j^*(x)\frac{\delta}{\delta j^*(x)}-
i\partial_\mu\frac{\delta}{\delta j_\mu(x)}
\right]W[j,j^*,j_\mu]=0.
$$

In the chiral symmetry, for example when scalar and pseudoscalar densities are defined as:
$$
S_a(x)=\bar q(x)\lambda_aq(x),\ \ \ P_a(x)=\bar q(x)\gamma_5\lambda_a q(x),
$$
and sometimes one uses for convenience:
$$
S(x)=\bar q(x)q(x),\ \ \ P(x)=\bar q(x)\gamma_5q(x)
$$
instead of $S_0$ and $P_0$, one can have:
$$
G^\mu_{APab}(x,y)=\langle0|T\left[A_a^\mu(x)P_b(y)\right]|0\rangle.
$$
Its divergence is:
$$
\partial_\mu^xG^\mu_{APab}(x,y)=
\delta(x_0-y_0)\langle0|\left[A_a^0(x),P_b(y)\right]|0\rangle+
\langle0|T\left[\partial_\mu A_a^\mu(x)P_b(y)\right]|0\rangle.
$$

###### Chiral symmetry breaking
When a symmetry is broken, the ground state is degenerate and  is invariant only under some subgroup H of the full symmetry group G of the Lagrangian. An infinitesimal perturbation, which can be realized, for example, by adding a term to the Lagrangian that does not have the symmetry G, will lead to selecting an actual ground state.

Generators which belong to H annihilate the ground state, that is, group elements leave the ground state unchanged. They correspond to massive fields. There is a quadratic term in the potential corresponding to this "field direction", so the "restoring force" in this "direction" is linear. Other generators do not annihilate the ground state, that is, group elements do not leave the ground state unchanged. They correspond to massless **Goldstone bosons**, which do not have the quadratic term and the "restoring force" for those "directions" are of higher order.

There are $n=n_G-n_H$ independent Goldstone bosons.

When the symmetry is *explicitly* broken, Goldstone bosons acquire masses proportional to the symmetry breaking parameter (quark mass for the chiral symmetry) and the mass of the massive field is also increased.

In QCD, degeneracy of the minimum of the potential is not readily seen. However, hadron spectrum indicates the presence of generators, that do not annihilate the ground state.
Let:
$$
|\alpha+\rangle=b_{\alpha+}^\dagger|0\rangle
$$
be an eigenstate of QCD Hamiltonian in the chiral limit with eigenvalue $\alpha$ and of parity $+$.
One can define, e.g., the state $|\psi_{a\alpha}\rangle=Q_{Aa}|\alpha+\rangle$, then, using:
$$
\left[Q_{Aa}, b_{\alpha+}^\dagger\right]=b_{\beta-}^\dagger t_{a,\beta\alpha},
$$
one has:
$$
Q_{Aa}|\alpha+\rangle=Q_{Aa}b_{\alpha+}^\dagger|0\rangle=
\left(\left[Q_{Aa}, b_{\alpha+}^\dagger\right]+
b_{\alpha+}^\dagger Q_{Aa}\right)|0\rangle\stackrel{?}{=}
t_{a,\beta\alpha}b_{\beta-}^\dagger|0\rangle.
$$
If $Q_{Aa}$ annihilates the ground state, the state with positive parity would be a linear combination of members of the multiplet with negative parity. But if, for example, $|\alpha+\rangle$ belongs to baryon octet, then the low-energy baryon spectrun does not contain baryon octet of negative parity. Therefore we assume that $Q_{Aa}|0\rangle\neq 0$, so there are generators which do not annihilate the ground state and the chiral symmetry is spontaneously broken.

Btw., the existence of mass-degenerate states of opposite parity is called **parity doubling**.

###### The scalar singlet quark condensate
We write nine scalar quark densities (similar for pseudoscalar):
$$
S_a(y)=\bar q(y)\lambda_aq(y),\ \ \ a=0,...,8.
$$
By calculating general equal time commutators, one can find:
$$
\begin{align}
\left[
Q_{Va}(t),S_0(t,\vec y)
\right]&=0,&\ \ \ a=1,...,8\\
\left[
Q_{Va}(t),S_b(t,\vec y)
\right]&=
i\sum_{c=1}^8f_{abc}S_c(t,\vec y).&\ \ \ a,b=1,...,8
\end{align}
$$
This means that the scalar quark densities transform as a singlet and as an octet, respectively. In fact, charge operators are time-independent, because they correspond to conserved quantities (in the $SU(3)_V$ and even more restrictive chiral limit). For the octet, 
using
$$
\sum_{a,b=1}^8f_{abc}f_{abd}=3\delta_{cd},
$$
one can write:
$$
S_a(t,\vec y)=-\frac{i}{3}\sum_{b,c=1}^8f_{abc}
\left[
Q_{Vb}(t),S_c(t,\vec y)
\right].
$$
In the chiral limit, the ground state is necessary invariant under $SU(3)_V$, that is, 
$$
Q_{Va}|0\rangle=0.
$$
Therefore:
$$
\langle0|S_a(t,\vec y)|0\rangle
\stackrel{\mathrm{trans.\ inv.\ of\ }|0\rangle}{=}
\langle0|S_a(0)|0\rangle\equiv\langle S_a\rangle = 0,\ \ \ a=1,...,8.
$$
For $a=3$ this gives:
$$
\langle\bar uu\rangle-\langle\bar dd\rangle=0,
$$
and for $a=8$:
$$
\langle\bar uu\rangle+\langle\bar dd\rangle-2\langle\bar ss\rangle=0,
$$
and thus:
$$
\langle\bar uu\rangle=\langle\bar dd\rangle=\langle\bar ss\rangle.
$$
For the singlet, because the commutator is 0, we cannot use similar argument to prove that $\langle S_0\rangle=0$. So we **assume that it is not zero**, and use the above equality:
$$
0\neq\langle\bar qq\rangle=\langle\bar uu+\bar dd+\bar ss\rangle
=3\langle\bar uu\rangle
=3\langle\bar qq\rangle
=3\langle\bar ss\rangle.
$$
Finally, one can derive:
$$
i\left[
Q_{Aa}(t),P_a(t,\vec y)
\right]=
\left\lbrace
\begin{align}
\bar uu + \bar dd,&\ \ \ a=1,2,3 \\
\bar uu + \bar ss,&\ \ \ a=4,5 \\
\bar dd + \bar ss,&\ \ \ a=6,7 \\
\frac{1}{3}\left(\bar uu + \bar dd + 4\bar ss\right),&\ \ \ a=8
\end{align}
\right..
$$
We evaluate this for the ground state invariant under $SU(3)_V$ (assuming non-vanishing $\langle\bar qq\rangle$):
$$
\langle0|i\left[
Q_{Aa}(t),P_a(t,\vec y)
\right]|0\rangle=\frac{2}{3}\langle\bar qq\rangle,\ \ \ a=1,...,8.
$$
Inserting a complete set of states into the commutator, one can see, that both the pseudoscalar quark densities $P_a(t,\vec y)$, and the axial charge operators $Q_{Aa}(t)$ must have non-vanishing matrix elements between the vacuum and a massless one particle state $|\phi_b\rangle$. This means that generators $Q_{Aa}$ do not annihilate the ground state and **the non-vanishing quark condensate is a sufficient (but not necessary) condition for chiral symmetry breaking**.
In particular:
$$
\langle0|A_a^\mu(0)|\phi_b(p)\rangle=ip^\mu F_0\delta_{ab},
$$
where $F_0$ is pion decay constant. **The non-vanishing pion decay constant is necessary and sufficient condition for chiral symmetry breaking.**

