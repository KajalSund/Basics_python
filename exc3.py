name, c = input("enter your name and a single charater and separated by comma").split(",")
print(f"hello {name} length of your name is {len(name)}")
name.lower()
c.lower()
count = name.count(c)
print(count)