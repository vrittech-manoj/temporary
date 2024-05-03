first_dict = {"name":"ram","age":22}
print(first_dict['name'])

print(first_dict.get('age'))
first_dict['address'] = "kathmandu"

print(first_dict)

for i in range(4):
    key = input("Enter field name#>>>.. ")
    value = input("Enter it's value#>>>.. ")

    first_dict[key] = value

print(first_dict)

# ram_dict = {"name":"ram","address":"ktm"}
# shyam_dict = {"name":"shyam","address":"pokhara"}

detail = []
loop_range = int(input(" Please Enter upto how much student data "))

for i in range(loop_range):
    name =  input("enter name ")
    address = input("enter addresd ")
    phone = input("enter phone number ")
    data = {"name":name,"address":address,"phone":phone}
    detail.append(data)

print(detail)