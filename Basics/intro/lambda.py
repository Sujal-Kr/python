# x = lambda a,b : a + b
# print(x(5,7))



# x= lambda a :a%2!=0
# print(x(4))


# wap to take any number as input display the square of that number

# def fun():
#     return lambda a : a*a

# x= fun()
# num=int(input("number please "))
# print(x(num))

# Map()
# 1. The map in python takes a function  and an itrable/iterables.
# It loops over  each  item of an iterable and applies the  transformation function to it.
# Then ,it returns a map object that stores the  values of the  ...

# Syntax:
# map(function ,iterables)
# function :it is the transformation function through  which all the items of the items of the 


# def myfunction(n):
#     return len(n)

# x=map(myfunction,("apple","banana","orange"))
# print(list(x))


# def table(n):
#     for i in range(1,11):
#         print(n*i)

# x=map(table,(1,2,4))
# print(list(x))


# n=int(input())
# def mul(i):
#     return n*i
# x=map(mul,(1,2,3,4,5,6,7,8,9,10))

# print(list(x))

def isprime(x):
    prime=True
    for i in range(2,x):
        if x%i==0:
            prime=False
    return prime


x=map(isprime,(19,2,3,4,6,10,23))
print(list(x))




  
