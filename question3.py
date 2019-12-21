#########IMPORT LIBRARIES HERE IF NEEDED#######

################END IMPORTS####################
"""
Given 2 two dimensional points (x1,y1) and (x2,y2), there exists a line that connects the 2 points that will have
a corresponding equation y = mx + b where m is the slope of the line and b is the y intercept. Write a function that
takes in 4 values x1, y1, x2, y2 in that order as input and returns m and b, the slope and y intercept of the connecting
line. In other words your function will calculate the values m and b, and the last line of your function should
look something like

return m, b

Note: you may run into cases where the line connecting the 2 points is a vertical line. In these cases, have your function
return None, None.
"""

def f(x1, y1, x2, y2):
    ##########YOUR CODE HERE##########
    if  (x2-x1) == 0:
        return ('None, none.')
    else:
        m = (y2-y1)/(x2-x1)
        b = (y1)-(x1)*((y2-y1)/(x2-x1))
        return m, b
    ###########END CODE###############
