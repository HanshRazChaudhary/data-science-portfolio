# Even Generator:
def even_generator(limit):
    for lim in range(2, limit + 1, 2):
        yield lim

for num in even_generator(10):
    print(num)