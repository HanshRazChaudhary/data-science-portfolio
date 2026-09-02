name = "01234"
rev_str = ""

for i in range(len(name)):
    rev_str += name[-(i + 1)]
print(rev_str)


# Another Solution:
name = '01234'
rev_str = ''

for char in name:
    rev_str = char + rev_str

print(rev_str)