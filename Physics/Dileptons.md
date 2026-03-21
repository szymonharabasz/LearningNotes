## Electromagnetic decays of hadrons
#### Dalitz decays
A general expression for a partial width for a decay of particle $P$ into $n$-body final state:
$$
d\Gamma=\frac{(2\pi)^4}{2M}|{\cal T}|^2d\Phi_n(P;p_1,...p_n),
$$
where $d\Phi_n$ is the $n$-body final state phase space. For a Dalitz decay of a particle into three particles
$$
d\Gamma=\frac{1}{(2\pi)^5}\frac{1}{16M^2}|{\cal T}|^2
|\vec p^*_1||\vec p_3|dm_{12}d\Omega^*_1d\Omega_3,
$$
where the variables ${\cdot}^*_1$ are for particle 1 in the two-body rest frame.
a hadron
$$
\sum_\mathrm{polarizations}|{\cal T}(P\rightarrow P'l^+l^-)|^2=
e^2{\cal W}^{mu\nu}\frac{1}{q^4}L_{\mu\nu}.
$$
The hadronic tensor,
$$
{\cal W}^{\mu\nu}=\sum_\mathrm{spins}{\cal M}^\mu{\cal M}^\nu,
$$
describes the $P\rightarrow P'\gamma^*$ transition. $1/q^4$ is square of the photon propagator. The lepton tensor,
$$
L_{\mu\nu}=\sum_\mathrm{spins}j_\mu j_\nu,
$$
with the leptonic current,
$$
j^\mu=\bar u(k_1)\gamma^\mu v(k_2),
$$
accounts for the photon-dilepton conversion. Explicitly,
$$
L^{\mu\nu}=4(k^\mu_1k^\nu_2+k^\mu_2k^\nu_1-(k_1\cdot k_2+m^2_l)g^{\mu\nu}).
$$
One can also define **density matrices**: hadronic (production):
$$
\rho^\mathrm{hadron}_{\lambda\lambda'}=
\frac{e^2}{q^4}\epsilon^\mu(q,\lambda)W_{\mu\nu}\epsilon^\nu(q,\lambda')^*,
$$
and leptonic (decay):
$$
\rho^\mathrm{lepton}_{\lambda\lambda'}=
\epsilon^\mu(q,\lambda)L_{\mu\nu}\epsilon^\nu(q,\lambda')^*
$$
The polarization vectors for the three helicities in the rest frame of the virtual photon are
$$
\begin{split}
\epsilon^\mu(m,-1)=&\frac{1}{\sqrt{2}}(0,1,-i,0),\\
\epsilon^\mu(m,0)=&\frac{1}{\sqrt{2}}(0,0,01),\\
\epsilon^\mu(m,1)=&-\frac{1}{\sqrt{2}}(0,1,i,0),\\
\end{split}
$$
Then one can write
$$
\sum_\mathrm{polarizations}|{\cal T}|^2=
\sum_{\lambda\lambda'}\rho^\mathrm{hadron}_{\lambda\lambda'}\rho^\mathrm{lepton}_{\lambda'\lambda},
$$
on utilizing the fact that
$$
\sum_\lambda\epsilon^\mu(q,\lambda)\epsilon^\nu(q,\lambda)^*=
-g^{\mu\nu}+\frac{q^\mu q^\nu}{q^2}.
$$
The vector meson dominance amounts to assume that
$$
{\cal M}^\mu=J^\mu=e\sum_V\frac{m^2_V}{g_V}V^\mu,
$$
where $V$ are the vector meson fields $\rho$, $\omega$, and $\phi$.
For Dalitz decays,
$$
{\cal M}^\mu(P\rightarrow P'\gamma^*)=f_{PP'}(q^2)
\varepsilon^{\alpha\beta\gamma\mu}p_\alpha q_\beta \epsilon_\gamma,
$$
where $p_\alpha$ and $q_\beta$ are the four momenta of the daughter particle and the virtual photon, respectively, $\epsilon_\gamma$ is the polarization vector, and $f_{PP'}(q^2)$ is eTFF, which is constant for a point-like particle.
The partial decay width can be factorized:
$$
d\Gamma(P\rightarrow P'l^+l^-)=
\frac{\alpha}{3\pi}
d\Gamma(P\rightarrow P'\gamma^*)
\sqrt{1-\frac{4m^2_l}{M_{l^+l^-}^2}}
\left(1+\frac{4m^2_l}{M_{l^+l^-}^2}\right)
\frac{dM_{l^+l^-}^2}{M_{l^+l^-}^2}.
$$
This gives
$$
\begin{split}
\frac{d\Gamma(P\rightarrow P'l^+l^-)}
{dM_{l^+l^-}^2\Gamma(P\rightarrow P'\gamma)}=&
\frac{\alpha}{3\pi}
\sqrt{1-\frac{4m^2_l}{M_{l^+l^-}^2}}
\left(1+\frac{4m^2_l}{M_{l^+l^-}^2}\right)
\frac{1}{M_{l^+l^-}^2}\\
\times&
\left[
\left(1+\frac{M_{l^+l^-}^2}{M^2-M^2_{P'}}\right)^2-
\frac{4M^2M_{l^+l^-}^2}{(M^2-M^2_{P'})^2}
\right]^{3/2}
\left|
\frac{f_{PP'}(M_{l^+l^-}^2)}{f_{PP'}(0)}
\right|^2.
\end{split}
$$
Compactly,
$$
\frac{d\Gamma(P\rightarrow P'l^+l^-)}
{dM_{l^+l^-}^2\Gamma(P\rightarrow P'\gamma)}=
\mathrm{QED}\times F^2_{PP'}(M_{l^+l^-}^2).
$$
Using the VDM, the eTFF normalized to the photon point is written as
$$
F^2_{PP'}(M_{l^+l^-}^2)=
\frac{\sum_V\frac{g_{PP'V}}{g_V}
\frac{My ^2_V}{M^2_V-M^2_{l^+l^-}-i\Gamma_VM_V}}
{\sum_V\frac{g_{PP'V}}{g_V}}\approx
\frac{1}{1-\frac{q^2}{\Lambda^2}}\approx
1+\frac{q^2}{\Lambda}^2=1+\frac{1}{6}q^2\langle r^2_{PP'}\rangle^{1/2},
$$
when in the limit of small widths a pole approximation has been used. The $\Lambda^{-2}$ is the derivative of the eTFF with respect to $q^2$ at the photon point.
#### Direct decays of vector mesons
The partial width is
$$
d\Gamma=\frac{1}{32\pi^2}|{\cal T}(V\rightarrow l^+l^-)|^2\frac{p}{M}d\Omega,
$$
where the momentum $p$ of electron in the center of mass is
$$
p=\frac{
\left(
(M^2-(m_a+m_b)^2)(M^2-(m_a-m_b)^2)
\right)^{1/2}
}{2M}.
$$
The matrix element, averaged over the vector meson polarization and lepton spin factorizes as
$$
|{\cal T}(V\rightarrow l^+l^-)|^2=|{\cal W}(V\rightarrow\gamma^*)|^2\frac{4}{M^4}
	|L(\gamma^*\rightarrow l^+l^-)|^2=
	\frac{16\pi^2\alpha^2}{3}\frac{M^4_V}{g^2_V}(M^2-2m^2_l)\frac{1}{M^4}.
$$
From the above expression for $\cal M^\mu$, one gets the matrix element at the meson pole mass
$$
|{\cal W}(V\rightarrow\gamma^*)|^2=\frac{4\pi\alpha}{g^2_V}M^4_V.
$$
One has also
$$
|L(\gamma^*\rightarrow l^+l^-|^2=\frac{4\pi\alpha}{3}(M^2-2m^2_l).
$$
Finally, the dilepton decay widths is written as
$$
\Gamma(M)_{l^+l^-}=\frac{4\pi\alpha^2}{3g^2_V}\frac{M^4_V}{M^3}
\sqrt{1-\frac{4m^2_l}{M^2}}
\left(1+\frac{4m^2_l}{M^2}\right).
$$
The coupling constants are:
$$
g_\rho=5.03,~~~g_\omega=17.1,~~~g_\phi=-12.9.
$$
These values are in *Feassler, Fuchs, Krivoruchenko, Phys. Rev. C **61**, 035206*. 
The resonance mass spectrum can be parametrized as
$$
\frac{dN}{dM}=\frac{dNp(M)}{dM}
\frac{\Gamma_\mathrm{in}\Gamma_{l^+l^-}M^2}
{(M^2-M^2_V)^2+M^2\Gamma^2_\mathrm{tot}},
$$
where $\Gamma_\mathrm{in}$ and $\Gamma_{l^+l^-}$ account for partial widths related to the production and the decay processes, respectively, $\frac{dN_p(M)}{dM}$ quantifies the number of initial states populating the resonance at mass $M$. In a two-step process, dominating in baryon-rich matter:
$$\
\mathrm{NN}\rightarrow\mathrm{NN^*}/\Delta\rightarrow
\mathrm{NN\rho}\rightarrow\mathrm{NN}l^+l^-,
$$
the low-mass tail of the vector meson will be strongly enhanced.
At high energies a big role is played by the pion annihilation, the cross-seciton is calculated as
$$
\begin{split}
\sigma_{\pi\pi\rightarrow\rho\rightarrow l^+l^-}=&
\frac{4\pi}{p^2_\pi}
\frac{M\Gamma_{\pi\pi}\Gamma_{l^+l^-}M}
{(M^2-M^2_\rho)^2+M^2\Gamma^2_\mathrm{tot}}\\
=&\frac{8\pi\alpha^2p_\pi}{3M^3}
\frac{M^4_\rho}{(M^2-M^2_\rho)^2+M^2\Gamma^2_\mathrm{tot}}
\sqrt{1-\frac{4m^2_l}{M^2}}
\left(1+\frac{4m^2_l}{M^2}\right)\\
=&\frac{4\pi\alpha^2}{3M^3}
\sqrt{1-\frac{4m^2_l}{M^2}}
\sqrt{1-\frac{4m^2_\pi}{M^2}}
\left(1+\frac{4m^2_l}{M^2}\right)
|F_\pi|^2,
\end{split}
$$
where $F_\pi$ is the eTFF of charged pions and 
$$
\Gamma_{\pi\pi}=\frac{g^2_\rho}{2\pi}\frac{p^3_\pi}{M^2}.
$$