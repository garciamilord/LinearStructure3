import numpy as np

A = np.matrix([[10, -7, 0], [-3, 2, 6], [5, -1, 5]])
'''''''''
Compute the SVD of the matrix above and write down the singular values
'''''''''
def Garcia_Milord_Q2_P2():
    u, s, vt = np.linalg.svd(A)
    return print('Singular values\n '+ str(s))
Garcia_Milord_Q2_P2()