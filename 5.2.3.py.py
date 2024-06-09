n = int(input("Enter the number of elements: "))
arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))
    
elements = sum(arr)
print(f"\nThe sum of the elements in the array is: {elements}")


