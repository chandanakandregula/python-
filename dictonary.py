dist = {
    "c": "Vijay",
    "java": "Ajay",
    "python": "Naresh",
    "java": "Kamal"
}
print(dist)
print(len(dist))
print(type(dist))

dict1 = dict(sname="Ramesh", age=22, country="India")
print(dict1)
print(dict1['age'])
print(dict1.get("age"))
print(dict1.keys())
print(dict1.values())


print(dict1.items())


dict1["age"]=23

print(dict1.items())

dict1.update({"age":25})

print(dict1.items())

#add key,value pairs
dict1["dept"]="cse"
dict1.update({"section":"A"})
print(dict1.items())

#removing item
dict1.pop("section")
print(dict1.items())

del dict1["dept"]
print(dict1.items())

print(dist.items())
#del dist
#print(dist)

dist.clear()
print(dist)

#travese the dictonary
for ele in dict1:
   # print(ele) #key
    print(dict1[ele])

for value in dict1.values():
    print(value)

for keys in dict1.keys():
    print(keys)

for key,value in dict1.items():
    print(key,value)

#copy dict elements
dict2 = dict1.copy()
print(dict2)

dict3 =dict(dict1)

#creating nested dictionary

college={
    "cse":{
        "hodname":"vjay",
        "nooffaculty":40
 },

    "ece":{
        "hodname":"Ajay",
        "nooffaculty":35
    }
}
print(college["ece"])
print(college["ece"]["hodname"])
print(college["ece"]["nooffaculty"])

for key,values in college.items():
    for hodname,noofFaculty in values.items():
        print(hodname,noofFaculty)

dept1={
        "hodname":"vjay",
        "nooffaculty":40
 },

dept2={
        "hodname":"Ajay",
        "nooffaculty":35
    }

college2={
    "cse":dept1,
    "ece":dept2
}




