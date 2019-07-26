def sublist_count(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count


list1 = [1,2,3, [1,2], [6,7]]
print(sublist_count(list1))

