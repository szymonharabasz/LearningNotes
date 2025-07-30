#### Scattering physics
$$
x_F=\frac{2p_L}{\sqrt{s}}
$$
W pracach *Szczurek et al.*:
- $t_E$ to współrzędna $x^0$ w c.m.?
- Spektatorzy mogą istnieć przed $t=0$? Ich położenie i prędkość w retardowanym czasie $t_r>0$ mają wpływ na ruch pionów?
- Czy modelowanie spektatorów jako sfer ma wpływ na wyniki w porównaniu z sytuacją gdyby były modelowane jako cząstki punktowe o odpowiedniej masie i ładunku
- Zrobić porównanie poza mid-rapidity
- Zaimplementować spektatorów istniejących przed $t_\mathrm{freezeout}$.
#### Drell-Yan
* Early results
    * D-Y successfully predicted: scaling behavior of the cross-section, angular distributions of leptons, linear dependence of the cross-section on the mass number of the target nucleus, universality of the PDFs.
    * Problems: 
        * cross-sections about 2 times larger than predicted (K-factor), based on naive parton model PDFs extracted from DIS experiments
        * mean $p_T$ about 1 GeV instead of about 0.3 GeV
* Drell-Yan cross section can be expanded:
$$
\frac{d\sigma}{dQ^2}=\frac{d\sigma}{dQ^2}^{LP}\left(1+{\cal O}\left(\frac{1}{Q^n}\right)\right).
$$
In that situation, quantum interferecne between the dynamics taking place at hard scale $Q\gg1/\mathrm{fm}$ and hadronic scale $\Lambda_\mathrm{QCD}\sim1/\mathrm{fm}$ is suppressed in terms of $(\Lambda_\mathrm{QCD}/Q)^n$. This holds not only for the exchange of a virtual photon, but any color neutral massive boson.
All known contributions to the leading power are either factorisable or calcelled in perturbative calculations to all orders in $\alpha_s$.
* Leading order - convolution of three classical "probabilities": perturbative hard scattering cross-section and two universal PDFs
* First subleading order - convolution of perturbative scattering, non-perturbative, universal PDF, nonperturbative, universal multiparton correlation funcion:
    * three partons for transversely polarized colliding hadrons
    * four partons for two unpolarized or longitudinally polarized
    * Factorization of the first subleading order is also valid for other hard scattering processes
    * Higher orders do not factorize
* EMC experiment observed deviation from linear $A$ scaling in p+Fe reactions
    * Modification of PDFs in nuclear matter
    * "pion-excess" model - mesons responsible for binding between nucleons can enhance antiquark content, no enahancement was observed
    * follow-up experiments found antiquark suppression at low $x$ - nuclear shadowing effect
    * Fermilab will extend to even larger $x$
* One can extract sea $\bar{d}/\bar{u}$ assymetry by comparing D-Y in p-d and p-p collisions
    * Gottfired integral:
    $$
    I_G=\int_0^1\frac{F_2^p(x) - F_2^n(x)}{x}dx=\frac{1}{3}+\frac{2}{3}\int_0^1\left[\bar{u}_p(x)-\bar{d}_p(x)\right]dx,
    $$
    where $F_2^{p/n}(x)$ are structure functions of proton and neutron, measured in DIS. For SU(3) flavor-symmetric sea one would have Gorrfried Sum Rule (GSR) $I_G=\frac{1}{3}$.
    * Complementary:
    $$
    \frac{\sigma_{DY}(p+d)}{2\sigma_{DY}(p+p)}\approx\frac{1}{2}\left[1+\frac{\bar{d}(x)}{\bar{u}(x)}\right].
    $$
    * Assuming charge symmetry ((anti-)$u$ in proton is distributed like (anti-)$d$ in neutron, this assumption is also behind assumong that gluons are distributed in the same way in $p$ and $n$.
    * At high energies can be tested with charmonium production (it is sensitive to gluons) in p-p vs. p-d.
* Intrinsic charm in nucleon - Fock state $|uudc\bar{c}\rangle$:
    * "Extrinsic" -  created in $g\rightarrow c\bar{c}$ - "sea-like", confined to low $x$
    * Intrinsic  - more "valence-line", peaked at higher $x$.
    * Important to consider measurements with small extrinsic contributions, for example, $\bar{d}(x)-\bar{u}(x)$, $s(x)-\bar{s}(x)$, $\bar{u}(x)+\bar{d}(x)-s(x)-\bar{s}(x)$
    * Important to probe high $x$ region, lower energies can be useful, E906/SeaQuest will have 120 GeV proton beam, J-PARC will have (not initially) 50 GeV
* A general angular distribution of the virtual photons polatization is:
$$
\frac{d\sigma}{d\Omega}\propto1+\lambda\cos^2\theta+\mu\sin2\theta\cos\phi+\frac{\nu}{2}\sin^2\theta\cos2\phi.
$$
In naive D-Y, $\lambda=1$ and $\mu=\nu=0$, QCD processes lead to other values, but Lam-Tung relation $1-\lambda=2\nu$ was predicted and falsified at CERN and Fermilab.
* New transverse momentum-dependent (TMD) structure function (Sivers function, Boer-Mulders function)
    * Provide infornation on quantum correlations between preferred parton transverse motion and hadron spin
    * Are process-dependent, but parity and time-reversal invariance of QCD imply that they they can only differ by sign
    * Can explain the violation of the Lam-Tung reltion.
    * Its effect is negligible at high $p_T$
    * At LHC large deviation was observesd even at $p_T\sim 300~\mathrm{GeV}$
    * Attributed to higher-order pQCD effects
* Longitudinally polarized beams allow to study spin composition of the proton
    * Only small fraction comes from valence quarks
    * With only one polarized beams single-spin asymmtrty $A_L$ of the parity-violating $W$-boosn production in negative rapidity region (opposite to the direction of the polarized beam) is directly sensitive to the difference in polarization of $\bar{u}$ and $\bar{d}$
    * First result in STAR show opposite effect than the asymmetry of sea quarks themselves
    * Complementary information on quark and antiquark helicity distributions inside the proton can be obtained from two-spin asymmetry $A_{LL}$ measured with two longitudinally polarized beams 
* Impact parameter space $b_T$ is just a Fourier transform of transverse momentum space.

* gluon content - charmonium production
* strangeness content - W/Z boson production
* asymmetry between $s$ and $\bar{s}$ seas - DIS and kaon induced D-Y
