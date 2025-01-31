#Lecture link:https://www.youtube.com/watch?v=DZIiigDWF_M&list=PLxCzCOWd7aiEb4apyN1Y8mD-QuUTr3SPQ&index=70

'''
append => to add single element in list at last
extend => to add single or more than 1 element in list at last
add    => to add single element in set
update => o add single or more than 1 element in set
'''

mylist=[1,2,3]
mylist.append(4)
print(mylist)
mylist.append([5,6])
print(mylist)
mylist.extend([7,8,9])
print(mylist)

myset={10,20,30}
myset.add(40)
print(myset)
myset.update({40,50,60})
print(myset)