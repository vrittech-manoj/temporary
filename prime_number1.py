def isPrime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True


number = int(input("input any number#>>>"))

if isPrime(number) == True:
    print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")