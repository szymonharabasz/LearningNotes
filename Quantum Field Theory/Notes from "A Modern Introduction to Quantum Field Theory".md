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
2.  Spinor representations: $$\psi_{L} \in \left( \frac{1}{2} , 0 \right)~~~\mathrm{and}~~~\psi_{R} \in \left( 0 , \frac{1}{2} \right)$$For left-handed representation: $$\overrightarrow{J} = \frac{\overrightarrow{\sigma}}{2},$$and $$\overrightarrow{K} = i \frac{\overrightarrow{\sigma}}{2}$$ nie jest hermitowski. Jest tak dlatego, że grupa Lorentza nie jest zwarta, a istnieje twierdzenie, które głosi, niezwarte grupy nie mają reprezentacji unitarnej skończonego wymiaru, oprócz takiej, w której niezwarte generatory są reprezentowane trywialnie, czyli przez zero.   
    $$\Lambda_{L} = e^{\left( - i \overrightarrow{\theta} - \overrightarrow{\eta} \right) \frac{\overrightarrow{\sigma}}{2}}\Lambda_{R} = e^{\left( - i \overrightarrow{\theta} + \overrightarrow{\eta} \right) \frac{\overrightarrow{\sigma}}{2}}$$Operację sprzężenia ładunkowego definiuje się jako:  
    $$\psi_{L}^{C} = i \sigma^{2} \psi^{*}_{L} \in \left( 0 , \frac{1}{2} \right)$$(gdzie skorzystano z tego, że $$\sigma^{2} \Lambda_{L}^{*} \sigma^{2} = \Lambda_{R}$$ oraz $$\sigma^{2} \sigma^{2} = 1$$)$$\psi_{R}^{C} = - i \sigma^{2} \psi^{*}_{R} \in \left( \frac{1}{2} , 0 \right)\left( \psi_{L}^{C} \right)^{C} = \psi_{L}$$

3.  Reprezentacja $$\left( \frac{1}{2} , \frac{1}{2} \right)$$ jest zespoloną reprezentacją wektorową (bo $$j = 0 , 1$$). Stany mają postać:  
    $$\left( \left( \psi_{L} \right)_{\alpha} , \left( \psi_{R} \right)_{\beta} \right) , \  \  \alpha , \beta = 1 , 0$$Stany $$\xi_{R}^{\dagger} \sigma^{\mu} \psi_{R}$$ i $$\xi_{L}^{\dagger} \overline{\sigma}^{\mu} \psi_{L}$$, gdzie $$\sigma^{\mu} = \left( 1 , \overrightarrow{\sigma} \right) , \  \overline{\sigma}^{\mu} = ( 1 , - \overrightarrow{\sigma} )$$, są zespolonymi czterowektorami.

# Reprezentacje na polach

Reprezentacja $$\delta \phi = \phi^{'} \left( x^{'} \right) - \phi ( x )$$ jest jednowymiarowa, reprezentacja nieskończenie wymiarowa to $$\delta_{0} \phi = \phi^{'} ( x ) - \phi ( x ) = - \delta x^{\mu} \partial_{\mu} \phi ( x ) = {\frac{i}{2} \omega^{\mu \nu} \left( J_{\mu \nu} \right)_{\  \  \  \sigma}^{\rho} \delta x^{\sigma} \  \partial_{\rho} \phi \equiv - \frac{i}{2} \omega^{\mu \nu} \  L_{\mu \nu}}$$, gdzie $$L^{\mu \nu} = i \left( x^{\mu} \partial^{\nu} - x^{\nu} \partial^{\mu} \right)$$.

## Pole Weyla i Diraca

$$
\psi_{L} ( x ) \rightarrow \psi_{L}^{'} \left( x^{'} \right) = \Lambda_{L} \psi_{L} ( x )
$$

$$
\delta_{0} \psi_{L} = \left( \Lambda_{L} - 1 \right) \psi_{L} ( x ) - \delta x^{\rho} \partial_{\rho} \psi_{L} ( x ) = \left( e^{- {\frac{i}{2} \ } \omega_{\mu \nu} S^{\mu \nu}} - 1 \right) \psi_{L} ( x ) - {\frac{i}{2} \ } \omega_{\mu \nu} L^{\mu \nu} \psi_{L} ( x ) - {\frac{i}{2} \ } \omega_{\mu \nu} \left( S^{\mu \nu} + L^{\mu \nu} \right) \psi_{L} ( x ) = - {\frac{i}{2} \ } \omega_{\mu \nu} J^{\mu \nu} \psi_{L} ( x )
$$

Pod wpływem transformacji parzystości:

$$\overrightarrow{J} \rightarrow \overrightarrow{J} , \  \  \  \overrightarrow{K} \rightarrow - \overrightarrow{K} , \  \  \  \overrightarrow{J}^{+} \rightarrow \overrightarrow{J}^{-} , \  \left( j_{-} , j_{+} \right) \rightarrow \left( j_{+} \  , j_{-} \right) \neq \left( j_{-} , j_{+} \right)$$, więc pole Weyla nie reprezentuje parzystości. Reprezentuje ją pole Diraca: $$\Psi = \begin{pmatrix}\psi_{L} \\ \psi_{R}\end{pmatrix}$$. Transformacja Lorentza reprezentowana jest a pomocą:

