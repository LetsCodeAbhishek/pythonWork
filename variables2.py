
#varoables

""""

In Python, variables are used to store data
A variable is essentially a name that is assigned to a value

Unlike many other programming languages, Python variables do not require explicit declaration of type. 
The type of the variable is inferred based on the value assigned.

Variables act as placeholders for data. They allow us to store and reuse values in our program.

"""

#Python variables do not require explicit declaration of type
x = 10
print(x)

x = "Abhishek"
print(x)


# case sensitive 
my = 10
My = 12

print(my, My)

# rule for variables
""""
Valid Example:

age = 21
_colour = "lilac"
total_score = 90

"""

# class = 11 invalid  syntax error
clas = 11
print(clas)

""""
Invalid Example:

1name = "Error"  # Starts with a digit
class = 10       # 'class' is a reserved keyword
user-name = "Doe"  # Contains a hyphen

"""

# Assigning values to variable:

# basic Assignment
x = 10
y = 20.112222
z = "How are you"

print(x, y, z)

# Dynamic Typing
i = 222
i = "python String"
print(i)


# Multiple Assignment

# Assigning the same value 
a = b = c = 200
print(a, b, c)

#Assigning Different value 
x, y, z = 10, 2.5, "String"
print(x, y, z)



"""
Type Casting a Variable

Type casting refers to the process of converting the value of one data type into another. 
Python provides several built-in functions to facilitate casting, including 
int(), float() and str() among others.

"""
a = "10"
m = int(a)
b = 12
n = float(b)
c = 14.99
o = str(c)

print(m, n, o)


#Getting the type of Variable

a = 10
b = 12.5
c = "String"
d = [1,2,4]
e = {1,2,4}
f = {"1":"111"}
g = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))


"""
Scope of a Variable
There are two methods how we define scope of a variable in python which are local and global.

Local Variables:
Variables defined inside a function are local to that function.

Global Variables:
Variables defined outside any function are global and can be accessed inside functions using the global keyword.

"""

#Local Variable

def f():
    a = "i am local variable"
    print(a)

f()
#print(a) give error


# gobal Variable
b = "gobal"
def Fun():
    global b
    b = "Modified variable"
    print(b)

Fun()
print(b)


"""
Object Reference in Python

Python variables hold references to objects, not the actual objects themselves.
Reassigning a variable does not affect other variables referencing the same object unless explicitly updated.

"""

# Delete a Variable Using del Keyword

q = 10
print(q)

del q

#print(q) error will occur



# Swapping Two Variables
a, b = 10, 20
a, b = b, a
print(a, b)
#20 10

#Counting Characters in a String

i = "Abhishek Mishra"
j = "Ravi Ravi"
print( "Length of String ",len(i))
print("Length of String ", len(j))








