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
e^2{\cal W}^{\mu\nu}\frac{1}{q^4}L_{\mu\nu}.
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
d\Gamma(P\rightarrow P'\gamma^*)L(M_{l^+l^-})
\frac{dM_{l^+l^-}^2}{M_{l^+l^-}^2}.
$$
where
$$
L(M_{l^+l^-})=\sqrt{1-\frac{4m^2_l}{M_{l^+l^-}^2}}
\left(1+\frac{4m^2_l}{M_{l^+l^-}^2}\right)
$$
is the dilepton phase space factor.
This gives
$$
\begin{split}
\frac{d\Gamma(P\rightarrow P'l^+l^-)}
{dM_{l^+l^-}^2\Gamma(P\rightarrow P'\gamma)}=&
\frac{\alpha}{3\pi}L(M_{l^+l^-})
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
\Gamma(M)_{l^+l^-}=\frac{4\pi\alpha^2}{3g^2_V}\frac{M^4_V}{M^3}L(M).
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
\frac{M^4_\rho}{(M^2-M^2_\rho)^2+M^2\Gamma^2_\mathrm{tot}}L(M)\\
=&\frac{4\pi\alpha^2}{3M^3}
\sqrt{1-\frac{4m^2_\pi}{M^2}}L(M)
|F_\pi|^2,
\end{split}
$$
where $F_\pi$ is the eTFF of charged pions and 
$$
\Gamma_{\pi\pi}=\frac{g^2_\rho}{2\pi}\frac{p^3_\pi}{M^2}.
$$
#### NN bremsstrahlung
In general, any process $NN\rightarrow NNX\gamma^*$,but some processes treated separately.
In the non-resonant, "quasi-elastic" process, one or both nucleons go off-shell before or after the photon emission and their virtuality is lifted by the strong interaction between nucleons, calculated with one boson exchange
In transport models - soft photon approximation:
- $\gamma^*$ emission following an elastic NN interaction with the phase space modifications due to the produced virtual photon. 
- Inference effects neglected
- Emission form a meson line are neglected - **but new GiBUU paper does not neglect!**
- Other processes, like resonance decay are added incoherently.
Sensitivity to form factors, interference terms.
$n-p$ much stronger than $p-p$ because of non-vanishing dipole moment and additional charged pion exchange channels. 
Important was and off-shell $\rho$ contributions to the eTFF of internal charged pion.
#### Drell-Yan
Cross-section for $q\bar q$ annihilation into dilepton
$$
\frac{d\hat\sigma}{dQ^2}=\frac{4\pi\alpha}{3Q^2}e^2(Q^2-\hat s).
$$
Factorization concept:
$$
\frac{d\sigma}{dQ^2}=\beta_c\sum_q\int dx\int dy f_q(x)f_{\bar q}
(y)\frac{d\hat\sigma}{dQ^2},
$$
where $\hat s = (xp_1+yp_2)^2\approx xys$.
Higher-order effects - implemented as $K$-factors.
In $p+A$ and $A+A$ additional effects:
- structure functions modified by embedding nucleons in medium
- gluon shadowing
- Croning effect - $p_T$ enhancement due to parton multiple scattering
#### Thermal dileptons
For a perturbative gas of quarks and gluons.
$$
\frac{dN_{ll}}{d^4x}=-4e^4\int
\frac{d^3k_1}{(2\pi)^32E_1}
\frac{d^3k_2}{(2\pi)^32E_2}
{\cal W}^{\mu\nu}\frac{1}{q^4}L_{\mu\nu},
$$
where the leptonic tensor, integrated over the momenta if final state leptons, for momentum transfer much larger than the lepton mass gives
$$
\frac{1}{q^4}L_{\mu\nu}=-\frac{\alpha^2}{3\pi^3M^2}\left(
g_{\mu\nu}-\frac{q_\mu q_\nu}{M^2}
\right).
$$
Partonic tensor is the thermal average
$$
W^{\mu\nu}(q)=\int d^4xe^{-iqx}
\langle\langle j^\mu_\mathrm{em}(x)j^\nu_\mathrm{em}(0)\rangle\rangle.
$$
This gives for $q^2>>m^2_e$, 
$$
\frac{dN_{ll}}{d^4xd^4q}=\frac{\alpha^2}{12\pi^3M^2}W\mu_\mu(q).
$$
In practice, it is enough to take only three lightest quarks, weighted by their electric charge,
$$
j^\mu_\mathrm{em}=\frac{2}{3}\bar u\gamma^\mu u-
\frac{1}{3}\bar d\gamma^\mu d-
\frac{2}{3}\bar s\gamma^\mu s.
$$
After integrating,
$$
\frac{dN_{ll}}{dM}=R_\mathrm{part}\frac{\alpha^2}{6\pi^2}M^2TK_1(M/T),
$$
where
$$
R_\mathrm{part}=N_c\sum_{f=u,d,s}e^2_f=
3\left(\frac{4}{9}+\frac{1}{9}+\frac{1}{9}\right)=2.
$$
The microscopic properties of QGP enter the rate only through the number $R_\mathrm{part}$.

For $M/T>5$, which corresponds to the IMR, the above formula agrees within 5% with black-body radiation, which allows to extract the temperature of the QGP. It also dominates the yield due to its larger temperature value.
For the hadronic part:
$$
j^\mu_\mathrm{em}=\frac{2}{3}\bar u\gamma^\mu u-
\frac{1}{3}\bar d\gamma^\mu d-
\frac{1}{3}\bar s\gamma^\mu s=
j^\mu_\mathrm{em,\rho}+j^\mu_\mathrm{em,\omega}+j^\mu_\mathrm{em,\phi}
$$
with
$$
\begin{split}
j^\mu_\mathrm{em,\rho}  =&\frac{1}{2}(\bar u\gamma^\mu u-\bar d\gamma^\mu d),\\
j^\mu_\mathrm{em,\omega}=&\frac{1}{6}(\bar u\gamma^\mu u+\bar d\gamma^\mu d),\\
j^\mu_\mathrm{em,\phi}  =&\frac{1}{2}\bar s\gamma^\mu s,
\end{split}
$$
and
$$
\frac{dN_{ll}}{dM}=R_\mathrm{had}\frac{\alpha^2}{6\pi^2}M^2TK_1(M/T),
$$
where 
$$
R_\mathrm{had}=
\frac{\sigma(e^+e^-\rightarrow\mathrm{hadrons})}
{\sigma(e^+e^-\rightarrow\mu^+\mu^-)}\propto
\frac{1}{M^2}\mathrm{Im}\Pi_\mathrm{em}.
$$
In vacuum $\rho$ propagator dominated by pion loops. $\Rightarrow$ Decays to $\pi^+\pi^-$ play important role. $\Rightarrow$  Inverse process $\pi^+\pi^-$ fusion. $\Rightarrow$ In the pion-dominated medium, $\rho$ propagator might be sensitive to chiral symmetry restoration, whose Goldstone bosons are pions.

Dilepton polarization make occur already from local anisotropy of plasma, due to, e.g., Bjorken flow, or, at finite transverse momentum, due to available phase space constrained by the parent particle decay.
#### Chiral symmetry restoration
Chiral symmetry is broken in vacuum due to gluon self-interaction, leading to the appearance of non-zero quark-antiquark and gluon condensates.
Originally, a nearly linear drop of chiral condensate was predicted because of its nearly zero value inside of baryons. More recent results do not support it because of a hard-core repulsive nucleon-nucleon interaction.

From current algebra, the relation was derived
$$
m_\rho=\sqrt 2g_Vf_\pi.
$$
Brown and Rho dropping mass suggestion amounts to
$$
\frac{m^*_V}{m_V}\sim\frac{f^*_\pi}{f_\pi}=
\left(\frac{\langle\bar qq\rangle^*}{\langle\bar qq\rangle}\right)^{1/3}.
$$
Weinberg sum rules are
$$
\begin{split}
\int dss^{-1}(D^V(s)-D^A(s))=&f^2_\pi,\\
\int ds(D^V(s)-D^A(s))=&f^2_\pi m_q=-2m_q\langle\bar qq\rangle,\\
\int dss(D^V(s)-D^A(s))=&-2\pi\alpha_sO^\mathrm{SB}_4,
\end{split}
$$
where $O^\mathrm{SB}_4$ is the chirally odd combination of four-quark condensates in vector and axial channels.

In chiral mixing scenario, the finite-temperature vector correlator can be expressed as a mixing of vacuum vector and axial correlators
$$
\Pi^{\mu\nu}_V(q,T)=(1-\epsilon)\Pi^{\mu\nu}_V(q,0)+\epsilon\Pi^{\mu\nu}_A(q,0),
$$
where the mixing parameter was calculated in chiral limit $m_\pi=0$, as a loop integral
$$
	\epsilon=\frac{2}{f^2_\pi}\int\frac{d^3k}{2\pi^3\omega_k}f_\pi(\omega_k,T)
$$
#### Dileptons in microscopic models
Writing the rate in the hadronic phase as
$$
\frac{dR}{d^4xd^qp}=-\frac{\alpha^2}{\pi^3}\frac{L(M)}{M^2}
\mathrm{Im}\Pi_\mathrm{em}(M,q,T,\mu_\mathrm{B})f^\mathrm{B}(q_0,T),
$$
one has, in analogy to hadronic tensor $W^{\mu\nu}$,
$$
\Pi^{\mu\nu}_\mathrm{em}(q)=
i\int d^4x~e^{ipx}\theta(x_0)\langle\Omega|[j^\mu(x),^\nu(0)]|\Omega\rangle,
$$
where $|\Omega\rangle$ characterizes the medium.
In strict VMD,
$$
\mathrm{Im}\Pi^\mathrm{had}_\mathrm{em}=
\sum_{V=\rho,\omega,\phi}\left(\frac{m^2_V}{g^2_V}\right)\mathrm{Im}D_V(M).
$$
The in-medium propagator is 
$$
D_\rho=\frac{1}
{M^2-m^2_\rho-\Sigma_{\rho\phi\phi}-\Sigma_{\rho M}-\Sigma_{\rho B}}.
$$
The additional terms are due to the dressing of a pion loop by interaction of virtual pions, for example with surrounding baryons to form a baryonic resonance-hole pair.
In the partonic phase, using pQCD,
$$
\mathrm{Im}\Pi^\mathrm{had}_\mathrm{em}=
N_c\sum_{q=u,d,s,c}\frac{M^2}{12\pi}e^2_q\left(1+\frac{\alpha_s(M)}{\pi}+...\right)
$$
#### Experiment
###### Nucleon-nucleon
1. RHIC and LHC data well described by hadronic cocktail
2. At SPS early experiments reported excess over "conventional sources"
3. Helios 1 directly measured $\eta$ Dalitz decays, this provided upper limits for unconventional sources
4. Further reduced to 23% by CERES
5. NA60 provided eTFF for $\eta$ and $\omega$ Dalitz thanks to an iterative procedure:
	- Not interesting processes, direct decays of $\omega$ and $\phi$, and cham are subtracted by fitting the normalization and peak shape by simulation
	- $\omega$, $\eta$ Dalitz and $\rho$ are retained
	- Corrected for acceptance using the extracted meson transverse mass distributions
	- After correction, the spectrum is fitted with $\eta$, $\omega$ and $\rho$ contributions, varying the normalization
6. Normalizing HI and NN to pion multiplicity takes into account baryon resonances, because pions come from baryon decays.
7. The observation that C+C agrees with NN ref. explains the long standing ‘‘DLS puzzle’’ connected to the dilepton yield measured in C–C collisions as being due to unexpected baryonic contributions not properly accounted for in the theoretical description of the data.
8. In the IMR, open charm and Drell-Yan dominate, but QGP contribution is also present
9. NA60: 130 kHz, 440.000 signal pairs. Drell-Yan: fix its contribution relative to open charm with p-A collisions at higher energy, scaled down with excitation functions calculated with properly adjusted PYTHIA, use the $J/\psi$ yield to fix DY.
10. The contributions from ηDalitz decay were determined by the conservative ansatz that the LMR yield at invariant masses around 200 MeV/$c^2$  is fully saturated by Dalitz decays
11. The acceptance filter of NA60 roughly cancels the Boltzmann factor.
12. At RHIC, the suppression of high $p_t$ $\pi^0$ and other mesons is attributed to quenching of hard partons in QGP created nearly instantaneously.
13. Important hadronic contribution above 1 GeV are multi-pion processes.