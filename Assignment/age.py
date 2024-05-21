# wap a  to take the age of all studensts persent in the class and filterr them out who are eligle for voting


age=[67,45,2,78,12]



def filter_age(age):
    return age>=18

arr=filter(filter_age,age)
print(list(arr))


