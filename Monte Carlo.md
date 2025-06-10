Transfer matrix is a matrix of probabilities for the system to go from one state to another.
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