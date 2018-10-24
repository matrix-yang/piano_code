
list=[12.3,12.5]
index=[]
interval=[]
for f in list:
    i=int(f)
    inter=f-i
    index.append(i)
    interval.append(inter)

print(index)
print(interval)


import random
list1 =[]
for i in range(100):
    b=random.uniform(1,88)
    list1.append(b)
print(list1)