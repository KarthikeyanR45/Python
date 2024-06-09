import math

n = int(input("Enter the number of elements: "))

arr = []

print("\nEnter the elements:")
for i in range(n):
    arr.append(int(input()))

mean = sum(arr) / n

variance = 0
for i in range(n):
    variance += (arr[i] - mean) ** 2
variance /= n

deviation = math.sqrt(variance)

print(f"The mean is: {mean}")
print(f"The variance is: {variance}")
print(f"The standard deviation is: {deviation}")


