#!/usr/bin/env python
# coding: utf-8

# In[4]:


num=int(input("Enter Number to check prime or not:"))
m=0
i=0
flag=0
m=int(num/2)
for i in range(2,m+1):
    if(num%i==0)  :     
        print("Number is not prime")    
        flag=1  
        break       
if(flag==0) :   
    print("Number is prime")   


# In[3]:


num=int(input("Enter Number to get Factotial:")) 
i=0 
fact = 1 
for i in range(2,num+1) :
    fact = fact * i 
print("Factorial of",num, "is:",fact)


# In[8]:


num=int(input("Enter Number till you need to find sum from 1 to:")) 
i=1 
sum =0
while(i<=num):
    sum = sum + i
    i=i+1
print(sum)


# In[ ]:




