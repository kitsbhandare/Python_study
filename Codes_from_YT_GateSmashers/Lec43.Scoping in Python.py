#Lecture link:https://www.youtube.com/watch?v=dPyalFo3YPw&list=PLxCzCOWd7aiEb4apyN1Y8mD-QuUTr3SPQ&index=51

'''
Scoping & Lifetime of a Variable
1) scope of a variable is the block of code in the entire program where the variable is declared, used, and can be modified.
2) Lifetime of a variable is the throughout time the variable exists in the memory.
3) variables get automatically destroyed ohen we return from function.
'''

#program 1
global_var="I am global variable"
def f1():
    local_var="I am lccal variable"
    print(global_var)
    print(local_var)
f1()
print(global_var)
#print(local_var)  #this will through NameError as its local variable cant use outside of function

#program 2
def f1():
    global local_var2 #local variable will act as global
    local_var2="I am lccal variable2"
    print(global_var)
    print(local_var2)
f1()
print(global_var)
print(local_var2)  #this will print successfully cz now local variable became global variable