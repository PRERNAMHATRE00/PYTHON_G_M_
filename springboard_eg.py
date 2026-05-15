# a= 262734654773674658486846874
# print(a)

# >>> 5.46e8
# 546000000.0
# >>> 6.79e-9
# 6.79e-09
# >>>

# >>> 9.89e-3
# 0.00989
# >>>

# >>> print(comp_num)
# (4+9j)
# >>> print(comp_num2)
# (5+9j)
# >>>



# >>> SEN1="BJSJVBUVKS CFHVJHIDHGKDH"
# >>> SEN2='''ZHVJH
# ... JHJHK
# ... JHIHK
# ... BJDHUMN
# ... HVUFH'''
# >>> print(SEN1)
# BJSJVBUVKS CFHVJHIDHGKDH
# >>> print(SEN2)
# ZHVJH
# JHJHK
# JHIHK
# BJDHUMN
# HVUFH


# ord() - character to ascii
# chr()- ASCII to character 


# >>> ord("C")
# 67
# >>> chr(89)
# 'Y'
# >>> chr(99)
# 'c'
# >>> ord("ESC")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: ord() expected a character, but string of length 3 found
# >>> ord("D")
# 68
# >>>


# >>> 5/3
# 1.6666666666666667
# >>> 5/3.0
# 1.6666666666666667
# >>> 8/2
# 4.0
# >>> 8/2.0
# 4.0
# >>> 11/2
# 5.5
# >>>
# >>>
# >>> 11/2
# 5.5



# >>> int(2.5)
# 2
# >>> int(45)
# 45
# >>> float(67)
# 67.0
# >>> float(5.5)
# 5.5
# >>> long(25)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'long' is not defined
# >>> Long(56)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'Long' is not defined
# >>> str(88)
# '88'


# >>>
# >>> x=20
# >>> y=10
# >>> x<y
# False
# >>> x>y
# True
# >>> x<>y
#   File "<stdin>", line 1
#     x<>y
#      ^^
# SyntaxError: invalid syntax
# >>> x!=y
# True
# >>>
# >>>
# >>> x<y<john
# False
# >>> john>y>x
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'john' is not defined
# >>> john<y<x
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'john' is not defined
# >>> cls()

#  cls()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'cls' is not defined
# >>>
# >>> 6==6.0
# True
# >>> 6==6
# True
# >>> 6<=6
# True
# >>> 6<=6.0
# True
# >>> 6>=6.0
# True



# >>> x=50
# >>> y=2
# >>> x|y
# 50
# >>>
# >>> x=240
# >>> y=1
# >>> x|y
# 241
# >>>
# >>> x&y
# 0
# >>>
# >>> x^y
# 241
# >>>
# >>> x<<2
# 960
# >>>
# >>>
# >>> x>>2
# 60
# >>>
# >>> ~x
# -241
# >>> ~y
# -2



# >>> 2>8
# False
# >>> 4>1
# True
# >>> 2>8 and 4>1
# False
# >>> 2>8 or 4>1
# True
# >>> not(4>1)
# False
# >>> not(2>8)
# True


# >>> name="Berry"
# >>> 'e' in name
# True
# >>> "t" in name
# False
# >>> "v" not in name
# True
# >>>



# >>> x=10
# >>> y=10
# >>> x is y
# True
# >>> x=11
# >>> y=12
# >>> x is y
# False
# >>> x is not y
# True


# >>>
# >>> x=20
# >>> y=20
# >>> id(x)
# 140708963306520
# >>> id(y)
# 140708963306520
# >>> x is y
# True
# >>> x=[1,2,3]
# >>> y=[1,2,3]
# >>> x is y
# False
# >>> id(x)
# 2047977312832
# >>> id(y)
# 2047977312640




# >>> x=685
# >>> y=685
# >>> id(x)
# 2047981026672
# >>> id(y)
# 2047981026416
# >>>
# >>> x=256
# >>> y=256
# >>> id(x)
# 140708963314072
# >>> id(y)
# 140708963314072
# >>>
# >>>
# >>> x=257
# >>> y=257
# >>> id(x)
# 2047981026672
# >>> id(y)
# 2047981011472
# >>> id(c)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'c' is not defined
# >>>


/////////////////////////////////////////////////////////////////////////////////////////////////////
# STRING

