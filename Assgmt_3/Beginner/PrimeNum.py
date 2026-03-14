num = int(input("Enter a number: "))

i = 2
is_prime = True

while i < num:
    if num % i == 0:
        is_prime = False
        break
    i += 1

if num <= 1:
    print(f"Number entered: {num}\nNot a prime number")
elif is_prime:
    print(f"Number entered: {num}\nPrime number")
else:
    print(f"Number entered: {num}\nNot a prime number")