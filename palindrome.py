def palindrome(s):
    reverse = s[: : -1]
    if s == reverse:
        return True
    return False

s = input("enter any string  ")
print(palindrome(s))