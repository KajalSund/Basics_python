def list_o_e(l):
    odd = []
    even = []
    for i in l:
        if i % 2 == 0:
            odd.append(i)
        else:
            even.append(i)
    return odd, even
list = [1,2,3,4,5,6,7,8,9]
print(list)            
print(list_o_e(list))