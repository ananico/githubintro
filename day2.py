# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 09:35:26 2018

@author: bn13amn
"""

####Multiple- valued variables or containrs
# 1) Strings
# 2) Tuples
# 3) Lists

a= "ana"
print(a)
print(len(a)) #len gives the number of values in the string

###Access individual values by index

print(a[0], a[1])
## in pyhon is the first 
# the final element of any string is a[-1] always

#String are immutable
# can change a single value in it
# a[1]='a' is not allowed
# a. - gives all the things you can do with the string 
#(putting the dot after the element)

#cancotanate strings#

a='ana'
b='nico'

print (a+b)

# dif between "" and ''

c= "ana's bike"
d='ana is "awesome"'
e= "ana's bike is \"awesome\"" #called escaping
f= ''' use a whoe bunch of quotes'''



###TUPLES

q= (1,2,3,4)

##the same things as for stings for indexing them 
# tuples are imutable
# you kind of need to replace them 

# not necessary to use the brackets

w = 2,3,4
print(type(w))# gives you the type of the variables 


###LISTS
# they use [] this kind of brackets
g= [5,6,7,8]

#you can changes individuals in lists- they are mutable

g[2]=33

# diff between lists and tuples

a= [1,2,3]
b=a

# now labels a and b are both atached to the same list
b[0]=100
#print(a)
#this is gonna change both a and b  

###Slices


a = [1,2,3,4,5,6,7,8,9,10]

print(a[2:6]) # the first index element is included the last is not 
#i.e 6th element not included

print(a[:6]) # from the first till the one mentioned
print(a[6:]) # from the one mention till the last
print(a[:]) # all of them 
a[2:5:2]

# how to change b withot changing a like in the previous example

b = a[:]

b[0] = 100

print(b)
print(a)

#this changes b but not a 


###RANGES

# the things generated are not lists 
# but rather are interated
# range(x,y)

range(1,10)

#to make it a list

list(range(1,10))

range(40, 10, -3) 
#from 40 to 10 by -3
range(10, 40, +3)
# from 10 to 40 by +3

#ranges are only for integers

##float are more than integers



#you can put a list in a list
#mixing things up 
q=[[1,2,3], [4,5,6,8,9],3]
len(q)

q1=[[1,2,3], (3,4,5), 'ana']

# give my the tuple twice

a=(1,2,3)
b=a*2


#packing

#divmod- give both the integer and the remainder of 
#the divison as a tuple


divmod(9,2)

##swap things around
a=1
b=2

a,b=b,a

### put two list in pairs 
#using the zip command- more on slides

##set-not ordedred uisng {}- can be indexed- does not contin copies, 
# make ita list and then a set to eliminate duplicates


###FUNCTIONS

def squared(x):
    x_squared=x**2
    return x_squared
#x is only defiened within the function and not outsied

def double_it(z):
    return 2*z

#functions can be given multiple arguments 
#you can ask it to give you multiple back

def pythagoras(a,b):
    c_squared = a**2 + b**2
    return c_squared**0.5, c_squared 

# numpy arrays

import numpy as np 

a = np.array([[1,2],[3,4]])
print(a)
print(np.ndim(a))
print(np.shape(a))
print(np.size(a))
print(a.min())
print(a.sum())


b= np.array(range(20))
print(b.reshape(4,5))

#numpy arrays are mutable

c=np.zeros([4,3])
d=np.ones([2,5])
e=np.eye(5)

#numpy has range, which is like range but for real numbers 

print(np.arange(1.1, 2.5,0.2))

#also

q= np.linspace(1.0,20.0, 150)
print(q)

##slicing as for lists, but a bit better

a=np.arange(0,15)
print(a[3:6])
print(a[12:5:-1])

b=np.array(range(20))
b=b.reshape(4,5)
print(b)


b[:,1] # get the second column
b[1,:] # get the second row of an array

#element wise operations 
#apply the same shit to all values in the array
# addition, square, 

#####Control flow 
# how it get from where to where



#if
x=12
if x<10:
    print('rob is awesome')
else:
    print('lunchtime')


x=17
if x<10:
    print('rob is awesome')
elif x<15:
    print('lunchtime')
elif x<20:
    print('dinnertime')
else:
    print('beer')

###    WHILE
n=10 
tr=0

while n>0:
    tr+=n
    n-=1 # increment must be in the loop 
print(tr)


for i in range(10): #i in this case is not dumy
    print(i**2+i+1)
        
for _ in range(5):
    print('rob')

for a in [4,6,2,4,8]:
    for b in 'rob':
        print(a,b)
        
        
        
        
###Classes

def gcd(a,b):
    r=a%b
    if r==0:
        return b
    else:
        return gcd(b,r)
    
class Rational:
    def __init__(self,a,b):
    
        hcf=gcd(a,b)
        self.__n = a/hcf
        self.__d = b/hcf
    def getNumerator(self):
        return self.__n
    def getDenominator(self):
        return self.__d
    def __mul__(self,rhs):
        a=self.__n * rhs.getNumerator()
        b=self.__d * rhs.getDenominator()
        return Rational(a,b)
    def __repr__(self):
        str='%d' % self._n
        str=str+ '/'
        str=str+  '%d' % self._d
        return str 