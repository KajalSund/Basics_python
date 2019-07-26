 #use of dictionaries
 #because of limitations of lists, lists are not enough to represents real data

 #dictionaries:  unordered collections of data in key : value pair.

 #way to create
user = dict(name = 'kajal', age = 20)
print(user)
print(type(user))

#access data
print(user['name'])

#add elements to empty dictionary
user_info = {}
user_info['name'] = 'kajal'
print(user_info)