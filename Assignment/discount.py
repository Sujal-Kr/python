# generate the customer bill and provide the discount of 5% if the bill is of more than 3000 .if the total purchase is more than 10000 the discount will be 10 %, if the total purchase is more than 20000 the discount will be 2000


amount=int(input("amount"))

if(amount ==20000):
    amount-=2000
    print("New amount is",amount)
elif amount >=3000 and amount<=10000:
    amount-=amount*0.05
    print("New amount is",amount)
elif amount>=10000 and amount<20000:
    amount-=amount*0.10
    print("New amount is",amount)
