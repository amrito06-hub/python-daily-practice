num = int(input("Enter a number: "))


is_prime = True
if num < 2:
    is_prime= False
i=2
while i < num :
    if num % i == 0:
        is_prime = False
        break
    i += 1
print(num, "is Prime?", is_prime)