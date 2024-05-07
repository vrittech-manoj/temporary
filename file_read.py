# datas = open("class-test.txt", "w")
# print(datas.readlines())
# for data in datas:
#     print(data)


# open("filename.txt","action")
# data = open("filename","r")
# data.readline() #it read single line
# data.readlines() #it return whole txt(lines)
# data.close()


data = open("passwords.txt",'a')
data.write("apple\n")
data.write("ball\n")
data.close()

#WAP to store electronics products user input and display,
print("type 1 for store products ")
print("type 2 for display stored products ")
user_input = input("#>>>...")

#WAP to take data from user and store in file
    # Enter Product name 
    # Enter price
    # Enter brand
# like as;
# products.txt 
#     Laptop-vostro-I5,Dell,15000
#     mac-328,Apple,200000

# and display all products in proper format
# like as;
# product-name:Laptop-vostro-I5   brand:Dell   price:15000
# product-name:mac-328   brand:Apple   price:200000
