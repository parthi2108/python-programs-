num = int(input("Enter the number:"))

divisors = [i for i in range(1, num+1) if num % i == 0]

print(divisors)