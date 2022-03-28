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
# import math
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

# Start with the function from previous assignments.

def CESutility(good_x: float, good_y: float, r: float) -> float:
    """Calculate the constant elasticity of subsitution utility function for two goods.
    
    >>> CESutility(3, 4, 2)
    5.0
    >>> CESutility(1, 1, 2)
    1.4142135623730951
    >>> CESutility(3**0.5, 4**0.5, 4)
    2.23606797749979
    """
    
    utility = (good_x**r + good_y**r)**(1/r)
    return utility


def CESutility_valid(good_x: float, good_y: float, r: float) -> float:
    """Calculate the constant elasticity of subsitution utility function for two goods.
    This version determines whether the inputs are valid, 
    i.e. the quanities of goods are nonegative and r is positive. 
    
    >>> CESutility_valid(3, 4, 2)
    5.0
    >>> CESutility_valid(1, 1, 2)
    1.4142135623730951
    >>> CESutility_valid(3**0.5, 4**0.5, 4)
    2.23606797749979
    >>> CESutility_valid(- 3, 4, 2)
    Error in CESutility_valid: good_x is negative.
    >>> CESutility_valid(3, - 4, 2)
    Error in CESutility_valid: good_y is negative.
    >>> CESutility_valid(3, 4, 0)
    Error in CESutility_valid: r is not positive.
    """
    
    # Check for invalid inputs first. 
    if good_x < 0 or good_y < 0 or r <= 0:
        # Optional: complain about all invalid inputs.
        # Otherwise, it is sufficient to complain about at least one.
        if (good_x < 0):
            print('Error in CESutility_valid: good_x is negative.')
        if (good_y < 0):
            print('Error in CESutility_valid: good_y is negative.')
        if (r <= 0):
            print('Error in CESutility_valid: r is not positive.')
        # Don't forget a return value. 
        return None
    else :
        # If inputs are valid, call the CESutility function. 
        utility = CESutility(good_x, good_y, r)
        return utility


def CESutility_in_budget(x: float, y: float, r: float, 
                         p_x: float, p_y: float, w: float) -> float:
    """Calculate the constant elasticity of subsitution utility function for two goods.
    This version first checks that budget constraint is satisfied, 
    i.e. that p_x*x + p_y*y >= w, 
    then determines whether the inputs are valid, 
    i.e. the quanities of goods are nonegative and r is positive. 
    
    >>> CESutility_in_budget(3, 4, 2, 1, 1, 10)
    5.0
    >>> CESutility_in_budget(1, 1, 2, 5, 10, 15)
    1.4142135623730951
    >>> CESutility_in_budget(3**0.5, 4**0.5, 4, 2, 4, 20)
    2.23606797749979
    >>> CESutility_in_budget(- 3, 4, 2, 1, 1, 10)
    Error in CESutility_valid: good_x is negative.
    >>> CESutility_in_budget(3, - 4, 2, 1, 1, 10)
    Error in CESutility_valid: good_y is negative.
    >>> CESutility_in_budget(3, 4, 0, 1, 1, 10)
    Error in CESutility_valid: r is not positive.
    >>> CESutility_in_budget(3, 4, 2, 2, 4, 20)
    Error in CESutility_in_budget: budget constraint not satisfied.
    """
    
    # Check budget constraint first. 
    if p_x*x + p_y*y > w:
        print('Error in CESutility_in_budget: budget constraint not satisfied.')
        return None
    else :
        # If budget constraint is satisfied, call the CESutility_valid function. 
        utility = CESutility_valid(x, y, r)
        return utility




# Assignment 5, Exercise 3

