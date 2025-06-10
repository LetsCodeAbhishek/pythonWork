#Sets

"""
A set is an unordered, mutable collection of unique elements.
Defined using curly braces {} or the set() constructor.

No duplicate elements:
An unordered collection:
Internally use hashing that makes set efficient for search, insert and delete operations:
Mutable, meaning we can add or remove elements after their creation, 
the individual elements within the set cannot be changed directly:
"""

#Creating Sets
s = {1,2,3,3,3,3}
print(s)
print(type(s))
print(s)

# creating set with list
sn = set([10,20,30,40])
print(sn)

#creating empty set
es = set()
print(es)




# There is no specific order for set elements to be printed

#Type Casting with Python Set method

    ## typecasting list to set
s = set([1,2,3,4])
print(s)


    #Adding elements to Python Sets
s.add(5);
print(s)

for i in range(5,9):
    s.add(i)
print(s)

#Check unique and  Immutable with Python Set

#Python sets cannot have duplicate values. While you cannot modify the individual elements directly, 
# you can still add or remove elements from the set.

a = {1,2,3,"Abhi",3,"Abhi"} # a set cannot have duplicate values
print(a)
print(type(a))

# a[6] = 11
# print(a)  # values of a set cannot be changed
# Error

#Heterogeneous Element with Python Set
a = {"abhi", True, 1.9, 1.5, 0,2}
print(a) # Python example demonstrate that a set
# can store heterogeneous elements

#Python Frozen Sets
"""
A frozenset is:

An immutable version of a Python set
Unchangeable: you cannot add, remove, or update items
Still supports set operations (union, intersection, etc.)

"""

fs = frozenset([1,2,3,4])
print(fs)
s = set([1,2,3,4])
print(s)
print(type(s))
print(type(fs))


#Methods for Sets
#Adding elements to Python Sets
s = {"Abhi", "Sunny", "Ravi"}
s.add("Rajan")
print(s)

# Adding elements to the
# set using iterator
for i in range(1,5):
    s.add(i)
print(s)


#Union operation on Python Sets
s1 = {1,2,2,3,4,5}
s2 = {"Abhi","Sun","Thik","yo"}
s3 = s1.union(s2)
print(s3)
s4 = s1 | s2
print(s4)


#Intersection operation on Python Sets
a1 = {1,2,3,4,5}
a2 = {3,4,5,6,7}
a3 = a1.intersection(a2)
print(a3)
a4 = a1 & a2
print(a4)

#Finding Differences of Sets in Python
a3 = a1.difference(a2)
print(a3)
a4 = a1 - a2
print(a4)

#Clearing Python Sets
a1.clear()
print(a1)





