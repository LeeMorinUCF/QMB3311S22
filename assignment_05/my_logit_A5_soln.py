# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: 
#
# Date:
# 
##################################################
#
# Sample Script for Assignment 5: 
# Suggested Function Definitions
#
##################################################
"""



"""
##################################################
##################################################
# Note: there should be no printing or calculations
# in this script, aside from function definitions. 
# Save those for another script that would
# execute the scripts (to run the doctests)
# and imports the modules to test the functions.
##################################################
##################################################
"""






##################################################
# Import Required Modules
##################################################

# import name_of_module
import math
import numpy as np
from typing import List


##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

#--------------------------------------------------
# Question 1
# Functions from Previous Assignments
#--------------------------------------------------

# Copy the function definitions from Assignment 3.

def logit(x: float, beta_0: float, beta_1: float) -> float:
    """Calculates the value of the logit link function
     for a variable x and coefficients beta_0 and beta_1.
    >>> logit(13.7, 0.0, 0.0)
    0.5
    >>> logit(0.0, math.log(2), 2.0)
    0.6666666666666666
    >>> logit(1.0, 0.0, math.log(5))
    0.8333333333333333
    """
    link = math.exp(beta_0 + x*beta_1)/(1 + math.exp(beta_0 + x*beta_1))

    return link


def logit_like(y: int, x: float, beta_0: float, beta_1: float) -> float:
    """Calculates the value of the likelihood function
    for one observation of x and y.

    >>> logit_like(1, 13.7, 0.0, 0.0)
    -0.6931471805599453
    >>> logit_like(0, 0.0, math.log(2), 2.0)
    -1.0986122886681096
    >>> logit_like(1, 1.0, 0.0, math.log(5))
    -0.1823215567939547
    """
    link = logit(x, beta_0, beta_1)
    if y == 0:
        like = math.log(1 - link)
    elif y == 1:
        like = math.log(link)
    else:
        print("Warning: y is not binary. y should be either 1 or 0.")
        like = None

    return like


# Copy the function definitions from Assignment 4, 
# which depends on the previous functions.

def logit_like_sum(y: list, x: list, beta_0: float, beta_1: float) -> float:
    """Calculates the value of the likelihood function
    for the bivariate logistic regression model
    for sevaral pairs of observations in the lists x and y
    and coefficients beta_0 and beta_1.
    
    Notice if you are missing the space after the >>>, 
    it causes an error.
    Also, an example without the >>> does not get run.
    
    >>> logit_like_sum([1, 1, 1], [13.7, 12, 437], 0.0, 0.0)
    -2.0794415416798357
    >>> logit_like_sum([1, 0], [1, 1], 0.0, math.log(2))
    -1.504077396776274
    >>> logit_like_sum([1, 0], [2, 3], math.log(5), math.log(2))
    -3.762362230873739
    """
    
    like_sum = 0
    for i in range(len(y)):
        if y[i] in [0,1]:
            # Note that you could place the code from the body of 
            # logit_like() here but it is simpler to call the function
            # within this function. 
            like_sum_i = logit_like(y[i], x[i], beta_0, beta_1)
            like_sum = like_sum + like_sum_i
        else:
            print('Error: Observations in y must be either zero or one.')
            # This return statement ends the function early
            # as soon as there is an inadmissible observation.
            return None
        
    
    return like_sum



#--------------------------------------------------
# Question 2
# New Functions
#--------------------------------------------------

# Exercise 1


def logit_di(x_i: float, k: int) -> float:
    """
    >>> logit_di(2, 1) 
    2
    >>> logit_di(7, 0)
    1
    >>> logit_di(0.5, 1)
    0.5
    """
    if k == 0:
        di = 1
    elif k == 1:
        di = x_i
    return di


# Exercise 2


def logit_dLi_dbk(y_i: float, x_i: float, k: int, beta_0: float, beta_1: float) -> float:
    
    """
    >>> logit_dLi_dbk(1, 0, 0,0 ,0 )
    0.5
    >>> logit_dLi_dbk(0, math.log(15), 0, 0, 16)
    -1.0
    >>> logit_dLi_dbk(1, 2, 0, math.log(11), math.log(3))
    0.01
    >>> logit_dLi_dbk(0, 2, 1, math.log(11), math.log(3))
    -1.98
    >>> logit_dLi_dbk(23.275, 1, 2, 3, 4)
    Error: Observations in y must be either zero or one.
    """
    if y_i in [0, 1] :
        # Both cases work when you subtract logit() from y_i.
        dLi_dbk = logit_di(x_i, k)*(y_i - logit(x_i, beta_0, beta_1))
    else:
            print('Error: Observations in y must be either zero or one.')
            # This return statement ends the function early
            # as soon as there is an inadmissible observation.
            dLi_dbk =  None
    return dLi_dbk





# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 


# Make sure to include exampes in your docstrings
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 


# The tests are implemented below -- but only
# when the script is run, not when it is imported. 


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    






##################################################
# End
##################################################
