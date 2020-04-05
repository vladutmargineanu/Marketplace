"""
This module represents the Producer.

Computer Systems Architecture Course
Assignment 1
March 2020
"""

from threading import Thread
import time

class Producer(Thread):
    """
    Class that represents a producer.
    """

    def __init__(self, products, marketplace, republish_wait_time, **kwargs):
        """
        Constructor.

        @type products: List()
        @param products: a list of products that the producer will produce

        @type marketplace: Marketplace
        @param marketplace: a reference to the marketplace

        @type republish_wait_time: Time
        @param republish_wait_time: the number of seconds that a producer must
        wait until the marketplace becomes available

        @type kwargs:
        @param kwargs: other arguments that are passed to the Thread's __init__()
        """
        Thread.__init__(self, **kwargs)
        self.products = products
        self.marketplace = marketplace
        self.republish_wait_time = republish_wait_time
        self.kwargs = kwargs

    def publish_product(self, product, quantity, wait_time, id_producer):
        iterator = 0
        wait_publish = True
        # Publish a product in the given quantity
        while iterator < quantity:
            wait_publish = self.marketplace.publish(id_producer, product)
            # Producer must wait until the marketplace becomes available
            if wait_publish == True:
                iterator = iterator + 1
                time.sleep(wait_time)
            else:
                time.sleep(self.republish_wait_time)

    def run(self):
        while True:
            # Register the producer, generate id
            id_producer = self.marketplace.register_producer()
            for prod in self.products:
                self.publish_product(prod[0], prod[1], prod[2], id_producer)
