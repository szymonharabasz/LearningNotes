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