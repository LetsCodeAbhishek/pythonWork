#A tuple is an ordered, immutable collection of items.
#You define it using parentheses (), not square brackets.
#Once created, you can't change, add, or delete items.

"""
The main characteristics of tuples are being ordered , heterogeneous and immutable.
"""

#Creating a Tuple
a = (1,"Abhi", 1.22)
print(a)
print(type(a))

a = tuple("Abhi") # Using Built-in Function
print(a)

#Creating a Tuple with Mixed Datatypes.

a1 = (1,2,3)   # Creating a Tuple with nested tuples
a2 = ("Abhi","Aunty")
a3 = (a1, a2)
print(a3)

    # Creating a Tuple with repetition

a4 = (5,) * 5
print(a4) 


#Accessing of Tuples
t = (1,2,3,4,5)

    # Accessing Tuple with Indexing
print(t[2])
print(t[4])

    # Accessing a range of elements using slicing
print(t[0:2])
print(t[2:4])
print(t[::-1])

    # Tuple unpacking
a,b,c,d,e = t
print(a)
print(b)
print(c)

#Concatenation of Tuples
j1 = (1,2,3)
j2 = ("abhi", "yo")
print(j1+j2)

#Slicing of Tuple
a = tuple("AbhishekHero")
print(a[0:])
print(a[::-1])
print(a[1:5])

#Deleting a Tuple
del a
#print(a)

#Tuple Methods
#count 
#index

a = (1,2,2,3,4,4,5,4,4,4)
print(a.count(4))
print(a.index(2))


#Tuples can’t be changed directly.

"""
Convert to a list → modify → convert back
Create a new tuple with slices
Modify mutable items inside a tuple

"""
a = (1,2,3)
# a[1] = 100
# print(a)
a = a[:1] + (99,) + a[2:]
print(a)

li = (1,2,3)
print(li)
t = list(li)
print(t)
t[0] = 11
li = tuple(t)
print(li)

#Loop Through a tuple
t = (1,2,3,4)
for i in t:
    print(i)


