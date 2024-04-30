def print_prime(n):
    for num in range(1,n+1):
        prime=True
        for i in range(2,num):
            if num % i ==0:
                prime=False
        if prime==True:
            print(num)

print_prime(11)