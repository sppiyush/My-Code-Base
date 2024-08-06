#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator 

# In[7]:


#We will first take the inputs here 
# We need to convert these into integers so that we can multiply the inputs with 703
name = input("Enter Your name :- ")
weight = int(input("Enter your weight in pounds:-  "))
height = int(input("Enter your height in inches:-  ")) 

#Formula to calculate the BMI of a person 
BMI = (weight * 703) / (height * height)
print(BMI);


# In[8]:


if BMI>0:
    if(BMI<18.5):
        print(name + ", you are underweight.")
    elif(BMI<=24.9):
        print(name + ", you are normal weight.")
    elif(BMI<29.9):
        print(name + ", you are overweight. You need to exercise more and stop sitting and writing so many python tutorials")
    elif(BMI<34.9):
        print(name + ", you are obese.")
    elif(BMI<39.9):
        print(name + ", you are severly obese.")
    else:
        print(name + ", you are morbidly obese.")
else:
    print("Enter valid Inputs!")


# In[ ]:


#@piyushpkcorp@gmail.com

