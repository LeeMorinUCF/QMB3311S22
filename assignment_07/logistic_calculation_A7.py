# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Computing Logistic Regression Coefficients
#
# Lealand Morin, Ph.D.
# Assistant Professor
# Department of Economics
# College of Business Administration
# University of Central Florida
#
# March 30, 2022
#
# This script estimates logistic regression in python, 
# using several numerical methods.
# It uses a sample dataset credit_data.csv with the following variables:
#   default: 1 if borrower defaulted on a loan
#   bmaxrate: Maximum rate of interest on any part of the loan
#   amount: the amount funded on the loan
#   close: borrower takes the option of closing the listing
#     until it is fully funded
#   AA: borrowers FICO score greater than 760
#   A: borrowers FICO score between 720 and 759
#   B: borrowers FICO score between 680 and 719
#   C: borrowers FICO score between 640 and 679
#   D: borrowers FICO score between 600 and 639
#
##################################################
"""

##################################################
# Import Modules.
##################################################


import os # To set working directory
# import numpy as np # Not needed here but often useful
import pandas as pd # To read and inspect data
# from sklearn.linear_model import LogisticRegression

# import statsmodels.formula.api as smf # Another way to estimate logistic regression
import statsmodels.api as sm # Another way to estimate logistic regression

# Need exponential function in likelihood function. 
import numpy as np
# And np arrays are used in calculation. 

# Import scipy package for optimization
# from scipy import optimize
from scipy.optimize import minimize

# To plot regression results
# import matplotlib.pyplot as plt  



##################################################
# Set Working Directory.
##################################################




# Find out the current directory.
os.getcwd()
# Change to a new directory.
drive_path = 'C:\\Users\\le279259\\OneDrive - University of Central Florida\\Documents\\'
git_path = 'GitHub\\QMB3311S22\\'
os.chdir(drive_path + git_path + 'assignment_07')
# Check that the change was successful.
os.getcwd()


##################################################
# Load Data.
##################################################


credit = pd.read_csv('credit_data.csv')



##################################################
# Inspect Data.
##################################################



# Inspect the target variable.
credit['default'].value_counts()


# Look at the explanatory variables in groups.
credit[['bmaxrate','amount','close','bankcardutil']].describe()
credit[['AA','A','B','C']].describe()







##################################################
# Logistic Regression.
##################################################


#--------------------------------------------------
# Fit the Logistic Model (with statsmodels module).
#--------------------------------------------------

# Select the target variable as y.
y = credit['default']
# y = np.array(credit['default'])

# Create a matrix of explanatory variables.
# Add a column of 1s for the constant. 
credit['Intercept'] = 1
# Get names of explanatory variables (in order).
# X_cols = credit.columns[[10, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
# X_cols = credit.columns[[10, 4, 5, 6, 7, 8]]
# Select one variable (interest rate) for Assignment 7.
X_cols = credit.columns[[10, 1]]
# Create matrix of explanatory variables.
X = credit[X_cols]
# X = np.array(credit[X_cols])
X.describe()


# Note that this does not include a constant
# but that is included by default.

# Initialize and specify the logistic model.
logit_model_sm = sm.Logit(y, X)

# Fit the model.
logit_model_fit_sm = logit_model_sm.fit()

# Display the parameters.
print(logit_model_fit_sm.params)
# This is the goal: calculate these coefficients.


# Display a summary table of regression results.
print(logit_model_fit_sm.summary())
# Objective is -572.83 regression output above:
# Log-Likelihood:                -572.83


##################################################
# The likelihood function
##################################################

# Import your functions.
import my_logit_A7 as my_logit


# Redefine a vector of only the selected variable
# for our self-defined function.
X_cols = credit.columns[1]
X = credit[X_cols]
X.describe()

#--------------------------------------------------
# Test the objective function: 
# The (negative of the) value of the likelihood function
#--------------------------------------------------


# Test the likelihood function function 
# with a value of the parameter beta.
beta = logit_model_fit_sm.params
# Goal is 572.83 in regression output above:
# Log-Likelihood:                -572.83
print(my_logit.logit_like_sum_opt(beta, y, X))
# Is it equal to the value in the printout above?

# If not, you must correct the function logit_like_sum_opt
# in your module my_logit_A7. 


#--------------------------------------------------
# Test the gradient vector of the objective function: 
# The (negative of the) slope of the likelihood function
#--------------------------------------------------


# Test this function with a value of the parameter beta.
beta = logit_model_fit_sm.params
# Goal is zero when likelihood function is optimized.
print(my_logit.logit_like_grad(beta, y, X))
# Is it almost zero? 

# If the above value is not zero, you must correct the 
# logit_like_grad function in the my_logit_A7 module.


##################################################
# Optimize the Likelihood Function
# Find the beta such that the likelihood function is maximized
##################################################


#--------------------------------------------------
# Nelder-Mead Simplex algorithm
# Use the method = 'nelder-mead' algorithm. 
#--------------------------------------------------


beta_0 = np.zeros(len(logit_model_fit_sm.params))


# I suggested beta_0 above as a starting value for x0. 
# I did this because you generally don't know the optimum
# until you find it.
# Starting with x0 = beta (the estimates) is an artificial
# starting point. 

#--------------------------------------------------
# Code goes here.
soln_nm = None
# Code goes here.
#--------------------------------------------------

# The parameters:
print(soln_nm.x)
# Compare with the estimates from logit_model_fit_sm:
print(logit_model_fit_sm.params)

# Do the estimates match?


# The objective function:
print(soln_nm.fun)
print(my_logit.logit_like_sum_opt(soln_nm.x, y, X))

# Does the value of the likelihood match?

# If you find any differences, adjust the options.


#--------------------------------------------------
# Powell Method 
# AKA Davidon-Fletcher-Powell (DFP)
#--------------------------------------------------


beta_0 = np.zeros(len(logit_model_fit_sm.params))

#--------------------------------------------------
# Code goes here.
soln_dfp = None
# Code goes here.
#--------------------------------------------------

# The parameters:
print(soln_dfp.x)
# Compare with the estimates from logit_model_fit_sm:
print(logit_model_fit_sm.params)

# Do the estimates match?

# The objective function:
print(soln_dfp.fun)
print(my_logit.logit_like_sum_opt(soln_dfp.x, y, X))

# Does the value of the likelihood match?

# If you find any differences, adjust the options.



#--------------------------------------------------
# Broyden-Fletcher-Goldfarb-Shanno algorithm (BFGS)
# First try by only using the likelihood function
#--------------------------------------------------


beta_0 = np.zeros(len(logit_model_fit_sm.params))

#--------------------------------------------------
# Code goes here.
soln_bfgs = None
# Code goes here.
#--------------------------------------------------


# The parameters:
print(soln_bfgs.x)
# Compare with the estimates from logit_model_fit_sm:
print(logit_model_fit_sm.params)

# Do the estimates match?

# The objective function:
print(soln_bfgs.fun)
print(my_logit.logit_like_sum_opt(soln_bfgs.x, y, X))

# Does the value of the likelihood match?

# If you find any differences, adjust the options.



#--------------------------------------------------
# Broyden-Fletcher-Goldfarb-Shanno algorithm (BFGS)
# Uses gradient vector, as well as function evaluations
# to reduce number of iterations.
#--------------------------------------------------


beta_0 = np.zeros(len(logit_model_fit_sm.params))

#--------------------------------------------------
# Code goes here.
soln_bfgs_jac = None
# Code goes here.
#--------------------------------------------------


# The parameters:
print(soln_bfgs_jac.x)
# Compare with the estimates from logit_model_fit_sm:
print(logit_model_fit_sm.params)

# Do the estimates match?

# The objective function:
print(soln_bfgs_jac.fun)
print(my_logit.logit_like_sum_opt(soln_bfgs_jac.x, y, X))

# Does the value of the likelihood match?

# If you find any differences, adjust the options.






##################################################
# End
##################################################

