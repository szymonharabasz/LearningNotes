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

One CUDA device found

Device Number: 0
  Device Name: NVIDIA RTX 1000 Ada Generation Laptop GPU
  Compute Capability: 8.9
  Number of Multiprocessors: 20
  Single- to Double-Precision Perf Ratio: 64
  Max Threads per Multiprocessor: 1536
  Supports Cooperative Kernels: Yes

  Global Memory (GB):     5.640

  Execution Configuration Limits
    Max Grid Dims: 2147483647 x 65535 x 65535
    Max Block Dims: 1024 x 1024 x 64
    Max Threads per Block: 1024

  Managed Memory
    Can Allocate Managed Memory: Yes
    Device/CPU Concurrent Access to Managed Memory: Yes

$\overline{\sigma}$ 



$$
\vec a=\vec a_{n+1} \tau+\vec a_n(1-\tau),\;\;\;\tau\in]0,1]
$$
$$
\tau=(t_\mathrm{best}-t_{n+1}+\Delta t)/\Delta t

$$
#### Kids meeting 19.08.2026
Karina
Analysis note: probably sufficiently comprehensive based on the length (57 pages)
Paper proposal: ask Anar if 5 pages text is fine, should one prepare a talk? Physics forum?
Slide 3: how yellow-ish box is derived from the data points of the ratio? Have it explained in the analysis note
Are uncertainties of the fit parameters somehow included in the syst. uncertainty? Do they have to?
For Sacha: use mean momenta in bins, like Karina
Yes, please push the code to the repository

Carina: send me her plots, see what we have, write to Vladimir

Karina + Niklas vs. Sacha - fit parameters are large or small

#### Meeting 02.09.2026
Andrei: new student working on shining in Ag+Ag at 1.23*A* GeV - multidifferential spectra, comparison to Philipp

Possible task for me: what is the kink of the momentum in the magnetic field? Are the tracks in low field above 500 MeV too straight? Does the tracking have a tendency to make the kink larger than it actually is, which is especially relatively strong for more or less straight tracks?

Henrik: mainly programming issues

Jan: new student from Wuppertal who will analyze $\gamma e^+e^-$ in Au+Au at 800*A* MeV

Jessica: progress but still not finished translating Urban's code from Fortran to C++

LLM bot at GSI? Check slides from the AI workshop
###### p+p at 1.58 GeV
Analysis note (57 pages) and a written paper proposal (7 pages), with Claudia as Karina's supervisor, then will go to the writing committee in which I am. Should the proposal be converted to a talk and presented in the Physics Forum?
###### Ag+Ag at 1.58*A* GeV
With the writing committee there is paper draft and analysis note, both being edited now by Claudia as far as I know. The analysis is finalized and only the plots will need to be redone after the delta electron issue is finished, but nothing of the physics message should change.

###### Ag+Ag at 1.23*A* GeV low field
Investigation is ongoing about the smearing matrices being tilted (not diagonal). We think that it is a fact with which we have to live. Question is if there is the same bias in SIM and in EXP and what is then  the most reasonable upper cut on mometum

###### Au+Au at 1.23*A* GeV
Found in the changelog for hydra2-4.9m:

-HGeantKine : bug fix: init value for acceptance word was missing
              (all functions xxxBit() working on acceptance word were giving
              wrong results )

Embedded white leptons for gen8 were produced with hydra2-4.9l. As a check, I produced (only Geant) with 4.9m and the acceptance is very similar to gen10. Conclusion: Efficiency matrices are not 100% correct in gen8, we have already 3 important improvements from gen8 to gen10 so we will not try anymore to compare with old results but we take what we gen in gen10.
