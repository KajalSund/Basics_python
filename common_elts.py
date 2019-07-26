def common(l1, l2):
    c = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                c.append(l1[i])
    return c

list1 = [1,2,5,6,4,9,7]
list2 = [3,8,5,9,10]
print(common(list1, list2))


# 2nd method to same 
def common_finder(l1,l2):
    c = []
    for i in l1:
        if i in l2:
            c.append(i)
    return c

print(common_finder(list1,list2))
