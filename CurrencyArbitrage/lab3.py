
"""
@author: Aishwarya Supekar
Seattle University
"""
from fxp_bytes_subscriber import fxp_bytes_subscriber

class Lab3:
    
    def welcome():
        print("Program to find the Currency Arbritarage ")
        


if __name__ == '__main__':
    Lab3.welcome()
    subscriber = fxp_bytes_subscriber()                         # Creating object for the fxp_bytes_subscriber class
    print("Listening on {}".format(subscriber.listener_addr))
    subscriber.subscribe_renew()                                # Registering subscription with the Publisher
    subscriber.run_forever(True)                                    # calling the listener 
