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
    print(i)
    passwordD_list.append(i)
    for j in letter:
        print(i+j)
        passwordD_list.append(i+j)
        for k in letter:
            print(i+j+k)
            passwordD_list.append(i+j+k)

print(passwordD_list)









