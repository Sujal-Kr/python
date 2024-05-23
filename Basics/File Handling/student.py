# write a program to careate a file that can wirite ur name and reg no. close this file and then reopen to append the name of courses that u are learing right now , then after close the file and check the status weather the file is open or close


f=open("detail.txt",'w')
f.write("Name:Sujal\n")
f.write("Regno:23mca10069\n")
f.close()
f=open("detail.txt",'a')
f.write("Big Data Analytics")
f.write("Python")
f.write("info security")
f.close()
print(f.closed)


