# #define a function that takes a number(n)
# #return a dic containing cube of numbers from 1 to n

# def cube_finder(n):
#     dic = dict.fromkeys(range(1,n+1), 0)
#     for i in dic.keys():
#          dic[i] = i**3
#     return dic

# n = int(input("enter value of n: "))
# print(cube_finder(n))


user = {}
name = input("enter your name: ")
age = input("enter your age: ")
fav_movies = input("enter fav movies separated with comma: ").split(',')

user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
print(user)