# >>> str="Welcome to Python"
# >>> str
# 'Welcome to Python'
# >>> id(str)
# 2237592564400
# >>> str="Python"
# >>> str
# 'Python'
# >>> id(str)
# 140707983020848
# >>> import ctypes
# >>> ctypes.cast(2237592564400, ctypes.py_object).value
# 'CFuncPtr'
# >>> ctypes.cast(140707983020848, ctypes.py_object).value
# 'Python'
# >>>


# /// LENGTH

#  str="hellopython"
# >>> len(str)
# 11
# >>> str="hello python"
# >>> len(str)
# 12
# >>>

# SUBSTRING 
# >>> name="Ash"
# >>> name[2]
# 'h'
# >>> name[0]
# 'A'
# >>> name[5]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range
# >>>


# NEGATIVE INDEXING

# >>>
# >>> name[-1]
# 'h'
# >>> name[-2]
# 's'
# >>> name[-3]
# 'A'
# >>> name[-4]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range
# >>> name[0]
# 'A'
# >>> name[-3]
# 'A'


# SLICING STRING
# >>>
# >>> sent="milky way galaxy "
# >>> sent[0:4]
# 'milk'
# >>> sent[:len(sent)]
# 'milky way galaxy '
# >>> sent[3:]
# 'ky way galaxy '
# >>> sent[:7]
# 'milky w'
# >>> sent[0:-1]
# 'milky way galaxy'
# >>> sent[-3:6]
# ''
# >>> len(sent)
# 17
# >>> sent[-3:11]
# ''
# >>> sent[-2:-11]
# ''
# >>>


# >>> sent[::3]
# 'mkw ly'
# >>> sent[::2]
# 'mlywyglx '
# >>> sent[::1]
# 'milky way galaxy '
# >>> sent[::0]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: slice step cannot be zero
# >>>

# REVERSE STRING
# >>> sent[::-1]
# ' yxalag yaw yklim'



#COUNT
# sent.count("l")
# 2
# >>>
# >>>
# >>> str1="The MArvel"
# >>> str.count("e")
# 1
# >>> str1.count("e")
# 2
# >>> str1="The big bag was beautiful and blue in colour"
# >>> str1.count("b",4,30)
# 3
# >>>


#FIND
# >>> str1.find("blue")
# 30
# >>> str1.rfind("b")
# 30
# >>> str1.lfind("b")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'str' object has no attribute 'lfind'. Did you mean: 'find'?
# >>>

# CASE function
#LOWER
# >>> name="MISTY"
# >>> name.lower()
# 'misty'
# >>> name.lower(i)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'i' is not defined. Did you mean: 'id'?
# >>> name.lower(2)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: str.lower() takes no arguments (1 given)
# >>>

#  str= "Welcome to PYTHON"
# >>> str.lower()
# 'welcome to python'
# >>> str

#UPPER
# 'Welcome to PYTHON'
# >>> str.upper()
# 'WELCOME TO PYTHON'
# >>> name="deco"

#CAPITALIZE
# >>> name.capitalize()
# 'Deco'
# >>> str="i have been going to swimming everyweek"

#TITLE
# >>> str,title()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'title' is not defined. Did you mean: 'tuple'?
# >>> str.title()
# 'I Have Been Going To Swimming Everyweek'
# >>> str
# 'i have been going to swimming everyweek'
# >>>


#SWAPCASE
# >>> str.swapcase()
# 'I HAVE BEEN GOING TO SWIMMING EVERYWEEK'
# >>> str.uppercase()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'str' object has no attribute 'uppercase'
# >>> str.upper()
# 'I HAVE BEEN GOING TO SWIMMING EVERYWEEK'
# >>>



# RSTRIP
# >>> str="the great water fallen"
# >>> str.rstrip("en")
# 'the great water fall'
# >>> str
# 'the great water fallen'

#LSTRIP
# >>> str1="EL was beautiful"
# >>> str1.lstrip("el")
# 'EL was beautiful'
# >>> str1.lstrip("EN")
# 'L was beautiful'
# >>> str1.lstrip("EL")
# ' was beautiful'
# >>> str.strip()
# 'the great water fallen'
# >>> str1.strip()
# 'EL was beautiful'


