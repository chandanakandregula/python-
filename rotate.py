li = [1, 2, 3, 4, 5]

print("Original List:", li)

n = int(input("Enter n values: "))

new_li = li[n:] + li[:n]

print("Rotated List:", new_li)