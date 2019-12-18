#########IMPORT LIBRARIES HERE IF NEEDED#######

################END IMPORTS####################
"""
Write a function that takes in a block of text (a string of words) as input and returns a dictionary where the keys are the unique words
in the text and the values are the number of times they appear in the text. Before creating the dictionary, make sure to remove all commas,
periods, question marks, and exclamation points from the text. Also make sure all of the characters become lower cased. For example, the
string 'Hello world, my name is Tom. Do you like pie? Because I sure do!' should be transformed to
'hello world my name is tom do you like pie because i sure do'. The output of the function with the original string as the input should then
be {'hello': 1, 'world': 1, 'my': 1, 'name': 1, 'is': 1, 'tom': 1, 'do': 2, 'you': 1, 'like': 1, 'pie': 1, 'because': 1, 'i': 1, 'sure': 1}.
Note that the order of the key value pairs in the resulting dictionary does not matter.
"""

def f(s):
    ##########YOUR CODE HERE##########
    for char in ',.?!:";-''\n':
        s = s.replace(char,' ')
    s = s.lower()

    words = s.split()

    ds = {}
    for word in words:
        ds[word] = ds.get(word, 0) + 1

    return ds
    ###########END CODE###############
