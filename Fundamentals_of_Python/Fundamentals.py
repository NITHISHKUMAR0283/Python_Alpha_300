# variables 

name = "Nithish"
age = 20

# comments 

#datatypes 
print(isinstance(name,str))
print(isinstance(age,int))

"""
complex
bool
list
tuple
range
dict
set
"""

#Arithmetic operators

"""
1+1   2
2-1   1
2*2   4
4/2   2 float
4%3   1
4**2  16
4//2  2 floor
"""

#comparision operators

"""
a == b
a != b
a > b
a >=b
a<b
a<=b
and 
or 
not 

"""

print(0 or 1 , False or 'hey' , 'hi' or 'hey' , [] or False , False or [])
# 1 hey hi False []

print(0 and 1, 1 and 0, False and 'hey', 'hi' and 'hey', [] and False, False and [])
#0 0 False hey [] False

#binary operators 
 
"""
 &
 |
 ^
 ~
 <<
 >>
 """

"""
is
in 
"""

#strings
name = "nithish "
name += "kumar "
print (name) # nithish kumar 

"""
String methods 

isalpha()
isalnum()
isdecimal()
lower()
islower()
upper()
isupper()
title()
startswith()
endswith()
replace()
split()
join()
find()
"""

print(name.upper()) #NITHISH KUMAR 
print(name.title()) #Nithish Kumar 
print("ku" in name) # True
print (name.startswith("ni")) #True

# slicing [start:end:-1]
print(name[:4]) #nith

# complex 
num = complex(2,3)
print(num.real , num.imag)

#build in function

print(round(5.49,1))

dogs = ["Roger", 1, "Syd", True, "Quincy", 7]

dogs[2] = "Beau"
dogs +="nithish"

print(dogs[2:4])
print(dogs)

dogs.pop()
dogs.insert(2,"i")
print(dogs)

# Tuples
names = ("Roger", "Syd")

names.index("Roger")
print(names)

# Dictionaries

dog = { "name": "Roger", "age": 8 }

dog["name"] = "Syd"

print(dog)


# Sets

set1 = {"Roger", "Syd"}
set2 = {"Roger"}

mod = set1 - set2
print(mod)

# Functions

def hello():
    print('Hello!')

hello()
hello()
hello()