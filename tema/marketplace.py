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
        # Dictionary for the producers
        self.producers_dictionary = {}
        # Dictionary for the consumers carts
        self.carts_dictionary = {}
        # Lock used when add product in cart
        self.lock_add_cart = Lock()
        # Lock used when publish product in marketplace
        self.lock_publish = Lock()
    
    # Each carts need to have a list for store the product
    def initialize_cart(self):
        self.carts_dictionary[self.id_consumer] = []

    # Each producer need to have a list to store products
    def initialize_producer(self):
        self.producers_dictionary[self.id_producer] = []

    def register_producer(self):
        # Returns an id for the producer that calls this.
        self.id_producer = self.id_producer + 1
        # Initialize every producer with an empty list
        self.initialize_producer()
        
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
        # Just a single producer can publish an product in a time
        self.lock_publish.acquire()
        # Get the list of product for the id producer
        producers_list = self.producers_dictionary.get(producer_id)
        is_space = False
        # Verify if the len for the producer queue
        length_prod = len(producers_list)
        if length_prod < self.queue_size_per_producer:
            self.producers_dictionary.get(producer_id).append(product)
            is_space = True
            # Free the lock for the producer id
            self.lock_publish.release()
            return is_space

        return False

    def new_cart(self):
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """
        self.id_consumer = self.id_consumer + 1
        # Initialize an cart for the consumer
        self.initialize_cart()

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
        # Just a single consumer can add product in a time
        self.lock_add_cart.acquire()

        # Iterate in list of list of producers
        for key in list(self.producers_dictionary.keys()):
            for prod in self.producers_dictionary.get(key):
                # If the product is available for consumer
                if prod == product:
                    find_id_prod = key
                    find_product = True
                    break

        if find_product == True:
            # Remove product from producer with id
            self.producers_dictionary.get(find_id_prod).remove(product)
            # Add product in cart 
            self.carts_dictionary.get(cart_id).append([product, find_id_prod])
        # Free the lock for the consumer 
        self.lock_add_cart.release()

        return find_product

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """
        # Take the list of products with id from carts dictionary
        list_product = self.carts_dictionary.get(cart_id)
        find_id_prod= None
        # Iterate in the list to find the id for producer
        for prod, id_prod in list_product:
            if prod == product:
                find_id_prod = id_prod
                break
        # Remove product from cart
        list_product.remove([product, find_id_prod])
        self.carts_dictionary[cart_id] = list_product

        # Add back the product to the list of producer
        self.producers_dictionary.get(find_id_prod).append(product)

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """
        # List with the product to order
        list_order = []
        # List of tuples from cart with id
        list_product = self.carts_dictionary.get(cart_id)
        for prod, id_prod in list_product:
            list_order.append(prod)

        return list_order
