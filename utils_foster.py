"""
Module: utils_foster

Purpose: Reusable Module for My Bird Project

Description: This module provides a byline for my bird project. 
When we study the habits of birds, we can discover how they live.
A bird can fly, eat worms, and build nests.

Author: Lindsay Foster

"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics  # provides mean(), stdev() and more....

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
# TODO: Add another or replace this with your own boolean variable
has_wings: bool = True

# declare an integer variable 
# TODO: Add or replace this with your own integer variable
number_of_wings: int = 2

# declare a floating point variable
# TODO: Add or replace this with your own floating point variable
average_distance_of_flight: float = 3.5

# declare a list of strings
# TODO: Add or replace this with your own list  
skills_collected: list = ["Digging", "Flying", "Building"]

# declare a list of numbers so we can illustrate statistics skills
# TODO: Add or replace this with your own numeric list  
number_of_worms_eaten: list = [10.3, 7.9, 13.2, 11.7, 9.4]

# Calculate basic statistics using built-in Python functions and the statistics module
# TODO: Replace these variable names with the variable name of your own numeric list
min_score: float = min(number_of_worms_eaten)  
max_score: float = max(number_of_worms_eaten)  
mean_score: float = statistics.mean(number_of_worms_eaten)  
stdev_score: float = statistics.stdev(number_of_worms_eaten)

# Use a Python formatted string (f-string) to show information
# TODO: Modify the text in the byline to fit your information
# TODO: Modify the variables in the byline to use your variable names
byline: str = f"""
---------------------------------------------------------
Stellar Bird Verbage: Discovering Adaptability
---------------------------------------------------------
Has Wings:  {has_wings}
Number of Wings:         {number_of_wings}
Skills Collected:             {skills_collected}
Number of Worms Eaten: {number_of_worms_eaten}
Minimum Worms Eaten Score: {min_score}
Maximum Worms Eaten Score: {max_score}
Mean Worms Eaten Score: {mean_score:.2f}
Standard Deviation of Worms Eaten Scores: {stdev_score:.2f}
"""

#####################################
# Define global functions (resuable instructions)
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''

    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()

#TODO: Run this as a script and verify all code works as intended.
