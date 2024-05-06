first_list  = [2,4,6,2,8,4,6,9,8,12,8]
# print(first_list)
# first_set = set(first_list)
# first_list = list(first_set)
# print(first_list)

main_list = []

for data in first_list:
    if data not in main_list:
        main_list.append(data)
       

print("duplicate_list: ",first_list," main_list: ",main_list)


