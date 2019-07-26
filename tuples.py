#tuple data structure
#tuple can store any data type
#most important tuples are immutable, once tuple is created you can't update
#data inside tuple

tuple = ('one', 'two', 'three')
#no append, no insert, no pop, no remove
days = ('monday', 'tuesday')
#tuples are faster than lists

#methods
#count, index 
#len function

#slicing
print(tuple[:2])
#assignment error
#tuple[2] = 1   #error

#looping in tuples
mixed = (1,2,3,4,5.6)
for i in mixed:
    print(i)

#tuple with one element
num = (1,)
print(type(num))

#tuple without parenthesis
fruit = 'apple', 'banana', 'orange', 'dates', 'guava'
print(type(fruit))

# tuple unpacking
t = ('abc', 'jssfsf', 'fhwiuh', 'vbdjh')
t1, t2, t3, t4 = (t)
print(t2)

#list inside tuples
t = ('skf', 'ewrr', ['wwf', 'egeg'])
t[2].pop()
t[2].append('jdjbn')
print(t)

#tuple using range function

num = range(1,31)
for i in num:
    print(i)
print(num)

#min(), max(), len(), sum()

print(min(num))
print(max(num))
print(len(num))
print(sum(num))

#convert to str
num = str((1,2))
print(type(num))