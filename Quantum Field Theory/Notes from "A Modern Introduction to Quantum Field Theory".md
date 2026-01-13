#### Lorentz group

$$
\Lambda_{\  \  \nu}^{\mu} = \delta_{\nu}^{\mu} + \omega_{\  \  \  \nu}^{\mu} ,
$$
$$
\phi_{i} \rightarrow \left\lbrack e^{- \frac{i}{2} \omega_{\mu \nu} J_{R}^{\mu \nu}} \right\rbrack_{\  j}^{i} \phi^{j}
$$
#### Vector representation
$$
\left( J^{\mu \nu} \right)_{\  \  \sigma}^{\rho} = i \left( \eta^{\mu \rho} \delta_{\sigma}^{\nu} - \eta^{\nu \rho} \delta_{\sigma}^{\mu} \right)
$$
Vectors $$J^{i} = \frac{1}{2} \epsilon^{i j k} J^{j k}$$ and $$K^{i} = J^{i 0}$$ Follow SU(2) algebra. Defining: $$\theta^{i} = \epsilon^{i j k} \omega^{j k},$$$$\eta^{i} = \omega^{i 0}$$ one can write:
$$
\Lambda = e^{- i \mathbf{\theta J} + i \mathbf{\eta K}}
$$
Generators of the adjoint representation are: $${\left( T_{a d j}^{a} \right)^{b}}_c = - i {f^{a b}}_c$$With respect an SO(3) transformation: $$V^{\mu} \in 0 \oplus 1,$$$$
\begin{split}
T^{\mu \nu} \in & ( 0 \oplus 1 ) \otimes ( 0 \oplus 1 ) = ( 0 \otimes 0 ) \oplus ( 0 \otimes 1 ) \oplus ( 1 \otimes 0 ) \oplus ( 1 \otimes 1 ) = \\
& \underbrace{0}_\mathrm{tensor~trace} \oplus 
\underbrace{1 \oplus 1}_\mathrm{antisymmetric~tensor~(two~vectors)} \oplus 
\underbrace{( 0 \oplus 1 \oplus 2 ),}_\mathrm{antisymmetric~traceless~tensor}
\end{split}
$$
###### Spinor representations of Lorentz group
SU(2) representations of spin $\frac{1}{2}$. Generators are: $$\mathbf{J} = \frac{\mathbf{\sigma}}{2}.$$This one, and not SO(3) represents rotations, because the sign change after rotation by $2 \pi$ does not have physical consequences and leads to the same state. The generators $$\overrightarrow{J}^{\pm} = \frac{1}{2} \left( \overrightarrow{J} \pm i \overrightarrow{K} \right)$$ follow SU(2) algebra and commute with each other (however it does not mean that $SU(2)\times SU(2)=SO(3)$). Because $$\overrightarrow{J} = \overrightarrow{J}^{+} + \overrightarrow{J}^{-},$$one has:
$$\left| j_{-} - j_{+} \right| \leq j \leq j_{-} + j_{+}$$
1.  (0,0) is scalar representation, because: $$\overrightarrow{J} = \overrightarrow{K} = 0$$
2.  Spinor representations: $$\psi_{L} \in \left( \frac{1}{2} , 0 \right)~~~\mathrm{and}~~~\psi_{R} \in \left( 0 , \frac{1}{2} \right)$$For left-handed representation: $$\overrightarrow{J} = \frac{\overrightarrow{\sigma}}{2},$$and $$\overrightarrow{K} = i \frac{\overrightarrow{\sigma}}{2}$$is not hermitian. This is because Lorentz group is not compact and there is a theorem, that non-compact groups do not have unitary representation of finite dimension. except such, in which non-compact generators are represented trivially, that is, by zero.   

$$\Lambda_{L} = e^{\left( - i \overrightarrow{\theta} - \overrightarrow{\eta} \right) \frac{\overrightarrow{\sigma}}{2}}\Lambda_{R} = e^{\left( - i \overrightarrow{\theta} + \overrightarrow{\eta} \right) \frac{\overrightarrow{\sigma}}{2}}$$Charge cojugation is defined as: $$\psi_{L}^{C} = i \sigma^{2} \psi^{*}_{L} \in \left( 0 , \frac{1}{2} \right),$$(where one uses the fact that $\sigma^{2} \Lambda_{L}^{*} \sigma^{2} = \Lambda_{R}$ and $\sigma^{2} \sigma^{2} = 1$)$$\psi_{R}^{C} = - i \sigma^{2} \psi^{*}_{R} \in \left( \frac{1}{2} , 0 \right)\left( \psi_{L}^{C} \right)^{C} = \psi_{L}$$
3.  The representation $$\left( \frac{1}{2} , \frac{1}{2} \right)$$ is complex vector representation (because $j = 0 , 1$). States have the form:  
$$\left( \left( \psi_{L} \right)_{\alpha} , \left( \psi_{R} \right)_{\beta} \right) , \  \  \alpha , \beta = 1 , 0$$States $\xi_{R}^{\dagger} \sigma^{\mu} \psi_{R}$ and $\xi_{L}^{\dagger} \overline{\sigma}^{\mu} \psi_{L}$, where $\sigma^{\mu} = \left( 1 , \overrightarrow{\sigma} \right) , \  \overline{\sigma}^{\mu} = ( 1 , - \overrightarrow{\sigma} )$, are complex four-vectors.

#### Field representations

The representation $$\delta \phi = \phi^{'} \left( x^{'} \right) - \phi ( x )$$ is one-dimensional, the infinite-dimensional representation is $\delta_{0} \phi = \phi^{'} ( x ) - \phi ( x ) = - \delta x^{\mu} \partial_{\mu} \phi ( x ) = {\frac{i}{2} \omega^{\mu \nu} \left( J_{\mu \nu} \right)_{\  \  \  \sigma}^{\rho} \delta x^{\sigma} \  \partial_{\rho} \phi \equiv - \frac{i}{2} \omega^{\mu \nu} \  L_{\mu \nu}}$, where $L^{\mu \nu} = i \left( x^{\mu} \partial^{\nu} - x^{\nu} \partial^{\mu} \right)$.
###### Weyl and Dirac Fields

$$
\psi_{L} ( x ) \rightarrow \psi_{L}^{'} \left( x^{'} \right) = \Lambda_{L} \psi_{L} ( x )
$$

$$
\delta_{0} \psi_{L} = \left( \Lambda_{L} - 1 \right) \psi_{L} ( x ) - \delta x^{\rho} \partial_{\rho} \psi_{L} ( x ) = \left( e^{- {\frac{i}{2} \ } \omega_{\mu \nu} S^{\mu \nu}} - 1 \right) \psi_{L} ( x ) - {\frac{i}{2} \ } \omega_{\mu \nu} L^{\mu \nu} \psi_{L} ( x ) - {\frac{i}{2} \ } \omega_{\mu \nu} \left( S^{\mu \nu} + L^{\mu \nu} \right) \psi_{L} ( x ) = - {\frac{i}{2} \ } \omega_{\mu \nu} J^{\mu \nu} \psi_{L} ( x )
$$

