# Reverse a string 

def reverse_str():

    list = "Hello world How are you"

    string = "".join(list.split()[::-1])

    print(string)

reverse_str()