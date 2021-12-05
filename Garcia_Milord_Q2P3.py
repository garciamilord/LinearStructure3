import numpy as np

A = np.matrix([[10, -7, 0], [-3, 2, 6], [5, -1, 5]])

'''''''''
Compute the QR decomposition and write down the Q and R matrices.	
'''''''''

def Garcia_Milord_Q2_P3():
    Q, R = np.linalg.qr(A)
    print('Q')
    print(Q)
    print('R')
    print(R)

Garcia_Milord_Q2_P3()