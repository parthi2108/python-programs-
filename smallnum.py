numbers = [1,2,3,4,5,12,3,4,44,55,67,89,123,34]

for num in numbers :
    if num > 10:
        print(num)

less_than = [num for num in numbers if num>10 ]

print(less_than)