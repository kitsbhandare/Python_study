#Lecture link:https://www.youtube.com/watch?v=XIiwgc2uhhk&list=PLxCzCOWd7aiEb4apyN1Y8mD-QuUTr3SPQ&index=48

'''
File Handling in Python

File is used to store data permanently in Memory.
Operations on File:
1) Open a file
2) Read/Write
3) Close the file

• f1= open('abc.txt')
Opening a file
• File Modes(r, w, x, a, t, b, +)
1) 'r' means open a file in read mode.
2) 'w' means open a file in write mode (truncate). If file does not exist then create it.
3) 'x' means open a file for exclusive creation. If file already exists then operation fails.
4) 'a' means open a file in appending mode at the end of file without truncating. Create a new file if doesn't exists.
5) 'b' open in binary mode.
6) '+' open a file for updating.
'''

#read dile
f=open('filehandle.txt')
f.read()

#write file
f=open('filehandle.txt','w')
f.write("This is new file.")
f.close()
f=open('filehandle.txt')
f.read()

#append file
f=open('filehandle.txt','a')
f.write("\nthis is second line.")
f.close()
f=open('filehandle.txt')
f.read(10)