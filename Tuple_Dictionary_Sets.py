"""
Week 2 - Data Structures Practice
Topics:
- Strings
- Lists
- Tuples
- Sets
- Dictionaries
"""
#TUPLES
a=[1,2,3,4]
a=tuple(a)
print(a)
b=tuple("Muskan")
print(b)
tup=( 1 , 98.2, "Muskan", False , [1,2,3,4])
print(tup)
print(tup[1:3])
print(tup[::-1])
w,x,y,z=a
print(w,x,y,z)
print(a + b)
del a 
print(len(tup))
print(tup.count(1))

#SETS
s=("Hellohi")
print(set(s))  # duplicate values are removed
s1=set([1,"hello",2.3])
print(s1)   # any order of the elements can be printed
#no indexing or slicing in sets
s1.add(4)
s1.update([5,6,7]) #to add multiple elements
print(s1)
for i in s1:
    print(i)
s1.remove(1)  # throws error if element is not present
print(s1)
s1.discard(2)  # no error if element is not present
print(s1)
s1.pop()  # removes a random element
print(s1)
f=frozenset([1,2,3,4,5]) # immutable set
print(f)
d={1:"Muskan",2:"hello" , 3: "world"}
print(set(d))  # only keys are printed
a=[1,2,6,1,4,2,1,8,9,6]
print(set(a))  
common=set(a).intersection(f)
print(common)

#DICTIONARIES
a=dict(name="Muskan", age="18",State="UP")
print(a)
print(a["age"])
print(a.get("age"))
print(a.keys())
a["age"]=19
print(a)
del a["State"]
print(a.popitem())  # removes last inserted item
d= {1:"Muskan",2:"hello" , 3: "world"}
for i in d:
    print(i)
for i in d.values():
    print(i)
for i in d.items():
    print(i)

dict={1:"Hello" , 2:{2.1:"world"} , 3:20}
print(dict[2][2.1])
d1={1:"Muskan",2:"hello" , 3: "world"}
d2={4:"Python",5:"Java"}
d1.update(d2)
print(d1)
student={"Name":"Muskan" , "Age":18 , "Marks":250,"Grade":"A"}
print(student.items())

marks={"Muskan":90,"Manshi":98,"Nimish":100,"Riya":99}
maxmarks = max(marks,key=marks.get)
print(maxmarks)
#OR
marks={"Muskan":90,"Manshi":98,"Nimish":100,"Riya":99}
max= -1 # as this score isn't possible
for i in marks.values():
    if i > max :
        max=i
print(max)

squares=[x**2 for x in range(1,11)]
print(squares)
no=[1,24,6,88,2,3,65,8,3,21,5,67,1029]
for i in no:
    if i%2==0:
        print(i)
for i in no:
    if i>50:
        print(f"{i} is greater than 50")