Niklas:
- QCD-Phase-Diagram -> QCD phase diagram
- neutron star mergers which provides -> neutron star mergers, which provides
- an meaningful -> a meaningful
- the relevant nuclear Equation-Of-State - and which nuclear Equation-Of-State is irrelevant>
- "in order to constrain astrophysical phenomena" - first: it sounds that experiments at HADES will prevent supernovae from exploding, second: I think that studying the EoS is of fundamental importance, not just to help astrophysics
- "various aspects" - one has to say aspects of what
- "encode (...) information from the early stages and therefore the evolution" - maybe in a more broad context we should agree on the wording: early stages? They are for sure earlier-than-freeze-out, but for me "early" is what comes at the beginning and as such is strongly associated with "pre-equilibrium", which we prefer to subtract rather than attempt to get some information from it. 
- In any case, I would avoid "therefore" between "early stages" and "evolution"

#### NN ref. Tania

File name pp: /lustre/hades/user/harabasz/apr06_exp/dst_gen2/pair_analysis/day_all_spectra_masspty.root
File name np:
/lustre/hades/user/harabasz/may07_exp/dst_gen1/pair_analysis/dil_spectra_masspty.root

Histogram name pp: hmass_cut22_back_1_sig_norm
Histogram name np: hmass_cut45_back_1_sig_norm

Scaling procedure:
```C++
// for details see PhD TG page 63

    Double_t lvl2 = 0.85;
    Double_t dp_pp_el = 6.23e+9;  // pp analysis 2009 based on EDDA data
    Double_t dp_pi0 = 8.56;
    Double_t dp_el  = 22.1;

    Double_t dp_n_pi0 = dp_pp_el * dp_pi0 / dp_el;
    Double_t fwn = 0.85;
    h_np->Scale(1./dp_n_pi0);
    h_np->Scale(1./lvl2);
    h_np->Scale(1./fwn);

    Double_t pp_pp_el = 15.7e+9;  // pp analysis 2009 based on EDDA
    Double_t pp_pi0 = 4.45;       // mb
    Double_t pp_el  = 22.1;       // mb
    Double_t m3 = 0.84;   

    Double_t pp_n_pi0 = pp_pp_el * pp_pi0 / pp_el;

    h_pp->Scale(1./pp_n_pi0);
    h_pp->Scale(1./lvl2);
    h_pp->Scale(1./m3);
```

Normalizing:
$$
	0.48\mathrm{pp} + 0.52\mathrm{np}
$$
There is minimum efficiency of 5% on each leg, if not fulfilled, the pair is skipped, if fulfilled, correction factor is $\frac{1}{\mathrm{eff}_1\cdot\mathrm{eff}_2}$.

Names of efficiency matrix files
```
smoothedMatrix.ep.apr06.root
smoothedMatrix.em.apr06.root
```
Names of efficiency matrix histograms:
```
effi3DEleAllCut
effi3DPosAllCut
```
They are 3D, momentum is up to 2000 MeV, $\phi$ is from $-\pi$ to $\pi$, so it treats all sectors separately.

```C++
momLowCut=100.;
momUpCut=1977.;
```
Recursive cutting inefficiency due to nearby ghost tracks is NOT used, because it's only for NOV02.

Histograms are filled with conditions:
```C++
if (trigDec==0) goto endofloop;

// here comes all of the extra cuts, Tatyana applied for apr06
// cut on MetaMatchingQuality
if(metamatchqa1>3.) goto endofloop;
if(metamatchqa2>3.) goto endofloop;

// cut on innermdc chi2
if(innerchisquare1<0.) goto endofloop;
if(innerchisquare2<0.) goto endofloop;

// cut on rk chi2
if(rkchi1>100000.) goto endofloop;
if(rkchi2>100000.) goto endofloop;

// vertex cut (conversion on the flanch)
if(mom1 < 150. || mom2 < 150.) {
    if(theta1>thetaCut && evtVertZ<evtZcut) goto endofloop;
    if(theta2>thetaCut && evtVertZ<evtZcut) goto endofloop;
}

// pair x vs. pair y cut
r = sqrt(pairvertx*pairvertx+pairverty*pairverty);
if(r > (xBeamPos + rBeam)) goto endofloop;
if(r < (xBeamPos - rBeam)) goto endofloop;
if(r > (yBeamPos + rBeam)) goto endofloop;
if(r < (yBeamPos - rBeam)) goto endofloop;

if((mom1<400. && mom1>300.) ||
		(mom2<400. && mom2>300.)) {
    if(drmt1 < (0. - 3*0.6)) goto endofloop;
    if(drmt1 > (0. + 3*0.6)) goto endofloop;
    if(drmt2 < (0. - 3*0.6)) goto endofloop;
    if(drmt2 > (0. + 3*0.6)) goto endofloop;

    if(drmp1 < (0. - 3*0.4)) goto endofloop;
    if(drmp1 > (0. + 3*0.4)) goto endofloop;
    if(drmp2 < (0. - 3*0.4)) goto endofloop;
    if(drmp2 > (0. + 3*0.4)) goto endofloop;
}

if((mom1<2000. && mom1>400.) ||
		(mom2<2000. && mom2>400.)) {
    if(drmt1 < (0. - 3*0.4)) goto endofloop;
    if(drmt1 > (0. + 3*0.4)) goto endofloop;
    if(drmt2 < (0. - 3*0.4)) goto endofloop;
    if(drmt2 > (0. + 3*0.4)) goto endofloop;

    if(drmp1 < (0. - 3*0.3)) goto endofloop;
    if(drmp1 > (0. + 3*0.3)) goto endofloop;
    if(drmp2 < (0. - 3*0.3)) goto endofloop;
    if(drmp2 > (0. + 3*0.3)) goto endofloop;
}




//
if((sqrt(mom1*mom2) <= pp) &&
    (opang <= ((-opa/pp)*sqrt(mom1*mom2) + opa)))
{

```
where:
```C++
pp=680.;                                                                         
opa=180.;
```
I use:
```C++
if (kStandardAnalysisCuts && kIsLowerMomentum100MeV)   // apply in adition low momentum cut
```
The macro has another option, which I don't use:
```C++
// Include Ar+KCl cuts
if (kStandardAnalysisCuts && kIsLowerMomentum100MeV && kIsUpperMomentum1300MeV)
```
where
```C++
Bool_t kStandardAnalysisCuts = kAllPairCutsPassed && kNoLegIsClosePairCandidate && kIsUpperMomentum;
```
where
```C++
Bool_t kAllPairCutsPassed = kFALSE;
if (isCutNb==0 && kIsUpperMomentum) kAllPairCutsPassed = kTRUE;

// cut on close neighbour
Bool_t kNoLegIsClosePairCandidate = kFALSE;
if (angletoclosestnonfittedlep1>9 && angletoclosestnonfittedlep2>9 &&
		angletoclosestnonfittedhad1>9 && angletoclosestnonfittedhad2>9)
		kNoLegIsClosePairCandidate=kTRUE;
```