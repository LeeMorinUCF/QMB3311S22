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
# Function Definitions
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
from typing import List



##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

#--------------------------------------------------
# Question 1
# Functions from Previous Assignments
#--------------------------------------------------







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
    
    # Code goes here.
    
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







##################################################
# End
##################################################
