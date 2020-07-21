# Remindo-tron

Construct a reminder service, where users are able to schedule text message reminders
to be sent to them at a later date.

Users have to sign up for a free account, before being able to schedule text messages.

The user can review the currently pending messages, arranged in a queue.

An administrator can review all currently pending messages. Once a message
has been sent successfully, it is marked in some way.

There should be a live visitor counter (of people who have visited the page in
the last 20 minutes) on the home page.

The text message library will follow this given API, but you will not be provided
the actual implementation, and you should not implement one either. The exceptions
can be thrown randomly, these should be reported back to the user.

sms.py
```
def send(to: str, from: str, body: str) -> None:
    """Will throw OutOfCreditException if the website has run out of credit.
    
    Will throw InvalidDestinationException if destination number is invalid.

    Sends a message immediately when called, will block for some short amount
    of time."""
    ...

class MessageException(Exception):
    ...

class OutOfCreditException(MessageException):
    """The owner of this website has failed to pay enough money to
    the mobile phone company, ergo the message was not sent."""

class InvalidDestinationException(MessageException):
    """The given destination phone number is invalid."""
```

Your required technology stack (these are the core pieces)
- Python 3.8
- Django
- redis-py (use for the live visitor counter)
- celery (use for the message send scheduling)

Celery setup / demo here - https://www.youtube.com/watch?v=68QWZU_gCDA. Use `.delay()`
and schedule the message sending for the user's desired datetime.

No styling is required (if you want to make it look slightly shiny, that would
be a bonus).

PEP8 compliance is a must.

Ensure that in your git commit history and messages, you follow best practice.

Ensure that your code is clean, well commented, type hinted, and documented
(docstrings will be sufficient for documenting functions, modules and classes)

BONUS POINTS: Build a docker-compose.yml file that sets up all the services.
