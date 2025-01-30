#Lecture link:https://www.youtube.com/watch?v=8d8bmm4qPro&list=PLxCzCOWd7aiEb4apyN1Y8mD-QuUTr3SPQ&index=32

'''
break, continue & pass keywords
• break, continue & pass are used to control the flow of loops in python.
• 'break'      statement is used to exit a loop prematurely when a specific condition is met.
• 'continue'   statement is used to skip the current iteration of a loop when a specific condition is met, and it continues with the next iteration of the loop.
• 'pass'       statement is a no-op statement in Python, meaning it does nothing when executed.
'''

print("break statement")
mylist=[1,2,3,4,5,6,7,8,]
for x in mylist:
    if x==5:
        break
    print(x)

print("continue statement")
for y in mylist:
    if y==5:
        continue
    print(y)

print("pass statement")
for z in mylist:
    if z==5:
        pass
    print(z)

print("break statement2")
items=[1,2,3,4,5,6,7,8,9]
target=4
for item in items:
    if item==4:
        print("target found:",item)
        break
