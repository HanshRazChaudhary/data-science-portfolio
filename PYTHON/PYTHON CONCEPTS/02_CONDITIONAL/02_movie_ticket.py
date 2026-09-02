age = int(input("Enter Your Age: "))
day = "Sunday"

if (age > 17):
    if (day == "Wednesday"):
        print("Ticket Price Is: $10")
    else:
        print("Ticket Price Is: $12")
else:
    if (day == "Wednesday"):
        print("Ticket Price Is: $6")
    else:
        print("Ticket Price Is: $8")