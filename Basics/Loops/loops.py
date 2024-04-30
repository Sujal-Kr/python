# python prvides two types of
# For loop :the for loop is used for repeating the statement for a given reage of values.
# for the for loop usally the increment and decrement of the variables are with one value.
# if we wannt to increase or decrease the vales with more than we need to include step keyword


for i in range(0,10):
    print("i:",i)

# display the table of ten in reverse order

for i in range(1,11):
    print(10*(11-i))

for i in range(10,-1,-1):
    print(10*i)

# The range can be dicided with any intial point and can be terminated at any ending point




# The loop is used for checking some conditions usally , the condition is the terminating statment for the loop 
# the While loop is making use of increment and decrement operators directly without using the step keyword

p=0
while p<=10:
    print(p, "was called")
    p+=1

p=10
while p>=0:
    print(10*p)
    p-=1


# break
for i in range(10):
    if i==4:
        break
    else :
        print(i)

# continue
for i in range(10):
    if i==4:
        continue
    else :
        print(i)

