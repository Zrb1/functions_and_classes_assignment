"""
In this program, we are going to write a class that manages a cafe that sells products such as coffee and bagels to consumers. More
specifically, we are going to track the menu of the cafe which will show the prices of each item, the stock of the cafe items which
will list the quantity of each item currently in stock, and the total amount of money made by the cafe. When customers come in and order
items, those items will be subtracted from the cafe items stock, but the total amount of money made by the cafe will increase by the
total price of what the customer ordered. You should also be able to add items to your stock to supply the demands of the customers.

The __init__ method has been filled out for you. It takes as input a menu, the items of the cafe in stock, and the total amount of
money. The menu will be a dictionary where the keys are the menu items, and the corresponding values are the price of each item. The
stock will be another dictionary where the keys are the unique items currently in stock, and the corresponding values are the number of
each item in stock. The money is a number representing the amount of money the cafe has made. By default this starts out as zero. Fill
out the other 4 methods declared in this class according to what each method is supposed to do.
"""

class Cafe:
    def __init__(self, menu, stock, money = 0):
        #DO NOT CHANGE INIT METHOD
        self.menu = menu
        self.stock = stock
        self.money = money

    def add_menu_item(self, item, price):
        """
        This function should update the menu of the cafe so that the item argument is added as a key, and the price argument is added
        as a corresponding value. If the item is already in the menu, the price for that item should be adjusted so that it is equal
        to the price argument.
        """
        ###############YOUR CODE HERE#############
        self.menu[item] = price
        ##################END CODE################

    def add_stock(self, newstock):
        """
        This function should add items to the cafe stock. It will take a dictionary newstock as input which represents the items that
        you would like to add to the cafe stock. The keys are the unique items that are being added, and the corresponding values are
        the number of each item that is being added. With each item in newstock, if the item exists already in the cafe stock, add the
        number of that item in newstock to the corresponding number in the cafe stock. If the item doesn't exist in the cafe stock, create
        a key in the cafe stock that represents that item, and add the corresponding number in newstock to it.
        """
        ###############YOUR CODE HERE#############
        for key in newstock:
            if key in self.stock.keys():
                self.stock[key] = self.stock[key] + newstock[key]
            else:
                self.stock[key] = newstock[key]
        ##################END CODE################


    def order_cost(self, order):
        """
        This function should take in an order as an input, and return the cost of that order according to the cost of each item found
        on the menu. The order argument will be a dictionary where the keys will be the unique items in the order and the corresponding
        values will be the number of each item in the order. Find the cost of each item from the menu. The total cost is the sum over all
        the unique items in the order of the menu cost of each item times the number of that item in the order. If there are any items
        in the order that are not in the cafe menu, return the string 'Not for sale' instead.
        """
        ###############YOUR CODE HERE#############
        cost = 0
        for key, value in order.items():
            if key in self.menu.keys():
                cost += self.menu[key] * value
            else:
                print(key, 'Not for sale')
        print('Total Cost = $' , cost)
        ##################END CODE################



    def place_order(self, order):
        """
        This function should take in an order as an input, and process that order. The order argument will be a dictionary where the keys
        will be the unique items in the order and the corresponding values will be the number of each item in the order. The function needs
        to decide if the order is valid or not. An order is valid if all the items in the order exist in the cafe menu items, and there is
        to be enough of every item in the cafe stock to meet that order. If the order is valid, then the function should do 2 things. It
        should subtract all the items that were in the order from the cafe stock taking into account the number of each item in the order,
        and the total cost of that order should be added to the money made by the cafe. Have the function then return True if the order was
        valid and False if the order was not valid. Hint: it is possible to run an instance method within another instance method. In this
        case, running self.order_cost(order) will get you the value returned in the order_cost method.
        """
        ###############YOUR CODE HERE#############
        for key, value in order.items():
            if key in self.stock.keys():
                if value >= self.stock[key]:
                    return False
                else:
                    self.add_stock(-order)
                    return True
        ##################END CODE################

if __name__ == '__main__':
    """
    You are encouraged to create some test cases here to see if the methods in your class work as expected. The if __name__ == '__main__'
    notation means that the code under this clause will only be run if the program is called explicitly (i.e. by running python class1.py).
    It will not be run by importing this file to another program. An example of a Cafe instance is given here. This part is not graded though.
    """
    sbux = Cafe({'coffee':2,'mocha':3,'bagel':2.5}, {'coffee':10, 'mocha':5, 'bagel':7, 'tea':20})

    #########CREATE TEST CASES HERE###########
    print(sbux.menu)
    print(sbux.stock)
    print(sbux.money)
    sbux.add_menu_item('orange', 5)
    print(sbux.menu)
    stock = {'coffee':10, 'mocha':5, 'bagel':7, 'tea':20}
    newstock = {'coffee':3, 'mocha':1, 'tea':2,'orange':25, 'biscuit':7}
    order = {'coffee':6, 'mocha':1, 'orange':1}
    sbux.add_stock(newstock)
    print(sbux.stock)
    sbux.order_cost(order)
    ##########END TEST CASES##################