#SPILT
# >>> str="27-12-2026"
# >>> str.spliy("-")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'str' object has no attribute 'spliy'. Did you mean: 'split'?
# >>> str.split("-")
# ['27', '12', '2026']
# >>> str.split("-",1)
# ['27', '12-2026']
# >>> str.split("-",0)
# ['27-12-2026']
# >>> str.split("-",2)
# ['27', '12', '2026']
# >>>
# >>>

#LIST
# >>> list=str.split("-")
# >>> list[]
#   File "<stdin>", line 1
#     list[]
#          ^
# SyntaxError: invalid syntax
# >>> list[1]
# '12'
# >>> list[2]
# '2026'
# >>> list[0]
# '27'
# >>> print(list)
# ['27', '12', '2026']
# >>>


#STRING SPLIT

# >>> name="Butterfly flying"
# >>> name.split()
# ['Butterfly', 'flying']
# >>> name.rsplit("ing")
# ['Butterfly fly', '']
# >>> name.lsplit("But")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'str' object has no attribute 'lsplit'. Did you mean: 'rsplit'?
# >>>
# >>> str="25-12-2016"
# >>> str.rsplit("-")
# ['25', '12', '2016']

#JUSTIFY
#LJUST
#  name="John Sohn"
# >>> str.ljust(20,"*")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: descriptor 'ljust' for 'str' objects doesn't apply to a 'int' object
# >>> name.ljust(20,"*")
# 'John Sohn***********'

# #RJUST
# >>> name.rjust(13,"*")
# '****John Sohn'
# >>> name.center(10,"-")
# 'John Sohn-'
# >>> name.center(20,"-")
# '-----John Sohn------'


# #ZFILL
# >>> account_no=76372658238
# >>> account_no.zfill(20)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'int' object has no attribute 'zfill'
# >>> account_no="76372658238"
# >>> account_no.zfill(20)
# '00000000076372658238'
# >>>
# >>> bin_num="1010101011100"
# >>> bin_num.zfill(25)
# '0000000000001010101011100'

# #REPLACE
# >>> sent="Monkeys have turtle brains"
# >>> sent.replace("have","with")
# 'Monkeys with turtle brains'
# >>> sent
# 'Monkeys have turtle brains'
# >>> sent.replace("have",1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: replace() argument 2 must be str, not int
# >>> sent.replace("have","1")
# 'Monkeys 1 turtle brains'
# >>> sent.replace("have","with",1)
# 'Monkeys with turtle brains'
# >>> sent
# 'Monkeys have turtle brains'
# >>> sent="Monkeys have turtle brains have brians have brains"
# >>> sent.replace("have","with",2)
# 'Monkeys with turtle brains with brians have brains'
# >>> sent.replace("have","with",3)
# 'Monkeys with turtle brains with brians with brains'
# >>>


# #JOIM

# >>> name=["Rohan","&","Sania"]
# >>> name.join()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'list' object has no attribute 'join'
# >>> join(name)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'join' is not defined
# >>> .joint(name)
#   File "<stdin>", line 1
#     .joint(name)
#     ^
# SyntaxError: invalid syntax
# >>> "".joint(name)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'str' object has no attribute 'joint'. Did you mean: 'join'?
# >>> .join(name)
#   File "<stdin>", line 1
#     .join(name)
#     ^
# SyntaxError: invalid syntax
# >>> "".join(name)
# 'Rohan&Sania'
# >>> " ".join(name)
# 'Rohan & Sania'
# >>> ", ".join(name)
# 'Rohan, &, Sania'
# >>>

# #ENDSWITH
# >>> sent="today is a weekend"
# >>> sent.endswith("weekend")
# True
# >>> sent.endswith("day")
# False
# >>> sent.endswith("today",0,5)
# True
# >>> sent.endswith("today",0,len(sent))
# False
# >>> len(sent)
# 18
# >>> sent.endswith("today",0,18)
# False

# #STARTSWITH
# >>> sent.startswith("to")
# True
# >>> sent.startswith("we",11,19)
# True
# >>> sent.startswith("we")
# False
# >>>
# >>>

# #ISALPHA
# >>> name="sunny"
# >>> name.isalpha()
# True
# >>> na1="bunny"
# >>> na1="bunny b"
# >>> na1.isaplha()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
# >>> na1.isalpha
# <built-in method isalpha of str object at 0x000001DDF8F06130>
# >>>
# >>> na1.isalpha()
# False
# >>> na1="bunny"
# >>> na1.isalpha()
# True

