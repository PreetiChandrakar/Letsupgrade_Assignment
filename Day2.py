#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Python program to remove empty List from List.
list1=["12",[],"erf"] 
new_list1 = [elem for elem in list1 if elem !=[]]
print(new_list1)


# In[7]:


#Python program to remove all duplicates words from a given sentence
s = "Fruits are best but Vegetables are also best"
l = s.split() 
k = [] 
for i in l:  
    if (s.count(i)>1 and (i not in k)or s.count(i)==1): 
        k.append(i) 
print(' '.join(k)) 


# In[10]:


#Python program to find all occurrences of a character in the given string
str1 = input("Please enter String : ")
ch = input("Please enter Character : ")
i = 0

while(i < len(str1)):
    if(str1[i] == ch ):
        print(ch, " is Found at Position " , i)
    i = i + 1


# In[ ]:




