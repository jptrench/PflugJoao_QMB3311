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


##################################################
# Function Definitions
##################################################


# Only function definitions here - no other calculations. 

#--------------------------------------------------
# Question 1
# Functions from Previous Assignments
#--------------------------------------------------


def total_revenue(num_of_units_sold:int, fixed_price:float) -> float:
    """Return the total revenue earned by a firm from selling products at a fixed price.
    >>> total_revenue(10, 50)
    500    
    """
    return num_of_units_sold * fixed_price


def total_cost(a:float, q:int, b:float) -> float:
    """Return the total cost incurred by a firm to produce a product.
    total_cost(2, 10, 100)
    
    """
    return (a * (q ** 2)) + b

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

import math

def logit(x: float, beta_0: float, beta_1: float) -> float:
    """The logit link function transform a probability value (or an 
    independent variable) into a log-odds scale, which is commonly used 
    in logistic regression and statistical modeling.
    
    Create a logit function to calculate the logit transformation using 
    the given values of x, beta0 and beta1.
    
            Parameters:
            x (float): The input value.
            beta_0 (float): The intercept parameter.
            beta_1 (float): The slope parameter.
        
            Returns:
            float: The probability that y = 1 given x.
    
    """
    
    
    exponent = beta_0 + x * beta_1
    probability = math.exp(exponent) / (1 + math.exp(exponent))
    return probability


def logit_like(yi: int, xi: float, beta_0: float, beta_1: float) -> float:

    """Create a log-likelihood to calculate the observation of yi and xi,
        given the parameter of beta1 and beta0 and it's used to estimate
        the logistic regression.
        
        Calculate the log-likelihood of an observation (y_i, x_i).

        Parameters:
        y_i (int): The observed outcome (0 or 1).
        x_i (float): The input value.
        beta_0 (float): The intercept parameter.
        beta_1 (float): The slope parameter.
    
        Returns:
        float: The log-likelihood of the observation.
        
    """
    
    
    probability = logit(xi, beta_0, beta_1)

    if yi == 1:
        log_likelihood = math.log(probability)
    elif yi == 0:
        log_likelihood = math.log(1 - probability)
    else:
        print("Error! yi must be 0 or 1")

    return log_likelihood

def logit_like_sum(y:list[int],x:list[float],beta_0:float,beta_1:float) -> float:
    """Calculates the sum of the log-likelihood across all observation (yi, xi, i=1,...,n)
    y: Binary response variable of either 1 or 0, for each observation
    x: Predictor variable values for each observation
    beta_0: Intercept parameter
    beta_1: Slope parameter
    
    >>> logit_like_sum([1],[1.5], 2, 1)
    -0.02975
    >>> logit_like_sum([0], [2], 1, 2)
    -5.007
    >>> logit_like_sum([1], [5], 3, 3)
    -1.523
    """
    
    
    log_likelihood = 0
    for i in range(len(y)):
        log_likelihood += logit_like(y[i],x[i],beta_0,beta_1)
        
    return log_likelihood

#--------------------------------------------------
# Question 2
# New Functions
#--------------------------------------------------

# Exercise 1
def total_profit(num_units:float, unit_price:float, multiplier:float, fixed_cost:float) -> float:
    """Calculate the total profit earned by the company.
    >>> total_profit(10, 50, 2, 100)
    200
    >>> total_profit(20, 35, 1.5, 50)   
    50
    >>> total_profit(15, 60, 3, 0)
    225
    """
    revenue = total_revenue(num_units, unit_price)
    cost = total_cost(multiplier, num_units, fixed_cost)
    return revenue - cost


    
# Exercise 2
def max_profit_calc(unit_price:float, multiplier:float, fixed_cost:float) -> float:
    """Calculate the company's optimal production level q_max that maximizes profit.
    >>> max_profit_calc(50, 2, 100)
    12.5
    >>> max_profit_calc(30, 1.5, 200) 
    0
    >>> max_profit_calc(60, 3, 150)
    10
    """
    q_star = unit_price / (2 * multiplier)
    profit = total_profit(q_star, unit_price, multiplier, fixed_cost)
    return q_star if profit > 0 else 0



# Exercise 3
def profit_max_q(q_max:float, step:float, unit_price:float, multiplier:float, fixed_cost:float) -> float:
    """Use a grid search to verify the profit-maximizing production level.
    >>>profit_max_q(50, 5, 50, 2, 100)
    0
    >>>profit_max_q(100, 1, 35, 0.5, 200)
    35
    >>>profit_max_q(1250, 10, 150, 3, 500)   
    20
    """
    best_q = 0
    max_profit = float('-inf')
    for q in range(0, int(q_max) + 1, step):
        profit = total_profit(q, unit_price, multiplier, fixed_cost)
        if profit > max_profit:
            max_profit = profit
            best_q = q
    return best_q



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