# #ISALNUM
# >>> na2="536235462"
# >>> na2.isnum()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
# >>> na2.isalnum()
# True
# >>> na3="5362 35462"
# >>> na3.isalnum()
# False
# >>>
# >>>
# >>>

# #ISDIGIT
# >>> num=76475629
# >>> num.isdigits()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'int' object has no attribute 'isdigits'
# >>> num.isdigit()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'int' object has no attribute 'isdigit'
# >>> num="76475629"
# >>> num.isdigit()
# True
# >>>
# >>>
# >>> num1="757465gK"
# >>> num1.isdigit()
# False
# >>>

# #ISSPACE
# >>> num1.isspace()
# False
# >>> num4=" jchjhci "
# >>> num4.isspace()
# False
# >>> num4=" jchjh ci "
# >>> num4.isspace()
# False
# >>> nuum5=""
# >>> nuum5.isspace()
# False
# >>> nuum5=" "
# >>> nuum5.isspace()
# True
# >>>
# >>>

# #ISTITLE
# >>> name="Rohan"
# >>> name.istitle()
# True
# >>> name="Rohan And Sania"
# >>> name.istitle()
# True
# >>> name="Rohan and Sania"
# >>> name.istitle()
# False
# >>>

# ISLOWER
# >>> name="rohan and sania"
# >>> name.islower()
# True
# >>> name="Sania"
# >>> name.islower()
# False
# >>> name="and76r8"
# >>> name.islower()
# True
# >>> "!@#$%^&*46536376()"
# '!@#$%^&*46536376()'
# >>> name="!$%$^%&&*&*((((()*"
# >>> name.islower()
# False
# >>> name="!$%$and1233^%&&*&*((((()*"
# >>> name.islower()
# True
# >>>
# ISUPPER
# >>> name="MOHIT"
# >>> name.isupper()
# True
# >>> name="MOHIT54364287!@#"
# >>> name.isupper()
# True
# >>> name="mOHIT"
# >>> name.isupper()
# False
# >>>

# //////////////////////////////
# tuple
# tup1=()
# >>> tup1=()
# >>> tup=(1,2,3,4,5,6,7,"Hi" ,"a")
# >>> a=1,2,3,4
# >>> tup2=1,2,3,4
# >>> tup2
# (1, 2, 3, 4)
# >>> tup1
# ()
# >>> tup1
# ()
# >>> tup
# (1, 2, 3, 4, 5, 6, 7, 'Hi', 'a')
# >>> type(tup)
# <class 'tuple'>
# >>> type(tup2)
# <class 'tuple'>

# >>> fruits=("Mango","Apple","Orange","Litchi","Peach")
# >>> fruit(0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'fruit' is not defined. Did you mean: 'fruits'?
# >>> fruits(0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object is not callable
# >>> fruits[0]
# 'Mango'
# >>> fruits[3]
# 'Litchi'
# # >>>
# >>> fruits[-1]
# 'Peach'
# >>> fruits[-2]
# 'Litchi'
# >>> fruits[2:5]
# ('Orange', 'Litchi', 'Peach')
# >>> fruits[3:]
# ('Litchi', 'Peach')
# >>> fruits[:5]
# ('Mango', 'Apple', 'Orange', 'Litchi', 'Peach')
# >>> fruits[::1
# ...
# ... s
#   File "<stdin>", line 1
#     fruits[::1
#              ^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
# >>> fruits[::1]
# ('Mango', 'Apple', 'Orange', 'Litchi', 'Peach')
# >>> fruits[::3]
# ('Mango', 'Litchi')
# >>> fruits[-1:-4]
# ()
# >>> fruits[-4:-1]
# ('Apple', 'Orange', 'Litchi')
# >>>


# #GENERIC FUNCRION

#  a=1,b=2,c=3
#   File "<stdin>", line 1
#     a=1,b=2,c=3
#     ^^^
# SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?>>> a=1
# >>> b=2
# >>> c=3
# >>> a
# 1
# >>> b
# 2
# >>> c
# 3
# >>> tup2=(1,2,3)
# >>> x,z,c=tup2
# >>> x
# 1
# >>> z
# 2
# >>> c
# 3
# >>> y
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'y' is not defined
# >>> x,z,c,d=tup2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: not enough values to unpack (expected 4, got 3)
# >>>
# >>>
# #LEN
# >>> veg=("tomato","potato","carrot","radish")
# >>> len(veg)
# 4

