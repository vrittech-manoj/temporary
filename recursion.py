def isPrime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def NaturalNumber(n,end_number):
    if n == 1:
        pass
    elif isPrime(n) == True:
        print(f"{n} is prime number")
        
    if n < end_number:
        number = n+1
        NaturalNumber(number,end_number)


from_number = int(input("Enter  initial number "))
end_number = int(input("End number "))

NaturalNumber(from_number,end_number)


#WAP using recursion to print all prime number up to (user input) , must use isPrime as function  to check whether number is prime or not

