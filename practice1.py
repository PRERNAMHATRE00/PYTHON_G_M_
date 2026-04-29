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

What is the output?
pythona = 11
A = 32
print(a) # 11

Which ones are mutable? — string, list, tuple, set, dict, bytes, bytearray 
list , dict,set

. What error does this give and why?
python"5" + 5  # typerror

What does input() always return - str by default 

What is wrong here?
pythondef = 10
def is keyword so TypeError XX
def = 10 → ❌ SMALL CORRECTION
You said "TypeError" but it's actually SyntaxError
Reason: def is a keyword (used for functions), can't be variable name

What will this print?
pythonset1 = {3, 1, 2, 3, 5, 2}
print(set1)
# {1,2,3,5}

Difference between bytes and bytearray in one line
bytes - immutable 
bytearray - mutable

 What error and why?
pythontup = (10, 20, 30)
tup[0] = 99 # typerror

What does this print?
pythonprint(bool("")) # False
print(bool("hello"))# True

What is the output?
pythonnum = int(input("Enter: "))  # user types 7
num = num + 5
print(num)  # typerror since str + int no possible




///////////////////////////////////


**SyntaxError vs TypeError**

**SyntaxError** = Wrong spelling/grammar of code. Python reads your code top to bottom before running — if it sees something broken, it stops immediately and never even starts.

Like a teacher refusing to read your essay because your first sentence makes zero sense.

```python
1var = 4    # SyntaxError — can't start with number
def = 7     # SyntaxError — def is Python's word, not yours
```

**TypeError** = Code is written correctly, but you're doing something *impossible*. Python starts running, reaches that line, and says "wait... this doesn't make sense."

Like writing a perfect sentence but asking "add the word 'hello' plus the number 5" — grammatically fine, logically impossible.

```python
"11" + 1    # TypeError — string + number = impossible
name[0] = "x"  # TypeError — strings can't be changed
```

One line summary: **Syntax = bad writing. Type = bad action.**

---

**Why `b` in front of `b'ABa'`**

Python has two kinds of "text looking things":

`"ABa"` → normal string, made for humans, stores words and sentences.

`b"ABa"` → bytes, made for computers, stores raw data (images, files, network packets). It just *looks* like text because Python converts the numbers (65, 66, 97) into their letters to make it readable for you.

The `b` is Python saying — *"don't confuse these two, they are different things."*

Real life: `"ABa"` is a word written on paper. `b"ABa"` is that same word in morse code. Looks similar, totally different format.

Good questions! Let me explain both clearly:

---

## 1️⃣ Difference between TypeError and SyntaxError

### **SyntaxError** - You broke Python's grammar rules

**Happens BEFORE code runs** (Python can't even understand your code)

```python
# ❌ Examples of SyntaxError:

def = 10      # 'def' is keyword, can't use as variable
if x = 5      # Should be if x == 5
print("hi     # Missing closing quote
for i in range(5)  # Missing colon :
    print(i)
```

**When it happens:** When Python FIRST reads your file (before executing anything)

**How to spot:** Python points with `^` arrow at the exact problem

---

### **TypeError** - You used wrong data type together

**Happens DURING code execution** (Python understands grammar but can't do the operation)

```python
# ❌ Examples of TypeError:

"5" + 5       # Can't add str and int
len(123)      # len() only works on sequences, not numbers
None + 5      # Can't add None to number
[1,2,3] + 5   # Can't add list and int
```

**When it happens:** While running the code

---

### Quick Comparison Table

| | **SyntaxError** | **TypeError** |
|---|---|---|
| **When?** | Before running | During running |
| **Why?** | Grammar mistake | Wrong data type operation |
| **Example** | `def = 10` | `"5" + 5` |
| **Python says** | "I can't understand this code" | "I understand but can't do it" |

---

### Memory Trick 🧠

> **SyntaxError** = Spelling/grammar mistake in English 📝  
> **TypeError** = Trying to add apple + car 🍎 + 🚗 (makes no sense!)

---

## 2️⃣ Why `b'ABa'` has `b` in front?

### The `b` means **BYTES** (not string)

```python
byte = bytes([65, 66, 97])
print(byte)  # b'ABa'
```

### What `b'ABa'` tells you:

| Part | Meaning |
|------|---------|
| `b` | Bytes literal (raw data, not text) |
| `'ABa'` | Displayed as characters for readability |

---

### Without `b` = String (text)
```python
text = "ABa"
print(text)     # ABa (no b)
print(type(text))  # <class 'str'>
```

### With `b` = Bytes (raw data)
```python
data = b'ABa'
print(data)     # b'ABa'
print(type(data))  # <class 'bytes'>
```

---

### Why does Python show `b'ABa'` instead of `b'656697'`?

Because Python is **helping you read it**:

```python
# What's actually stored:
bytes([65, 66, 97])  # [65, 66, 97]

# Python DISPLAYS as:
b'ABa'  # Because 65='A', 66='B', 97='a'
```

It's just a **friendly display**! The computer sees numbers, but Python shows you letters.

---

### Real Example:

```python
data = bytes([72, 101, 108, 108, 111])
print(data)  # b'Hello'

# Same data, just displayed nicely!
```

---

### When do you use bytes (with `b`)?

- Reading images, videos, files
- Network communication
- Encryption/Decryption
- Working with raw binary data

---

## Quick Test 🧪

Which error is this?

```python
# Example 1
for i in range(5)  # Missing colon
print(i)
```
**Answer:** SyntaxError (missing colon)

```python
# Example 2
result = "10" + 10
```
**Answer:** TypeError (str + int)

```python
# Example 3
if = 20
```
**Answer:** SyntaxError ('if' is keyword)

---

