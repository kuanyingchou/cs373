#!/usr/bin/env python
def find_coconut_brute():
   for n in range(6, 20000):
      c=n
      print str(c) + ' coconuts:'
      for p in range(5):
         if (c%5) == 0 or (c-1)%5 != 0: 
            break
         else: 
            t=1+(c-1)/5
            c-=t
            print 'person '+str(p)+' hide '+str(t-1)+' coconuts, ',
            print str(c)+' coconuts remain'
      else:
         if c>5 and c%5!=0 and (c-1)%5 == 0:
            print n
            break
def find_coconut_ni():
   for j in range(0, 20000):
      n=j
      for i in range(6):
         if n%4 != 0:
            break
         n=n/4*5+1
      else:
         print n
def find_coconut_isint():
   def f(n):
       return (n-1) / 5 * 4

   def f6(n):
       for i in range(6):
           n = f(n)
       return n 

   def is_int(n):
       return abs(n-int(n)) < 0.0000001
      
   n=1.
   MAXTRY=16000
   while n<MAXTRY:
       if is_int(f6(n)):
           break
       n+=1

       
   if n == MAXTRY:
       print 'failed to find n'
   else:
       pass
   print n

def find_coconut_wow():
   print 5**6-4 # how do you know it's the smallest answer?

#[ main
#find_coconut_brute()
#find_coconut_ni()
#find_coconut_isint()
find_coconut_wow()
