specie = input("Is Your Pet Dog Or A Cat: ").capitalize()

if (specie == 'Dog'):
    age = int(input("Enter The Age Of The Dog: "))
    if (age < 2):
        food = "Puppy Food"
    else:
        food = "Senior Dog Food"
    print(f"You Have A {age} Years Old {specie} So, I Reccomend You {food}")


if (specie == 'Cat'):
    age = int(input("Enter The Age Of The Cat: "))
    if (age < 2):
        food = "Kitten Food"
    else:
        food = "Senior Cat Food"
    print(f"You Have A {age} Years Old {specie} So, I Reccomend You {food} For Your Pet.")

