
n = int(input("Enter the number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

largest = arr[0]
smallest = arr[0]

for i in range(1, n):
    if arr[i] > largest:
        largest = arr[i]
    if arr[i] < smallest:
        smallest = arr[i]

print(f"The largest element is: {largest}")
print(f"The smallest element is: {smallest}")

