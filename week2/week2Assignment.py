#!/usr/bin/env python
# coding: utf-8

# #Q1

# In[5]:


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return 'FizzBuzz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'
    return input
print(fizz_buzz(60))


# #Q2

# In[19]:


lst = [5, 10, 20]
for i in range(len(lst)):
    try:
        print(i, lst[i])
    except IndexError:
        None


# #Q3
# 

# In[11]:


class Jets:

    def __init__(self, name, country):
        self.name = name
        self.country = country
        
        
        
first_item = Jets("F16", "DANMARK")


a=first_item.name
b=first_item.country
print(a, b)


# #Q4
# 

# In[20]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[21]:


df = pd.read_csv('gender_submission.csv')
df.head()


# In[22]:



df.info()


# #Q5

# In[23]:


d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)


# #Q6

# In[27]:


def shownumber(limit):
    for i in range(0, limit):
        if i==0:
            print(i,end='')
            print('EVEN')
        elif i%2==0:
            print(i,end='')
            print('EVEN')
        else:
            print('ODD')
    
print(shownumber(5))      


# #Q7
# 

# In[29]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[30]:


df = pd.read_csv('creditcard.csv')
df.head()


# In[31]:


print(pd.read_csv('creditcard.csv'))


# #Q8

# In[36]:


class Person:
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname  = lastname
  def display(self):
    print("your first name is " + self.firstname)
    print("your last name is " + str(self.lastname))
    
p = Person("Dax", "Wen")
p.display()


# #Q9

# In[40]:


def int_input(prompt):
    while True:
        try:
            age = int(input(prompt))
            return age
        except ValueError as e:
            print("Not a proper integer! Try it again")


# #Q10
# 

# In[39]:


class Student:
    pass 
class Marks:
    pass 
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("\nTo Check whether the said classes are subclasses of the built-in class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object)) 


# In[ ]:




