#Lecture link:https://www.youtube.com/watch?v=qs9VBwobK3w&list=PLxCzCOWd7aiEb4apyN1Y8mD-QuUTr3SPQ&index=75

list1=[1,2,3,4,5,6]
print(list1)
new_list=[x*2 for x in list1 if x%2==0]
print(new_list)

dict1={1:10,2:20,3:30,4:40}
print(dict1)
new_dict={i:i*2 for i in dict1 if i%2==0}
print(new_dict)

my_list=[x for x in range(20)]
print(my_list)

my_dict={x:x*2 for x in range(20)}
print(my_dict)
