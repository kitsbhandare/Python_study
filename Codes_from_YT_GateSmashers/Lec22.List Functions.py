#Lecture link:https://www.youtube.com/watch?v=cS_4YJx5KvU&list=PLxCzCOWd7aiEb4apyN1Y8mD-QuUTr3SPQ&index=27

list1=['k','i','r',4,5]
print(len(list1))

list2=list(()) #empty list
print(list2)
name="Kiran"
list2=list(name)
print(list2)
list2.append(100) #will add only one element
print(list2)
list2.append([200,'now']) #appending single list element
print(list2)
list2.extend([300,400,500,222,222]) #it will add more one or more than one elements at last
print(list2)
list2.insert(6,'inserted') #will add element in any index
print(list2)
a=list2.count(222)  #it will count the occurance of element from list
print(a)
b=list2.index(222)  #it will print the index of given element
print(b)
list2.remove(500)
print(list2)
list2.pop(9)  #remive element using its index
print(list2)
list2.reverse()
print(list2)


list3=list(('kiran','manas','jyoti','zulan','prem','balu'))
list3.sort()
print(list3)

list4=[10,34,2,56,666,74,1345,33,566]
z1=min(list4)
z2=max(list4)
z3=sum(list4)
print(z1,z2,z3)
print(min(list4),max(list4),sum(list4))