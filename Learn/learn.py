#Python *args and **kwargs

def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))
#print(sum_all(10, 20, 30, 40))