#Lecture link: https://www.youtube.com/watch?v=M-JKYzxgHCo&list=PLxCzCOWd7aiEb4apyN1Y8mD-QuUTr3SPQ&index=13

'''
Logical Operator

• In Python, logical operators are used to combine multiple conditions or
expressions and produce a Boolean result.
• There are three logical operators in Python.
• and:    It returns True if both the operands are True, otherwise it returns False.
• or:     It returns True if at least one of the operands is True, otherwise it returns False
• not:    It returns the opposite Boolean value of the operand. If the operand is
True, it returns False, and if the operand is False, it returns True.
'''

age=30
salary=25000
if age>20 and salary<22000:
    print("Eligible")
else:
    print("Not eligible")

age=30
salary=25000
if age>20 or salary<22000:
    print("Eligible")
else:
    print("Not eligible")