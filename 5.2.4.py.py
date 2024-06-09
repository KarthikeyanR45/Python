n1 = int(input("Enter the number of elements in the first array: "))
arr1 = []
print("\nEnter the elements of the first array:")
for i in range(n1):
    arr1.append(int(input()))

n2 = int(input("\nEnter the number of elements in the second array: "))
arr2 = []
print("\nEnter the elements of the second array:")
for i in range(n2):
    arr2.append(int(input()))

if arr1 == arr2:
    print("\nThe two arrays are the same")
else:
    print("\nThe two arrays are different")
    
