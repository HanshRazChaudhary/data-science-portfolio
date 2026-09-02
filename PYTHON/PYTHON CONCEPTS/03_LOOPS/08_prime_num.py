num = 6
is_prime = True

if num > 1:
    for n in range(2, num):
        if (num % n ) == 0:
            is_prime = False
            break
print(is_prime)