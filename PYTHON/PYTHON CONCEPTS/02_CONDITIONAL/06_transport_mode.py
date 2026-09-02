km = int(input("Enter The Distance:"))

if (km < 3):
    mod = 'Walk'
elif (km <= 15):
    mod = 'Bike'
elif (km > 15):
    mod = 'Car'

print(f"Distance Is {km} Km, So Take A {mod}")