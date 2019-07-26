user_info = {
     'name' : 'Daljit',
     'age' : 18,
     'fav_sport' : ['basketball', 'vollyball'],
     'fav_tunes' : ['morning', 'bird charm']
 }  

#how to add data
user_info['fav_place'] = ['usa', 'canada']
print(user_info)

#pop method
popped_item = user_info.pop('fav_tunes')
print(f"popped item is {popped_item}")
print(user_info)
print(type(popped_item))

# popitem
popped_item = user_info.popitem()
print(user_info)
print(type(popped_item))