# def is_even(num):
#     if num%2 == 0:
#         return True
#     return False


# n = int(input("enter any number "))
# print(is_even(n))  

# #greater num

# def greater(num1, num2):
#     if num1 > num2:
#         return num1
#     elif num2 > num1:
#         return num2
#     else:
#         print("both are equal")

# n1 = int(input("enter number 1: "))
# n2 = int(input("enter number 2: "))
# print(greater(n1, n2))



def greater(a, b):
    if a > b:
        return a
    return b

def greatest(a, b, c):
    bigger = greater(a, b)
    return greater(bigger, c)

print(greatest(12,300,44))    