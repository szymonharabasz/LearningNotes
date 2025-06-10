#### Heat bath method  for the Ising model
  
The energy for a given configuration $C$ is:
$$
E(C)=-\epsilon\sum_{\langle ij\rangle}s_is_j-h\sum_is_i.
$$
We calculate the probability to reverse a given spin using a heat bath method. The probability to flip one spin if it has $s=1$ is equal  
$$  
T=\frac{1}{1+e^{-2\beta\left(\sum+h\right)}},  
$$  
where $\sum$ denotes the sum of over nearest neighbors. For $s=-1$, it is:  
$$  
1-T=\frac{1}{1+e^{2\beta\left(\sum+h\right)}},  
$$  
The sum over nearest neighbors can take onlt one of the values:  
$$  
\sum=-4,-2,0,2,4.  
$$  
We calculate mean energy, mean squared energy, and mean magnetization as averages over the configurations after equilibrium has been reached. The heat capacity is then calculated as:
$$
C_\mathrm{Ising}=\frac{1}{kT^2}\left(\langle E^2\rangle-\langle E\rangle^2\right).
$$