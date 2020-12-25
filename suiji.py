#随机生成英语字符
import random
a=[]
for i in range(0,1000):
    s= random.randint(65,90)
    r=chr(s)
    a.append(r)
    i+=1
print(a)





