#########IMPORT LIBRARIES HERE IF NEEDED#######
import numpy as np
################END IMPORTS####################
"""
Write a function that returns both the sample mean and sample standard deviation of a list of numbers. Your function will calculate
the mean and standard deviation separately and the last line of your function should look something like

return m, sd

where m is the mean, and sd is the standard deviation. Make sure to return them in that order. See
https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-sample/a/population-and-sample-standard-deviation-review
for the equations to calculate the sample standard deviation. Make sure you use the sample standard deviation and not the population
standard deviation.
"""

def f(l):
    ##########YOUR CODE HERE##########
    m = np.mean(l)
    sd = np.std(l)
    return m, sd
    ###########END CODE###############