$$
\Lambda_{D} = \begin{pmatrix}\Lambda_{L} & 0 \\ 0 & \Lambda_{R}\end{pmatrix} ,
$$

A transformacja parzystości:

$$
\Psi ( x ) \rightarrow \begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix} \Psi \left( x^{'} \right) , \  \  \  x^{'} = \left( t , - \overrightarrow{x} \right) .
$$

Sprzężenie ładunkowe zdefiniowane jest jako:

$$
\Psi^{C} = - i \begin{pmatrix}0 & \sigma^{2} \\ - \sigma^{2} & 0\end{pmatrix} \Psi^{*}
$$

## Pole Majorany

$$
\Psi_{M} = \begin{pmatrix}\psi_{L} \\ i \sigma^{2} \psi_{L}^{*}\end{pmatrix}
$$

Być może opisuje ono neutrina. Jest ono neutralne w takim sensie, że $$\Psi_{M}^{C} = \Psi_{M}$$ (warunek $$\Psi_{M}^{*} = \Psi$$ nie byłby lorentzowsko niezmienniczy).

Pole wektorowe

Należy do reprezentacji $$\left( \frac{1}{2} , \frac{1}{2} \right)$$, więc reprezentuje parzystość.

$$
V^{\mu} ( x ) \rightarrow V^{' \mu} \left( x^{'} \right) = \Lambda_{\  \  \nu}^{\mu} V^{\nu} ( x )
$$

Zakładamy, że wszystkie pola są skalarne względem translacji, czyli $$\delta_{0} \phi = - \epsilon^{\mu} \partial_{\mu} \phi ( x ) = i \epsilon^{\mu} P_{\mu} \phi ( x )$$, czyli $$P_{\mu} = i \partial_{\mu}$$.

Reprezentacje na stanach z przestrzeni Hilberta

Twierdzenie Wignera głosi, że symetrie są reprezentowane przez operatory unitarne. Reprezentacje są numerowane przez wartości własne operatorów Casimira, np.:

$$
P_{\mu} P^{\mu} \rightarrow - m^{2} , \  W_{\mu} W^{\mu} , \  W^{\mu} = - \frac{1}{2} \epsilon^{\mu \nu \rho \sigma} J_{\nu \rho} P_{\sigma}
$$

Jest to lorentzowsko niezmienniczy wektor Pauliego-Lubańskiego.

## Reprezentacja masywna

Wybieramy układ spoczynkowy i $$W_{\mu} W^{\mu} = - m^{2} j ( j + 1 )$$. Reprezentacja jest numerowana przez masę i spin cząstki, a stany różnią się rzutem spinu.

Reprezentacja bezmasowa

Wybieramy $$P^{\mu} = ( \omega , 0 , 0 , \omega )$$ i małą grupą jest SU(2). Reprezentacje są numerowane przez wartość własną $$h$$ operatora $$J_{3}$$ zwaną skrętnością. Algebraiczny dowód, że $$h = 0 , \pm \frac{1}{2} . \pm 1 , \ldots$$ nie działa, bo nie ma tu $$J_{1} , J_{2}$$, ale działa pewien dowód topologiczny.

# Symetrie i prawa zachowania

