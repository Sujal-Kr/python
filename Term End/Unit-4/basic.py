f=open("sujal.txt","a+")
f.seek(0)
txt=f.readline()
for line in f.read().split(" "):
    print(line)
