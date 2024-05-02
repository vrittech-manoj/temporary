#list
first_list  =  ["ramesh","rohan","shyam","hari","sita"]
# for i in first_list:
#     print(i,end="           ")


# second_list = ["mukesh"]
# second_list = second_list + first_list
# print(second_list)

#WAP to store password generated data in list
passwordD_list = []
letter = "abcd"
for i in letter:
   
    passwordD_list.append(i)
    for j in letter:
      
        passwordD_list.append(i+j)
        for k in letter:
         
            passwordD_list.append(i+j+k)

print(passwordD_list)


WAP to convert ["23","45,"12","54"] into [23,45,12,54] using for loop #class task
first_list = ["23","45,"12","54"] 







