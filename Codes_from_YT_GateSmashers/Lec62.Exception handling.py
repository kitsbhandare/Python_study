'''
try, except, else and finally Blocks
try Block:       try block lets us test a block of code for errors. Python will “try” to execute the code in this block.
If an exception occurs, execution will immediately jump to the except block.
except Block:    except block enables us to handle the error or exception.
If the code inside the try block throws an error, Python jumps to the except block and executes it.
We can handle specific exceptions or use a general except to catch all exceptions.
else Block:      else block is optional and if included, must follow all except blocks.
The else block runs only if no exceptions are raised in the try block. This is useful for code that should execute if the try block succeeds.
finally Block:    finally block always runs, regardless of whether an exception occurred or not.
It is typically used for cleanup operations (closing files, releasing resources).
'''

#example2
try:
    a=10/2
    #print(a)
except ZeroDivisionError:
    print("You can't divide by zero")
else:
    print("Outpur is:",a)
finally:
    print("This ia a end of program")

#example2
try:
    b=10/2
    assert b==4,"This is an error"
except AssertionError:
    print("This is wrong answer")
else:
    print("Outpur is:",b)
finally:
    print("This is end of program")