Under the parity transformation:

$$\overrightarrow{J} \rightarrow \overrightarrow{J} , \  \  \  \overrightarrow{K} \rightarrow - \overrightarrow{K} , \  \  \  \overrightarrow{J}^{+} \rightarrow \overrightarrow{J}^{-} , \  \left( j_{-} , j_{+} \right) \rightarrow \left( j_{+} \  , j_{-} \right) \neq \left( j_{-} , j_{+} \right),$$so the Weyl field does not represent parity. It is represented by the Dirac field:
$$\Psi = \begin{pmatrix}\psi_{L} \\ \psi_{R}\end{pmatrix}.$$
The Lorentz transform is represented by:
$$
\Lambda_{D} = \begin{pmatrix}\Lambda_{L} & 0 \\ 0 & \Lambda_{R}\end{pmatrix} ,
$$

And the parity transformation:

$$
\Psi ( x ) \rightarrow \begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix} \Psi \left( x^{'} \right) , \  \  \  x^{'} = \left( t , - \overrightarrow{x} \right) .
$$

Charge conjugations is defined as:
$$
\Psi^{C} = - i \begin{pmatrix}0 & \sigma^{2} \\ - \sigma^{2} & 0\end{pmatrix} \Psi^{*}
$$
###### Majorana Field
$$
\Psi_{M} = \begin{pmatrix}\psi_{L} \\ i \sigma^{2} \psi_{L}^{*}\end{pmatrix}
$$
Perhaps it describes neutrinos. It is neutral in the sense that $\Psi_{M}^{C} = \Psi_{M}$ (the condition $\Psi_{M}^{*} = \Psi$ would not be Lorentzian invariant).

##### Vector Field
It belongs to the representation $\left( \frac{1}{2} , \frac{1}{2} \right)$, so it represents parity. $$

V^{\mu} ( x ) \rightarrow V^{' \mu} \left( x^{'} \right) = \Lambda_{\  \  \nu}^{\mu} V^{\nu} ( x )
$$
We assume that all fields are scalar with respect to translation, i.e., $\epsilon^{\mu} \partial_{\mu} \phi ( x ) = i \epsilon^{\mu} P_{\mu} \phi ( x )$, which means $\delta_{0} \phi = - P_{\mu} = i \partial_{\mu}$.
##### Representations on states from Hilbert space
Wigner's theorem states that symmetries are represented by unitary operators. Representations are numbered by the eigenvalues of Casimir operators, e.g.:
$$
P_{\mu} P^{\mu} \rightarrow - m^{2} , \  W_{\mu} W^{\mu} , \  W^{\mu} = - \frac{1}{2} \epsilon^{\mu \nu \rho \sigma} J_{\nu \rho} P_{\sigma}
$$
It is a Lorentz-invariant Pauli-Lubański vector.
###### Massive representation
Select the rest frame and $W_{\mu} W^{\mu} = - m^{2} j ( j + 1 )$. The representation is numbered by the mass and spin of the particle, and the states differ in the spin projection.
###### Massless representation
We select $P^{\mu} = ( \omega , 0 , 0 , \omega )$ and the small group is SU(2). Representations are numbered by an eigenvalue $h$ of the operator $J_3$ called *helicity*. An algebraic proof that $h = 0 , \pm \frac{1}{2} . \pm 1 , \ldots$ doesn't work, because there is no $ J_{1} , J_{2}$, but a certain topological proof works.
#### Symmetries and laws conservation laws
$$
x^\mu\rightarrow x'^\mu=x^\mu+\epsilon^\alpha A^\mu_\alpha(x),
$$
$$
\phi_i(x)\rightarrow\phi'_i(x')=
\phi_i(x)+\epsilon^\alpha F_{i\alpha}(\phi,\partial\phi)
$$

