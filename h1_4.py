#!usr/bin/env python

colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT
         
# Return the sum of a matrix
def matrix_sum(p):
   s=0
   for i in range(len(p)):
      s += sum(p[i])
      #for j in range(len(p[i])):
      #   s+=p[i][j]
   return s

# Normalize matrix p so that matrix_sum(p)==1
def matrix_norm(p):
   s=matrix_sum(p)
   #q=matrix_create(len(p), len(p[0]))
   q=[]
   for i in range(len(p)):
      r=[]
      for j in range(len(p[i])):
         r.append(p[i][j] / float(s)) #modifying p leads to wrong answers
         #print str(i)+', '+str(j)+': '+str(p[i][j])+' -> '+str(t)
      q.append(r)
   return q

def matrix_create(i, j):
   return matrix_create_value(i, j, 0)

#[ Create a i*j list. Initialize each element to k
def matrix_create_value(i, j, k):
   q=[[k]*j]*i
   return q

def move(p, m):
   #q=matrix_create(len(p), len(p[0]))
   q=[]
   for i in range(len(p)):
      r=[]
      for j in range(len(p[i])):
         px=(i-m[0])%len(p)
         py=(j-m[1])%len(p[i])
         r.append(p[px][py] * p_move + p[i][j] * (1-p_move))
         #print q[i][j],
      q.append(r)
   #print(q)
   q=matrix_norm(q)
   return q

def sense(p, c, Z):
   #q=matrix_create(len(p), len(p[0]))
   q=[]
   for i in range(len(p)):
      r=[]
      for j in range(len(p[i])):
         if(c[i][j]==Z):
            r.append(p[i][j]*sensor_right)
         else:
            r.append(p[i][j]*(1-sensor_right))
      q.append(r)
   q=matrix_norm(q)
   return q

#[ test
def test_matrix_sum():
   print matrix_sum([[1, 2], [3, 4]])
def test_matrix_norm():
   p=[[1, 2], [3, 4]]
   print p
   matrix_norm(p)
   print p
   print matrix_sum(p)

#print matrix_sum(p)
#test_matrix_norm()
#] test

#[ main
#p=matrix_create_value(len(colors), len(colors[0]), 1)
#p=matrix_norm(p)
p=[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
p=matrix_norm(p)
show(p)
#p=move(p, motions[1])
#p=sense(p, colors, measurements[0])
for i in range(len(motions)):
   p=move(p, motions[i])
   p=sense(p, colors, measurements[i])
#] main

#Your probability array must be printed 
#with the following code.

show(p)





