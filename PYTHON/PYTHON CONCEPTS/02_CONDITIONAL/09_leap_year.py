year = int(input("Enter A Year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Yes! Year {year} Is A Leap Year")
else:
    print(f"No! Year {year} Is Not A Leap Year")