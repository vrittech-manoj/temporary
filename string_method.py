# name = "Hello World"
# name_2 = "    hello world "
# # print(name.lower()) #it converts to lower case

# # print(name_2.upper()) #it converts to upper case
# print(name_2.strip()) #it remove white space

# print(name_2.replace("world","VRIT")) #syntax string_variable.replace(old,new)

# #write examples for all string methods  with description.

# print(len(name_2)) #it returns length of variable

numbers = "12,   23,34,    23"
numbers_2_list = []
numbers_list = numbers.split(",")
for i in numbers_list:
    print(i.strip())
# print(numbers_list)
# numbers = numbers.strip()
# print(numbers)
