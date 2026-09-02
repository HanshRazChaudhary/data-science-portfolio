passw = input("Enter Your Password To Check: ")

if (len(passw) < 6):
    out = 'Weak'
elif (len(passw) <= 10):
    out = 'Medium'
elif (len(passw) > 10):
    out = 'Strong'

print(f"Your Password Have {len(passw)} Character, Which Is {out}")