n = int(input("number between 1, 100:  "))

count = 1
i = int(input("guess number "))
while i != n:
    i = int(input("guess number "))
    if i < n:
        print("number is too low try again ")
        count += 1
        continue
    elif i > n:
        print("number is too large try again ")
        count += 1
        continue
    else:
        print(f"you win..... and you tried {count} times")
        break
        