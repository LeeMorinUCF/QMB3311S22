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
import numpy as np


##################################################
# Function Definitions
##################################################


# Only function definitions here - no other calculations. 

#--------------------------------------------------
# Question 1
# Functions from Previous Assignments
#--------------------------------------------------

# Copy the function definitions from Assignment 2.



# Assignment 2, Exercise 3

def total_revenue(num_units: int, unit_price: float) -> float:
    """Calculate the total revenue by multiplying the number of units sold 
    by the price per unit.
    
    >>> total_revenue(20, 20.0)
    400.0
    >>> total_revenue(1, 100.0)
    100.0
    >>> total_revenue(100, 1.0)
    100.0
    """
    return num_units*unit_price



# Assignment 2, Exercise 4

def total_cost(num_units:float, multiplier:float, fixed_cost:float) -> float:
    """Calculate the total cost which includes a fixed cost plus the square of num_units 
    times a cost multiplier.
    >>> total_cost(10, 20, 50)
    2050
    >>> total_cost(40, 10, 57)
    16057
    >>> total_cost(20, 50, 93)
    20093
    """
    total = fixed_cost + multiplier*num_units**2
    return total



#--------------------------------------------------
# Question 2
# New Functions
#--------------------------------------------------

# Exercise 1

def total_profit(num_units:float, unit_price:float, 
                 multiplier:float, fixed_cost:float) -> float:
    """Calculate the total profit by multiplying the number of units sold 
    by the price per unit and then subtracting the total cost, 
    which includes a fixed cost plus the square of num_units 
    times a cost multiplier.
    Function call: total_profit(num_units, unit_price, multiplier, fixed_cost)
    
    >>> total_profit(10, 300, 20, 50)
    950
    >>> total_profit(40, 500, 10, 57)
    3943
    >>> total_profit(20, 2000, 50, 93)
    19907
    """
    
    revenue = total_revenue(num_units, unit_price)
    cost = total_cost(num_units, multiplier, fixed_cost)
    profit = revenue - cost
    
    return profit


# Exercise 2

def max_profit_calc(unit_price:float, 
                 multiplier:float, fixed_cost:float) -> float:
    """
    Calculates the quantity to produce that maximizes profit.
    The calculation is performed following a calculation derived using calculus.
    It is assumed that unit_price and multiplier are positive
    and that all three inputs are non-negative.
    Function call: max_profit_calc(unit_price, multiplier, fixed_cost)
    
    >>> max_profit_calc(100, 0.10, 2)
    500.0
    >>> max_profit_calc(200, 2.5, 5)
    40.0
    >>> max_profit_calc(100, 0.10, 50001)
    0
    """
    
    # First, calculate the solution using calculus.
    q_star = unit_price/(2*multiplier)
    # Check if profit is positive, otherwise return zero.
    profit = total_profit(q_star, unit_price, multiplier, fixed_cost)
    if profit < 0:
        q_star = 0
        
    return q_star
    


# Exercise 3

def profit_max_q(q_max:float, step:float, unit_price:float, 
                 multiplier:float, fixed_cost:float) -> float:
    """
    Calculates the quantity to produce that maximizes profit.
    The calculation is performed by grid search over a grid of values 
    of the quantity produced from zero to q_max in increments of size step.
    Function call: profit_max_q(q_max, step, unit_price, multiplier, fixed_cost)
    
    >>> profit_max_q(1000, 10, 100, 0.10, 2)
    500
    >>> profit_max_q(100, 1, 200, 2.5, 5)
    40
    >>> profit_max_q(1000, 10, 100, 0.10, 50001)
    No positive value of quantity was profitable.
    0
    """
    
    q_list = np.arange(0, q_max, step)
    i_max = 0
    max_profit = 0
    for i in range(len(q_list)):
        q_i = q_list[i]
        profit_i = total_profit(q_i, unit_price, multiplier, fixed_cost)
        if (profit_i > max_profit):
            i_max = i
            max_profit = profit_i
            
    if (max_profit < 0):
        print("No positive value of quantity was profitable.")
        return 0
    else:
        return q_list[i_max]
        



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