If the transformation is only a global symmetry, then assuming that the parameter $\epsilon$ is not a constant, but changes slowly:
$$
S \left( \phi^{'} \right) = S ( \phi ) + \int_{}^{} {d^{4} x} \left\lbrack \epsilon^{\alpha} K_{\alpha} ( \phi ) - \left( \partial_{\mu} \epsilon^{\alpha} j_{\alpha}^{\mu} ( \phi ) \right) + O ( \partial \  \partial \epsilon ) \right\rbrack + O ( \epsilon^{2} )
$$
In the case where it is constant, we have symmetry and $S \left( \phi^{'} \right) = S ( \phi ) , \  K = 0$. And when $\epsilon \rightarrow 0 , \  x \rightarrow \infty$, then:

$$
S \left( \phi^{'} \right) = S ( \phi ) + \int_{}^{} {d^{4} x \epsilon^{\alpha} \partial_{\mu} j_{\alpha}^{\mu} ( x )} + O ( \partial \partial \epsilon ) + O ( \epsilon^{2} )
$$
By change of variables in the action we have $x^{\mu} \rightarrow x^{\mu}$ and $\phi_{i} ( x ) \rightarrow \phi_{i} \left( x - \epsilon^{\alpha} A_{\alpha} \right) + \epsilon^{\alpha} F_{i \alpha} = \phi_{i} ( x ) - \epsilon^{\alpha} \partial_{\mu} \phi_{i} A_{\alpha}^{\mu} + \epsilon^{\alpha} F_{i \alpha} = \phi_{i} ( x ) + \delta \phi_{i} ( x )$. The last term is the same variation as when solving the equations of motions and goes to zero when $x \rightarrow \infty$.  If $\phi_{i} ( x )$ solves classical equations of motion, the integral must vanish independently of  $\epsilon$ and so:
$$
\partial_{\mu} j_{\alpha}^{\mu} \left( \phi^{c l} \right) = 0 .
$$

The variation of the action under the transformation contains a term proportional to $\epsilon^\alpha$ equal:
$$
j_{\alpha}^{\mu} = \frac{\partial L}{\partial \left( \partial_{\mu} \phi_{i} \right)} \left\lbrack A_{\alpha}^{\nu} \partial_{\nu} \phi_{i} - F_{i \alpha} ( \phi , \partial \phi ) \right\rbrack - A_{\alpha}^{\mu} L .
$$

If now $\epsilon$ **is not global symmetry**, then $K_{\alpha} ( \phi ) \neq 0$, but $K_{\alpha} ( \phi ) = \left( \delta_{\alpha} L \right)_{g l o b a l}$ where $( \delta L )_{g l o b a l} = {\epsilon^{\alpha} \left( \delta_{\alpha} L \right)}_{g l o b a l}$, under the of global  **transformation**. Then:
$$
\partial_{\mu} j_{\alpha}^{\mu} \left( \phi^{c l} \right) = - \left( \delta_{\alpha} L \right)_{g l o b a l} .
$$
Under the translation, all fields are scalars ($\alpha$ becomes a Lorentz index). Then from  $x^{\mu} \rightarrow x^{' \mu} + \epsilon^{\nu} \delta_{\nu}^{\mu}$ and $\phi_{i} ( x ) \rightarrow \phi_{i}^{'} \left( x^{'} \right) = \phi_{i} ( x ) A_{\nu}^{\mu} = \delta_{\nu}^{\mu}$ it follows that $F_{i \nu} = 0$
The energy-momentum tensor, defined as $\theta_{\  \  \  \nu}^{\mu} = j_{( \nu )}^{\mu}$, is equal:
$$
\theta^{\mu \nu} = \frac{\partial L}{\partial \left( \partial_{\mu} \phi_{i} \right)} \partial^{\nu} \phi_{i} - \eta^{\mu \nu} L .
$$

The charge associated with the symmetry transformation is the average value of the generator expressed as an operator acting on the field between states. For example, for U(1) $j_{\mu} = i \phi^{*} \overset{\overleftrightarrow{}}{\partial}_{\mu} \phi$ and $$Q_{U ( 1 )} = \int_{}^{} {d^{3} x j^{0} = i \int_{}^{} {d^{3} x \phi^{*} \overset{\overleftrightarrow{}}{\partial}_{0} \phi \equiv \left\langle \phi | \phi \right\rangle} = \left\langle \phi | I | \phi \right\rangle}$$

#### Classical Fields
For the Weyl field, $\mathcal{L}_{L} = i \psi_{L}^{\dagger} \overline{\sigma}^{\mu} \partial_{\mu} \psi_{L}$ and the plane-wave solution $\psi_{L} = u_{L} e^{- i p x}$ has $h = - \frac{1}{2}$

For the Dirac field $\mathcal{L}_{D} = i \psi_{L}^{\dagger} \overline{\sigma}^{\mu} \partial_{\mu} \psi_{L} + i \psi_{R}^{\dagger} \sigma^{\mu} \partial_{\mu} \psi_{R} - m ( \psi_{L}^{\dagger} \psi_{R} + \psi_{R}^{\dagger} \psi_{L} )$. 
Chiral representation: $$ \psi = \begin{pmatrix}\psi_{L} \\ \psi_{R}\end{pmatrix} , \  \gamma^{\mu} = \begin{pmatrix}0 & \sigma^{\mu} \\ \overline{\sigma}^{\mu} & 0\end{pmatrix} , \  \overline{\psi} \equiv \psi^{\dagger} \gamma^{0} = ( \psi_{R}^{\dagger} , \psi_{L}^{\dagger} ) $$
and
$$
\mathcal{L}_{D} = \overline{\psi} ( i \partial - m ) \psi 
$$
Other relate to the chiral one by $\psi^{'} = U \psi$, where $U$ is a unitary operator, e.g. for a standard representation $U = \frac{1}{\sqrt{2}} \begin{pmatrix}1 & 1 \\ - 1 & 1\end{pmatrix}$. 

Operators $J^{\mu \nu} = \frac{\sigma^{\mu \nu}}{2} , \  \sigma^{\mu \nu} = \frac{1}{2} \left\lbrack \gamma^{\mu} , \gamma^{\nu} \right\rbrack$ (Dirac algebra: $\left\{ \gamma^{\mu} , \gamma^{\nu} \right\} = 2 \eta^{\mu \nu}$ gives a reducible representation of the Lorentz group).
#### Chiral symmetry
Introduce a global transformation of the Dirac field:
$$
\psi_{L} \rightarrow e^{i \theta_{L}} \psi_{L} , \  \psi_{R} \rightarrow e^{i \theta_{R}} \psi_{R} ,
$$
Which for $\theta_{R} = \theta_{L} = \alpha$ is a vector transform U(1) $\psi \rightarrow e^{i \alpha} \psi$ and for $\theta_{R} = - \theta_{L} = \beta$ is the chiral transformation $\psi \rightarrow e^{i \beta \gamma_{5}} \psi   , \  \gamma_{5} = i \gamma^{0} \gamma^{1} \gamma^{2} \gamma^{3}$. Both are symmetries for $m=0$. Noether currents are:
$$
j_{V}^{\mu} = \overline{\psi} \gamma^{\mu} \psi , \  j_{A}^{\mu} = \overline{\psi} \gamma^{\mu} \gamma_{5} \psi .
$$
For $m\neq 0$, the symmetry is broken:
$$
\partial_{\mu} j_{A}^{\mu} = 2 \mathrm{Im} \overline{\psi} \gamma_{5} \psi
$$
#### LZS reduction formula
$$
\left( 2 E_{\mathbf{k}} \right)^{\frac{1}{2}} a_{\mathbf{k}}^{\dagger \left( \frac{i n}{o u t} \right)} = - i Z^{- \frac{1}{2}} \lim_{t \rightarrow \mp \infty} {\int_{}^{} {d^{3} x} e^{- i k x} \overset{\overleftrightarrow{}}{\partial}_{0}} \phi
$$
$$
\left( 2 E_{\mathbf{k}} \right)^{\frac{1}{2}} \left( a_{\mathbf{k}}^{\dagger ( i n )} - a_{\mathbf{k}}^{\dagger ( o u t )} \right) = i Z^{- \frac{1}{2}} \int_{}^{} {d^{4} x} \partial_{0} \left( e^{- i k x} \overset{\overleftrightarrow{}}{\partial}_{0} \phi \right) = i Z^{- \frac{1}{2}} \int_{}^{} {d^{4} x} e^{- i k x} \left( \blacksquare_{x} + m^{2} \right) \phi
$$
(the last equality is valid if convoluted with a wave package). Similarly:
$$
\left( 2 E_{\mathbf{p}} \right)^{\frac{1}{2}} \left( a_{\mathbf{p}}^{( o u t )} - a_{\mathbf{p}}^{( i n )} \right) = i Z^{- \frac{1}{2}} \int_{}^{} {d^{4} y} e^{i p y} \left( \blacksquare_{y} + m^{2} \right) \phi
$$
$$
\left\langle \mathbf{p}_{1} , \ldots , \mathbf{p}_{n} ; T_{f} | \mathbf{k}_{1} , \ldots , \mathbf{k}_{m} ; T_{i} \right\rangle = \left( i Z^{- \frac{1}{2}} \right)^{n + m} \int_{}^{} {\prod_{i = 1}^{m} {d^{4} x_{i}} \prod_{j = 1}^{n} {d^{4} y_{j}} \exp \left( i \sum_{j = 1}^{n} {p_{j} y_{j}} - i \sum_{i = 1}^{m} {k_{i} x_{i}} \right)} \left( \blacksquare_{x_{1}} + m^{2} \right) \times \ldots \times \left( \blacksquare_{y_{n}} + m^{2} \right) \left\langle 0 \left| T \left( \phi \left( x_{1} \right) \ldots \phi \left( y_{n} \right) \right) \right| 0 \right\rangle = \left\langle \mathbf{p}_{1} , \ldots , \mathbf{p}_{n} | S | \mathbf{k}_{1} , \ldots , \mathbf{k}_{m} \right\rangle_{S c h r o e d i n g e r} = \left\langle \mathbf{p}_{1} , \ldots , \mathbf{p}_{n} | i T | \mathbf{k}_{1} , \ldots , \mathbf{k}_{m} \right\rangle_{S c h r o e d i n g e r}
$$
(The last equality is correct assuming that there are no spectators.) Temporal evolution operator:
$$
U \left( t , t_{0} \right) \equiv e^{i H_{0} \left( t - t_{0} \right)} e^{- i H \left( t - t_{0} \right)}
$$
$$
\phi_{H} \left( t , \mathbf{x} \right) \mathbf{=} e^{i H \tau} \phi_{S} \left( t_{0} , \mathbf{x} \right) e^{- i H \tau} {= e}^{i H \tau} e^{- i H_{0} \tau} \left\lbrack e^{i H_{0} \tau} \phi_{S} \left( t_{0} , \mathbf{x} \right) e^{- i H_{0} \tau} \right\rbrack e^{i H_{0} \tau} e^{- i H \tau} \equiv e^{i H \tau} e^{- i H_{0} \tau} \phi_{I} \left( t , \mathbf{x} \right) e^{i H_{0} \tau} e^{- i H \tau} = U^{\dagger} \left( t , t_{0} \right) \phi_{I} \left( t , \mathbf{x} \right) U \left( t , t_{0} \right) .
$$
The penultimate equality is the definition of the evolution of the operator in the interaction picture, $\tau = t - t_{0}$.
$$
H_{I} \equiv e^{i H_{0} \tau} H_{i n t} e^{- i H_{0} \tau}
$$
$$
U \left( t , t_{0} \right) = T \exp \left( - i \int_{t_{0}}^{t} {d t^{'} H_{I} ( t ' )} \right)
$$
$$
\left\langle 0 | \phi \left( x_{1} \right) \ldots \phi \left( x_{n} \right) | 0 \right\rangle = \left\langle 0 | U^{\dagger} \left( t_{1} , t_{0} \right) \phi_{I} \left( x_{1} \right) U ( t_{1} , t_{0} ) \ldots U^{\dagger} \left( t_{n} , t_{0} \right) \phi_{I} \left( x_{n} \right) U ( t_{n} , t_{0} ) | 0 \right\rangle = \left\langle 0 | U^{\dagger} \left( t_{1} , t_{0} \right) \phi_{I} \left( x_{1} \right) U ( t_{1} , t_{2} ) \phi_{I} \left( x_{2} \right) \ldots U \left( t_{n - 1} , t_{n} \right) \phi_{I} \left( x_{n} \right) U ( t_{n} , t_{0} ) | 0 \right\rangle = \left\langle 0 | U^{\dagger} \left( t , t_{0} \right) \left\lbrack {U \left( t , t_{1} \right) \phi}_{I} \left( x_{1} \right) U ( t_{1} , t_{2} ) \phi_{I} \left( x_{2} \right) \ldots U \left( t_{n - 1} , t_{n} \right) \phi_{I} \left( x_{n} \right) U ( t_{n} , - t ) \right\rbrack U ( - t , t_{0} ) | 0 \right\rangle = \left\langle 0 | U^{\dagger} \left( t , t_{0} \right) T \left\{ \phi_{I} \left( x_{1} \right) \ldots \phi ( x_{n} ) U ( t , - t ) \right\} U ( - t , t_{0} ) | 0 \right\rangle \overset{t_{0} = - t , \  t \rightarrow \infty}{\rightarrow} \left\langle 0 | U^{\dagger} ( \infty , - \infty ) T \left\{ \phi_{I} \left( x_{1} \right) \ldots \phi \left( x_{n} \right) \exp \left( - i \int_{}^{} {d^{4} x \mathcal{H}_{I} ( x )} \right) \right\} | 0 \right\rangle = \frac{\left\langle 0 \left| T \left\{ \phi_{I} \left( x_{1} \right) \ldots \phi \left( x_{n} \right) \exp \left( - i \int_{}^{} {d^{4} x \mathcal{H}_{I} ( x )} \right) \right\} \right| 0 \right\rangle}{\left\langle 0 \left| T \exp \left( - i \int_{}^{} {d^{4} x \mathcal{H}_{I} ( x )} \right) \right| 0 \right\rangle} \  .
$$
Also, because $H_{i n t} = \frac{\lambda}{4 !} \phi^{4}$ , so $H_{I} ( t ) = \frac{\lambda}{4 !} \phi_{I}^{4} ( x )$. From splitting the fields into the creating and annihilating parts:
$$D ( x - y ) = \left\langle 0 | T \left\{ \phi ( x ) \phi ( y ) \right\} | 0 \right\rangle = \int_{}^{} {\frac{d^{4} p}{( 2 \pi )^{4}} \frac{i e^{- i p ( x - y )}}{p^{2} - m^{2} + i \epsilon}}$$is the Greene function of the differential operator in the Klein–Gordon equation. The four ways of circumventing the poles give different Green functions that meet different boundary conditions.
## Amputation of the outer legs
Bypass factors related to the outer propagators of the diagram that cancel out with the corresponding factors of the LZS formula. Then we immediately get a matrix element.

## Feynman's rules 
#### $\phi^4$ theory 
###### Vertex 
$- i \lambda$: (coupling constant)
###### Loop
$\int_{}^{} \frac{d^{4} k \ }{( 2 \pi )^{4}}$ (integral over free momentum variable)
#### QED
###### Dirac field
$$
S ( x - y ) = \left\langle 0 | T \left\{ \psi ( x ) \overline{\psi} ( y ) \right\} | 0 \right\rangle , \  T \left\{ \psi ( x ) \overline{\psi} ( y ) \right\} = \begin{cases}\psi ( x ) \overline{\psi} ( y ) \\ - \overline{\psi} ( y ) \psi ( x )\end{cases}
$$
$$
\widetilde{S} ( p ) = \frac{i}{p\!\!\!/ - m}
$$
###### Photon
In covariant gauge:
$$
D_{\mu \nu} ( x - y ) = \left\langle 0 | T \left\{ A_{\mu} ( x ) A_{\nu} ( y ) \right\} | 0 \right\rangle
$$
$$
\widetilde{D}_{\mu \nu} ( k ) = \frac{- i}{k^{2} + i \epsilon} \eta_{\mu \nu}
$$
###### Vertex
$$
{}- i e \gamma^{\mu}
$$
###### Outer legs
(except exponential factors)

|         | Photon                         | Electron                     | Positron                     |
|---------|--------------------------------|------------------------------|------------------------------|
| Initial | $$ \epsilon_{\mu} ( k ) $$     | $$ u^{s} ( p ) $$            | $$ \overline{v}^{s} ( p ) $$ |
| Final   | $$ \epsilon_{\mu}^{*} ( k ) $$ | $$ \overline{u}^{s} ( p ) $$ | $$ v^{s} ( p ) $$            |
$$
\psi ( x ) = \int_{}^{} {\frac{d^{3} p}{( 2 \pi )^{3} \sqrt{2 E_{\mathbf{p}}}} \left( \sum_{s = 1 , 2}^{} \left( a_{\mathbf{p} , s} u^{s} ( p ) e^{- i p x} + b_{\mathbf{p} , s}^{\dagger} v^{s} ( p ) e^{i p x} \right) \right)}
$$
###### Loops
Additional minus on integration
## Path integrals

$$
\left\langle q_{f} , T_{f} | q_{i} , T_{i} \right\rangle = \int_{q \left( T_{i} \right) = q_{i}}^{q \left( T_{f} \right) = q_{f}} {[ d q ] \exp {\left( \frac{i}{\hslash} S \right) .}}
$$

Because $\int_{q \left( T_{i} \right) = q_{i}}^{q \left( T_{f} \right) = q_{f}} {[ d q ] = \int_{- \infty}^{\infty} {d \overline{q}}} \int_{q \left( T_{i} \right) = q_{i}}^{q ( t ) = \overline{q}} {[ d q ] \int_{q ( t ) = \overline{q}}^{q \left( T_{f} \right) = q_{f}} [ d q ]}$ (because there is $\int_{T_{i}}^{T_{f}} {d t '} L = \int_{t}^{T_{f}} {d t '} L + \int_{T_{i}}^{t} {d t '} L$ in exponent), then:
$$
\left\langle q_{f} , T_{f} | \widehat{q} ( t ) | q_{i} , T_{i} \right\rangle = \int_{q \left( T_{i} \right) = q_{i}}^{q \left( T_{f} \right) = q_{f}} {[ d q ] q ( t ) \exp {\left( \frac{i}{\hslash} S \right) ,}}
$$

$$
\left\langle q_{f} , T_{f} | T \left\{ \widehat{q} \left( t_{1} \right) \ldots \widehat{q} ( t_{n} ) \right\} | q_{i} , T_{i} \right\rangle = \int_{q \left( T_{i} \right) = q_{i}}^{q \left( T_{f} \right) = q_{f}} {[ d q ] q \left( t_{1} \right) \ldots q ( t_{n} ) \exp {\left( \frac{i}{\hslash} S \right) .}}
$$
In field theory, the notation for vacuum in $t = -\infty$: $| 0 , t = - \infty \rangle \equiv | 0 \rangle$. Hence:
$$
\left\langle 0 | T \left\{ \widehat{\phi} \left( x_{1} \right) \ldots \widehat{\phi} ( x_{n} ) \right\} | 0 \right\rangle = \frac{\int_{}^{} {D \phi \phi \left( x_{1} \right) \ldots \phi \left( x_{n} \right) e^{i S} \ }}{\int_{}^{} {D \phi e^{i S}}}
$$
(the denominator comes from the evolution of the vacuum state from $-\infty$ to $+\infty$). Generating functional:
$$
W [ J ] \equiv \int_{}^{} {D \phi \exp {\left\{ \frac{i}{2} \int_{}^{} {d^{4} x \left\lbrack \partial_{\mu} \phi \partial^{\mu} \phi - \left( m^{2} - i \epsilon \right) \phi^{2} \right\rbrack + \int_{}^{} {d^{4} x \  \phi ( x ) J ( x )}} \right\} .}}
$$
By the analogy to the formula:
$$
\int_{}^{} {\prod_{i = 1}^{N} {d y_{i} \exp {\left\lbrack - \frac{1}{2} \mathbf{y}^{\mathbf{T}} \mathbf{A y} + \mathbf{y}^{\mathbf{T}} \mathbf{z} \right\rbrack = ( 2 \pi )^{\frac{N}{2}} \left( \det A \right)^{- \frac{1}{2}} \exp \left\lbrack \frac{1}{2} \mathbf{z}^{\mathbf{T}} \mathbf{A}^{- 1} \mathbf{z} \right\rbrack}}}
$$
It can be concluded that:
$$
\begin{split}
W [ J ] = \int_{}^{} {D \phi \exp {\left\{ \int_{}^{} {\frac{d^{4} p}{( 2 \pi )^{4}} \left\lbrack \frac{i}{2} \widetilde{\phi} ( - p ) \left( p^{2} - m^{2} + i \epsilon \right) \widetilde{\phi} ( p ) + \widetilde{J} ( - p ) \widetilde{\phi} ( p ) \right\rbrack} \right\} = \int_{}^{} {D \phi e^{i S}} \exp {\left\{ \frac{1}{2} \int_{}^{} {\frac{d^{4} p}{( 2 \pi )^{4}} \widetilde{J} ( - p )  \widetilde{J} ( p )} \right\} = W [ 0 ] \exp \left\{ \frac{1}{2} \int_{}^{} {d^{4} x d^{4} y J ( x ) D ( x - y ) J ( y )} \right\}}} ,}
\end{split}
$$
where $$\widetilde{D} ( p )=\frac{i}{p^{2} - m^{2} + i \epsilon}$$
and we used
$$
W[0]=\int{\cal D}\phi~e^{iS}.
$$


Hence: $D ( x - y ) = \left\langle 0 | T \left\{ \phi ( x ) \phi ( y ) \right\} | 0 \right\rangle$ (corresponding functional derivative) and $\left\langle 0 | T \left\{ \phi \left( x_{1} \right) \phi \left( x_{2} \right) \phi \left( x_{3} \right) \phi \left( x_{4} \right) \right\} | 0 \right\rangle = D \left( x_{1} - x_{2} \right) D \left( x_{3} - x_{4} \right) + D \left( x_{1} - x_{3} \right) D \left( x_{2} - x_{4} \right) + D \left( x_{1} - x_{4} \right) D ( x_{2} - x_{3} ).$The functional:
$$
Z [ J ] = \ln {W [ J ] = Z [ 0 ] + \frac{1}{2} \int_{}^{} {d^{4} x d^{4} y J ( x ) D ( x - y ) J ( y )}}
$$
generates **connected** Green functions.
#### Renormalization of the theory $\mathbf{\phi}^{\mathbf{4}}$
When applying an ultraviolet cutoff $\Lambda$, the sum of a series of double-loop diagrams is:
$$
\frac{i}{A \left( \Lambda , p^{2} \right) p^{2} - m^{2} - B ( \Lambda )} , \  A \left( \Lambda , p^{2} \right) = 1 + \lambda^{2} \left( c_{1} \ln \frac{\Lambda^{2}}{p^{2}} + c_{2} \right) , \  B ( \Lambda ) = \frac{\lambda}{32 \pi^{2}} \left( \Lambda^{2} - m^{2} \ln \frac{\Lambda^{2} + m^{2}}{m^{2}} \right)
$$

Here, $\lambda = \lambda_{0} ( \Lambda ) , \  m = m_{0} ( \Lambda )$ etc. At the one-loop level, $A = 1$,  $m_{R}^{2} = m_{0}^{2} ( \Lambda ) + B ( \Lambda )$ and we choose $m_{0} ( \Lambda )$ so that the divergencies are eliminated and the propagator has a pole in the real, observed mass.

At the two-loop level.$\int_{}^{} {d^{4} x e^{i p x} \left\langle 0 \left| T \left\{ \phi_{0} ( x , \Lambda ) , \phi_{0} ( 0 , \Lambda ) \right\} \right| 0 \right\rangle_{C} = \frac{i Z}{p^{2} - m_{R}^{2}} + \ldots}$, where the remaining terms are finite, when $p^{2} = m_{R}^{2}$,  $Z = Z \left( \lambda_{0} ( \Lambda ) , \frac{\Lambda}{m_{R}} \right) = \left\lbrack \left( \frac{d}{d \left( p^{2} \right)} A \left( \Lambda , p^{2} \right) p^{2} \right)_{p^{2} = m_{R}^{2}} \right\rbrack^{- 1}$.

We assume that $m_R$ is such that $\left\lbrack A \left( \Lambda , p^{2} \right) p^{2} - m_{0}^{2} ( \Lambda ) - B ( \Lambda ) \right\rbrack_{p^{2} = m_{R}^{2}} = 0$. We define the renormalized wave function: $\phi_{0} = Z^{\frac{1}{2}} \left( \lambda_{0} , \frac{\Lambda}{m^{R}} \right) \phi_{R}$. If in the LZS formula we use $\phi_{R} , m_{R}$ instead of $\phi_{0} , m_{0}$. Then we get a finite expression for the Green function.

The four-point function gives a new contribution to the divergence:
$$
i \mathcal{M}_{2 \rightarrow 2} = - i \lambda + i \lambda^{2} \left( \beta_{0} \ln {\Lambda + \mathrm{finite}} \right) + O \left( \lambda_{0}^{3} \right) .
$$

The first term corresponds to a diagram without a loop $\beta_{0} = \frac{3}{16 \pi^{2}}$ , which corresponds to three contributions from diagrams in the form of a "candy": $\mathcal{M = -} \lambda + 3 \mathcal{A} ( 0 )$, where $\mathcal{A} ( p ) = \frac{( - i \lambda )^{2}}{2} \int_{}^{} \frac{d^{4} k}{( 2 \pi )^{2}} \frac{i}{k^{2} - m^{2} + i \epsilon} \frac{i}{( k - p )^{2} - m^{2} + i \epsilon} p$ (when calculating this expression, Wick's rotation is used) and depends only the finite part.
For $p_{1} = p_{2} = p_{3} = p_{4} = \left( m_{R} , 0 \right)$:

$$
{}- i \lambda_{R} \equiv i \mathcal{M}_{2 \rightarrow 2} ( 0 ) = - i \lambda_{0} ( \Lambda ) \left\lbrack 1 - \lambda_{0} ( \Lambda ) \left( \beta_{0} \ln \frac{\Lambda}{m_{R}} \right) + \mathrm{finite} \right\rbrack + O \left( \lambda_{0}^{3} \right) .
$$

For:$\left( p_{1} + p_{2} \right)^{2} = q^{2} \gg m_{R}$:
$$
i \mathcal{M}_{2 \rightarrow 2} \left( q^{2} \right) = - i \lambda_{0} ( \Lambda ) \left\lbrack 1 - \lambda_{0} ( \Lambda ) \left( \frac{\beta_{0}}{2} \ln \frac{\Lambda^{2}}{q^{2}} + \mathrm{finite} \right) \right\rbrack + O \left( \lambda_{0}^{3} \right) = - i \lambda_{R} \left\lbrack 1 + \lambda_{R} \frac{\beta_{0}}{2} \ln \frac{q^{2}}{m_{R}^{2}} \right\rbrack + O \left( \lambda_{R}^{3} \right) = - i \lambda_{e f f} ( q^{2} )
$$
And it is finite at every energy scale.
# Renormalization Group

N-point function:

$$
\Gamma_{R} \left( p_{i} ; g_{R} , \mu \right) = Z^{- \frac{n}{2}} \left( g_{0} ( \Lambda ) , \frac{\Lambda}{\mu} \right) \Gamma_{0} \left( p_{i} ; g_{0} ( \Lambda ) , \Lambda \right) .
$$

Renormalization group equation:

$$
\left\lbrack \Lambda \frac{\partial}{\partial \Lambda} + \beta \left( g_{0} \right) \frac{\partial}{\partial g_{0}} - n \eta \left( g_{0} \right) \right\rbrack \Gamma_{0} \left( p_{i} ; g_{0} , \Lambda \right) = 0 ,
$$

$$
\beta \left( g_{0} \right) = \Lambda \frac{d g_{0}}{d \Lambda} , \  \eta \left( g_{0} \right) = \frac{1}{2} \Lambda \frac{d}{d \Lambda} \ln Z
$$

The solution of the equation is of the form (this is the so-called expansion joint parameter):$$u$$

$$
\Gamma_{0} \left( p_{i} ; g_{0} , \frac{\Lambda}{u} \right) = Z_{e f f}^{- \frac{n}{2}} ( u ) \Gamma_{0} \left( p_{i} ; g_{e f f} ( u ) , \Lambda \right) , \  \  \Lambda \rightarrow \infty \Leftrightarrow u \rightarrow 0
$$

$$
u \frac{d g_{e f f} ( u )}{d u} = \beta \left( g_{e f f} ( u ) \right) , \  g_{e f f} ( 1 ) = g_{0}
$$

and hence it is divergent for , that is, the null place of the function . Next:$$\int_{g_{0}}^{g_{e f f} ( u )} {\frac{d g '}{\beta ( g^{'} )} = \ln u} u \rightarrow 0 g_{e f f} ( u \rightarrow 0 ) \rightarrow \beta$$

$$
\frac{1}{2} u \frac{d}{d u} \ln {Z_{e f f} = \eta \left( g_{e f f} ( u ) \right) , \  \  Z_{e f f} ( 1 ) = 1 .}
$$

Because , this is also the reason why $$g_{R} = g_{0} - \beta_{0} g_{0}^{2} \ln {\Lambda + O \left( g_{0}^{3} \right)} g_{0} = g_{R} + \beta_{0} g_{R}^{2} \ln {\Lambda + O ( g_{R}^{3} )} \beta \left( g_{0} \right) \equiv \frac{d g_{0}}{d \ln \Lambda} = \beta_{0} g_{0}^{2} + O ( g_{0}^{3} )$$

Callan-Symanzik equation

$$
\left\lbrack \mu \frac{\partial}{\partial \mu} + \beta \left( g_{R} \right) \frac{\partial}{\partial g_{R}} + \eta \gamma \left( g_{R} \right) \right\rbrack \Gamma_{R} \left( p_{i} ; g_{R} , \mu \right) = 0 ,
$$

$$
\beta \left( g_{R} \right) = \mu \frac{d g_{R}}{d \mu} , \  \gamma \left( g_{R} \right) = \frac{1}{2} \mu \frac{d}{d \mu} \ln Z .
$$

Solution:

$$
\Gamma_{R} \left( p_{i} ; g_{R} , \frac{\mu}{u} \right) = Z_{e f f}^{- \frac{n}{2}} \Gamma_{R} \left( p_{i} ; g_{e f f} ( u ) , \mu \right) ,
$$

$$
u \frac{d g_{e f f} ( u )}{d u} = \beta \left( g_{e f f} ( u ) \right) , \  g_{e f f} ( 1 ) = g_{R}
$$

$$
\frac{1}{2} u \frac{d}{d u} \ln {Z_{e f f} = - \gamma \left( g_{e f f} ( u ) \right) , \  \  Z_{e f f} ( 1 ) = 1 .}
$$

Dimensionality:

$$
\Gamma_{R} \left( p_{i} ; g_{R} , \mu \right) = \mu^{d} F \left( g_{R} , \frac{p_{i}}{\mu} \right) \Rightarrow \Gamma_{R} \left( p_{i} ; g_{R} , \frac{\mu}{u} \right) = \frac{\mu^{d}}{u^{d}} F \left( g_{R} , \frac{u p_{i}}{\mu} \right) = \frac{1}{u^{d}} \Gamma_{R} \left( {u p}_{i} ; g_{R} , \mu \right) .
$$

Hence:

$$
\Gamma_{R} \left( {u p}_{i} ; g_{R} , \frac{\mu}{u} \right) = {u^{d} Z}_{e f f}^{- \frac{n}{2}} \Gamma_{R} \left( p_{i} ; g_{e f f} ( u ) , \mu \right) = u^{d} {\exp \left( n \int_{0}^{\ln u} {\gamma \left( g_{e f f} ( u ' ) \right) d \ln {u '}} \right) \Gamma}_{R} \left( p_{i} ; g_{e f f} ( u ) , \mu \right) .
$$

In the above equation, there is an anomalous dimension and a floating coupling constant. In theory:$$\phi^{4}$$

$$
\lambda_{e f f} ( E ) = \frac{\lambda_{*}}{1 - \beta_{0} \lambda_{*} \ln \frac{E}{\mu}} , \  E = u \mu , \  \lambda_{e f f} ( u ) = \lambda_{*} , \  \beta_{0} = \frac{3}{16 \pi^{2}} .
$$

# Non-abelian featuring theories

Abelian Marking:

$$
A_{\mu} \rightarrow A_{\mu} + i \left( \partial_{\mu} U \right) U^{\dagger} , \  U = e^{i \theta ( x )}
$$

$$
\psi ( x ) \rightarrow e^{i q \theta ( x )} \psi ( x )
$$

$$
D_{\mu} \psi ( x ) = \left( \partial_{\mu} + i q A_{\mu} ( x ) \right) \psi ( x ) \rightarrow {e^{i q \theta ( x )} D}_{\mu} \psi ( x ) .
$$

For non-abelian featuring:

$$
\psi \rightarrow U_{R} \psi , \  \  U_{R} = \exp {\left( i g \theta^{a} ( x ) T_{R}^{a} \right) , \  \  T_{R}^{a}} - g e n e r a t o r \  S U ( N ) .
$$

We define and specify that .$$A_{\mu} \equiv A_{\mu}^{a} ( x ) T^{a} A_{\mu} ( x ) \rightarrow U A_{\mu} U^{\dagger} - \frac{i}{g} \left( \partial_{\mu} U \right) U^{\dagger}$$

Hence:

$$
A_{\mu}^{a} ( x ) \rightarrow A_{\mu}^{a} ( x ) + \partial_{\mu} \theta^{a} - g f^{a b c} \theta^{b} A_{\mu}^{c} + O ( \theta^{2} )
$$

$$
D_{\mu} = \partial_{\mu} - i g A_{\mu}^{a} T_{R}^{a}
$$

$$
F_{\mu \nu} = \partial_{\mu} A_{\nu} - \partial_{\nu} A_{\mu} - i g \left\lbrack A_{\mu} , A_{\nu} \right\rbrack = F_{\mu \nu}^{a} T^{a} \rightarrow U ( x ) F_{\mu \nu} ( x ) U^{\dagger} ( x )
$$

$$
F_{\mu \nu}^{a} = \partial_{\mu} A_{\nu}^{a} - \partial_{\nu} A_{\mu}^{a} + g f^{a b c} A_{\mu}^{b} A_{\nu}^{c} .
$$

For example:

$$
\mathcal{L}_{Y a n g - M i l l s} = \overline{\psi} ( i D - m ) \psi + \frac{1}{2} T r F_{\mu \nu} F^{\mu \nu}
$$

It contains triple and quadruple vertices where boson propagators meet. If the field belongs to an attached representation, then ( is $$\phi \  \Phi = \phi^{a} T^{a} \rightarrow U ( x ) \Phi ( x ) U^{\dagger} ( x ) T^{a}$$*the generator of any* representation). Then:

$$
\left( D_{\mu} \phi \right)^{a} = \partial_{\mu} \phi^{a} - g f^{a b c} \phi^{b} A_{\mu}^{c}
$$

$$
{\partial_{\mu} \Phi - i g \left\lbrack A_{\mu} , \Phi \right\rbrack = D}_{\mu} \Phi \equiv \left( D_{\mu} \phi \right)^{a} T^{a} \rightarrow \  U ( x ) \left( D_{\mu} \Phi \right) U^{\dagger} ( x )
$$

$$
\mathcal{L} = T r D_{\mu} \Phi D^{\mu} \Phi
$$

Spontaneous symmetry breaking (choice from many possible vacuum states) causes the appearance of a massive Goldstone boson. There are as many of them as there are generators that break symmetry, i.e. such that $$T^{a} | 0 \right\rangle \neq 0 :$$

$$
H T^{a} | 0 \right\rangle = T^{0} H | 0 \rangle
$$

(because if we are dealing with symmetry, then ).$$\left\lbrack H , t^{a} \right\rbrack = 0$$

# Higgs mechanism

$$
\mathcal{L}_{S U ( 2 ) , H i g g s} = \left( D_{\mu} \phi \right)^{\dagger} D^{\mu} \phi - V \left( \phi^{\dagger} \phi \right) - \frac{1}{4} F_{\mu \nu}^{a} F^{a \mu \nu} .
$$

$$
V \left( \phi^{\dagger} \phi \right) = \frac{1}{2} \lambda^{2} \left( \phi^{\dagger} \phi - \eta^{2} \right)^{2} .
$$

We use gauge symmetry to eliminate 3 out of 4 degrees of freedom:

$$
\phi = \begin{pmatrix}0 \\ \eta + \frac{1}{\sqrt{2}} \chi\end{pmatrix} , \  \chi \mathbb{\in R .}
$$

We define:

$$
\sigma^{+} = \frac{1}{\sqrt{2}} \left( \sigma^{1} + i \sigma^{2} \right) = \sqrt{2} \begin{pmatrix}0 & 1 \\ 0 & 0\end{pmatrix}
$$

$$
\sigma^{-} = \frac{1}{\sqrt{2}} \left( \sigma^{1} - i \sigma^{2} \right) = \sqrt{2} \begin{pmatrix}0 & 0 \\ 1 & 0\end{pmatrix}
$$

$$
A_{\mu}^{\pm} = \frac{1}{\sqrt{2}} \left( A_{\mu}^{1} \pm A_{\mu}^{2} \right) .
$$

Hence:

$$
D_{\mu} \phi = \begin{pmatrix}0 \\ \frac{1}{\sqrt{2}} \partial_{\mu} \chi\end{pmatrix} - \frac{i g}{2} \left( \eta + \frac{\chi}{2} \right) \begin{pmatrix}\sqrt{2} A_{\mu}^{-} \\ - A_{\mu}^{3} \ \end{pmatrix} ,
$$

How does it follow that fields gain mass . As massive fields, they now have three degrees of freedom instead of two:$$A_{\mu}^{\pm} , A_{\mu}^{3} m_{A} = \frac{g \eta}{\sqrt{2}}$$

1.  From the equations of motion for gauge fields: .$$\partial_{\nu} A^{\nu} = 0 \Rightarrow k_{\nu} \epsilon^{\nu} ( k ) = 0$$

2.  There can be no polarization , because .$$\epsilon^{\nu} ( k ) \propto k^{\nu} k_{\nu} \epsilon^{\nu} ( k ) \propto k^{2} = m_{A}^{2} \neq 0$$

3.  In the resting system and the polarization eliminated is $$k_{\nu} = m_{A} ( 1 , 0 , 0 , 0 ) \epsilon^{\nu} = ( 1 , 0 , 0 , 0 ) .$$

4.  The other three polarities are three degrees of freedom.

In the standard model:

$$
D_{\mu} = \partial_{\mu} - i g T^{a} A_{\mu}^{a} - i g^{'} S B_{\mu} = \partial_{\mu} - i g \frac{\sigma^{a}}{2} A_{\mu}^{a} - i g^{'} \frac{1}{2} B_{\mu} .
$$

We define: , where – Weinberg angle.$$\overline{g} = \sqrt{g^{2} + g^{' 2}} , \  g = \overline{g} \cos \theta_{W} , \  g^{'} = \overline{g} \sin \theta_{W} \theta_{W}$$

$$W_{\mu}^{\pm} = A_{\mu}^{\pm} , \  Z_{\mu}^{0} = A_{\mu}^{3} \cos \theta_{W} + B_{\mu} \sin \theta_{W}$$ – W and Z bosons, their masses are .$$m_{W} = \frac{1}{\sqrt{2}} g \eta , \  m_{Z} = \frac{1}{\sqrt{2}} \overline{g} \eta$$

$$A_{\mu} = A_{\mu}^{3} \sin {\theta_{W} + B_{\mu} \cos \theta_{W}}$$ – a massless photon.

# Gupt-Bleuler quantization

$$
\mathcal{L =} \frac{1}{4} F_{\mu \nu} F^{\mu \nu} + \frac{1}{2} \left( \partial_{\mu} A^{\mu} \right)^{2} \Rightarrow \blacksquare A_{\mu} = 0 .
$$

$$
A_{\mu} ( x ) = \int_{}^{} {\frac{d^{3} p}{( 2 \pi )^{3} \sqrt{2 \omega_{\mathbf{p}}}} \sum_{\lambda = 0}^{3} {\left\lbrack \epsilon_{\mu} \left( \mathbf{p} , \lambda \right) a_{\mathbf{p ,} \lambda} e^{- i p x} + h . c . \right\rbrack .}}
$$

For example: .$$\epsilon_{\mu} \left( \mathbf{p} , \lambda \right) = \delta_{\mu}^{\lambda}$$

$$
\left\lbrack a_{\mathbf{p ,} \lambda} , a_{\mathbf{q ,} \lambda^{'}}^{\dagger} \right\rbrack = - ( 2 \pi )^{3} \delta^{( 3 )} \left( \mathbf{p - q} \right) \eta_{\lambda \lambda^{'}} ,
$$

Which causes a problem with probabilistic interpretation for . We define the physical state: , from where . A state is a physical state if and only if . It follows that it is a physical state and it is . But it does not contribute to the scalar product of physical states and values of expected energy, momentum, and angular momentum between physical states. Therefore, the equivalence relation is introduced and $$\lambda = \lambda^{'} = 0 \left\langle p h y s | \partial_{\mu} A^{\mu} | p h y s \right\rangle = 0 \left( \partial_{\mu} A^{\mu} \right)^{+} | p h y s \right\rangle = 0 | \psi \right\rangle = \sum_{\lambda}^{} c_{\lambda} a_{\mathbf{q} \mathbf{,} \lambda}^{\dagger} | 0 \rangle c_{0} + c_{3} = 0 | \psi \right\rangle = \left( a_{\mathbf{q} \mathbf{,} 0}^{\dagger} - a_{\mathbf{q} \mathbf{,} 3}^{\dagger} \right) | 0 \right\rangle \left| \psi_{T} \right\rangle + c | \psi \rangle | \psi \rangle \left| \psi_{T}^{'} \right\rangle \sim \left| \psi_{T} \right\rangle : \  \left| \psi_{T}^{'} \right\rangle \sim \left| \psi_{T} \right\rangle + c | \psi \rangle$$ the purely transversal state is taken as a representative of the equivalence class.

