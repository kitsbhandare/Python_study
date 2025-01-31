#Lecture link:https://www.youtube.com/watch?v=uhvljGKWges&list=PLxCzCOWd7aiEb4apyN1Y8mD-QuUTr3SPQ&index=68

list1=[1,2,3,4,5,6,7]
print(list1)
new_list=[x-1 for x in list1]
print(new_list)

new_cube=[x**3 for x in range(10) if (x%2)==0]
print("cube of even numbers",new_cube)