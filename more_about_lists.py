# # # #generate list from range function
# # # numbers = list(range(1, 13))

# # # print(numbers)

# # # #bydefault last number poped
# # # #or specific index given as argument
# # # pop = numbers.pop()
# # # print(numbers)

# # # #index method used to display index of number
# # # #list.index(number, start, end)
# # # print(numbers.index(3))

# # # #pass list to a fuction
# # # def negative_list(l):
# # #     negative = []
# # #     for i in l:
# # #         negative.append(-i)
# # #     return negative

# # # print(negative_list(numbers)) 
   
# # #def func that takes list and returns square of that list
# # def square(l):
# #     s_list = []
# #     for i in l:
# #         s_list.append(i ** 2)
# #     return s_list

# # list = [5,8,9,7,6,4,3]

# # print(list)

# # print(square(list))


# #reverse of list
# def r_list(l):
#     reverse = []
#     for i in range(len(l)):
#         reverse.append(l.pop())
#     return reverse

# list = [1,2,3,4,5,6]
# print(list)
# print(r_list(list))

# min and max functions
num = [200,6666,59]
print(min(num))
print(max(num))


#function to find greatest difference
def greatest_diff(n):
    return max(n) - min(n)

print(greatest_diff(num))