# #MAX
# >>> max(veg)
# 'tomato'
# >>> max(veg)
# 'tomato'
# >>> num=(1,4,9,10,11.5,11.50)
# >>> max(num)
# 11.5
# >>> num=(1,4,9,10,11.50,11.5)
# >>> max(num)
# 11.5
# >>> num=(1,4,9,10,11.5,11.50,11.0)
# >>> max(num)
# 11.5
# >>> num=(1,4,9,10,11.50,11.0,11.5)
# >>> max(num)
# 11.5
# >>> num=(1,4,9,10,450,450.0)
# >>> max(num)
# 450
# >>> num=(1,4,9,10,450.0,450)
# >>> max(num)
# 450.0
# >>> sent=(1,543,"2","a")
# >>> max(sent)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: '>' not supported between instances of 'str' and 'int'
# >>> sent=(1,543,"2")
# >>> max(sent)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: '>' not supported between instances of 'str' and 'int'
# >>> (3,"4")
# (3, '4')
# >>> s=(1,"2")
# >>> max(S)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'S' is not defined. Did you mean: 's'?
# >>> max(s)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: '>' not supported between instances of 'str' and 'int'
# >>> a=(500,"1")
# >>> max(a)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: '>' not supported between instances of 'str' and 'int'
# >>>

# > tup=("a","b","c")
# >>> len(tup)
# 3
# >>> max(tup)
# 'c'
# >>> t1=(1,2,5,9,4,50,50.0)
# >>> max(t1)
# 50
# >>> t1=(1,2,5,9,4,50.0,50)
# >>> max(t1)
# 50.0
# >>> t2=(900,"2")
# >>> max(t2)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: '>' not supported between instances of 'str' and 'int'
# >>> t3=("a","z","c")
# >>> max(t3)
# 'z'
# >>> t4=("aa","ab","bb","z","cc","za","zz")
# >>> max*t4)
#   File "<stdin>", line 1
#     max*t4)
#           ^
# SyntaxError: unmatched ')'
# >>> max(t4)
# 'zz'
# >>> min(t4)
# 'aa'
# >>> t5=("1","3","0",1)
# >>> t5=("1","3","0")
# >>> min(t5)
# '0'
# >>> name="Ash"
# >>> tuple(name)
# ('A', 's', 'h')
# >>>

#  fruit=("Apple","Mango")
# >>> veg=("Potato","radish")
# >>> fruit+veg
# ('Apple', 'Mango', 'Potato', 'radish')
# >>> fruit=("Apple","Mango","tomato")
# >>> veg=("Potato","radish","tomato")
# >>> fruit+veg
# ('Apple', 'Mango', 'tomato', 'Potato', 'radish', 'tomato')
# >>> fruit*2
# ('Apple', 'Mango', 'tomato', 'Apple', 'Mango', 'tomato')
# >>> id(fruit[3])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: tuple index out of range
# >>> id(veg[2])
# 1566970634688
# >>> veg(2)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object is not callable
# >>> veg[2]
# 'tomato'
# >>> id(veg[2])
# 1566970634688
# >>> fruit[2]
# 'tomato'
# >>> id(fruit[2])
# 1566970634688
# >>>


# >>> sent="We have to go to picnic this weekend"
# >>> if "to: in sent:
#   File "<stdin>", line 1
#     if "to: in sent:
#        ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> sent="We have to go to picnic this weekend"
# >>> if "to" in sent:
# ... print"yes"
#   File "<stdin>", line 2
#     print"yes"
#     ^
# IndentationError: expected an indented block after 'if' statement on line 1
# >>> if "to" in sent:
# ...     print"yes"
#   File "<stdin>", line 2
#     print"yes"
#     ^^^^^^^^^^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
# >>> if "to" in sent:
# ...    print "yes"
#   File "<stdin>", line 2
#     print "yes"
#     ^^^^^^^^^^^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
# >>> if "to" in sent:
# ...     print("yes")
# ...
# yes
# >>>


















































































































