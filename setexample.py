set1={"c","c++","java","c","python",1,2, True,False,0}
print(len(set1))
print(set1)
#print(set1[0])
print(type(set1))


set2= set(("ajay","vijay","suresh","mahesh"))
print(set2)
print(type(set2))



#acess element
for ele in set2:
    print(ele)



print("suresh" in set2)
print("suresh" not in set2)



#modifications
#add and delete possible but modification not allowed
set2.add("ramesh")
print(set2)

li=["A","B","C"]
set1.update(set2)
set1.update(li)
print(set1)


set1.remove("A")
print(set1)
set1.discard("AB")
print(set1)


print(set1.pop())
print(set1)


print(set2)
#set2.clear() -this will remove all the elements from the list
#delete set2  -this will remove complete set
print(set2)


set3={"c","java","python""c++"}
set4={"java","javascript","python","r"}
set5={".net"}
set5=set3.union(set4,set5)
set6=set3.intersection(set4)
set7=set3.difference(set4)
set8=set3.symmetric_difference(set4)
print(set5)
print(set6)
print(set7)
print(set8)
