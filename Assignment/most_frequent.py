file=open("file.txt",'r')

words={}
for line in file:
    for word in line.split(' '):
        words[word] = words.get(word,0)+1

max_count=0
ans=""
for keys in words.keys():
    if words[keys]>max_count:
        max_count=words[keys]
        ans=keys
    
print (ans,":",words[ans])
