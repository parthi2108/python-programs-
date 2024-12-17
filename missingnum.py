numbers = [ 1,2,3,4,5,6]

full_range = set(range(1,15))

numbers_set = set(numbers)

missing = full_range - numbers_set

print(missing)  