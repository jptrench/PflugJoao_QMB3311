# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Joao Pflug
#
# Date: 02/25/2025
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
import math
import numpy as np
##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

#--------------------------------------------------
# Question 1
# Functions from Previous Assignments
#--------------------------------------------------
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


def CESutility_valid(x: float, y: float, r: float) -> float:
   
    """Return the value of the constant elasticity of substitution utitlity
    function to determine the satistfaction of two goods of x and y. R is
    the parameter that determines the curvature of the indifference curves.
    x: Quantity of good1 (must be non-negative).
    y: Quantity of good2 (must be non-negative).
    r: Substitution parameter (must be strictly positive).

    >>> CESutility_valid(5, 5, 0.5)
        20.0
    >>> CESutility_valid(5, -3, 0.5)
        None (Non-eligible input, quantity of good 2 (y) must be non-negative.)
    >>> CESutility_valid(5, 3, -0.5)
        None (Non-eligible input, the substitution parameter (r) must be strictly positive.)
    """
    if x < 0:
        print("Non-eligible input, quantity of good1 (x) must be non-negative.")
        return None
    if y < 0:
        print("Non-eligible input, quantity of good 2 (y) must be non-negative.")
        return None
    if r <= 0:
        print("Non-eligible input, the substitution parameter (r) must be strictly positive.")
        return None
    
    
    return CESutility(x,y,r)


def CESutility_in_budget(x: float, y: float, r: float, p_x: float, p_y: float, w: float) -> float:
    
    """Return the value of the constant elasticity of substitution utitlity
    function to determine the satistfaction of two goods of x and y. R is
    the parameter that determines the curvature of the indifference curves.
    Testing under budget constraint w.
    x: Quantity of good1 (must be non-negative).
    y: Quantity of good2 (must be non-negative).
    r: Substitution parameter (must be strictly positive)
    p_x: Price of good1 (x) 
    p_y: Price of good2 (y) 
    w: Consumer wealth (budget constraint)
    
    >>> CESutility_in_budget(5, 7, 0.4, 3, 3, 50)
    33.66
    >>> CESutility_in_budget(10, 15, 0.5, 7, 8, 40)
    None (Consumer's basket of goods not within set budget constraint (w). Cost of Basket: 190, Budget: 40)
    >>> CESutility_in_budget(3, 3, -0.6, 2, 3, 45)
    None (Non-eligible input, the substitution parameter (r) must be strictly positive.)
    """
    if p_x < 0:
        print("Non-eligible input, price of good1 (p_x) must be non-negative.")
        return None
    if p_y < 0:
        print("Non-eligible input, price of good2 (p_y) must be non-negative.")
        return None
    
    total_cost = p_x * x + p_y * y
    if w < total_cost:
        print(f"Consumer's basket of goods not within set budget constraint (w). Cost of Basket: {total_cost}, Budget: {w}")
        return None

  
    return CESutility_valid(x, y, r)


#--------------------------------------------------
# Question 2
# New Functions
#--------------------------------------------------

# Exercise 4
def max_CES_util(x_min:float, x_max:float, y_min:float, y_max:float, step:float, r:float, p_x:float, p_y:float, w:float) -> float:
    """Find the maximum value of the CES utility function subject to budget constraints.
    >>> max_CES_util(1, 10, 1, 10, 1, 0.5, 2, 3, 50)
    40
    >>> max_CES_util(1, 12, 2, 8, 1, 0.75, 3, 6, 60)
    19.49
    >>> max_CES_util(2, 16, 4, 20, 1, 0.25, 5, 3, 1000)
    286.66
    """
    best_utility = float('-inf')
    for x in range(x_min, x_max + 1, step):
        for y in range(y_min, y_max + 1, step):
            if CESutility_valid(x, y, r) is not None:
                utility = CESutility_in_budget(x, y, r, p_x, p_y, w)
                if utility is not None and utility > best_utility:
                    best_utility = utility
    return best_utility

# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 
import doctest
if __name__ == "__main__":
    doctest.testmod()

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
