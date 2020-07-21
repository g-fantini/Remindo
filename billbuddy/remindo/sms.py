import logging
import random

def send(to, sender, body):
    """Will throw OutOfCreditException if the website has run out of credit.
        
    Will throw InvalidDestinationException if destination number is invalid.
    
    Sends a message immediately when called, will block for some short amount
    of time."""
    
    #Create random exceptions for simulation
    event = random.randint(0,2) 
    try:
        if(event==0):
            raise InvalidDestinationException
            return False; 
        elif(event==1):
            raise OutOfCreditException
            return False; 
        elif(event==2):
            logging.error('Sms sent succesfully') 
            return True;
    except MessageException:
        logging.error('Sms sending failed')

class MessageException(Exception):
    pass

class OutOfCreditException(MessageException):
    """The owner of this website has failed to pay enough money to
    the mobile phone company, ergo the message was not sent."""
    pass

class InvalidDestinationException(MessageException):
    """The given destination phone number is invalid."""
    pass