li=[1,1,2,2,3,3,4,4,5,5]
print(li)
new_li=[]
for i in li:
     if i not in new_li:
         new_li.append(i)
         print(new_li)