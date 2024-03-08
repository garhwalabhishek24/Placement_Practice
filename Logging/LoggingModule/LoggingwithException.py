import logging
logging.basicConfig(
    filename="log.text",
    level = logging.DEBUG,
    format=" %(asctime)s:%(levelname)s:%(message)s",
    datefmt= "%d:%m:%Y %I:%M %p "
)
    
logging.info("a new reqest come:")
try:
    x=int(input("enter first number:"))
    y=int(input("enter second number:"))
    print("the result ",x/y)
except ZeroDivisionError as msg:
    print("you cant divide with zero")
    logging.exception(msg)
except ValueError as msg:
    print("you cant not divide with datatypes")
    logging.exception(msg)      
        
    