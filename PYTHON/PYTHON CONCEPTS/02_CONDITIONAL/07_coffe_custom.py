size = input("Enter The Size Of Coffee Cup: ").capitalize()
shot = input("Do You Want Extra Shot Of Expresson: ").capitalize()

if (shot == 'Yes'):
    print(f"Collect Your Order From The Counter, {size} Size Of Latte With Extra Shot Of Expresso.")
else:
    print(f"Collect Your Order From The Counter, {size} Size Of Latte.")