# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

# Set up variables
y0=50

x0=50

#Random walk one step

random_number=random.random()

if random_number < 0.5:
     y0 = y0 + 1 
     
     x0= x0 + 1
          
else:
     y0 = y0 - 1
     x0= x0 - 1 
    
print(y0, x0)

if random_number < 0.5:
     y0 = y0 + 1 
     
     x0= x0 + 1
          
else:
     y0 = y0 - 1
     x0= x0 - 1 
    
print(y0, x0)

if random_number < 0.5:
     y0 = y0 + 1 
     
     x0= x0 + 1
          
else:
     y0 = y0 - 1
     x0= x0 - 1 
    
print(y0, x0)

y1=50

x1=50
if random_number < 0.5:
     y1 = y1 + 1 
     
     x1= x1 + 1
          
else:
     y1 = y1 - 1
     x1= x1 - 1 
    
print(y1, x1)

if random_number < 0.5:
     y1 = y1 + 1 
     
     x1= x1 + 1
          
else:
     y1 = y1 - 1
     x1= x1 - 1 
    
print(y1, x1)

if random_number < 0.5:
     y1 = y1 + 1 
     
     x1= x1 + 1
          
else:
     y1 = y1 - 1
     x1= x1 - 1 
    
print(y1, x1)

answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print(answer)