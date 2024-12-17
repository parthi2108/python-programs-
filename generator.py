def count_upto(max_val):
    count = 1

    while count <= max_val:
        yield count

        count += 1

counter = count_upto(10)


print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

