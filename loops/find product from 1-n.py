num = int(input("Enter a number to find product: "))
product = 1
for i in range(1, num + 1):
    product *= i
print("Product of numbers from 1 to", num, "is:", product)