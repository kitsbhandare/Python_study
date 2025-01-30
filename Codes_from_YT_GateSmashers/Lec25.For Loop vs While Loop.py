#Lecture link:https://www.youtube.com/watch?v=_Li18QM_9U4&list=PLxCzCOWd7aiEb4apyN1Y8mD-QuUTr3SPQ&index=30

'''
• A for loop is used to iterate over a sequence (such as a list, tuple, or string).
• Use for loop when you know exactly how many times you want to execute the loop.
• Example
        colors=["blue","black","green","grey"]
        for i in colors:
            print(i)
• A while loop is used to repeatedly execute a block of code as long as a certain condition is true.
• Use while loop when you don't know how many times you need to execute the loop beforehand.
• Example
        i = 1
        while i < 5:
            print(i)
            i += 1
'''

print("for loop ex1")
list1=['a',2,'b',4,'c',6]
for i in list1:
    print(i)

print("for loop ex2")
for r in range(1,6):
    print(r)

print("while loop ex1")
p=1
while p<8:
    print(p)
    p=p+1