largest = 0(99)
second_largest  = 0(88)

numbers = [1,88,99,3,23,45,2,23]

for n in numbers:
    if n > largest:
        second_largest = largest
        largest = n
        
print("largest_number: ",largest, " second_largest_number : ", second_largest)

#sort the above list (sort) #assignment
