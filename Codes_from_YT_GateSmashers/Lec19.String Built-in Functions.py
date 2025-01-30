#Lecture link:https://www.youtube.com/watch?v=9qqIn9OnPTg&list=PLxCzCOWd7aiEb4apyN1Y8mD-QuUTr3SPQ&index=24

name="kiran hanumant bhandare"
print(len(name))
print(name.title()) #only first letter in upper case
print(name.upper())
print(name.lower())
print(name[1:4])
print(name.count('ant')) #how many time 'ant' string came in name
print(name.find('ant')) #It will find index of mentioned string
print(name.find('xyz')) #finding non existing string will return -1
#print(name.index('xyz')) #finding non existing string will ValueError

print(name.endswith('e')) #true
print(name.endswith('x')) #false
print(name.startswith('k')) #true
print(name.startswith('x')) #true
print(name.isalnum()) #False as in given string alphanumeric or numbers or spacees are present

print(name.replace('k','*'))
print(name.split())