The Helmholtz free energy,
$$
\Gamma[B]=-k_{\rm B}T\log Z[B]
$$
is a functional of the magnetic field, Gibbs free energy is its Legendre transform $\Gamma[M]$ and it is a functional of the magnetization.

In the Polchinski-Wilson approach, we integrate out short-range/rapid fluctuation modes $\phi_>$ at momentum scale $p>k$ and obtain a series of Hamiltonians for long-range/slow modes. In the effective average action approach, we concentrate on calculating the Gibbs free energy *of rapid modes that have been already integrated out*.
In the Polchinski-Wilson approach, $k$ is the UV cutoff for the Hamiltonian, analogous to $\Lambda$, in the effective average action, $k$ is the IR cutoff for calculating the effective action.

The effective average action at $k=\Lambda$, that is, when no fluctuations are integrated out, is equal to the microscopic Hamiltonian:
$$
\Gamma_{k=\Lambda}[M]=H[\phi=M].
$$
At $k=0$, when all fluctuations are integrated out, is it just the Gibbs free energy of the original model:
$$
\Gamma_{k=0}[M]=\Gamma[M].
$$
To decouple the slow modes, the idea is to give them large mass. For the physics of critical phenomena, this means that the mass term, $r\phi^2/2$ corresponds to a deviation from criticality, because $r\propto T=T_c$ at least at the mean-field level. With large mass the deviation is large and the system is far from criticality, where thermal fluctuations are small.

One adds a "momentum-dependent mass term" to the Hamiltonian:
$$
Z_k[B]=\int{\cal D}\phi(x)\exp\left(
-H[\phi]-\Delta H_k[\phi]+\int B\phi
\right),
$$
where
$$
\Delta H_k[\phi]=\frac{1}2 \int_qR_k[q]\phi_q\phi_{-q}.
$$
The **cutoff function** $R_k(q)$ should fulfil:
- For $k=0$, $R_{k=0}(q)=0$ identically to ensure:
$$
Z_[k=0][B]=Z[B].
$$
- For $k=\Lambda$, all fluctuations are *frozen* (they do not propagate), which is ensured by $R_{k=\Lambda}(q)=\infty$. It means that the functional integral is dominated by the stationary point of the free energy (action in QFT) and the saddle-point approximation (Gaussian integral) can be used that filters out the classical field configurations (and the bare action in QFT).
- In between, rapid modes are almost unaffected, so $R_k(|q|>k)\approx 0$. 
One then defines:
$$
W_k[B]=\log Z_k[B].
$$
It is the Helmholtz free energy. 
In QFT we write:
$$
Z[j]=e^{W[J]}=\int{\cal D}\varphi e^{-S[\varphi]+\int J\varphi}.
$$

