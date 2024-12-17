# def unique_num():

#     array = [1, 2, 3, 2, 4, 1, 5]

#     unique_list = list(set(array))

#     print(unique_list)

# unique_num()



# uni = [1,1,2,2,3,3,4,4,5]

# numb = (len(set(uni)))

# print(numb)

list_a = set([1, 2, 3])
list_b = set([3, 4, 5])

previ = dict(list_a & list_b) 

print(previ)