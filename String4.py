
# String
"""
A string is a sequence of characters (letters, numbers, symbols) enclosed in quotes.

"""
#Quotes can be single ('), double ("), or even triple (''' or """) for multiline strings.

#Creating a String

a = 'abhi'
b = "Sunny"
print(a)
print(b)
  
  #Multi-line Strings
c = """Hi, i am
Abhishek Mishra  """
print(c)

#Accessing characters in Python String

d = "Python"
print(d[1])
print(d[4])

    #Access string with Negative Indexing
print(d[-2])
print(d[-1])

    #String Slicing
print(d[0:3])
print(d[1:])
print(d[:4])
print(d[::-1])  # Reverse a string

#String Immutability
"""
Strings in Python are immutable. 
This means that they cannot be changed after they are created. 

If we need to manipulate strings then we can use methods 
like concatenation, slicing, or formatting 
to create new strings based on the original.

"""
a = "Dad"
 # a[0] = "M" TypeError
a = "M" + a[1:]  # new String is created
print(a)

#Deleting a String
del a

#Updating a String
"""
To update a part of a string we need to create a new string since strings are immutable.
used replace() method to replace ‘geeks’ with ‘GeeksforGeeks’.
"""
a = "Abhi Mishra"
a1 = a.replace("Abhi", "Sunny")
print(a1)



#Common String Methods

a = "Freedom"

#len(): The len() function returns the total number of characters in a string.
print(len(a))

#upper() and lower(): upper() method converts all characters to uppercase. lower() method converts all characters to lowercase.
print(a.upper())
print(a.lower())

#strip() and replace(): strip() removes leading and trailing whitespace from the string and 
# replace(old, new) replaces all occurrences of a specified substring with another.
i = "  Abhi Mishra"
print(i)
print(i.strip()) # Removes spaces from both ends

print(i.replace("Abhi", "Sunny"))

#Concatenating and Repeating Strings

#Strings can be combined by using + operator.
a1 = "Sunny"
a2 = "Mishra"
a3 = a1 + a2
print(a3)
print(a1 + " "+a2)

#We can repeat a string multiple times using * operator.

a1 = "Aunty "
print(a1 * 10)


#Formatting Strings
#Python provides several ways to include variables inside strings.

#Using f-strings
#The simplest and most preferred way to format strings is by using f-strings.

name = "Aunty"
age = "30"
print(f"Name: {name}, Age: {age}") 

print("Name:",name,"Age:",age)

#Using format()
#Another way to format strings is by using format() method.

s = "my name is {} and i am {} year old".format(name,age)
print(s)


#Using in for String Membership Testing

a1 = "Hi my name is Aunty"
print("Aunty" in a1)
print("Age" in a1)


