#### Files and histograms that are read
File name pp: `/lustre/hades/user/harabasz/apr06_exp/dst_gen2/pair_analysis/day_all_spectra_masspty.root`
File name np: `/lustre/hades/user/harabasz/may07_exp/dst_gen1/pair_analysis/dil_spectra_masspty.root`

Histogram name pp: `hmass_cut22_back_1_sig_norm`
Histogram name np: `hmass_cut45_back_1_sig_norm`

#### Normalization
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
#### Efficiency corrections
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
#### Filling histograms
These conditions seem to be present only in PP macro, e.g., in NP macro `metamatchqa1` is only read from the tree but the variable is never used, and similar for other variables:
```C++
if (trigDec==0) goto endofloop;

// here comes all of the extra cuts, Tatyana applied for apr06
// cut on MetaMatchingQuality
if(metamatchqa1>3.) goto endofloop;
if(metamatchqa2>3.) goto endofloop;

// cut on innermdc chi2
if(innerchisquare1<0.) goto endofloop;
if(innerchisquare2<0.) goto endofloop;

// ...

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

// ...

if((sqrt(mom1*mom2) <= pp) &&
    (opang <= ((-opa/pp)*sqrt(mom1*mom2) + opa)))
{
```
where the values used in the last condition are:
```C++
pp=680.;                                                                         
opa=180.;
```
But this cut is also in NP macro but as the `kRKcut` flag:
```C++
// cut on rk chi2
if(rkchi1>100000.) goto endofloop;
if(rkchi2>100000.) goto endofloop;
```
###### Vertex cut, conversion on the flange
In PP macro:
```C++
// vertex cut (conversion on the flanch)
if(mom1 < 150. || mom2 < 150.) {
    if(theta1>thetaCut && evtVertZ<evtZcut) goto endofloop;
    if(theta2>thetaCut && evtVertZ<evtZcut) goto endofloop;
}
```
`thetaCut` is `50`, and `evtZcut` is `-50`
In NP macro:
```C++
// vertex cut (conversion on the flanch)
if(mom1 < 150. || mom2 < 150.) {        
	if(theta1>65. && evtVertZ<-50.) goto endofloop;      
    if(theta2>65. && evtVertZ<-50.) goto endofloop;   
}
```
#### Final conditions
They are directly related to histogram names with `cut22` and `cut45` respectively: 
###### In PP macro:
```C++
if (kStandardAnalysisCuts && kIsLowerMomentum100MeV)   // apply in adition low momentum cut
```
The macro has another option, corresponds to different number (`cut23`), but it is not used for the spectrum that I plot:
```C++
// Include Ar+KCl cuts
if (kStandardAnalysisCuts && kIsLowerMomentum100MeV && kIsUpperMomentum1300MeV)
```
The variable `kStandardAnalysisCuts` is defined like this:
```C++
Bool_t kStandardAnalysisCuts = kAllPairCutsPassed && kNoLegIsClosePairCandidate && kIsUpperMomentum;
```
For the `kAllPairCutsPassed` flag, PP macro has:
```C++
Bool_t kAllPairCutsPassed = kFALSE;
if (isCutNb==0 && kIsUpperMomentum) kAllPairCutsPassed = kTRUE;
```
###### In NP macro
```C++
if (kStandardAnalysisCutsNOV02 && kSpectator && kRKchi)
```
where
```C++
Bool_t kStandardAnalysisCutsNOV02 = kAllPairCutsPassed && 
	kNoLegIsClosePairCandidate && kIsUpperMomentum2GeV;
```
also, `kSpectator` is some complex condition on the Forward Wall signal, and `kRKchi` is set to `true` when:
```C++
if (rkchi1<100000. && rkchi2<100000.) kRKchi = kTRUE; 
```
For the `kAllPairCutsPassed` flag, NP macro has:
```C++
Bool_t kAllPairCutsPassed = kFALSE;
if (isCutNb==0) kAllPairCutsPassed = kTRUE;
```
###### Flag that seems to be the same in both macros
```C++
// cut on close neighbour
Bool_t kNoLegIsClosePairCandidate = kFALSE;
if (angletoclosestnonfittedlep1>9 && angletoclosestnonfittedlep2>9 &&
		angletoclosestnonfittedhad1>9 && angletoclosestnonfittedhad2>9)
		kNoLegIsClosePairCandidate=kTRUE;
```
where `isCutNb` comes from the ntuple and:
```C++
Bool_t kIsUpperMomentum = kFALSE;
if (mom1<momUpCut && mom2<momUpCut) kIsUpperMomentum = kTRUE;
```
###### Additional condition that seems to be present only in NP macro
```C++
if( (mom1<100.)  || (mom2<100.) )  goto endofloop;   
if( (mom1>1100.) || (mom2>1100.))  goto endofloop;  
```