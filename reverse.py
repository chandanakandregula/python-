list=[1,2,3,4,5]
a: int=0
b=len(list)-1

while a<b:
 list[a],list[b]=list[b],list[a]
 a+=1
 b-=1
 print(list)