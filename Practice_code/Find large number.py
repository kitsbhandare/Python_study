mylist=[1,400,20,37,22]

#find large number from list
large_num=mylist[0]
for i in mylist:
    if large_num < i:
        large_num = i
print("Large number is:",large_num)

#find large number from list
small_num=mylist[0]
for j in mylist:
    if small_num > j:
        small_num = j
print("Small number is:",small_num)