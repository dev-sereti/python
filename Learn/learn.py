n = int(input())

if n % 2 == 1:  # If n is odd
    print("Weird")
else:  # If n is even
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:  # n > 20
        print("Not Weird")