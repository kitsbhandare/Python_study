#Lecture link:https://www.youtube.com/watch?v=uG4FD0SZ-cQ&list=PLxCzCOWd7aiEb4apyN1Y8mD-QuUTr3SPQ&index=74

#• Decorator is a function that takes another function as argument and returns a function.

'''
def decorator(func):
    def start():
        print("Starting task")
        func()
        print("Ending task")
    return start

def hello():
    print("Hello")

a=decorator(hello)
a()'''

def decorator(func):
    def start():
        print("Starting task")
        func()
        print("Ending task")
    return start

@decorator
def hello():
    print("Hello")

hello()