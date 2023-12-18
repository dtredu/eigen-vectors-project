# eigen-vectors-project
few python files to find eigenvectors and eigenvalues

## there are two modules:
### validation
this module has only one function
```py
validate(A, eigenvalues, eigenvectors, epsilon = 1e-6)
```
that returns 
```py
(all_correct, [i_correct])
```
### methods
this module has functions for different methods of finding eigenvectors and eigenvalues
for example
```py
power_iteration(A,epsilon = 1e-6, iter_limit = 1e3):
```
