thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))



count = {}

for i in "sujal":
    count[i] = count.get(i, 0) + 1

print(count)



def prime(num):
    isprime=True
    for i in range(2,num):
        if num%i==0:
            isprime=False
            break
    return isprime


x=filter(prime,range(100))
print(list(x))
