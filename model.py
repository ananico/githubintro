# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import operator 
import matplotlib.pyplot
import agentsframework
import csv

# Set up variables
#y0=50

#x0=50

#Random walk one step

#random_number=random.random()

#if random_number < 0.5:
 #    y0 = y0 + 1 
     
  #   x0= x0 + 1
          
#else:
 #    y0 = y0 - 1
  #   x0= x0 - 1 
    
#print(y0, x0)

#if random_number < 0.5:
 #    y0 = y0 + 1 
     
  #   x0= x0 + 1
          
#else:
 #    y0 = y0 - 1
  #   x0= x0 - 1 
    
#print(y0, x0)

#if random_number < 0.5:
 #    y0 = y0 + 1 
     
  #   x0= x0 + 1
          
#else:
  #   y0 = y0 - 1
 #    x0= x0 - 1 
    
#print(y0, x0)

#y1=50

#x1=50
#if random_number < 0.5:
 #    y1 = y1 + 1 
     
   #  x1= x1 + 1
          
#else:
 #    y1 = y1 - 1
  #   x1= x1 - 1 
    
#print(y1, x1)

#if random_number < 0.5:
 #    y1 = y1 + 1 
     
#     x1= x1 + 1
          
#else:
#     y1 = y1 - 1
#     x1= x1 - 1 
    
#print(y1, x1)

#if random_number < 0.5:
#     y1 = y1 + 1 
     
#     x1= x1 + 1
          
#else:
#     y1 = y1 - 1
#     x1= x1 - 1 
    
#print(y1, x1)

#answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
#print(answer)

##### PRACTICAL 2######

#agents = []

#y0 = random.randint(0,99)
#x0 = random.randint(0,99)


#y1 = random.sample(range(0, 99),2)

#x1 = random.sample(range(0, 99), 50)

#agents = list(zip(y1,x1))



#agents.append([y0,x0])

###append adds to the end of the list - for how many times 
#you are running it

#needs to be run multiple times to add to the list
#agents.append([random.randint(0,99),random.randint(0,99)])

#print(max(agents))
#maxeast=(max(agents, key=operator.itemgetter(1)))

#matplotlib.pyplot.ylim(0, 99)
#matplotlib.pyplot.xlim(0, 99)
#matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
#matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
#matplotlib.pyplot.scatter(agents[2][1],agents[2][0])
#matplotlib.pyplot.scatter(agents[3][1],agents[3][0])
#matplotlib.pyplot.scatter(maxeast[1], maxeast[0], color='red')
#matplotlib.pyplot.show()



 #num_of_iterations= 100

#agents=[]
#num_of_agents = 10
#for i in range(num_of_agents):
#    agents.append([random.randint(0,100),random.randint(0,100)])    

#print(agents)
#m =0
#while m <2: 
   # print('hey')
#    for i in range(num_of_agents):  
#        if random.random() < 0.5:
#            agents[i][0] += 1
#        else:
#            agents[i][0] -= 1

#        if random.random() < 0.5:
#            agents[i][1] += 1
 #       else:
 #           agents[i][1] -= 1
 #   m +=1 

#print(agents)   


#matplotlib.pyplot.ylim(0, 99)
#matplotlib.pyplot.xlim(0, 99)
#maxeast=(max(agents, key=operator.itemgetter(1)))

#for i in range(num_of_agents):
#    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
#matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
#matplotlib.pyplot.scatter(maxeast[1], maxeast[0], color='red')
#matplotlib.pyplot.show()
 

#num_of_iterations=100 

#print(agents)
#m = 0
#while m < num_of_iterations: 
 #   print('hey')
#for j in range(num_of_iterations):  
#     for i in range(num_of_agents):  
#        if random.random() < 0.5:
#            agents[i][0] += 1
#        else:
#            agents[i][0] -= 1
            
#        if random.random() < 0.5:
#            agents[i][1] += 1
#        else:
 #           agents[i][1] -= 1
 #    m +=1 

#print(agents)   
  


#num_of_agents = 10
#num_of_iterations = 1
#agents = []

# Make the agents.
#for i in range(num_of_agents):
#    agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.
#for j in range(num_of_iterations):
#    for i in range(num_of_agents):

 #       if random.random() < 0.5:
 #           agents[i][0] = (agents[i][0] + 1) % 100
 #       else:
 #           agents[i][0] = (agents[i][0] - 1) % 100

 #       if random.random() < 0.5:
 #           agents[i][1] = (agents[i][1] + 1) % 100
 #       else:
 #           agents[i][1] = (agents[i][1] - 1) % 100

#answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] 
#- agents[1][1])**2))**0.5
#print(answer)


#matplotlib.pyplot.ylim(0, 99)
#matplotlib.pyplot.xlim(0, 99)
#for i in range(num_of_agents):
#    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
#matplotlib.pyplot.show()

#def distance_between(agents_row_a, agents_row_b):
#    distance_between = (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_a[1])**2))**0.5
    #distance = distance_between(agents_row_a[0], agents_row_b[0])
    #print(distance) 
#    return distance_between

#for i in range(num_of_agents):
#    for j in range(num_of_agents):
 #       print (distance_between(agents[i], agents[j])) 
 

#import time

#start = time.clock()

#for i in range(num_of_agents):
#    for j in range(num_of_agents):
 #    print (distance_between(agents[i], agents[j]))

#end = time.clock()

#print("time = " + str(end - start))

#a = agentsframework.Agent()

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + 
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentsframework.Agent())

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()

for i in range(num_of_agents):
   for j in range(num_of_agents):
     print (distance_between(agents[i], agents[j]))



###reading the file in 

dataset=open("in.txt", newline='')
#environment=[]
#rowlist=[]
environment=[]


reader=csv.reader(dataset, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    rowlist=[]
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
        
#rowlist=[row for row in environment]
#environment.append(rowlist)

matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()


######








for line in dataset:
	print(line)
dataset.close()


environment=[]
rowlist=[]

rowlist.append(dataset)
environment.append(rowlist)