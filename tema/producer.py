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

    def run(self):
        while True:
            # Register the producer, generate id
            id_producer = self.marketplace.register_producer()
            wait_publish = True
            for prod in self.products:
                iterator = 0
                while iterator < prod[1]:
                    wait_publish = self.marketplace.publish(id_producer, prod[0])
                    # Producer must wait until the marketplace becomes available
                    if wait_publish == True:
                        iterator = iterator + 1
                        time.sleep(prod[2])
                    else:
                        time.sleep(self.republish_wait_time)
