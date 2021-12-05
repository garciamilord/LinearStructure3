import numpy as np
import scipy
import scipy.linalg as lu



'''''''''
Compute the LU decomposition of the matrix above and write down your solution. 
It is possible that you obtain a permutation matrix, P, from the result; if so, include it in your answer.
'''''''''
A = np.matrix([[10, -7, 0], [-3, 2, 6], [5, -1, 5]])

def Q2pt1():
    P, L, U = scipy.linalg.lu(A)
    print("Lower Matrix\n" +str(L))
    print("Upper Matrix\n" +str(U))
    print('Permutation Maxtrix\n'+str(P))
Q2pt1()
