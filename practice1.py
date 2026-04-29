my_set={5,2,8,2,1}
print(my_set) # 1,2,5,8

tup=(10,20,30)
tup[0]=90 # error

'''
Which data types are mutable
list, dictionary ,set

wrong variable 
2pac = "rapper"  - variable name cant start with number it can start with chartacter or underscore

 What will bool(input("Enter: ")) return if user presses Enter without typing anything  - False

 set1 = {"apple", "banana", "cherry"}
print(set1)  # Order changes sometimes! - because set is unordered 

 What's the difference between bytes and bytearra
 byte is immutable cant modify
 bytearray is mutable can odify 

 _hello123 = "test" - yes because it follow protocols of variable, that is it can start either with indercore or charcter 

 Why does {1,2,3} print in order but {"a","b","c"} prints randomly - bescause set only arrange number data in order that is in ascending while rest of data type whether it be str, charcter it arrrnage them randomly because its unordered 

 Can a dictionary have duplicate keys? Duplicate values - it can have duplicate values but not keys because keys are unique

 list1 = [1, 2, 3] - list is initilize in square brackets and is mutable
tuple1 = (1, 2, 3) - tuple is initilize in round bracket is immutable


'''

num= input("enter age : ")
print(num + 5)

num1= int(input("enter age = "))
print(num1 + 5)

value = None
print(type(value)) # special None

a=10
A=5
print(a+A) #15


set_1={1,2,3,4,5}
set_1.add(6)
set_1.remove(3)
print(set_1)

#{1,2,4,5,6}

disc1 = {"name":"James", "age":30}
print(disc1["age"])
"age"
30
James
TypeError
✓ Correct! Dictionaries use keys to access values. disc1["age"] returns the value 30.

Which variable name is INVALID in Python?
_var1
var_1
1var
deff
✓ Correct! Variable names CANNOT start with a number. 1var is invalid — Python says 'invalid decimal literal'.

What will input() always return, even if you type a number?
int
float
str
bool
✓ Correct! input() always returns a string (str). That's why you need int(input()) or float(input()) to do math.

tup = (20, 30, 40)
tup[1] = 99
print(tup)
(20, 99, 40)
(20, 30, 40)
TypeError
SyntaxError
✓ Correct! Tuples are IMMUTABLE. You cannot change any item. Python throws TypeError.
byte = bytes([65, 66, 97])
print(byte)
[65, 66, 97]
b'ABa'
(65, 66, 97)
ABa
✓ Correct! 65=A, 66=B, 97=a in ASCII. bytes() shows them as b'ABa'.
What is the difference between bytes and bytearray?
bytes is faster, bytearray is slower — both mutable
bytes is immutable (can't change), bytearray is mutable (can change)
They are exactly the same
bytes stores text, bytearray stores numbers
✓ Correct! bytes = locked (immutable). bytearray = editable (mutable). Like a printed photo vs Photoshop.
a = 11
A = 32
print(a)
print(A)
32 then 11
11 then 32
Error — a and A are same
11 then 11
✓ Correct! Python is CASE SENSITIVE. 'a' and 'A' are two completely different variables.
You want to store a person's latitude and longitude that should NEVER change. Which type is best?
List
Dictionary
Tuple
Set
✓ Correct! Tuple is perfect for fixed data like coordinates. It's immutable and faster than a list.
What will bool(input()) return if you press Enter without typing anything?
True
False
None
Error
✓ Correct! Empty string is falsy in Python. bool('') = False. You saw this in your own output today!
What will this print?
name = "bunny"
name[3] = "r"
print(name)
"bunry"
"bunny"
TypeError
SyntaxError
✓ Correct! Strings are IMMUTABLE — you cannot change individual characters. Python throws a TypeError.
Which data types are MUTABLE (changeable)?
String, Tuple, int
List, Set, Dictionary
Tuple, bytes, range
int, float, bool
✓ Correct! List, Set, and Dictionary are all mutable — you can add, remove, or change their values.
What will this print?
set1 = {1, 2, 3, 5, 3}
print(set1)
{1, 2, 3, 5, 3}
{1, 2, 3, 5}
{3, 5, 1, 2}
Error
✓ Correct! Sets automatically remove duplicates. So 3 appears only once. Output: {1, 2, 3, 5}

