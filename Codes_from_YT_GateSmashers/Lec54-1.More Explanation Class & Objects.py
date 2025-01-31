#Lecture link:https://www.youtube.com/watch?v=D0bgKfJFdeI&list=PLxCzCOWd7aiEb4apyN1Y8mD-QuUTr3SPQ&index=62

class employee:
    def __init__(self,emp_id,emp_name,emp_salary):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary=emp_salary

    def display_data(self):
        print("Employee id is:",self.emp_id)
        print("Employee name is:",self.emp_name)
        print("Employee salary is:",self.emp_salary)

a=employee(1,'Kiran',2000)
#print(a.emp_id)
#print(a.emp_name)
#print(a.emp_salary)
a.display_data()

b=employee(2,'Anagha',3000)
b.display_data()
