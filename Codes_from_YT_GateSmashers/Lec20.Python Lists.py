#Lecture link: https://www.youtube.com/watch?v=Icw4cLTtKh4&list=PLxCzCOWd7aiEb4apyN1Y8mD-QuUTr3SPQ&index=25

'''
List in Python
• The data type list is an ordered sequence that is mutable and made up of one or more elements.
• A list can have elements of different data types, such as integer, float, string, tuple or even another list.
• A list is very useful to group together elements of mixed data types.
• Elements of a list are enclosed in square brackets and are separated by a comma.
• List indices also start from 0.
'''

list1=[100,100.002,"xyz"]
print(list1)
list1[1]=200.002
print(list1)
print(list1[2])

list2=[['ram',1990],["shyam",1991],['rahul',1992]]
print(list2)
print(list2[1])
print(list2[-1]) #last index element