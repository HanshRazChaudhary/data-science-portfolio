score = int(input("Enter Your Score: "))

if score >= 101:
    print("Enter Valid Score")
else:
    if (score >= 90):
        print("Your Grade Is 'A'")
    elif (score >= 80):
        print("Your Grade Is 'B'")
    elif (score >= 70 ):
        print("Your Grade Is 'C'")
    elif (score >= 60):
        print("Your Grade Is 'D'")
    else:
        print("Your Are Fail")