number = int(input("Enter Any Number: "))

for num in range(11):
    if num == 5:
        continue
    print(f"{number} X {num} = {num * number}")