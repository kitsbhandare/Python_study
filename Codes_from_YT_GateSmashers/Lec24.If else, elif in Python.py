#Lecture link:https://www.youtube.com/watch?v=9xiFcK3MRYA&list=PLxCzCOWd7aiEb4apyN1Y8mD-QuUTr3SPQ&index=29

'''
In Python, there are four forms of the if...else statement.
if statement
if...else statement
if...elif...else statement
nested if
'''

#if statement
age=int(input("Enter you age:"))
if age>18:
    print("You are elgible for license")
print("This is out of if block")

#if...else statement
agge=int(input("Enter you age:"))
if agge>18:
    print("You are ready to go")
else:
    print("Grow fast")

#if...elif...else statement
agee=int(input("Enter your age:"))
salary=float(input("Enter your salary:"))

if  agee>18 and salary>=25000:
    print("Rich person")
elif agee<=18 and salary>=25000:
    print("Rich boy")
elif agee>18 and salary<25000:
    print("Poor person")
else:
    print('Poor boy')

#nested if
new_age=19
own_car=False
if new_age>18:
    if own_car==True:
        print("You are eligible for license.")
    else:
        print("Elgible but You dont have own car.")
else:
    print("Badhe ho jao")