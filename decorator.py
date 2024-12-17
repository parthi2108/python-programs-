
def my_decorator(func):
    def wrapper():
        print("keep learning")
        func()
        print("practice python")
    return wrapper()

@my_decorator
def learn_python():
    print("Iam learing python")

learn_python



