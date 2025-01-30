#Lecture link: https://www.youtube.com/watch?v=NXwpH79BUb4&list=PLxCzCOWd7aiEb4apyN1Y8mD-QuUTr3SPQ&index=18

'''
Membership Operator

These Operators used to test whether a specific value or item
is present within a sequence, such as a string, list, tuple, or set.
• There are 2 membership operators: 'in' & 'not in'
• Always return "True or False" as a output.
'''

list1=[10,20,30,40,50]
print(10 in list1)
print(11 in list1)
print(12 not in list1)

people=['kiran','dipak','jyoti','anagha','akira']
name=input("Enter your name:")
if name in people:
    print("Welcome! you are known person")
else:
    print("Sorry! you are not registered")