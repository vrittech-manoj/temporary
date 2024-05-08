file_obj = open("products_datasets.txt","r")
datas = file_obj.readlines()

delete_data = "mac-23"

file_2_obj =  open("products_datasets.txt","w")
copied_data= []
for p in datas:
    if delete_data in p:
        pass
    else:
        copied_data.append(p)
print(copied_data)
file_2_obj.writelines(copied_data)
    