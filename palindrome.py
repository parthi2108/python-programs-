# def palindrome(string):

#     reversed_string = string[::-1]

#     return reversed_string == string

# word = input("Enter a word: ")

# if palindrome(word):
#     print("is a palindrome")
# else:
#     print("Not a palindrome")




phrase = "python is fun"

reversed_phrase = "".join(phrase.split()[::-1])

print(reversed_phrase)