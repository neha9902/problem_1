import random
import logging 
import threading

LOG_FORMAT = '%(asctime)s : %(message)s'

logging.basicConfig(filename="python_output.log" , level=logging.DEBUG , filemode='a' , format=LOG_FORMAT)

def func():
    '''python script (.py file) that generates a log file called python_output.log
     i)Once every minute generate a random number between 1 and 30 (boh included)
     ii)If the number is between 1 and 10 (both included) use logging.error, else use logging.info
     iii)In both cases the log message should have the format: TIMEOFDAY:RandomnumberGenerated
    '''
    randomNo=random.randint(1,30)
    if(randomNo<=10):
        logging.error(f"Random no generated is {randomNo}")
    else:
        logging.info(f"Random no generated is {randomNo}") 

while(true):
    timer = threading.Timer(1.0, func)
    timer.start()  
    
     




