#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Python program to merge two files into a third file.
data = data2 = "" 
  
# Reading data from file1 
with open('G://assignment//python//file1.txt') as fp: 
    data = fp.read() 
  
# Reading data from file2 
with open('G://assignment//python//file2.txt') as fp: 
    data2 = fp.read() 
  
# Merging 2 files 
# To add the data of file2 from next line 
data += "\n"
data += data2 
  
with open ('G://assignment//python//file3.txt', 'w') as fp: 
    fp.write(data)


# In[5]:


#Take two lists as input list1 = [1,2,3,4,5] and list2 = ["a", "b", "c", "d", "e"] 
#From that make a dictionary ouput {1:"a", 2:"b", 3:"c", 4:"d", 5:"e"}

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
dictionary = dict(zip(list1, list2))
print(dictionary)


# In[ ]:




