from contextlib import contextmanager
from time import time, sleep 


@contextmanager
def timed(label):
    start = time()
    # Setup -__enter__ 
    print(f"{label}: Start at {start}") 
    try: yield 
    # yield to body of `with` statement 
    finally: # Teardown - __exit__ 
        end = time() 
    print(f"{label}: End at {end} ({end - start} elapsed)")
    
    
    
#look here: since timed is a contextmanager, we  can apply with   
with timed("Counter"): 
    print("I will sleep a while")
    sleep(3) 
