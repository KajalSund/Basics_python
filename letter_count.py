name = input("enter your name ")
len = len(name)
i = 0
tem_var = ""
while  i < len:
    if name[i] not in tem_var:
        print(f"{name[i]} : {name.count(name[i])}")
        tem_var += name[i]
    i += 1        