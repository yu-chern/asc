import numpy as np
import math
import matplotlib.pyplot as plt

X = [408, 89, -66, 10, 338, 807, 1238, 1511, 1583, 1462, 1183, 804]
#X = [0, 89, -66, 10, 338, 807, 0, -807, -338, -10, 66, -89]
#X = [50, 89, -66, 10, 338, 807, 22, 807, 338, 10, -66, 89]

# find coefficients for interpolation function
A = np.array([[math.cos(math.pi*k*l/6) for k in range(0,7)] for l in range(0,12)])
B = np.array([[math.sin(math.pi*k*l/6) for k in range(1,6)] for l in range(0,12)])

M = np.concatenate([A,B], axis=1);

#print "A = " + str(A)
print ("A = ")
for Ai in A:
    print ('%s' % ''.join(['%7.3f' % Aij for Aij in Ai]))
    
#print "B = " + str(B)
print ("B = ")
for Bi in B:
    print ('%s' % ''.join(['%7.3f' % Bij for Bij in Bi]))

#print "M = " + str(M)
print ("M = ")
for Mi in M:
    print ('%s' % ''.join(['%7.3f' % Mij for Mij in Mi]))

#solve the system to get ab
ab = np.linalg.solve(M,X)
#separate a and b
a = ab[0:7];
b = ab[7:12];

print ("a:", a)
print ("b:", b)

#generate interpolation point
def Xint_gen(a,b,t):
    return np.sum(np.array([a[k]*math.cos(math.pi*k*t/180) for k in range(0,7)])) + \
        np.sum(np.array([b[k-1]*math.sin(math.pi*k*t/180) for k in range(1,6)]))
        

# plotting interpolation results and initial data
resolution = 2
plt.plot(range(0,720,resolution), [Xint_gen(a,b,t) for t in range(0,720,resolution)])
plt.plot(range(0,360,30), X, 'o')
plt.xlabel('ascension')
plt.ylabel('declination')
plt.show()


#--------------------


#Note: we are in the same python environment as the previous python demo so X is still defined
import cmath

#compute c_k using the IDFT formula, only the c_k with k>=0 are required
c = np.array([np.sum([X[l]*cmath.exp(-2*math.pi*k*l*1J/12)/12 for l in range(0,12)]) for k in range(0,7)])

#compute a and b coefficients using the formula from exercise 1
aFromC = c.real
aFromC[1:6] = np.product([[2],aFromC[1:6]])
bFromC = np.product([[-2],c[1:6].imag])

# plotting interpolation results and initial data (reuse previously defined X_int_gen)
plt.plot(range(0,720,resolution), [Xint_gen(aFromC,bFromC,t) for t in range(0,720,resolution)])
plt.plot(range(0,360,30), X, 'o');
plt.xlabel('ascension')
plt.ylabel('declination')
plt.show()