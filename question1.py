#########IMPORT LIBRARIES HERE IF NEEDED#######

################END IMPORTS####################
"""
Write a function that takes a list of numbers as input and returns the index location
within the list of the largest number. If there is more than one location within the
list that contains the largest number, then have the function return the LAST index
location. For example, f([1,2,3,2,3,1]) should return 4.
"""
def f(l):
    ##########YOUR CODE HERE##########
    indices = [i for i, x in enumerate(l) if x == max(l)]
    return max(indices)
    ###########END CODE###############
