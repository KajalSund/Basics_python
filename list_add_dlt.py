#addition to list via : append,  insert,  extend

list = ['abc', 'xyz', 'pqr', 'efg', 'ijk']
print(list)
list.append('123') #add at the end of list
print(list)
list.insert(2,'000')  #insert at assigned index
print(list)

list1 = ['#', '$']
list.extend(list1)  #adds 2nd list to the end of first
print(list)

#to delete elements from list via : pop, delete, remove

list.pop()  #pop last elt
print(list) 

list.pop(3) #elt at 3rd index pop up
print(list)

del list[2]  #delete elt at index 2
print(list)

list.remove('123')  #remove elt
print(list)

#in method

if 'ijk' in list:
    print("ijk is present in the list")
else:
    print("not present")    