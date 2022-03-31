#!/usr/bin/python
"""
##################################################
# 
# QMB 3311: Python for Business Analytics
# 
# Optimization with Scipy
# 
# Lealand Morin, Ph.D.
# Assistant Professor
# Department of Economics
# College of Business
# University of Central Florida
# 
# January 19, 2021
# 
# This program provides introductory examples of 
# numerical methods for optimization.
# 
##################################################
"""


##################################################
# Import Modules.
##################################################


import numpy as np
# import math
import matplotlib.pyplot as plt
# We used these earlier to solve equations:
# from scipy.optimize import fsolve
# from scipy import optimize
# THese modules optimize by minimizing. 
from scipy.optimize import minimize_scalar
from scipy.optimize import minimize
# Other modules to use when you have constraints:
# from scipy.optimize import Bounds
# from scipy.optimize import LinearConstraint



##################################################
# Univariate Optimization
##################################################

#--------------------------------------------------
# Newton's Method
#--------------------------------------------------

# Consider the following cubic function:
def f(x):
    return x**3-6*x**2+4*x+2


# Caculate this on a grid of values to plot this function.
x_grid = np.arange(-1.0, 2, 0.01)
f_grid = f(x_grid)

plt.figure()
plt.plot(x_grid, f_grid, label='f(x)' )
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
# plt.savefig("f_example_0.png")

# It has a maximum of just over 2, for x just under 0.5 .

# Now define functions for the first and second derivatives.
def f_prime(x):
    return 3*x**2-12*x+4

def f_2prime(x):
    return 6*x - 12


# Now we use these in the following algorithm.
# Note that we are restricting the algorithm to 
# perform no more than 100 iterations
# and to stop when the step size is less than ```tol = 0.0001```.

def newton_f_opt(x0, f_prime, f_2prime, 
                 maxiter = 100, tol = 0.0001):
    x = x0
    for i in range(maxiter):
        x_next = x - f_prime(x)/f_2prime(x)
        if abs(x_next - x) < tol:
            print('Optimization terminated successfully.')
            print('Current parameter value: ' + str(x))
            print('Iterations: ' + str(i))
            # return x_next
            break
        x = x_next
        
        
    if i == maxiter - 1 and abs(x_next - x) > tol:
        print('Optimization terminated after maximum number of iterations.')
        
    return x


# Now calculate the optimum.
x_star = newton_f_opt(0, f_prime, f_2prime)
print(x_star)


print(f(x_star))


print(f_prime(x_star))


# Set the tolerance lower (more accuracy):
x_star = newton_f_opt(0, f_prime, f_2prime, 
                      maxiter = 100, 
                      tol = 0.000000001)
print(x_star)

print(f(x_star))


print(f_prime(x_star))


# Start from a different point:
x_star = newton_f_opt(3.5, f_prime, f_2prime, 
                      maxiter = 100, 
                      tol = 0.00001)
print(x_star)

print(f(x_star))

print(f_prime(x_star))
# Seems like an optimum but it's lower.


# Calculate the graph on a wider grid of values.
x_grid = np.arange(-1.0, 5, 0.01)
f_grid = f(x_grid)

plt.figure()
plt.plot(x_grid, f_grid, label='f(x)' )
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()



#--------------------------------------------------
# Using Python Modules
#--------------------------------------------------


# Now use Python modules to perform the optimization. 

# Other approach to defining functions:
f = lambda x: (x - 2) * (x + 1)**2

# Plot this function to show an approximate optimum.
x_grid = np.arange(0.1, 2, 0.01)
f_grid = x_grid*0
for i in range(0, len(x_grid)):
    f_grid[i] = f(x_grid[i])


plt.figure()
plt.plot(x_grid, f_grid, label='f(x)' )
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
# plt.savefig("f_example_1.png")


#--------------------------------------------------
# Unconstrained minimization: Brent Method
#--------------------------------------------------

res_sc_br = minimize_scalar(f, method='brent')

print(res_sc_br.x)
print(res_sc_br.fun)
print(f(res_sc_br.x))


#--------------------------------------------------
# Bounded method: Need to specify an interval. 
#--------------------------------------------------

from scipy.special import j1
# Plot this function to show an optimum.
x_grid = np.arange(4, 7, 0.01)
f_grid = x_grid*0
for i in range(0, len(x_grid)):
    f_grid[i] = j1(x_grid[i])


