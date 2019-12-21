#########IMPORT LIBRARIES HERE IF NEEDED#######

################END IMPORTS####################
"""
Write a function that takes a path to a text file as input and returns a list of strings, where each string shows one of the lines in the
file. The strings should be ordered by the order that they appeared in the text. Each line in the text file will contain some empty whitespace
and the end of the line, and possibly at the beginning depending on the file you are working with. Before appending the lines to the list
being returned, you should remove this whitespace. The build in strip() method may be helpful. For example, there is a text file called text_text.txt.
Your function should open this file given its path and return the list ['Roses are red,', 'Violets are blue,', 'Sugar is sweet,', 'And so are you.'].
See https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python for an intro to file processing.
"""

def f(path):
    ##########YOUR CODE HERE##########
    def f(path):
        with open(path) as afile:
            x=[]
            for i in afile:
                i=i.strip().split(" ,")
                x.append(i)
            return x
    ###########END CDE###############

#path = '/home/zacharyraymond-becker/Documents/paloaltoinsight/Highoutputpython/assigment/functions_and_classes_assignment/test_text.txt'
