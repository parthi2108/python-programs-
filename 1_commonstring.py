def common_letter():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    s1 = set(str1)
    s2 = set(str2)

    lst = s1&s2

    print(lst)

common_letter()
