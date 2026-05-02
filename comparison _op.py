# num1=4
# num2=6
# greathan= (num1>num2) == False
# print(bool(greathan))
# print(greathan)
# # True

# /////////////////////////////////////////////

# # Chain comparison
# result1 = 4 > 6 == False
# print(result1)  # False

# # This is NOT the same as:
# result2 = (4 > 6) == False
# print(result2)  # True (because False == False = True)

# # See the difference?
# print(4 > 6 == False)      # False (chained)
# print((4 > 6) == False)    # True (grouped differently)
# //////////////////////////////////////////////////////////


# print("True == True==False")
# a= True
# b= True
# c=False
# d= ((a==b)==c)
# print(bool(d))
# False

# x=5
# result1= (1<x)
# result2=(x<10)
# if result1 and result2:
#  print(bool(result1))
#  print(bool(result2))


# print(result1)
# print(result2)
# True
# True
# True
# True



x=5
# # num=((x==x)==x)
# num2=(x==x)
# num1= (x==x)
# if num1 and num2:
#     print("true")

# true

# num1=3
# num2=2
# res= (num1>num2)
# if res == True:
#     print("F")
# F

num1=3
# num2=2
# res= ((num1>num2) and (num2==True))
# print(bool(res))
# False

# n1=3
# n2=2
# res1=(n1>n2)
# res2=(n2==2)
# result= res1 == res2
# print(bool(result))
# True