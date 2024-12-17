num = [1,2,3,4,6,7,9,10,13]

new_num = set(num)

next_num = set(range(1,14))

missing = next_num - new_num

print(missing)