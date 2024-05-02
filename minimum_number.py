datas = "10,2,5,45,6,99"
print(type(datas))
datas_list = datas.split(",")
print(datas_list)

maximum_number = 0
for  number in datas_list:
    number = int(number)
    if maximum_number > number:
        pass
    else:
        maximum_number = number #99

print(f"maximum  number is {maximum_number}")
# minimum_number = 9999999
# for number in datas:
#     if minimum_number<number:
#         pass
#     else:
#         minimum_number  = number

# print(f"minimum number is {minimum_number}")
    