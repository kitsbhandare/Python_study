#Lecture link:https://www.youtube.com/watch?v=DBWde9iWBLw&list=PLxCzCOWd7aiEb4apyN1Y8mD-QuUTr3SPQ&index=61

class employee:
    def put_data(self):                                    #Method 1
        self.id=int(input("Enter employee id:"))
        self.name=input("Enter employee name:")
        self.salary=float(input("Enter employee salary:"))
    def display_data(self):                                #Method 2
        print("Employee id is",self.id)
        print("Employee name is",self.name)
        print("Employee salary is",self.salary)

a=employee()
a.put_data()
a.display_data()

b=employee()
b.put_data()
b.display_data()
