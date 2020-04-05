"""
This module represents the Marketplace.

Computer Systems Architecture Course
Assignment 1
March 2020
"""

from threading import Lock

class Marketplace:
    """
    Class that represents the Marketplace. It's the central part of the implementation.
    The producers and consumers use its methods concurrently.
    """
    def __init__(self, queue_size_per_producer):
        """
        Constructor

        :type queue_size_per_producer: Int
        :param queue_size_per_producer: the maximum size of a queue associated with each producer
        """
        self.queue_size_per_producer = queue_size_per_producer
        self.id_producer = 0
        self.id_consumer = 0
        self.producers_dictionary = {}
        self.carts_dictionary = {}
        self.lock = Lock()

    def register_producer(self):

        # Returns an id for the producer that calls this.
        self.id_producer = self.id_producer + 1
        
        # Initialize every producer with an empty list
        self.producers_dictionary[self.id_producer] = []
        
        return self.id_producer

    def publish(self, producer_id, product):
        """
        Adds the product provided by the producer to the marketplace

        :type producer_id: String
        :param producer_id: producer id

        :type product: Product
        :param product: the Product that will be published in the Marketplace

        :returns True or False. If the caller receives False, it should wait and then try again.
        """
        producers_list = self.producers_dictionary.get(producer_id)

        if len(producers_list) < self.queue_size_per_producer:
            self.producers_dictionary.get(producer_id).append(product)
            return True
        else:
            return False

    def new_cart(self):
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """
        self.id_consumer = self.id_consumer + 1
        # Initialize an cart for the consumer
        self.carts_dictionary[self.id_consumer] = []

        return self.id_consumer

    def add_to_cart(self, cart_id, product):
        """
        Adds a product to the given cart. The method returns

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to add to cart

        :returns True or False. If the caller receives False, it should wait and then try again
        """
        # Find producer id wich have the product
        find_id_prod = None
        find_product = False

        self.lock.acquire()

        # iterate in list of list of producers
        for key in list(self.producers_dictionary.keys()):
            for prod in self.producers_dictionary.get(key):
                # if the product is available for consumer
                if prod == product:
                    find_id_prod = key
                    find_product = True
                    break

        if find_product == True:
            # remove product from producer with id
            self.producers_dictionary.get(find_id_prod).remove(product)
            # add product in cart 
            self.carts_dictionary.get(cart_id).append((product, find_id_prod))
        
        self.lock.release()

        return find_product

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """
        # take the list of products with id from carts dictionary
        list_product = self.carts_dictionary.get(cart_id)
        find_id_prod= None
        # iterate in the list to find the id for producer
        for prod, id_prod in list_product:
            if prod == product:
                find_id_prod = id_prod
                break
        # remove product from cart
        list_product.remove((product, find_id_prod))
        self.carts_dictionary[cart_id] = list_product

        # add back the product to the list of producer
        self.producers_dictionary.get(find_id_prod).append(product)

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """
        # list with the product to order
        list_order = []
        # list of tuples from cart with id
        list_product = self.carts_dictionary.get(cart_id)
        for prod, id_prod in list_product:
            list_order.append(prod)

        return list_order
