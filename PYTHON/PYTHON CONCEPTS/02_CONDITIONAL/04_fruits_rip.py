fruits = input("Enter Fruits Name: ").capitalize()

if (fruits == 'Banana'):
    color = input("Enter The Color: ").capitalize()
    if (color == 'Green'):
        print("Unripe")
    elif(color == "Yellow"):
        print("Ripe")
    elif (color == "Brown"):
        print("Overripe")
    else:
        print("Try Again!")
else:
    print("Try Again Some Other Time For", fruits)