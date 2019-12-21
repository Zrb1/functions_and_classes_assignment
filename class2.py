"""
If you have used Excel or some other spreadsheet program in the past you may be familiar with creating linear
trendlines of data. Given a series of points that lie on the XY plane, a trendline is a line that attempts to
model the relationship between the y values of the points and the x values of the points through the equation
y = mx + b. Whether this is actually a good fit or not depends on the data that is being looked at, but we are
going to create a class that takes in some data, creates a trendline based on the data that follows this equation,
and then create a score that tells us how well the trendline fits to our data. Notice that in this class there
is no __init__ method. There only needs to be one if there is code that needs to be run when an instance of the
class is initialized. Fill in the three methods below according to what they are supposed to do.
"""

class TrendLine:
    def fit(self, X, Y):
        """
        This function takes 2 lists as inputs, X and Y. X is the x values of the datapoints and Y is the y values
        of the datapoints, so for example (X[1], Y[1]) would create the second datapoint in our dataset. This
        function should initialize 2 instance variables, self.m and self.b, where self.m is the slope of the
        trendline and self.b is the y intercept. See
        https://math.stackexchange.com/questions/204020/what-is-the-equation-used-to-calculate-a-linear-trendline
        for the equations used to calculate m and b based off the data.
        """
        #######YOUR CODE HERE##########
            xavg = X.mean()
            self.m = (Y*(x-xavg)).sum()/(X*(x-xavg)).sum()
            self.b = Y.mean()-self.m*xavg
            return self

        ##########END CODE#############

    def predict(self, X):
        """
        This function takes the list X as input. These are the x values of a list of datapoints. The function of
        the predict method is to predict the corresponding y values based off the values self.m and self.b calculated
        in the fit method. Because of this, this predict method cannot be run without running the fit method on
        some datapoints first since self.m and self.b are not initialized until the fit method is run. This function
        should return a list where suppose x_i is the ith element of X. The ith element of the list returned should
        then be m * x_i + b where m and b are the values calculated in the fit method.
        """
        #######YOUR CODE HERE##########
        y = self.m*X + self.b
        return y
        ##########END CODE#############

    def score(self, X, Y):
        """
        Like the fit method, this function takes 2 lists as inputs, X and Y. X is the x values of the datapoints and
        Y is the y values of the datapoints. This function should create the predicted values of Y by running the
        predict method you wrote on X, and then it should return the r^2 score between these predicted values and the
        actual values Y. See https://en.wikipedia.org/wiki/Coefficient_of_determination for the equations used to
        calculate the r^2 score. (It is 1 - SS_res/SS_tot)
        """
        #######YOUR CODE HERE##########

        ##########END CODE#############

if __name__ == '__main__':
    """
    Create and run test cases here if you wish. There is a jupyter notebook that was created also that once you have
    finished writing this class, you should be able to run the cells and visualize the trendline created from this
    code. The notebook is called TrendLine_Test.ipynb.
    """
    #########CREATE TEST CASES HERE###########
    pass
    ##########END TEST CASES##################
