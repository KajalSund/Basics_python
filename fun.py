#function returing 2 values as tuple

def add(n1, n2):
    add = n1 + n2
    multiply = n1 * n2
    return add, multiply

print(add(3, 5))
add, multiply = add(3, 5) 
print(f"sum = {add}\n multiplication = {multiply}")

    