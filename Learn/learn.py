#Python Recursion

def even_numbers(num):
    if num%2 == 1:
        return num+1
    else:
        return num
x = [44,56,53,22,123,45,67,8,89,87,56]

y = list(map(even_numbers,x))
print(y)
    