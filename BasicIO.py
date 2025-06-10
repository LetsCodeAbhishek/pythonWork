
# Intro
#comments 

print("Comments")
# comments are not display on screen
print("Comments in Python are the lines in the code that are ignored \n by the interpreter during the execution of the program.") ;


#Indentation 
""""
In Python, indentation is used to define blocks of code. 
It tells the Python interpreter that a group of statements belongs to a specific block.

Indentation is achieved using whitespace (spaces or tabs) at the beginning of each line.

 print statements are indented by 4 spaces, so they belong to the if block.
"""
a = 10
if a > 5:
    print("correct")
print("After if statement")


# Input in python

"""
Python input() function is used to take user input. By default, it returns the user input in form of a string. 
"""

#i = input("Enter your Name: ")
#print("Hello",i,",Welcome" )


# Python Output

print("Print statment is for output in python")

#Printing variables
   #single
a = 10
print(a)

   #Multiple Variables
a = 11
b = 13
print(a,b)



# Take Multiple Input in Python

x, y, z = input("Enter your Value ").split()
print("Value of X ", x)
print("Value of y ", y)
print("Value of Z ", z)

#Take Conditional Input from user in Python
age_input = input("Enter your Age ")
age = int(age_input)

if age<0:
    print("NA")
elif age<18:
    print("your are minor")
elif age >= 18 and age < 65:
    print("Your are Adult") 
else:
    print("Very Old")


# How to Change the Type of Input in Python

color = input("write your Color ")
print(color)

n = int(input("Enter no.  color "))
print(n) 
print(type(n))

p = float(input("Enter a prize of color "))
print(p)
print(type(p))









