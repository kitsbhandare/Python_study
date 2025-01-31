#Lecture link:https://www.youtube.com/watch?v=jpqi_HRdpGA&list=PLxCzCOWd7aiEb4apyN1Y8mD-QuUTr3SPQ&index=47

'''
Function in Python
Functions help to organize code into logical blocks that perform specific tasks.
def function_name(parameters):
    """
    Docstring - brief description of the function.
    """
    # function body - statements that define what the function does.
    # the body can contain one or more statements.
    return value
'''

def f1():
    print("Hello")
f1()

def f2(name):
    print(name)
f2("Kiran")

def square(num):
    return num**2

num=int(input("Enter any number:"))
out=square(num)
print(f"square of {num} is {out}.")