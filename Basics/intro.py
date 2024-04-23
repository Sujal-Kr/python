

print(" What do you truly desire")
print(' Good question')


# Tripple single quotes are used to print the statement in the same format as written by the user .
print(''' Good 
      question''')

# Creating Variables
num=100
x="Lord Sujal"

print(x)
print(num)

# Type casting 
str=str(100)
num=float(10)

print(type(str)) #class str
print(type(num)) #class float


# Multiple Variables

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# You need to unpack all the variables
fruits=["grapes","avacado","orange"]
one,two,three=fruits

print(one)
print(two)

# + ane , are used the contact the string  but nums and string can't be combined
#global keyword can be used to create global variables

def fun():
    global x
    x="i am global"

fun()
print("global:",x)

