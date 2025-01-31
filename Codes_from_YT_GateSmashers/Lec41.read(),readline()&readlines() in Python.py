#Lecture link:https://www.youtube.com/watch?v=5xEUDOA5PJA&list=PLxCzCOWd7aiEb4apyN1Y8mD-QuUTr3SPQ&index=49

#read options
f=open('filehandle.txt')
print(f.read(10)) #it will read only first 10 elements and print
print(f.read(10)) #it will read only second 10 elements and print
print(f.tell())   #tell the current position of pointer
f.seek(0) #we can change pointer position
print(f.tell())
print(f.read(10))

#read all line
f.seek(0)
for line in f:
    print(line)

#read particular line
f=open('filehandle.txt')
#print(f.readline()) #it will read first line
#print(f.readline()) #it will read second line
print(f.readlines()) #it will read all lines