$$
x^{\mu} \rightarrow x^{'}^{\mu} = x^{\mu} + \epsilon^{\alpha} A_{\alpha}^{\mu} ( x )\phi_{i} ( x ) \rightarrow \phi^{'}_{i} \left( x^{'} \right) = \phi_{i} ( x ) + \epsilon^{\alpha} F_{i \alpha} ( \phi , \partial \phi )
$$

Jeśli transformacja jest tylko symetrią globalną, to przy założeniu, że parametr $$\epsilon$$ nie jest stałą, ale zmienia się wolno:

$$
S \left( \phi^{'} \right) = S ( \phi ) + \int_{}^{} {d^{4} x} \left\lbrack \epsilon^{\alpha} K_{\alpha} ( \phi ) - \left( \partial_{\mu} \epsilon^{\alpha} j_{\alpha}^{\mu} ( \phi ) \right) + O ( \partial \  \partial \epsilon ) \right\rbrack + O ( \epsilon^{2} )
$$

W przypadku, gdy $$\epsilon$$ jest stały, mamy symetrię i $$S \left( \phi^{'} \right) = S ( \phi ) , \  K = 0$$. Gdy zaś $$\epsilon \rightarrow 0 , \  x \rightarrow \infty$$:

$$
S \left( \phi^{'} \right) = S ( \phi ) + \int_{}^{} {d^{4} x \epsilon^{\alpha} \partial_{\mu} j_{\alpha}^{\mu} ( x )} + O ( \partial \partial \epsilon ) + O ( \epsilon^{2} )
$$

Dzięki zamianie zmiennej całkowania w działaniu mamy $$x^{\mu} \rightarrow x^{\mu}$$ oraz $$\phi_{i} ( x ) \rightarrow \phi_{i} \left( x - \epsilon^{\alpha} A_{\alpha} \right) + \epsilon^{\alpha} F_{i \alpha} = \phi_{i} ( x ) - \epsilon^{\alpha} \partial_{\mu} \phi_{i} A_{\alpha}^{\mu} + \epsilon^{\alpha} F_{i \alpha} = \phi_{i} ( x ) + \delta \phi_{i} ( x )$$. Ostatni wyraz jest wariacją taką samą, jak przy obliczaniu równań ruchu i zmierza do zera, gdy $$x \rightarrow \infty$$. Jeśli $$\phi_{i} ( x )$$ jest rozwiązaniem klasycznych równań ruchu, to całka zaznaczona na zielono musi znikać niezależnie od parametru $$\epsilon$$ i:

$$
\partial_{\mu} j_{\alpha}^{\mu} \left( \phi^{c l} \right) = 0 .
$$

Zmiana działania pod wpłytwem transformacji zawiera człon proporcjonalny do $$\epsilon^{\alpha}$$ równy:

$$
j_{\alpha}^{\mu} = \frac{\partial L}{\partial \left( \partial_{\mu} \phi_{i} \right)} \left\lbrack A_{\alpha}^{\nu} \partial_{\nu} \phi_{i} - F_{i \alpha} ( \phi , \partial \phi ) \right\rbrack - A_{\alpha}^{\mu} L .
$$

Jeśli teraz $$\epsilon$$ **nie jest symetrią globalną**, to $$K_{\alpha} ( \phi ) \neq 0$$, lecz $$K_{\alpha} ( \phi ) = \left( \delta_{\alpha} L \right)_{g l o b a l}$$, gdzie $$( \delta L )_{g l o b a l} = {\epsilon^{\alpha} \left( \delta_{\alpha} L \right)}_{g l o b a l}$$ pod wpływem globalnej **transformacji**. Wtedy:

$$
\partial_{\mu} j_{\alpha}^{\mu} \left( \phi^{c l} \right) = - \left( \delta_{\alpha} L \right)_{g l o b a l} .
$$

Pod wpływem translacji wszystkie pola są skalarami ($$\alpha$$ staje się indeksem lorentzowskim). Wówczas z $$x^{\mu} \rightarrow x^{' \mu} + \epsilon^{\nu} \delta_{\nu}^{\mu}$$ oraz $$\phi_{i} ( x ) \rightarrow \phi_{i}^{'} \left( x^{'} \right) = \phi_{i} ( x )$$ wynika, że $$A_{\nu}^{\mu} = \delta_{\nu}^{\mu} , \  F_{i \nu} = 0$$. Tensor energii-pędu zdefiniowany jako $$\theta_{\  \  \  \nu}^{\mu} = j_{( \nu )}^{\mu}$$ równa się:

$$
\theta^{\mu \nu} = \frac{\partial L}{\partial \left( \partial_{\mu} \phi_{i} \right)} \partial^{\nu} \phi_{i} - \eta^{\mu \nu} L .
$$

Ładunek związany z przekształceniem symetrii jest wartością średnią generatora wyrażonego jako operator działający na pole pomiędzy stanami. Na przykład dla U(1) $$j_{\mu} = i \phi^{*} \overset{\overleftrightarrow{}}{\partial}_{\mu} \phi$$ i $$Q_{U ( 1 )} = \int_{}^{} {d^{3} x j^{0} = i \int_{}^{} {d^{3} x \phi^{*} \overset{\overleftrightarrow{}}{\partial}_{0} \phi \equiv \left\langle \phi | \phi \right\rangle} = \left\langle \phi | I | \phi \right\rangle}$$

# Pola klasyczne

Dla pola Weyla $$\mathcal{L}_{L} = i \psi_{L}^{\dagger} \overline{\sigma}^{\mu} \partial_{\mu} \psi_{L}$$ i rozwiązanie w postaci fali płaskiej $$\psi_{L} = u_{L} e^{- i p x}$$ ma $$h = - \frac{1}{2}$$.

Dla pola Diraca $$\mathcal{L}_{D} = i \psi_{L}^{\dagger} \overline{\sigma}^{\mu} \partial_{\mu} \psi_{L} + i \psi_{R}^{\dagger} \sigma^{\mu} \partial_{\mu} \psi_{R} - m ( \psi_{L}^{\dagger} \psi_{R} + \psi_{R}^{\dagger} \psi_{L} )$$. Reprezentacji chiralnej $$\psi = \begin{pmatrix}\psi_{L} \\ \psi_{R}\end{pmatrix} , \  \gamma^{\mu} = \begin{pmatrix}0 & \sigma^{\mu} \\ \overline{\sigma}^{\mu} & 0\end{pmatrix} , \  \overline{\psi} \equiv \psi^{\dagger} \gamma^{0} = ( \psi_{R}^{\dagger} , \psi_{L}^{\dagger} )$$ i $$\mathcal{L}_{D} = \overline{\psi} ( i \partial - m ) \psi$$. Inne reprezentacje wiążą się z chiralną poprzez $$\psi^{'} = U \psi$$, $$U$$ jest operatorem unitarnym, np. dla reprezentacji standardowej $$U = \frac{1}{\sqrt{2}} \begin{pmatrix}1 & 1 \\ - 1 & 1\end{pmatrix}$$

Operatory $$J^{\mu \nu} = \frac{\sigma^{\mu \nu}}{2} , \  \sigma^{\mu \nu} = \frac{1}{2} \left\lbrack \gamma^{\mu} , \gamma^{\nu} \right\rbrack$$ (algebra Diraca: $$\left\{ \gamma^{\mu} , \gamma^{\nu} \right\} = 2 \eta^{\mu \nu}$$ daje redukowalną reprezentację grupy Lorentza.

## Symetria chiralna

Wprowadzamy transformację globalną dla pola Diraca:

$$
\psi_{L} \rightarrow e^{i \theta_{L}} \psi_{L} , \  \psi_{R} \rightarrow e^{i \theta_{R}} \psi_{R} ,
$$

Która dla $$\theta_{R} = \theta_{L} = \alpha$$ jest transformacją wektorową U(1) $$\psi \rightarrow e^{i \alpha} \psi$$, a dla $$\theta_{R} = - \theta_{L} = \beta$$ jest transformacją chiralną $$\psi \rightarrow e^{i \beta \gamma_{5}} \psi , \  \gamma_{5} = i \gamma^{0} \gamma^{1} \gamma^{2} \gamma^{3} .$$ Obie są symetriami dla $$m = 0 .$$ Prądy Noether wynoszą:

$$
j_{V}^{\mu} = \overline{\psi} \gamma^{\mu} \psi , \  j_{A}^{\mu} = \overline{\psi} \gamma^{\mu} \gamma_{5} \psi .
$$

Dla $$m \neq 0$$ symetria jes złamana:

$$
\partial_{\mu} j_{A}^{\mu} = 2 i m \overline{\psi} \gamma_{5} \psi
$$

# Wzór LZS

$$
\left( 2 E_{\mathbf{k}} \right)^{\frac{1}{2}} a_{\mathbf{k}}^{\dagger \left( \frac{i n}{o u t} \right)} = - i Z^{- \frac{1}{2}} \lim_{t \rightarrow \mp \infty} {\int_{}^{} {d^{3} x} e^{- i k x} \overset{\overleftrightarrow{}}{\partial}_{0}} \phi
$$

$$
\left( 2 E_{\mathbf{k}} \right)^{\frac{1}{2}} \left( a_{\mathbf{k}}^{\dagger ( i n )} - a_{\mathbf{k}}^{\dagger ( o u t )} \right) = i Z^{- \frac{1}{2}} \int_{}^{} {d^{4} x} \partial_{0} \left( e^{- i k x} \overset{\overleftrightarrow{}}{\partial}_{0} \phi \right) = i Z^{- \frac{1}{2}} \int_{}^{} {d^{4} x} e^{- i k x} \left( \blacksquare_{x} + m^{2} \right) \phi
$$

(ostatnia równość z zastrzeżeniem o konwolucji w paczkę falową). Tak samo:

$$
\left( 2 E_{\mathbf{p}} \right)^{\frac{1}{2}} \left( a_{\mathbf{p}}^{( o u t )} - a_{\mathbf{p}}^{( i n )} \right) = i Z^{- \frac{1}{2}} \int_{}^{} {d^{4} y} e^{i p y} \left( \blacksquare_{y} + m^{2} \right) \phi
$$

$$
\left\langle \mathbf{p}_{1} , \ldots , \mathbf{p}_{n} ; T_{f} | \mathbf{k}_{1} , \ldots , \mathbf{k}_{m} ; T_{i} \right\rangle = \left( i Z^{- \frac{1}{2}} \right)^{n + m} \int_{}^{} {\prod_{i = 1}^{m} {d^{4} x_{i}} \prod_{j = 1}^{n} {d^{4} y_{j}} \exp \left( i \sum_{j = 1}^{n} {p_{j} y_{j}} - i \sum_{i = 1}^{m} {k_{i} x_{i}} \right)} \left( \blacksquare_{x_{1}} + m^{2} \right) \times \ldots \times \left( \blacksquare_{y_{n}} + m^{2} \right) \left\langle 0 \left| T \left( \phi \left( x_{1} \right) \ldots \phi \left( y_{n} \right) \right) \right| 0 \right\rangle = \left\langle \mathbf{p}_{1} , \ldots , \mathbf{p}_{n} | S | \mathbf{k}_{1} , \ldots , \mathbf{k}_{m} \right\rangle_{S c h r o e d i n g e r} = \left\langle \mathbf{p}_{1} , \ldots , \mathbf{p}_{n} | i T | \mathbf{k}_{1} , \ldots , \mathbf{k}_{m} \right\rangle_{S c h r o e d i n g e r}
$$

(ostatnia równość jest słuszna przy założeniu braku spektatorów). Operator ewolucji czasowej:

$$
U \left( t , t_{0} \right) \equiv e^{i H_{0} \left( t - t_{0} \right)} e^{- i H \left( t - t_{0} \right)}
$$

$$
\phi_{H} \left( t , \mathbf{x} \right) \mathbf{=} e^{i H \tau} \phi_{S} \left( t_{0} , \mathbf{x} \right) e^{- i H \tau} {= e}^{i H \tau} e^{- i H_{0} \tau} \left\lbrack e^{i H_{0} \tau} \phi_{S} \left( t_{0} , \mathbf{x} \right) e^{- i H_{0} \tau} \right\rbrack e^{i H_{0} \tau} e^{- i H \tau} \equiv e^{i H \tau} e^{- i H_{0} \tau} \phi_{I} \left( t , \mathbf{x} \right) e^{i H_{0} \tau} e^{- i H \tau} = U^{\dagger} \left( t , t_{0} \right) \phi_{I} \left( t , \mathbf{x} \right) U \left( t , t_{0} \right) .
$$

Przedostatnia równość jest definicją ewolucji operatora w obrazie oddziaływania, $$\tau = t - t_{0}$$.

$$
H_{I} \equiv e^{i H_{0} \tau} H_{i n t} e^{- i H_{0} \tau}
$$

$$
U \left( t , t_{0} \right) = T \exp \left( - i \int_{t_{0}}^{t} {d t^{'} H_{I} ( t ' )} \right)
$$

$$
\left\langle 0 | \phi \left( x_{1} \right) \ldots \phi \left( x_{n} \right) | 0 \right\rangle = \left\langle 0 | U^{\dagger} \left( t_{1} , t_{0} \right) \phi_{I} \left( x_{1} \right) U ( t_{1} , t_{0} ) \ldots U^{\dagger} \left( t_{n} , t_{0} \right) \phi_{I} \left( x_{n} \right) U ( t_{n} , t_{0} ) | 0 \right\rangle = \left\langle 0 | U^{\dagger} \left( t_{1} , t_{0} \right) \phi_{I} \left( x_{1} \right) U ( t_{1} , t_{2} ) \phi_{I} \left( x_{2} \right) \ldots U \left( t_{n - 1} , t_{n} \right) \phi_{I} \left( x_{n} \right) U ( t_{n} , t_{0} ) | 0 \right\rangle = \left\langle 0 | U^{\dagger} \left( t , t_{0} \right) \left\lbrack {U \left( t , t_{1} \right) \phi}_{I} \left( x_{1} \right) U ( t_{1} , t_{2} ) \phi_{I} \left( x_{2} \right) \ldots U \left( t_{n - 1} , t_{n} \right) \phi_{I} \left( x_{n} \right) U ( t_{n} , - t ) \right\rbrack U ( - t , t_{0} ) | 0 \right\rangle = \left\langle 0 | U^{\dagger} \left( t , t_{0} \right) T \left\{ \phi_{I} \left( x_{1} \right) \ldots \phi ( x_{n} ) U ( t , - t ) \right\} U ( - t , t_{0} ) | 0 \right\rangle \overset{t_{0} = - t , \  t \rightarrow \infty}{\rightarrow} \left\langle 0 | U^{\dagger} ( \infty , - \infty ) T \left\{ \phi_{I} \left( x_{1} \right) \ldots \phi \left( x_{n} \right) \exp \left( - i \int_{}^{} {d^{4} x \mathcal{H}_{I} ( x )} \right) \right\} | 0 \right\rangle = \frac{\left\langle 0 \left| T \left\{ \phi_{I} \left( x_{1} \right) \ldots \phi \left( x_{n} \right) \exp \left( - i \int_{}^{} {d^{4} x \mathcal{H}_{I} ( x )} \right) \right\} \right| 0 \right\rangle}{\left\langle 0 \left| T \exp \left( - i \int_{}^{} {d^{4} x \mathcal{H}_{I} ( x )} \right) \right| 0 \right\rangle} \  .
$$

Ponadto ponieważ $$H_{i n t} = \frac{\lambda}{4 !} \phi^{4}$$, to $$H_{I} ( t ) = \frac{\lambda}{4 !} \phi_{I}^{4} ( x )$$. Z rozkładu pól na część kreującą i anihilującą:

$$D ( x - y ) = \left\langle 0 | T \left\{ \phi ( x ) \phi ( y ) \right\} | 0 \right\rangle = \int_{}^{} {\frac{d^{4} p}{( 2 \pi )^{4}} \frac{i e^{- i p ( x - y )}}{p^{2} - m^{2} + i \epsilon}}$$ jest funkcją Greena operatora różniczkowego w równaniu Kleina-Gordona. Różne spośród czterech sposobów obchodzenia biegunów dają różne funkcje Greena spełniające różne warunki brzegowe.

## Amputacja zewnętrznych nóg

Ominięcie czynników związanych z zewnętrznymi odnogami diagramu, które skracają się z odpowiednimi czynnikami wzoru LZS. Dostajemy wtedy od razu element macierzowy,

## Reguły Feynmana dla teorii $$\mathbf{\phi}^{\mathbf{4}}$$

Wierzchołek: $$- i \lambda$$ (stała sprzężenia)

Pętla $$\int_{}^{} \frac{d^{4} k \ }{( 2 \pi )^{4}}$$ (całka po wolnej zmiennej pędowej)

# QED

## Pole Diraca

$$
S ( x - y ) = \left\langle 0 | T \left\{ \psi ( x ) \overline{\psi} ( y ) \right\} | 0 \right\rangle , \  T \left\{ \psi ( x ) \overline{\psi} ( y ) \right\} = \begin{cases}\psi ( x ) \overline{\psi} ( y ) \\ - \overline{\psi} ( y ) \psi ( x )\end{cases}
$$

$$
\widetilde{S} ( p ) = \frac{i}{p - m}
$$

## Foton

W cechowaniu kowariantnym:

$$
D_{\mu \nu} ( x - y ) = \left\langle 0 | T \left\{ A_{\mu} ( x ) A_{\nu} ( y ) \right\} | 0 \right\rangle
$$

$$
\widetilde{D}_{\mu \nu} ( k ) = \frac{- i}{k^{2} + i \epsilon} \eta_{\mu \nu}
$$

## Wierzchołek

$$
{}- i e \gamma^{\mu}
$$

## Zewnętrzne nogi

(oprócz czynników eksponenecjalnych)

|            | Foton                          | Elektron                     | Pozyton                      |
|------------|--------------------------------|------------------------------|------------------------------|
| Początkowy | $$ \epsilon_{\mu} ( k ) $$     | $$ u^{s} ( p ) $$            | $$ \overline{v}^{s} ( p ) $$ |
| Końcowy    | $$ \epsilon_{\mu}^{*} ( k ) $$ | $$ \overline{u}^{s} ( p ) $$ | $$ v^{s} ( p ) $$            |

$$
\psi ( x ) = \int_{}^{} {\frac{d^{3} p}{( 2 \pi )^{3} \sqrt{2 E_{\mathbf{p}}}} \left( \sum_{s = 1 , 2}^{} \left( a_{\mathbf{p} , s} u^{s} ( p ) e^{- i p x} + b_{\mathbf{p} , s}^{\dagger} v^{s} ( p ) e^{i p x} \right) \right)}
$$

**Pętle** Dodatkowy minus przy całkowaniu

# Całki po trajektoriach

$$
\left\langle q_{f} , T_{f} | q_{i} , T_{i} \right\rangle = \int_{q \left( T_{i} \right) = q_{i}}^{q \left( T_{f} \right) = q_{f}} {[ d q ] \exp {\left( \frac{i}{\hslash} S \right) .}}
$$

Ponieważ $$\int_{q \left( T_{i} \right) = q_{i}}^{q \left( T_{f} \right) = q_{f}} {[ d q ] = \int_{- \infty}^{\infty} {d \overline{q}}} \int_{q \left( T_{i} \right) = q_{i}}^{q ( t ) = \overline{q}} {[ d q ] \int_{q ( t ) = \overline{q}}^{q \left( T_{f} \right) = q_{f}} [ d q ]}$$ (bo w wykładniku jest $$\int_{T_{i}}^{T_{f}} {d t '} L = \int_{t}^{T_{f}} {d t '} L + \int_{T_{i}}^{t} {d t '} L$$), to:

$$
\left\langle q_{f} , T_{f} | \widehat{q} ( t ) | q_{i} , T_{i} \right\rangle = \int_{q \left( T_{i} \right) = q_{i}}^{q \left( T_{f} \right) = q_{f}} {[ d q ] q ( t ) \exp {\left( \frac{i}{\hslash} S \right) ,}}
$$

$$
\left\langle q_{f} , T_{f} | T \left\{ \widehat{q} \left( t_{1} \right) \ldots \widehat{q} ( t_{n} ) \right\} | q_{i} , T_{i} \right\rangle = \int_{q \left( T_{i} \right) = q_{i}}^{q \left( T_{f} \right) = q_{f}} {[ d q ] q \left( t_{1} \right) \ldots q ( t_{n} ) \exp {\left( \frac{i}{\hslash} S \right) .}}
$$

W teorii pola stosuje się oznaczenie na próżnię w $$t = - \infty : | 0 , t = - \infty \right\rangle \equiv | 0 \rangle$$. Stąd:

$$
\left\langle 0 | T \left\{ \widehat{\phi} \left( x_{1} \right) \ldots \widehat{\phi} ( x_{n} ) \right\} | 0 \right\rangle = \frac{\int_{}^{} {D \phi \phi \left( x_{1} \right) \ldots \phi \left( x_{n} \right) e^{i S} \ }}{\int_{}^{} {D \phi e^{i S}}}
$$

(mianownik bierze się z ewolucji stanu próżni od $$- \infty$$ do $$+ \infty$$). Funkcjonał generujący:

$$
W [ J ] \equiv \int_{}^{} {D \phi \exp {\left\{ \frac{i}{2} \int_{}^{} {d^{4} x \left\lbrack \partial_{\mu} \phi \partial^{\mu} \phi - \left( m^{2} - i \epsilon \right) \phi^{2} \right\rbrack + \int_{}^{} {d^{4} x \  \phi ( x ) J ( x )}} \right\} .}}
$$

Na podstawie analogii do wzoru:

$$
\int_{}^{} {\prod_{i = 1}^{N} {d y_{i} \exp {\left\lbrack - \frac{1}{2} \mathbf{y}^{\mathbf{T}} \mathbf{A y} + \mathbf{y}^{\mathbf{T}} \mathbf{z} \right\rbrack = ( 2 \pi )^{\frac{N}{2}} \left( \det A \right)^{- \frac{1}{2}} \exp \left\lbrack \frac{1}{2} \mathbf{z}^{\mathbf{T}} \mathbf{A}^{- 1} \mathbf{z} \right\rbrack}}}
$$

można wnioskować, że:

$$
W [ J ] = \int_{}^{} {D \phi \exp {\left\{ \int_{}^{} {\frac{d^{4} p}{( 2 \pi )^{4}} \left\lbrack \frac{i}{2} \widetilde{\phi} ( - p ) \left( p^{2} - m^{2} + i \epsilon \right) \widetilde{\phi} ( p ) + \widetilde{J} ( - p ) \widetilde{\phi} ( p ) \right\rbrack} \right\} = \int_{}^{} {D \phi e^{i S}} \exp {\left\{ \frac{1}{2} \int_{}^{} {\frac{d^{4} p}{( 2 \pi )^{4}} \widetilde{J} ( - p ) \widetilde{D} ( p ) \widetilde{J} ( p )} \right\} = W [ 0 ] \exp \left\{ \frac{1}{2} \int_{}^{} {d^{4} x d^{4} y J ( x ) D ( x - y ) J ( y )} \right\}}} ,}
$$

gdzie $$\frac{i}{p^{2} - m^{2} + i \epsilon}$$.

Stąd: $$D ( x - y ) = \left\langle 0 | T \left\{ \phi ( x ) \phi ( y ) \right\} | 0 \right\rangle$$ (odpowiednia pochodna funkcjonalna) i $$\left\langle 0 | T \left\{ \phi \left( x_{1} \right) \phi \left( x_{2} \right) \phi \left( x_{3} \right) \phi \left( x_{4} \right) \right\} | 0 \right\rangle = D \left( x_{1} - x_{2} \right) D \left( x_{3} - x_{4} \right) + D \left( x_{1} - x_{3} \right) D \left( x_{2} - x_{4} \right) + D \left( x_{1} - x_{4} \right) D ( x_{2} - x_{3} )$$. Funkcjonał:

$$
Z [ J ] = \ln {W [ J ] = Z [ 0 ] + \frac{1}{2} \int_{}^{} {d^{4} x d^{4} y J ( x ) D ( x - y ) J ( y )}}
$$

generuje **spójne** funkcje Greena.

# Renormalizacja teorii $$\mathbf{\phi}^{\mathbf{4}}$$

Przy zastosowaniu obcięcia nadfioletowego $$\Lambda$$ suma szeregu diagramów dwupętlowych wynosi:

$$
\frac{i}{A \left( \Lambda , p^{2} \right) p^{2} - m^{2} - B ( \Lambda )} , \  A \left( \Lambda , p^{2} \right) = 1 + \lambda^{2} \left( c_{1} \ln \frac{\Lambda^{2}}{p^{2}} + c_{2} \right) , \  B ( \Lambda ) = \frac{\lambda}{32 \pi^{2}} \left( \Lambda^{2} - m^{2} \ln \frac{\Lambda^{2} + m^{2}}{m^{2}} \right)
$$

Tutaj $$\lambda = \lambda_{0} ( \Lambda ) , \  m = m_{0} ( \Lambda )$$ itd. Na poziomie jednopętlowym $$A = 1$$, $$m_{R}^{2} = m_{0}^{2} ( \Lambda ) + B ( \Lambda )$$ i tak dobieramy $$m_{0} ( \Lambda )$$, aby zniosły się rozbieżności i propagator miał biegun w rzeczywistej, obserwowanej masie.

Na poziomie dwupętlowuym $$\int_{}^{} {d^{4} x e^{i p x} \left\langle 0 \left| T \left\{ \phi_{0} ( x , \Lambda ) , \phi_{0} ( 0 , \Lambda ) \right\} \right| 0 \right\rangle_{C} = \frac{i Z}{p^{2} - m_{R}^{2}} + \ldots}$$, gdzie pozostałe wyrazy są skończone, gdy $$p^{2} = m_{R}^{2}$$, $$Z = Z \left( \lambda_{0} ( \Lambda ) , \frac{\Lambda}{m_{R}} \right) = \left\lbrack \left( \frac{d}{d \left( p^{2} \right)} A \left( \Lambda , p^{2} \right) p^{2} \right)_{p^{2} = m_{R}^{2}} \right\rbrack^{- 1}$$.

Zakładamy, że $$m_{R}$$ jest taki, że $$\left\lbrack A \left( \Lambda , p^{2} \right) p^{2} - m_{0}^{2} ( \Lambda ) - B ( \Lambda ) \right\rbrack_{p^{2} = m_{R}^{2}} = 0$$. Definiujemy zrenormalizowaną funkcję falową: $$\phi_{0} = Z^{\frac{1}{2}} \left( \lambda_{0} , \frac{\Lambda}{m^{R}} \right) \phi_{R}$$. Jeśli we wzorze LZS użyjemy $$\phi_{R} , m_{R}$$ zamiast $$\phi_{0} , m_{0}$$. To otrzymamy skończone wyrażenie na funkcję Greena.

Funkcja czteropunktowa daje nowy wkład do rozbieżności:

$$
i \mathcal{M}_{2 \rightarrow 2} = - i \lambda + i \lambda^{2} \left( \beta_{0} \ln {\Lambda + s k o ń c z o n e} \right) + O \left( \lambda_{0}^{3} \right) .
$$

Pierwszy człon odpowiada diagramowi bez pętli. $$\beta_{0} = \frac{3}{16 \pi^{2}}$$, co odpowiada trzem wkładom od diagramów w formie „cukierka”: $$\mathcal{M = -} \lambda + 3 \mathcal{A} ( 0 )$$, gdzie $$\mathcal{A} ( p ) = \frac{( - i \lambda )^{2}}{2} \int_{}^{} \frac{d^{4} k}{( 2 \pi )^{2}} \frac{i}{k^{2} - m^{2} + i \epsilon} \frac{i}{( k - p )^{2} - m^{2} + i \epsilon}$$ (przy obliczeniu tego wyrażenia stosuje się obrót Wicka) i od $$p$$ zależy tylko skończona część.

Dla $$p_{1} = p_{2} = p_{3} = p_{4} = \left( m_{R} , 0 \right) :$$

$$
{}- i \lambda_{R} \equiv i \mathcal{M}_{2 \rightarrow 2} ( 0 ) = - i \lambda_{0} ( \Lambda ) \left\lbrack 1 - \lambda_{0} ( \Lambda ) \left( \beta_{0} \ln \frac{\Lambda}{m_{R}} \right) + s k o ń c z . \right\rbrack + O \left( \lambda_{0}^{3} \right) .
$$

Dla $$\left( p_{1} + p_{2} \right)^{2} = q^{2} \gg m_{R}$$:

$$
i \mathcal{M}_{2 \rightarrow 2} \left( q^{2} \right) = - i \lambda_{0} ( \Lambda ) \left\lbrack 1 - \lambda_{0} ( \Lambda ) \left( \frac{\beta_{0}}{2} \ln \frac{\Lambda^{2}}{q^{2}} + s k o ń c z . \right) \right\rbrack + O \left( \lambda_{0}^{3} \right) = - i \lambda_{R} \left\lbrack 1 + \lambda_{R} \frac{\beta_{0}}{2} \ln \frac{q^{2}}{m_{R}^{2}} \right\rbrack + O \left( \lambda_{R}^{3} \right) = - i \lambda_{e f f} ( q^{2} )
$$

I jest skończona w każdej skali energii.

Grupa renormalizacji

Funkcja n-punktowa:

$$
\Gamma_{R} \left( p_{i} ; g_{R} , \mu \right) = Z^{- \frac{n}{2}} \left( g_{0} ( \Lambda ) , \frac{\Lambda}{\mu} \right) \Gamma_{0} \left( p_{i} ; g_{0} ( \Lambda ) , \Lambda \right) .
$$

Równanie grupy renormalizacji:

$$
\left\lbrack \Lambda \frac{\partial}{\partial \Lambda} + \beta \left( g_{0} \right) \frac{\partial}{\partial g_{0}} - n \eta \left( g_{0} \right) \right\rbrack \Gamma_{0} \left( p_{i} ; g_{0} , \Lambda \right) = 0 ,
$$

$$
\beta \left( g_{0} \right) = \Lambda \frac{d g_{0}}{d \Lambda} , \  \eta \left( g_{0} \right) = \frac{1}{2} \Lambda \frac{d}{d \Lambda} \ln Z
$$

