first_list = [1,2,3,4,5,6,7,8,9]
# print(first_list)

second_list = []

# for item in first_list:
#     if item%2 == 0:
#         second_list.append(item)

second_list = [item for item in first_list if item%2==0]

# print(second_list)


#*******************************************

first_list_data = [{'name':"ram","mark":80},{'name':"shyam","mark":60},{'name':"hari","mark":30},{'name':"gopal","mark":40}]
# print(first_list_data)

# second_list_data = []

# for item in first_list_data:
#     if item['mark'] >= 60:
#         second_list_data.append(item)


# print(second_list_data)
        
second_list_data = [item for item in first_list_data if item['mark']>60 or item['mark']==30]
print(second_list_data)


second_list_data = [item if {'name':item['name'],'status':"pass",'mark':item['mark']}  else {'name':item['name'],'status':"fail",'mark':item['mark']} for item in first_list_data]
print(second_list_data)




