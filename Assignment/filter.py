from functools import reduce


def filter_fun(num):
    return num%2==0

arr=filter(filter_fun,range(1,51))
print(list(arr))



str="Sujal"
vowel=['a','e','i','o',]

for i in str.lower():
    if i == 'a' or i == 'e' or i == 'o' or i == 'u':
        print(i)



ans="s" in "sujal"
print(ans)

# x=reduce(lambda x:i == 'a' or i == 'e' or i == 'o' or i == 'u',"sujal")
# print(x)