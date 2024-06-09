n = int(input("Enter the number of elements: "))

arr = []

print("\nEnter the elements:")
for i in range(n):
    arr.append(int(input()))

target = int(input("\nEnter the element to search: "))

found_index = -1
for i in range(n):
    if arr[i] == target:
        found_index = i
        break

if found_index != -1:
    print(f"Element {target} found at index {found_index}")
else:
    print("Element not found")
    
