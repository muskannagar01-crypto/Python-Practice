"""
Week 2 - Data Structures Practice
Topics:
- Strings
- Lists
- Tuples
- Sets
- Dictionaries
-Exception Handling
-File Handling
"""
#FILE HANDLING
# open
f=open("random.txt","r")
print(f)
print("filename:",f.name)
print("mode:",f.mode)
print("Is it closed?",f.closed)
#close
f.close()
print("Is it closed?",f.closed)
#read
f1=open("random.txt","r")
text=f1.read()
print(text)
f1.close()
#with open
with open ("random.txt","w") as file:    #using with open functions closes the file itself
    file.write("Hello, Python.\n")
    file.write("File handling programs.")
print("File written.")
file = open("random.txt")   #have to write again
text=file.read()
print(text)
#exception handling
try:
    file=open("hi.txt","r")
    content=file.read()
    print(content)
except FileNotFoundError as error:
    print("Error:",error)
finally:
    file.close()
#append
lines=["\nLINE 1","\nLINE 2","\nLINE 3"]
with open("random.txt","a") as f:
    f.write("\nNew line added.")
    f.writelines(lines)
# append + read  
with open("random.txt","a+") as f:
    f.write("\nHI")
    f.seek(0)
    file=f.read()
    print(file)

#copy one file to another
f1=open("sample.txt","r")
f2=open("random.txt","a")
for lines in f1:
    f2.write(lines)
#OR
with open("sample.txt","r") as a , open("random.txt","a") as b:
    for i in a:
        b.write(i)
# count lines
with open("sample.txt") as f:
    lines=len(f.readlines())
    print(lines)
#count only lines with text
with open("sample.txt") as f:
    lines=sum(1 for line in f)
    f.seek(0)
    non_blanklines = sum(1 for line in f if line.strip())
print(lines)
print(non_blanklines)
#count words
with open("sample.txt") as f:
    words=sum(len(line.split()) for line in f)
print(words)