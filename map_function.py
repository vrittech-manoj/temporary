def check_odd_even(value):
    if value%2 == 0:
        print(value, " is even")
    else:
        print(value, " is odd")


first_list = [1,2,3,4,5,6,7,8]
for item in first_list:
    check_odd_even(item)


#************************************************************
def check_odd_even(value):
    if value%2 == 0:
        # print(value, " is even")
        return f'{value},  is even'
    else:
        return f'{value},  is odd'


first_list = [1,2,3,4,5,6,7,8]
output = map(check_odd_even,first_list)
print(list(output))





