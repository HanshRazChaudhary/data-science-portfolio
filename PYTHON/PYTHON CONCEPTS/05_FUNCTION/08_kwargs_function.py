def print_mul_string(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_mul_string(name = "Motu", friends = "Patlu")