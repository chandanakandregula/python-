from unicodedata import name


def displayhelloworld():
    print("hello world")


def sumofElements(data):
    sum = 0
    for ele in data:
        sum = sum + ele
    return sum

def add(numbers):
    print(numbers[0])
    print(numbers[1])
    print(numbers[2])

def add(num1,num2,num3):
    print(num1+num2+num3)

def greetingmessage(name= "chandana"):
    print("hello",name)

def setstudent(name,age,/,*, dept,sid):
    print(f"hello{name}, your age is{age},with student id{sid},with department{dept}")



def forwordbysecs(secs):
    pass




li = [1, 2, 3, 4, 5]
sum1 = sumofElements(li)

li2 = [10, 20, 30, 40, 40]
sum2 = sumofElements(li2)

li3 = [100, 120, 30, 40, 40]
sum3 = sumofElements(li3)

print(sum1, sum2, sum3)

# displayhelloworld()
#add(5,21)

greetingmessage("Ajay")
greetingmessage()

setstudent("suresh", 22, dept="cse", sid="sid123")

#positional arguments
#setstudent("suresh"25)

add(*[1,2,3])