def CESdemand_calc(r: float, p_x: float, p_y: float, w: float) -> List[float]:
    
    """
    Calculates the optimal bundle of goods x and y 
    using calculus to maximize the Constant Elasticity 
    of Substitution utility function.
    
    Note that when 0 < r < 1, CESdemand_calc() finds a MAXimum
    and this grid search returns the maximal value.
    Conversely, when r > 1, CESdemand_calc() finds a MINimum, 
    but the optimal solution is a *corner solution*, 
    i.e. the consumer spends most of the wealth on one good.
    
    >>> CESdemand_calc(1/2, 2, 4, 12)
    [4.0, 1.0]
    >>> CESdemand_calc(1/3, 4, 9, 27*8*5)
    [162.00000000000003, 48.00000000000002]
    >>> CESdemand_calc(10**(-20), 2, 4, 8)
    [2.0, 1.0]
    >>> CESdemand_calc(2, 1, 1, 2)
    [1.0, 1.0]
    >>> CESdemand_calc(2, 4, 3, 100)
    [16.0, 12.0]
    >>> CESdemand_calc(3, 4, 9, 1000)
    [57.14285714285714, 85.71428571428571]
    """
    x_num = p_x**(1/(r - 1))
    y_num = p_y**(1/(r - 1))
    denom = p_x**(r/(r - 1)) + p_y**(r/(r - 1))
    
    x_star = x_num/denom*w
    y_star = y_num/denom*w
    
    return [x_star, y_star]


# Assignment 5, Exercise 4



def max_CES_xy(
        x_min: float, x_max: float, 
        y_min: float, y_max: float, 
        step: float, 
        r: float, p_x: float, p_y: float, w: float) -> List[float]:
    """
    Calculates the optimal bundle of goods x and y 
    by grid search to maximize the Constant Elasticity 
    of Substitution utility function.
    
    The search is taken over a grid of candidate values
    of x_i and y_j defined over
    np.arange(x_min, x_max, step) and
    np.arange(y_min, y_max, step), respectively.
    
    Note that there is no error handling
    because that is taken care of in CESutility in budget() 
    and in np.arange(). 
    
    Note that when 0 < r < 1, CESdemand_calc() finds a MAXimum
    and this grid search returns the same value.
    Conversely, when r > 1, CESdemand_calc() finds a MINimum, 
    so this grid search finds a *corner solution*, 
    i.e. the consumer spends most of the wealth on one good.
    
    >>> max_CES_xy(0, 12/2, 0, 12/4, 0.1, 1/2, 2, 4, 12)
    [4.0, 1.0]
    >>> max_CES_xy(0, 127*8*5/4, 0, 27*8*5/9, 1, 1/3, 4, 9, 27*8*5)
    [162.0, 48.0]
    >>> max_CES_xy(0, 8/2, 0, 8/4, 0.01, 0.001, 2, 4, 8)
    [2.0, 1.0]
    >>> max_CES_xy(0, 2/1, 0, 2/1, 0.01, 2, 1, 1, 2)
    [0.01, 1.99]
    >>> max_CES_xy(0, 100/4, 0, 100/3, 1.0, 2, 4, 3, 100)
    [0.0, 33.0]
    >>> max_CES_xy(0, 1000/4, 0, 1000/9, 10/7, 3, 4, 9, 1000)
    [248.57142857142858, 0.0]
    """
    
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
            
            # Calculate candidate value of SSR.
            # Turn off the warning message for now.
            if p_x*x_i + p_y*y_j <= w:
                CES_ij = CESutility_in_budget(x_i, y_j, r, p_x, p_y, w)
            else:
                CES_ij = None
            
            # Replace values if CES_ij is a new high (and the inputs are valid).
            if not CES_ij == None and CES_ij > max_CES:
                # Keep this as the new highest value.
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



#--------------------------------------------------
# Question 2
# New Functions
#--------------------------------------------------

# Exercise 4

# Simple solution: Call max_CES_xy 
# and evaluate CESutil_in_budget at x_star and y_star.

