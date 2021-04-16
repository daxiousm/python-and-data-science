#!/usr/bin/env python
# coding: utf-8

# 1. Write a python script to print your name and age

# In[ ]:


a = input("Name")

b = int(input("Age"))

print("Your name is : ", a, " Your age is : ", b)


# 2. Create a list of your 5 favorite movies and store it in the variable

# In[ ]:


favorite_movies = ['Bourne triology','Good will hunting','James bond','mission impossible','the wire']


# 3. Write a Python program to display the first and last colors from the following list. 
# color_list = ["Red","Green","White" ,"Black"]

# In[ ]:


color_list = ["Red","Green","White" ,"Black"]
 
print(color_list[0],color_list[-1])


# 4. Write a Python script to add a key to a dictionary
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
# 

# In[ ]:


sample_dictionary = {0:10, 1:20}
print(sample_dictionary)
sample_dictionary.update({2:30})
print(sample_dictionary)


# 5. Write a Python program to calculate body mass index.

# In[ ]:


height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

# the formula for calculating bmi

bmi = weight/(height**2) 


print("Your BMI is: {0} and you are: ".format(bmi), end='')


# 6. Guess a number game - between 1 to 9.

# In[ ]:



import random

a=int(input("enter a number")) 

b= random.randint(1, 10)

while a!= b:

    b= int(input('Guess a number between 1 to 10 '))

print('Well guessed!')


# 7. Create a tuple with different data types

# In[ ]:


different_data=("data types", True, 10.2, 7)
print(different_data)


# 8.Create a list of 5 city names and convert it into tuples.

# In[ ]:


city-names = ('Addis Ababa','Lisbon','London','Paris','Seychelles')
sample-city = list(city_names)
city-names = tuple(sample-city)


# 9. Remove duplicated from the list:
#    a = [10,20,30,20,10,50,60,40,80,50,40] and store the values in the same list.
#    

# In[ ]:


list_with_duplicates = [10,20,30,20,10,50,60,40,80,50,40]
list_without_duplicates = list(set(list_with_duplicates))
print(list_without_duplicates)


# 10. Accept a string from user and remove the characters which have odd index values of a given string and print them.

# In[ ]:


insert_chr = input()

new_chr = ""

for i in range(len(insert_chr)):

    if i%2==0:

        new_chr = new_chr+insert_chr[i]

print(new_chr)

