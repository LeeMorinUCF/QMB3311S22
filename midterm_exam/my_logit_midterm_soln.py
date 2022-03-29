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
# Sample Script for Midterm Examination: 
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



# Assignment 5, Exercise 1
# For completeness. Not used here.

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


# Assignment 5, Exercise 2
# For completeness. Not used here.


def logit_dLi_dbk(y_i: float, x_i: float, k: int, beta_0: float, beta_1: float) -> float:
    
    """
    >>> logit_dLi_dbk(1, 0, 0,0 ,0 )
    0.5
    >>> logit_dLi_dbk(0, math.log(15), 0, 0, 16)
    -1.0
    >>> logit_dLi_dbk(1, 2, 0, math.log(11), math.log(3))
    0.010000000000000009
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


#--------------------------------------------------
# Question 2
# New Functions
#--------------------------------------------------


# Exercise 6

def max_logit(y: List[float], x: List[float], 
        beta_0_min: float, beta_0_max: float, 
        beta_1_min: float, beta_1_max: float, 
        step: float) -> float:
    """
    Calculates the estimated coefficients 
    by grid search on the value of the logit_like_sum function
    for the logistic regesssion model 
    given two lists of data y and x.
    
    The search is taken over a grid of candidate values
    of beta_0 and beta_1 defined over
    np.arange(beta_0_min, beta_0_max, step) and
    np.arange(beta_1_min, beta_1_max, step), respectively.
    
    
    >>> max_logit([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], \
                  -2.0, 2.0, -2.0, 2.0, 0.10)
    [0.0, 0.0]
    >>> max_logit([1, 0, 1], [15.0, 10.0, 5.0], \
                  -1.0, 1.0, -1.0, 1.0, 0.01)
    [0.69, 0.0]
    >>> max_logit([1, 0, 1, 0, 1], [0, 0, 1, 1, 1], \
                  -1.0, 1.0, -1.0, 1.0, 0.01)
    [0.0, 0.69]
    """
    
    # Define grid of parameters for search.
    beta_0_list = np.arange(beta_0_min, beta_0_max, step)
    beta_1_list = np.arange(beta_1_min, beta_1_max, step)
    
    # Initialize logit and index numbers. 
    max_logit_sum = float("-inf")
    i_max = None
    j_max = None
    
    # Loop over candidate values to find a maximum logit_like_sum.
    for i in range(len(beta_0_list)):
        for j in range(len(beta_1_list)):
            
            # Extract candidate values of parameters.
            beta_0 = beta_0_list[i]
            beta_1 = beta_1_list[j]
            
            # Calculate candidate value of logit_like_sum.
            logit_sum_ij = logit_like_sum(y, x, beta_0, beta_1)
            
            # Replace values if logit_sum_ij is a new high.
            if logit_sum_ij > max_logit_sum:
                # Keep this as the new highest value.
                max_logit_sum = logit_sum_ij
                # Record the location of the parameter values.
                i_max = i
                j_max = j
                
    # At the end, if a highest value was found, 
    # output those values.
    if (i_max is not None and j_max is not None):
        return [beta_0_list[i_max], beta_1_list[j_max]]
    else:
        print("No value of logit_like_sum was higher than the initial value.")
        print("Choose different values of the parameters for beta_0 and beta_1.")
        return None



# Ugly version that works and is directly stolen from Assignment 5.
# Only a few lines of code had to be changed, outlined by #---.

def max_logit_CES_xy(y: List[float], x: List[float], 
        beta_0_min: float, beta_0_max: float, 
        beta_1_min: float, beta_1_max: float, 
        step: float) -> float:
    """
    Calculates the estimated coefficients 
    by grid search on the value of the logit_like_sum function
    for the logistic regesssion model 
    given two lists of data y and x.
    
    The search is taken over a grid of candidate values
    of beta_0 and beta_1 defined over
    np.arange(beta_0_min, beta_0_max, step) and
    np.arange(beta_1_min, beta_1_max, step), respectively.
    
    
    >>> max_logit_CES_xy([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], \
                  -2.0, 2.0, -2.0, 2.0, 0.10)
    [0.0, 0.0]
    >>> max_logit_CES_xy([1, 0, 1], [15.0, 10.0, 5.0], \
                  -1.0, 1.0, -1.0, 1.0, 0.01)
    [0.69, 0.0]
    >>> max_logit_CES_xy([1, 0, 1, 0, 1], [0, 0, 1, 1, 1], \
                  -1.0, 1.0, -1.0, 1.0, 0.01)
    [0.0, 0.69]
    """
    
    #--------------------------------------------------------------------------------
    # Swap the parameters from the logit optimization problem for the CES problem.
    
    # In this case, the optimization is over beta_0 and beta_1 instead of x and y.
    x_min = beta_0_min
    x_max = beta_0_max
    y_min = beta_1_min
    y_max = beta_1_max
    # step is the same parameter.
    # Likewise, the x and y are given parameter values passed below.
    
    # Aside from one line added below, these are all the changes that *must* be done.
    # However, this function is confusing, even though it works. 
    #--------------------------------------------------------------------------------
    
    
    # Define grid of parameters for search.
    x_list = np.arange(x_min, x_max, step)
    y_list = np.arange(y_min, y_max, step)
    
    # Initialize utility function and indices (in case no optimum found).
    max_CES = float('-inf')
    i_max = None
    j_max = None
    
    # Loop over candidate values to find a minimum SSR.
    for i in range(len(x_list)):
        for j in range(len(y_list)):
            
            # Extract candidate values of parameters.
            x_i = x_list[i]
            y_j = y_list[j]
            
            #--------------------------------------------------------------------------------
            # Calculate candidate value of utility function.
            # Turn off the warning message for now.
            # if p_x*x_i + p_y*y_j <= w:
            #     CES_ij = CESutility_in_budget(x_i, y_j, r, p_x, p_y, w)
            # else:
            #     CES_ij = None
            
            # Call the logit_sum function in the place of CES_ij.
            CES_ij = logit_like_sum(y, x, x_i, y_j)
            #--------------------------------------------------------------------------------
            
            # Replace values if CES_ij is a new high (and the inputs are valid).
            if not CES_ij == None and CES_ij > max_CES:
                # Keep this as the new lowest value.
                max_CES = CES_ij
                # Record the location of the parameter values.
                i_max = i
                j_max = j
                
    # At the end, if a highest value was found, 
    # output those values.
    if (i_max is not None and j_max is not None):
        return [x_list[i_max], y_list[j_max]]
    else:
        print("No value of utility was higher than the initial value.")
        print("Choose different values of the parameters for x and y.")
        return None




# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 


# Make sure to include examples in your docstrings
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 


# The tests are implemented below -- but only
# when the script is run, not when it is imported. 


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    
    






##################################################
# End
##################################################
