# # Natural numbers 

# i = 1 

# while i < 10:
    
#     print(i)
          
#     i += 1

# for i in range(1,11):
#     print(i)


# Even number and odd numbers 
# for i in range (1,20):
#     if i % 2 == 0:
#         print(i,"Is a Even numbers")
#     else:
#         print(i,"Is a Odd Numbers")


# sum of numbers 
# num = int(input("Enter the number: "))

# sum = (num*(num+1))/2

# print(sum)

# num = 5

# for i in range (1,10):
#     print(num,"x",i,'=', num*i )

# printing numbers in lists

# num = [1,2,3,4,5,6,7,8,9]

# for i in num:

#     print(i)

# for loop 

# fruits = ["apple","mango","peach"]

# for x in fruits :
#     print(x,"")

# for x in "banana":
#     print(x,"")
# 
# fruits = ["apple","mango","banana","peach"]

# for x in fruits :

#     if x == "banana":
#         continue
#     print(x)
       
# for x in range (10):

#     if x == 5: break
#     print(x)
# else:
#      print("end")

# fruits = ["apple","banana","cherry","plums"]
# veg = ["carrot","beetroot","cabbage","potato"]
# flower = ["jasmine","rose","marigold","sunflower"]
# for x in fruits:
#     for y in veg:
#         for z in flower:

#         print("Eat the :",(x,y,z))

# def my_def(*kids):
#     print("The youngest child is :" + kids[1]) #the kids name is called by order number in this method 

# my_def("hole","die","busty","rabbit")
          
        
# def my_def(kid1, kid2, kid3):
#     print("The youngest child is :" + kid2) 
# my_def(kid1 = "hole", kid2 = "die", kid3 = "busty")
         
# a = ("best thubfs ate firee ")

# print("expensive" in a)


# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"person(name:{self.name}, age:{self.age})"
    
#     def __repr__(self):
#         return f"person:{self.name},{self.age}"
    
# p = person("dumbo", 4)

# print (str(p)) 
# print (repr(p))

# a = [1,2,3,4,5,5,6,6,7,7,8,8]

# a = list(set(a))

# print (a)

# word = input("enter the phrase: ")

# reversed_string = word[::-1]

# print(reversed_string)

# numb = [ 1,1,2,2,3,3,4,4,5,5,6,6,7,7]

# numb = list(set(numb))

# print(numb)


# a=25
# def first():
#     prefix = "value of 'a' is"
#     print(f'{prefix},{a}')

# first()

# a = [1,4,2,3,4,5,5,6,7,7]

# b = [2,3,4,5,6,7,8,7]

# common = [x for x in a if x in b]

# print(common)

# import random

# def random_number():
#     random_num = random.randint(1,10)

#     attempts = 0

#     while True:
#         try:
#             guess = int(input())
#             attempt = 1

#             if guess < random_num :
#                 print("low")

#             elif guess > random_num:
#                 print("high")

#             else:
#                 print("invalid")

#             break

#         except ValueError:
#             print("error")

# random_number()

# a = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7]

# a = list(set(a))

# print(a)

# num = int(input("enter the num"))

# sum = (num*(num+1)/2)

# print(sum)

# def min_num(array):
#     minimum_num = array[0]
#     for num in array :
#         if num < minimum_num:
#             minimum_num = num
#         return min_num
        
# numbers = [ 1,2,3,4,5,6,7,8]

# minimum_num = min_num(numbers)

# print(minimum_num)

# num = [1,2,3,4,5,6,7,8]


# reversed = num[::-1]

# print(reversed)


def factorial(n):

    if n==0 :
        return 1
    
    else:
        return n*factorial(n-1)
    
num = int(input())

result = factorial(num) 

print(result)

    
    