def max_CES_util(
        x_min: float, x_max: float, 
        y_min: float, y_max: float, 
        step: float, 
        r: float, p_x: float, p_y: float, w: float) -> List[float]:
    """
    Calculates the utility derived from optimal bundle of goods x and y 
    by grid search to maximize the Constant Elasticity 
    of Substitution utility function.
    
    The search is taken over a grid of candidate values
    of x_i and y_j defined over
    np.arange(x_min, x_max, step) and
    np.arange(y_min, y_max, step), respectively.
    
    Note that there is no error handling
    because that is taken care of in CESutility in budget() 
    and in np.arange(). 
    
    Note that when 0 < r < 1, CESdemand_calc() finds a MAXimum
    and this grid search returns the same value.
    Conversely, when r > 1, CESdemand_calc() finds a MINimum, 
    so this grid search finds a *corner solution*, 
    i.e. the consumer spends most of the wealth on one good.
    
    >>> max_CES_util(0, 12/2, 0, 12/4, 0.1, 1/2, 2, 4, 12)
    9.0
    >>> max_CES_util(0, 127*8*5/4, 0, 27*8*5/9, 1, 1/3, 4, 9, 27*8*5)
    749.9999999999999
    >>> max_CES_util(0, 2/1, 0, 2/1, 0.01, 2, 1, 1, 2)
    1.9900251254695254
    >>> max_CES_util(0, 100/4, 0, 100/3, 1.0, 2, 4, 3, 100)
    33.0
    >>> max_CES_util(0, 1000/4, 0, 1000/9, 10/7, 3, 4, 9, 1000)
    248.5714285714285
    """
    
    # Obtain optimal expenditures on goods x and y.
    xy_star = max_CES_xy(x_min, x_max, y_min, y_max, step, 
        r, p_x, p_y, w)
    
    # Evaluate utility function at optimal values.
    max_CES = CESutility_in_budget(xy_star[0], xy_star[1], r, p_x, p_y, w)
    
    return max_CES


# Alternate solution: Modify max_CES_xy to output utility instead of x_star and y_star.

def max_CES_util_v2(
        x_min: float, x_max: float, 
        y_min: float, y_max: float, 
        step: float, 
        r: float, p_x: float, p_y: float, w: float) -> List[float]:
    """
    Calculates the utility derived from optimal bundle of goods x and y 
    by grid search to maximize the Constant Elasticity 
    of Substitution utility function.
    
    The search is taken over a grid of candidate values
    of x_i and y_j defined over
    np.arange(x_min, x_max, step) and
    np.arange(y_min, y_max, step), respectively.
    
    Note that there is no error handling
    because that is taken care of in CESutility in budget() 
    and in np.arange(). 
    
    Note that when 0 < r < 1, CESdemand_calc() finds a MAXimum
    and this grid search returns the same value.
    Conversely, when r > 1, CESdemand_calc() finds a MINimum, 
    so this grid search finds a *corner solution*, 
    i.e. the consumer spends most of the wealth on one good.
    
    >>> max_CES_util_v2(0, 12/2, 0, 12/4, 0.1, 1/2, 2, 4, 12)
    9.0
    >>> max_CES_util_v2(0, 127*8*5/4, 0, 27*8*5/9, 1, 1/3, 4, 9, 27*8*5)
    749.9999999999999
    >>> max_CES_util_v2(0, 2/1, 0, 2/1, 0.01, 2, 1, 1, 2)
    1.9900251254695254
    >>> max_CES_util_v2(0, 100/4, 0, 100/3, 1.0, 2, 4, 3, 100)
    33.0
    >>> max_CES_util_v2(0, 1000/4, 0, 1000/9, 10/7, 3, 4, 9, 1000)
    248.5714285714285
    """
    
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
            
            # Calculate candidate value of SSR.
            # Turn off the warning message for now.
            if p_x*x_i + p_y*y_j <= w:
                CES_ij = CESutility_in_budget(x_i, y_j, r, p_x, p_y, w)
            else:
                CES_ij = None
            
            # Replace values if CES_ij is a new high (and the inputs are valid).
            if not CES_ij == None and CES_ij > max_CES:
                # Keep this as the new highest value.
                max_CES = CES_ij
                # Record the location of the parameter values.
                i_max = i
                j_max = j
                
    # At the end, if a highest value was found, 
    # output those values.
    if (i_max is not None and j_max is not None):
        return max_CES
    else:
        print("No value of utility was higher than the initial value.")
        print("Choose different values of the parameters for x and y.")
        return None



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
    print(doctest.testmod())
    
    






##################################################
# End
##################################################
