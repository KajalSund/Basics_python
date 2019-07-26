#split method : convert string to list
name , age = input("enter your name and age ").split(',')
print(name)
print(age)


#join method : convert list to string
list = ["kajal", "99"]
print(','.join(list))


#type method gives type of data structure
print(type(list))  