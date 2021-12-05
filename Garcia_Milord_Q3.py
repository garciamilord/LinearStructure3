import json
import numpy as np
'''''''''
Computing Singular Values
Goal: The goal of this assignment is 
to compute the singular values of the given matrix yourself and 
compare those results with what numpy’s function computes.
Instructions: Use what you learned about SVD from your lectures to compute 
the singular values of the matrix provided in the SVD_dataset.json. You will first compute 
them yourself and then use numpy’s svd function to compute them. Once you have both results, 
You will submit one single pdf file, including explanation for any details of your project 
(i.e. if you’re using a compiled language, details on compilation) and also copy and paste 
your code in the submission file. Your submission file should describe any issues you had including 
reasons you may have gotten stuck and were not able to finish.
'''''''''

    # SVD_DA_1.JSO
with open('SVD_DA_1.JSO') as f:
    d = json.load(f)


print('Build in library function')
u, s, vt = np.linalg.svd(d)
print("Σ=\n "+str(s))
print()
print('U=\n'+str(u))
print()
print('Vt=\n'+str(vt))
print()

print("My function for the SVD")
A = np.array(d)
#line 37-42 doing the code swap column thing
'''The eigenvectors of 𝐴𝐴𝑇 are the columns of U'''
AAT= np.linalg.eig( A @ A.T)[1]
'''The eigenvectors of 𝐴𝑇𝐴 are the columns of V'''
ATA = np.linalg.eig(A.T @ A)[1]
'''The square root of the eigenvalues of 𝐴𝐴𝑇 , or 𝐴𝑇𝐴, make up the diagonal matrix Σ'''
Sigma = np.sqrt(np.linalg.eig(A.T @ A)[0])

#Singular values was to sort my last work row
# and know there is better way
Sigma[[4,3]] = Sigma[[3,4]]
print('U=\n'+ str(AAT))
print()
print('V=\n'+ str(ATA))
print()
print('Σ=\n'+ str(Sigma))






