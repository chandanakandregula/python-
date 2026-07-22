li = [1,2,3,4,5]
print(li)
largest=max(li)
smallest=min(li)
second_largest=0
second_smallest=largest
for i in li:
     if i<second_smallest:
         if i !=smallest:
             second_smallest=i
             for i in li:
                 if i>second_largest:
                     if i !=largest:
                         second_largest=i


print("second_smallest",second_smallest)
print("second_largest",second_largest)

