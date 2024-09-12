

Assignment 4:
1.Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
also create a lambda function that multiplies argument x with argument y and prints the result. 
 
 Sample Output: 
 25 
 48 

# :: Solution ::
adds_15 = lambda x: x + 15

adds_15(10)
# =>
25

multiplies_x_with_y = lambda x,y: x*y

multiplies_x_with_y(12,4)
# =>
48
--- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 

2.Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number. 
 Sample Output: 
 Double the number of 15 = 30 
 Triple the number of 15 = 45 
 Quadruple the number of 15 = 60 
 Quintuple the number 15 = 75 

3.Write a Python program to sort a list of tuples using Lambda. 
 Original list of tuples: 
 [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] 
 Sorting the List of Tuples: 
 [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)] 

4.Write a Python program to sort a list of dictionaries using Lambda. 
 Original list of dictionaries : 
 [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}] 
 Sorting the List of dictionaries : 
 [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}] 

5.Write a Python program to filter a list of integers using Lambda. 
 Original list of integers: 
 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
 Even numbers from the said list: 
 [2, 4, 6, 8, 10] 
 Odd numbers from the said list: 
 [1, 3, 5, 7, 9] 

6.Write a Python program to square and cube every number in a given list of integers using Lambda. 
 Original list of integers: 
 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
 Square every number of the said list: 
 [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 
 Cube every number of the said list: 
 [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000] 

7.Write a Python program to find if a given string starts with a given character using Lambda. 
 Sample Output: 
 True 
 False 

8.Write a Python program to extract year, month, date and time using Lambda. 
 Sample Output: 
 2020-01-15 09:03:32.744178 
 2020 
 1 
 15 
 09:03:32.744178 

9.Write a Python program to check whether a given string is a number or not using Lambda. 
 Sample Output: 
 True 
 True 
 False 
 True 
 False 
 True 
 Print checking numbers: 
 True 
 True 

10.Write a Python program to create Fibonacci series up to n using Lambda. 
 Fibonacci series upto 2: 
 [0, 1] 
 Fibonacci series upto 5: 
 [0, 1, 1, 2, 3] 
 Fibonacci series upto 6: 
 [0, 1, 1, 2, 3, 5] 
 Fibonacci series upto 9: 
 [0, 1, 1, 2, 3, 5, 8, 13, 21] 

11.Write a Python program to find the intersection of two given arrays using Lambda. 
 Original arrays: 
 [1, 2, 3, 5, 7, 8, 9, 10] 
 [1, 2, 4, 8, 9] 
 Intersection of the said arrays: [1, 2, 8, 9]