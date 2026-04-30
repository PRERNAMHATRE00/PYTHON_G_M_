'''
# int
age = 40
print(age)
#float
pie_ = 3.14
print(pie_)
# string 
name= "Suga"
print(name)
#boolean
is_adult= True
print(is_adult)
#list
list1=[100,200,300]
print(list1)
print(type(list1))
#dictionary
dict1={'name':'Suga','age':32,}
print(dict1)
print(dict1['age'])
#tuple
tup=(20,30,40)
print(tup)
#set
set1={1,2,3,4,5}
print(set1)
#none
sibling= None
print(sibling)
#complex
com = 1+2j
print(com)
#range
num = range(0,5)
print(num)
print(type(num))
#byte & bytearray
byte= bytes([65,66,97])
print(byte)
byte1= bytearray([65,66,97])
print(byte1)


40
3.14
Suga
True
[100, 200, 300]
<class 'list'>
{'name': 'Suga', 'age': 32}
32
(20, 30, 40)
{1, 2, 3, 4, 5}
None
(1+2j)
range(0, 5)
<class 'range'>
b'ABa'
bytearray(b'ABa')


name="bunny"
name[3]="r"
print(name)

#  name[3]="r"
   # ~~~~^^^
#TypeError: 'str' object does not support item assignment

#list
list_1=["red",'green','white']
print(list_1)
list_1[2]= "black"
print(list_1)

['red', 'green', 'white']
['red', 'green', 'black']

///////////////////
list_1=["red",'green','white']
print(list_1)
list_1.append( "black")
print(list_1)
['red', 'green', 'white']
['red', 'green', 'white', 'black']
////////////////////

#tuple
tup1=("rice","wheat")
print(tup1)
tup1[1]="jowar"
print(tup1)
, line 84, in <module>
    tup1[1]="jowar"
    ~~~~^^^
TypeError: 'tuple' object does not support item assignment


#set
set1={1,2,3,5,3,}
print(set1)
#{1, 2, 3, 5}
set1.add(4)
print(set1)
#{1, 2, 3, 4, 5}

#dictionary
disc1={'name':"James","age":30,"country":"USA"}
print(disc1)
disc1["country"]="Europe"
print(disc1)
{'name': 'James', 'age': 30, 'country': 'USA'}
{'name': 'James', 'age': 30, 'country': 'Europe'}


set1={2,  4,3,7,5}
print(set1) #{2, 3, 4, 5, 7}


set1={"b","d",'a'}
print(set1)
{'b', 'a', 'd'}

{'a', 'b', 'd'}

{'b', 'a', 'd'}

What you put in set	Order behavior
Small integers (like 1,2,3,4,5)	✅ Always in order
Anything else (words, letters, big numbers)	❌ Random/Weird order
'''