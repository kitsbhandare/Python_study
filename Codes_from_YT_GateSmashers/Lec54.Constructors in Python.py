#Lecture link:https://www.youtube.com/watch?v=RdhRAsItraI&list=PLxCzCOWd7aiEb4apyN1Y8mD-QuUTr3SPQ&index=63

'''
Constructors
• It is a special method within a class that gets automatically called when an object is created.
• It is used to initialize the attributes of the object.
• It is written with __init__
'''

class employee:
    def __init__(self):                                    #Method 1
        self.id=int(input("Enter employee id:"))
        self.name=input("Enter employee name:")
        self.salary=float(input("Enter employee salary:"))
    def display_data(self):                                #Method 2
        print("Employee id is",self.id)
        print("Employee name is",self.name)
        print("Employee salary is",self.salary)

a=employee()
a.display_data()

b=employee()
b.display_data()