def NaturalNumber(n,end_number):
    print(n)
    if n < end_number:
        number = n+1
        NaturalNumber(number,end_number)


from_number = int(input("Enter  initial number "))
end_number = int(input("End number "))

NaturalNumber(from_number,end_number)

#WAP using recursion to print prime number (user input) , must use isPrime as function  to check whether number is prime or not

