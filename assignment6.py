Assignment 6

1. Write a Python program to create a decorator that logs the arguments and return value of a function.

# :: Solution ::

# Decorator to log arguments and return values
def log_decorator(func):
    def wrapper(*args, **kwargs):
        # Log function arguments
        print(f"Calling {func.__name__} with arguments: {args} and keyword arguments: {kwargs}")
        
        # Call the original function
        result = func(*args, **kwargs)
        
        # Log the return value
        print(f"{func.__name__} returned: {result}")
        
        # Return the result
        return result
    return wrapper

# Example function to test the decorator
@log_decorator
def add(a, b):
    return a + b

# Another example with keyword arguments
@log_decorator
def greet(name="Guest"):
    return f"Hello, {name}!"

# Test the decorated functions
add(5, 10)          # Logs the arguments and return value for 'add'
greet(name="Alice")  # Logs the arguments and return value for 'greet'


--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 


2. Write a Python program to create a decorator function to measure the execution time of a function.

# :: Solution ::


import time

# Decorator to measure execution time
def measure_execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()	# Record the start time
        print("Start Time:", start_time)
        result = func(*args, **kwargs)	# Call the original function
        end_time = time.time()
        print("End Time:", end_time) # Record the end time
        execution_time = end_time - start_time	# Calculate execution time
        print("Exection Time:", execution_time)
        return result
    return wrapper

# Example function using the decorator
@measure_execution_time_decorator
def greet(name, age):
    print("Name:", name)
    print("Age:", age)    


# Call the decorated function
greet('Rahul', 24)

# Output 
Start Time: 1727535193.885
Name: Rahul
Age: 24
End Time: 1727535193.8860002
Exection Time: 0.0010001659393310547
--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

3. Write a Python program to create a decorator to convert the return value of a function to a specified data type.


# :: Solution ::

def convert_to_a_specified_data_type(func):
    def wrapper(*args, **kwargs):
        # Extract the target_type from kwargs and remove it before passing to the original function
        target_type = kwargs.pop('target_type', None)  # Remove target_type from kwargs
        result = func(*args, **kwargs)  # Get the function result
        if target_type:
            return target_type(result)  # Convert result to the desired type
        return result  # Return as is if no type specified
    return wrapper

@convert_to_a_specified_data_type
def greet(name):
    return name

# Calling without specifying a target type (no conversion)
print(greet('Hello!'))  # Output: 'Hello!' (no conversion)


print(greet('123'))  # Output: 123 (as int)

greet('123', target_type=float) # Otput: 123.0 (as float)

@convert_to_a_specified_data_type()
def add(a, b):
    return a + b

add(5, 7, target_type=float)  # Output: 12.0 (as float)

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

4. Write a Python program that implements a decorator to cache the result of a function.

# :: Solution ::

def cache_decorator(func):
    cache = {}	# Cache dictionary to store function results

    def wrapper(args):
        if args in cache:
            print(f"{args} Available in Cache:")
            return cache[args] # Return cached result
        else:
            result = func(args)	# Call original function
            cache[args] = result	# Cache the result
            print(f"{args} computed with function:")
            return result
    return wrapper

@cache_decorator
def square(n):
    return n*n

# Output ::

square(4)
# =>
4 computed with function:
16

square(4)
# =>
4 Available in Cache:
16

square(5)
# =>
5 computed with function:
25

square(4)
# =>
4 Available in Cache:
16

square(6)
# =>
6 computed with function:
36

square(6)
# =>
6 Available in Cache:
36

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

5. Write a Python program that implements a decorator to validate function arguments based on a given condition.


# :: Solution ::

def validate_arguments(func):
    def wrapper(a, b):
        if a > 0 and b > 0: # Validate arguments
            print('Valid Arguments:')
            return func(a, b) # Call original function
        else:
            print('Invalid Argumets:')
    return wrapper


@validate_arguments
def add(a, b):
    return a + b

add(2, 3)
# =>
Valid Arguments:
5

add(2, -3)
# =>
Invalid Argumets:
--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

6. Write a Python program that implements a decorator to retry a function multiple times in case of failure.

 # Imagine a scenario where you are trying to simulate checking a server's status, 
 # but the server might occasionally fail to respond. 
 # You want to retry a few times before giving up.

# :: Solution ::

import random
import time

def retry_decorator(retries=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
                    if attempts < retries:
                        print(f"Retrying in {delay} seconds...")
                        time.sleep(delay)
            print(f"Failed after {retries} attempts.")
        return wrapper
    return decorator


@retry_decorator(retries=3, delay=2)
def check_server_status():
    print("Checking server status...")
    # Simulate random server failure
    if random.choice([True, False]):
        raise ConnectionError("Server not responding")
    print("Server is up!")


# Output :

check_server_status()
# =>
Checking server status...
Attempt 1 failed: Server not responding
Retrying in 2 seconds...
Checking server status...
Attempt 2 failed: Server not responding
Retrying in 2 seconds...
Checking server status...
Server is up!

check_server_status()

Checking server status...
Attempt 1 failed: Server not responding
Retrying in 2 seconds...
Checking server status...
Attempt 2 failed: Server not responding
Retrying in 2 seconds...
Checking server status...
Server is up!


--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

7. Write a Python program that implements a decorator to enforce rate limits on a function.

# :: Solution ::
import time
from functools import wraps

# Rate limit decorator
def rate_limit(max_calls, period):
    def decorator(func):
        last_called = [0.0]  # Use a list to persist the state across calls

        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            elapsed_time = current_time - last_called[0]

            if elapsed_time < period:
                wait_time = period - elapsed_time
                print(f"Rate limit exceeded. Please wait {wait_time:.2f} seconds.")
                time.sleep(wait_time)

            last_called[0] = time.time()  # Update the last called time
            return func(*args, **kwargs)

        return wrapper
    return decorator

@rate_limit(max_calls=1, period=5)  # Allow 1 call every 5 seconds
def greet(name):
    print(f"Hello, {name}!")

# Output :
greet('Rahul')

greet('Rahul')

Rate limit exceeded. Please wait 0.80 seconds.
Hello, Rahul!

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 
8. Write a Python program that implements a decorator to add logging functionality to a function.

9. Write a Python program that implements a decorator to handle exceptions raised by a function and provide a default response.

10. Write a Python program that implements a decorator to enforce type checking on the arguments of a function.

11. Write a Python program that implements a decorator to measure the memory usage of a function.

12. Write a Python program that implements a decorator to provide caching with expiration time for a function.



