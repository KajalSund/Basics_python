n = int(input("enter number to sum till "))
sum = 0
for i in range(1, n):
    sum += i
print(sum)


# sum of digits using for loop in python
n = input("enter multi digit number ")
sum = 0
length = len(n)
for i in range(0, length):
    sum += int(n[i])
print(sum)    


#count letters repetition in entered string using for loop

name = input("enter any string ")
temp_var = ""
length = len(name)
for i in range(0, length):
    if name[i] not in temp_var:
        print(f"{name[i]} : {name.count(name[i])}")
        temp_var += name[i]


