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
#### Transfer matrix
Transfer matrix is a matrix of probabilities for the system to go from one state to another. It is equal to the evolution operator over one lattice spacing of Euclidean time. In simple cases. it is therefore equal to the Boltzmann weight.
Equilibrium state is an eigenstate of the transfer matrix with eigenvalue 1. Second largest eigenvalue $\lambda$ determines the decay of corrections to equilibrium, like:
$$
\exp(-t/\tau),\;\;\;1/\tau=|\ln\lambda|.
$$
In NumPy, eigenvectors and eigenvalues can be found like this:
```Python
eigenvalues, eigenvectors = numpy.linalg.eig(transfer)
```
If the transfer matrix is not irreducible, there will be more than one eigenvectors with eigenvalue 1 and the steady state will not be unique.
If the second eigenvalue of the transfer matrix will a complex number with modulus 1, there will be no steady state.This happens if there are recurring states.
Markov Chain must fulfil:
- Global balance
- Irreducibility - restored by imposing a small probability of moving from one irreducible block of the transfer matrix to another
- Aperiodicity - restored by introducing a small probability of staying in the same configuration