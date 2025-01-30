#Lecture link:https://www.youtube.com/watch?v=jfV5BnUPD6I&list=PLxCzCOWd7aiEb4apyN1Y8mD-QuUTr3SPQ&index=16

'''
Identity Operator
• These Operators used to check whether two objects are of
same type or not & they share same memory location or not.
• There are 2 Identity operators: 'is' & 'is not'
• Always return "True or False" as a output.
'''

x=100
y=100
print(x is y) #'is' is checking variables location not value ('==' will check values)
z=x
print(z is x)
