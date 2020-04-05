"""
This module represents the Consumer.

Computer Systems Architecture Course
Assignment 1
March 2020
"""

from threading import Thread
import time

class Consumer(Thread):
    """
    Class that represents a consumer.
    """

    def __init__(self, carts, marketplace, retry_wait_time, **kwargs):
        """
        Constructor.

        :type carts: List
        :param carts: a list of add and remove operations

        :type marketplace: Marketplace
        :param marketplace: a reference to the marketplace

        :type retry_wait_time: Time
        :param retry_wait_time: the number of seconds that a producer must wait
        until the Marketplace becomes available

        :type kwargs:
        :param kwargs: other arguments that are passed to the Thread's __init__()
        """
        Thread.__init__(self, **kwargs)
        self.carts = carts
        self.marketplace = marketplace
        self.retry_wait_time = retry_wait_time
        self.kwargs = kwargs

    def run(self):
        id_cart = self.marketplace.new_cart()
        wait_time = True
        list_order = []
        # Iterate in lists from carts to extract elements from dictionary
        for list_element in self.carts:
            for dict_element in list_element:
                type_command = dict_element.get("type")
                id_prod = dict_element.get("product")
                quantity_prod = dict_element.get("quantity")
                # Add product in marketplace, or wait time to become available
                if type_command == "add":
                    iterator = 0
                    while iterator < quantity_prod:
                        wait_time = self.marketplace.add_to_cart(id_cart, id_prod)
                        if wait_time == True:
                            iterator  = iterator + 1
                        else:
                            time.sleep(self.retry_wait_time)
                # Remove product from marketplace
                else:
                    for count in range(quantity_prod):
                        self.marketplace.remove_from_cart(id_cart, id_prod)
        # Get the list with all the products in the cart
        list_order = self.marketplace.place_order(id_cart)
        for product in list_order:
            print(self.name, "bought", product)
         