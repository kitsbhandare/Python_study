#Lecture link:https://www.youtube.com/watch?v=brnsFCa7npc&list=PLxCzCOWd7aiEb4apyN1Y8mD-QuUTr3SPQ&index=28

'''
Dictionary in Python

• It is a data structure which is similar to Hash table.
• It is an unordered collection of items.
• A dictionary has key value pairs and is mutable in nature.
>dic1={}
>dict2= {1: 'varun', 2: 'ravi', 3: 'nitin'}
>print(dict2)
The key should be unique and must be an immutable object like a number, strings, and tuples.
'''

dict1={}
print(dict1)

dict2={1:'kiran',2:200,3:'dipak','third':('a','b','c')}
print(dict2)
print(dict2.get(1))
print(dict2[2])
print(dict2['third'])
