n = int(input("Enter the number of elements: "))
arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

print("The elements of the array are:")
for element in arr:
    print(element, end=' ')
print()

