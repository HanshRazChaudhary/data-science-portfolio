num = int(input("Enter Any Number: "))
sum_even = 0

for n in range(num + 1):
    if (n % 2 == 0):
        sum_even += n
print(sum_even)