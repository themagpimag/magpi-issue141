def add_numbers(*args):
    total = 0
    for number in args:
        total += number
    return total

print(add_numbers(1, 2, 3))  # 6
print(add_numbers(1, 2, 3, 4, 5))  # 15
