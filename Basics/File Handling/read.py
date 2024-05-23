f=open("detail.txt", "r")
data=f.read()
print(data)
f.close()

f=open("detail.txt", "r")
text=f.readline()
print(text)
text=f.readline(5)
print(text)
f.close()
# readLines :the function reads the total number of characters present in the file starting from the menetioned size till end of the file


