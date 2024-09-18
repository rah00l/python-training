Assignment: 1 

1. What is the output of the following code?  
nums = set([1,1,2,3,3,3,4,4])  
print(len(nums))   

# :: Solution ::
4
--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

2. What will be the output? d = {"john":40, "peter":45} print(list(d.keys()))

# :: Solution ::
['john', 'peter']

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

3.  A website requires a user to input username and password to register. Write a program to check the validity of password given by user. 
Following are the criteria for checking password:   

At least 1 letter between [a-z] 
At least 1 number between [0-9]  
At least 1 letter between [A-Z] 
At least 1 character from [$#@] 
Minimum length of transaction password: 6  
Maximum length of transaction password: 12 


# :: Solution ::

import re

def validate_password(password):
    if (6 <= len(password) <= 12
        and re.search("[a-z]", password)
        and re.search("[A-Z]", password)
        and re.search("[0-9]", password)
        and re.search("[$#@]", password)):
        return True
    else:
        return False

password = input("Enter your password: ")
if validate_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")


--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

4. Write a for loop that prints all elements of a list and their position in the list.      
  a = [4,7,3,2,5,9]  

  # :: Solution ::
  a = [4, 7, 3, 2, 5, 9]

  for index, value in enumerate(a):
      print(f'Element {value} is at position {index}')

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---   

5. Please write a program which accepts a string from console and print the characters that have even indexes. 
Example: If the following string is given as input to the program: H1e2l3l4o5w6o7r8l9d 
Then, the output of the program should be: Helloworld 

# :: Solution ::

s = input("Enter a string: ")
print(s[::2])

# Example Input: H1e2l3l4o5w6o7r8l9d
# Output: Helloworld

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

6. Please write a program which accepts a string from console and print it in reverse order.

 Example: If the following string is given as input to the program:  rise to vote sir 
Then, the output of the program should be: ris etov ot esir

# :: Solution ::

s = input("Enter a string: ")
print(s[::-1])

Example Input: rise to vote sir
Output: ris etov ot esir

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---


7. Please write a program which count and print the numbers of each character in a string input by console. 
Example: If the following string is given as input to the program: abcdefgabc 
Then, the output of the program should be: 
a,2
c,2
b,2
e,1
d,1
g,1
f,1


# :: Solution ::
from collections import Counter

s = input("Enter a string: ")
counter = Counter(s)

for char, count in counter.items():
    print(f'{char},{count}')

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

8. With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list 
whose elements are intersection of the above given lists. 


# :: Solution ::

array1 = [1,3,6,78,35,55]
array2 = [12,24,35,24,88,120,155]

intersection = list(filter(lambda x: x in array2, array1))
print(intersection)


--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

9. With a given list [12,24,35,24,88,120,155,88,120,155], write a program to 
  print this list after removing all duplicate values with original order reserved. 

# :: Solution ::
  lst = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

  result = []
  [result.append(x) for x in lst if x not in result]
  print(result)  

Output: [12, 24, 35, 88, 120, 155]

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

 10. By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155]. 


# :: Solution ::
 lst = [12, 24, 35, 24, 88, 120, 155]
 result = [x for x in lst if x != 24]
 print(result)

Output: [12, 35, 88, 120, 155]

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

11. By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155]. 


# :: Solution ::
 lst = [12, 24, 35, 24, 88, 120, 155]
 result = [x for x in lst if x != 24]
 print(result)

Output: [12, 35, 88, 120, 155]

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---


12. By using list comprehension, please write a program to print the list after removing delete numbers 
which are divisible by 5 and 7 in [12,24,35,70,88,120,155]. 

# :: Solution ::

lst = [12, 24, 35, 70, 88, 120, 155]
result = [x for x in lst if not (x % 5 == 0 and x % 7 == 0)]
print(result)

Output: [12, 24, 88]

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

13. Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.


# :: Solution ::
import random

result = random.sample([x for x in range(1, 1001) if x % 35 == 0], 5)
print(result)



--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

14. Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0). 

Example: If the following n is given as input to the program: 5 
Then, the output of the program should be: 3.55  

# :: Solution ::

n = int(input("Enter n: "))
result = sum(i / (i + 1) for i in range(1, n + 1))
print(f"{result:.2f}")

Example Input: 5
Output: 3.55

--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

