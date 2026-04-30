'''
print("I'll call you later")
#I'll call you later

print('I'll call you later')  ^
SyntaxError: unterminated string literal (detected at line 5)

print('I will call you later')
I will call you later

print('I\'ll call you later')
I'll call you later

print("Prepare well for "Gate - 2026" exam")
  print("Prepare well for "Gate - 2026" exam")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?


print('Prepare well for "Gate - 2026" exam') #desi ghugad
#Prepare well for "Gate - 2026" exam

print("Prepare well for \"Gate - 2026\" exam")
Prepare well for "Gate - 2026" exam


#backlash double quote 

#newline
a= "Welcome to , Python"
print(a)
Welcome to , Python

a= "Welcome to ,\n Python"
print(a)
Welcome to ,
 Python

#Tab - space
a= "Welcome to ,\t Python"
print(a)
Welcome to ,     Python

a= "Welcome to ,\t\t\t Python"
print(a)
Welcome to ,                     Python


print("no_benefits_of_study Huge_benefits")
no_benefits_of_study Huge_benefits
'''
print("no_benefits_of_study\rHuge_benefits")
Huge_benefitsf_study
print("no__benefits__of_study\rHuge_benefits")
Huge_benefits_of_study