Its Legendre transform:
$$
\Gamma'_k[M]+W_k[B]=\int BM,
$$
where $M(x)$ is by definition the average of $\phi(x)$ and is given by:
$$
M(x)=\frac{\delta W_k}{\delta B(x)}.
$$
In the context of QFT we define:
$$
\Gamma[\phi]=\sup_J\left(
\int J\phi-W[J]
\right)
$$
(this definition guarantees that $\Gamma$ is convex) and at $J=J_\rm{sup}$ we get:
$$
0=\frac{\delta}{\delta J(x)}\left(
\int J\phi-W[J]
\right)\Rightarrow\phi=\frac{\delta W[J]}{\delta J}=
\frac{1}{Z[J]}\frac{\delta Z[J]}{\delta J}=
\langle\varphi\rangle_J.
$$
Here we *obtain* that the variable, on which $\Gamma$ depends is the average of the field.
The meaning of $\Gamma$ is revealed by studying its derivative:
$$
\frac{\delta\Gamma[\phi]}{\delta\phi(x)}=
-\int_y\frac{\delta W[J]}{\delta J(y)}\frac{\delta J(y)}{\delta\phi(x)}+
\int_y\frac{\delta J(y)}{\delta\phi(x)}\phi(y)+J(x)\equiv J(x).
$$
From definitions, one can obtain:
$$
e^{-\Gamma[\phi]}=e^{W[J]-\int J\phi}=
\int_\Lambda{\cal D}\varphi e^{-S[\varphi]+\int J\varphi}e^{-\int J\phi}
\stackrel{\varphi\rightarrow\varphi+\phi}{=}
\int_\Lambda{\cal D}\varphi e^{-S[\varphi+\phi]+\int J\varphi}=
\int_\Lambda{\cal D}\varphi e^{-S[\varphi+\phi]+
\int \frac{\delta\Gamma[\phi]}{\delta\phi}\varphi},
$$
where already a regularization of the integration measure has been indicated by $\int_\Lambda$.
For $k\rightarrow 0$, it is easy to show that $\Gamma'_k=\Gamma$ - the Gibbs free energy. However, $\Gamma'_\Lambda[M]\neq H[M]$, because of $\Delta H_{k=\Lambda}$ which is large. Then it is better to work with a modified free energy, defined by:
$$
\Gamma_k[M]+W_k[B]=\int BM-\frac{1}2\int_q R_k(q)M_qM_{-q}.
$$
It gives the right $k\rightarrow\Lambda$ limit.
In QFT, the interpretation is:
$$
\Gamma_{k\rightarrow\Lambda}[\phi]\sim S_\rm{bare},~~~
\Gamma_{k\rightarrow0}[\phi]=\Gamma[\phi].
$$
The regularized functional is then written as:
$$
e^{W_k[J]}=Z_k[J]:=\exp\left(
-\Delta S_k\left[\frac{\delta}{\delta J}\right]
\right)Z[J]=
\int_\Lambda{\cal D}\varphi e^{-S[\varphi]-\Delta S_k[\varphi]+\int J\varphi},
$$
where
$$
\Delta S_k[\varphi]=\frac{1}2\int\frac{d^Dq}{(2\pi)^D}
\varphi(-q)R_k(q)\varphi(q).
$$
The modified Legendre transform is written as
$$
\Gamma_k[\phi]=\sup_J\left(\int J\phi-W_k[J]\right)-\Delta S_k[\phi].
$$
The average field remains
$$
\phi(x)=\frac{\delta W[J]}{\delta J(x)},
$$
and the equation of motion receives an additional term from the regulator,
$$
J(x)=\frac{\delta\Gamma_k[\phi]}{\delta\phi(x)}+(R_k\phi)(x),
$$
from which
$$
\frac{\delta J(x)}{\delta\phi(y)}=
\frac{\delta^2\Gamma_k[\phi]}{\delta\phi(x)\delta\phi(y)}+R_k(x,y).
$$
On the other hand,
$$
\frac{\delta\phi(y)}{\delta J(x')}=
\frac{\delta^2W_k[J]}{\delta J(x')\delta J(y)}\equiv
G_k(y-x').
$$
Putting together,
$$
\delta(x-x')=\frac{\delta J(x)}{\delta J(x')}=
\int d^Dx\frac{\delta J(x)}{\delta\phi(y)}\frac{\delta\phi(y)}{\delta J(x')}=
\int d^Dy(\Gamma^{(2)}_k[\phi]+R_k)(x,y)~G_k(y-x'),
$$
or, in operator notation
$$
\mathbb{1}=(\Gamma^{2}_k+R_k)~G_k,
$$
where
$$
\Gamma^{(n)}_k[\phi]=\frac{\delta^n\Gamma_k[\phi]}{\delta\phi...\delta\phi}.
$$
Note that for a fixed $\phi$. the $J$ that attains supremum, $J=J_\sup$, necessarily depends on $k$. In any case, in such situation one writes:
$$
\begin{split}
\partial_t\Gamma_k[\phi]&=
-\left.\partial_tW_k[J]\right|_\phi+\int(\partial_t\phi)J
-\partial_t\Delta S_k[\phi]=
-\left.\partial_tW_k[J]\right|_J
-\partial_t\Delta S_k[\phi]\\
&=\frac{1}{2}\int\frac{d^dq}{(2\pi)^D}\partial_tR_k(q)G_k(q)\\
&=\frac{1}{2}\mathrm{Tr}\left[
\partial_tR_k\left(\Gamma^{(2)}_k[\phi]+R_k\right)^{-1}
\right].
\end{split}
$$
The **exact RG** equation is:
$$
\delta_k\Gamma_k=\frac{1}2\int_q\partial_k R_k(q)\left(
\Gamma_k^{(2)}[M]+{\cal R_k}
\right)^{-1}_{q,-q}.
$$
It is often rewritten as
$$
\partial_k\Gamma_k=\frac{1}2{\tilde \partial}_k\rm{Tr}\log\left(
\Gamma_k^{(2)}+R_k
\right),
$$
where ${\tilde \partial}_k$ acts only on the $k$-dependence of $R_k$ and not of $\Gamma_k^{(2)}$:
$$
{\tilde \partial}_k=\frac{\partial R_k}{\partial k}\frac{\partial}{\partial R_k}.
$$
One often uses the RG "time" $t=\log k/\Lambda$ with $\dot R_k=\partial_t R_k=k\partial_k R_k$.

Popular choices for the regulator are:
$$
R_k(q)=\frac{q^2}{e^{q^2/k^2}-1}
$$
or
$$
R_k(q)=(k^2-q^2)\theta(k^2-q^2).
$$