plt.figure()
plt.plot(x_grid, f_grid, label='J_1(x)' )
plt.xlabel('x')
plt.ylabel('J_(x)')
plt.show()
# plt.savefig("f_example_2.png")

# Search for good bounds first:
j1(4)
j1(5)
j1(7)


res_sc_bdd = minimize_scalar(j1, bounds=(4, 7), method='bounded')

print(res_sc_bdd.x)
print(res_sc_bdd.fun)
print(j1(res_sc_bdd.x))

# Try to break it:
res_sc_bdd_wrong = minimize_scalar(j1, bounds=(4, 5), method='bounded')

print(res_sc_bdd_wrong.x)
print(res_sc_bdd_wrong.fun)
print(j1(res_sc_bdd_wrong.x))
# It's the right answer to a different question.


##################################################
# Multivariate Optimization
##################################################


#--------------------------------------------------
# Nelder-Mead Simplex algorithm
#--------------------------------------------------

def rosen(x):
    """The Rosenbrock function"""
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res_nm = minimize(rosen, x0, method='nelder-mead',
               options={'xtol': 1e-8, 'disp': True})

print(res_nm.x)
print(res_nm.fun)
print(rosen(res_nm.x))


#--------------------------------------------------
# Powell Method 
# AKA Davidon-Fletcher-Powell (DFP)
#--------------------------------------------------


x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res_dfp = minimize(rosen, x0, method='powell',
               options={'xtol': 1e-8, 'disp': True})

print(res_dfp.x)
print(res_dfp.fun)
print(rosen(res_dfp.x))

#--------------------------------------------------
# Broyden-Fletcher-Goldfarb-Shanno algorithm (BFGS)
# Uses gradient vector, as well as function evaluations
# to reduce number of iterations.
#--------------------------------------------------

def rosen_der(x):
    xm = x[1:-1]
    xm_m1 = x[:-2]
    xm_p1 = x[2:]
    der = np.zeros_like(x)
    der[1:-1] = 200*(xm-xm_m1**2) - 400*(xm_p1 - xm**2)*xm - 2*(1-xm)
    der[0] = -400*x[0]*(x[1]-x[0]**2) - 2*(1-x[0])
    der[-1] = 200*(x[-1]-x[-2]**2)
    return der


res_bfgs = minimize(rosen, x0, method='BFGS', jac=rosen_der,
                    options={'disp': True})

print(res_bfgs.x)
print(res_bfgs.fun)
print(rosen(res_bfgs.x))


#--------------------------------------------------
# Newton-Conjugate-Gradient algorithm
# AKA Outer Product of the Gradient Method (OPG)
# Can use a Hessian matrix of approximation to it. 
#--------------------------------------------------

# Uses Hessian matrix, as well as function evaluations

def rosen_hess(x):
    x = np.asarray(x)
    H = np.diag(-400*x[:-1],1) - np.diag(400*x[:-1],-1)
    diagonal = np.zeros_like(x)
    diagonal[0] = 1200*x[0]**2-400*x[1]+2
    diagonal[-1] = 200
    diagonal[1:-1] = 202 + 1200*x[1:-1]**2 - 400*x[2:]
    H = H + np.diag(diagonal)
    return H

res_ncg = minimize(rosen, x0, method='Newton-CG',
               jac=rosen_der, hess=rosen_hess,
               options={'xtol': 1e-8, 'disp': True})

print(res_ncg.x)
print(res_ncg.fun)
print(rosen(res_ncg.x))



#--------------------------------------------------
# Hessian product example:
# NCG needs only the product of the Hessian
# with an arbitrary vector. 
#--------------------------------------------------


def rosen_hess_p(x, p):
    x = np.asarray(x)
    Hp = np.zeros_like(x)
    Hp[0] = (1200*x[0]**2 - 400*x[1] + 2)*p[0] - 400*x[0]*p[1]
    Hp[1:-1] = -400*x[:-2]*p[:-2]+(202+1200*x[1:-1]**2-400*x[2:])*p[1:-1] -400*x[1:-1]*p[2:]
    Hp[-1] = -400*x[-2]*p[-2] + 200*p[-1]
    return Hp

res_hp = minimize(rosen, x0, method='Newton-CG',
                  jac=rosen_der, hessp=rosen_hess_p,
                  options={'xtol': 1e-8, 'disp': True})

print(res_hp.x)
print(res_hp.fun)
print(rosen(res_hp.x))



# ... and many more ...




##################################################
# End
##################################################
