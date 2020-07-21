import logging
import random

def send(to, sender, body):
    """Will throw OutOfCreditException if the website has run out of credit.
        
    Will throw InvalidDestinationException if destination number is invalid.
    
    Sends a message immediately when called, will block for some short amount
    of time."""
    
    #Create random exceptions for simulation
    event = random.randint(0,2) 
    log = ""
    try:
        if(event==0):
            log="FID"
            raise InvalidDestinationException
        elif(event==1):
            log="FOC"
            raise OutOfCreditException
        elif(event==2):
            log="SEN";
            logging.info('Sms sent succesfully') 
         
    except MessageException:
        logging.error('Sms sending failed')
    
    return log

class MessageException(Exception):
    pass

class OutOfCreditException(MessageException):
    """The owner of this website has failed to pay enough money to
    the mobile phone company, ergo the message was not sent."""
    pass

class InvalidDestinationException(MessageException):
    """The given destination phone number is invalid."""
    pass