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

# detail = []
# loop_range = int(input(" Please Enter upto how much student data "))

# for i in range(loop_range):
#     name =  input("enter name ")
#     address = input("enter addresd ")
#     phone = input("enter phone number ")
#     data = {"name":name,"address":address,"phone":phone}
#     detail.append(data)

# print(detail)

student_dict = []
num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    name = input("Enter student name: ")
    subject = input("Enter subject name: ")
    marks = float(input("Enter obtained marks : "))
    details= {"name": name, "subject": subject,"marks":marks}
    student_dict.append(details)
print(f"Dictionary of students and their marks: {student_dict}.")