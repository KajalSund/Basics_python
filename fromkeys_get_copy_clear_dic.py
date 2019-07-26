#fromkeys
# d = {'name' : 'unknown', 'age': 'unknown'}
# print(d)

# d = dict.fromkeys(['name', 'age'], 'unknown')
# print(d)

d = dict.fromkeys("xyz", '123')
print(d)

# d = dict.fromkeys(range(1,22),'unknown')
# print(d)

#get method 
#print(d['name'])  #error
print(d.get('name'))
if 'name' in d:
    print('present')
else:
    print("not present")
#to clear dic
# d.clear()
# print(d)


#to create copy of dictionary
d1 = d.copy()
print(d1)