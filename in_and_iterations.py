#in keyword and iteration in dictioanry

user_info = {
     'name' : 'Daljit',
     'age' : 18,
     'fav_sport' : ['basketball', 'vollyball'],
     'fav_tune' : ['morning', 'bird charm']
 }  

#check if key exist in dictionary
# if 'name' in user_info:
#     print("present")
# else:
#     print("not present")

#check if value exist in dictionary--->values method
# if 20 in user_info.values():
#     print('present')
# else:
#     print('not present')  


#loop in dictionary
# for i in user_info:
#     print(user_info[i])

# user_info_values = user_info.values()    
# print(user_info_values)
# print(type(user_info_values))


# user_info_keys = user_info.keys()    
# print(user_info_keys)
# print(type(user_info_keys))


#items method
user_info_items = user_info.items()
print(user_info_items)
print(type(user_info_items))

for key, value in user_info.items():
    print(f"key is {key} and value is {value}")