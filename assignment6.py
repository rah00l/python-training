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

5. Write a Python program that implements a decorator to validate function arguments based on a given condition.

6. Write a Python program that implements a decorator to retry a function multiple times in case of failure.

7. Write a Python program that implements a decorator to enforce rate limits on a function.

8. Write a Python program that implements a decorator to add logging functionality to a function.

9. Write a Python program that implements a decorator to handle exceptions raised by a function and provide a default response.

10. Write a Python program that implements a decorator to enforce type checking on the arguments of a function.

11. Write a Python program that implements a decorator to measure the memory usage of a function.

12. Write a Python program that implements a decorator to provide caching with expiration time for a function.



