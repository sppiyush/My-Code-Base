#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing the required modules to interact with OS and get access to file explorer
import os, shutil


# In[2]:


#We will select the path of the Folder where we have to sort the files 
path=r"C:/Users/Piyush-PC/Documents/Data-Analytics-Bootcamp/" 


# In[5]:


#Inside the variable "file_name", we are storing all the files of the chosen folder
file_name = os.listdir(path)
print(file_name)


# In[11]:


#Creating directories in a specified path if they do not already exists 
#Declaring an array of the file names we have to create
folder_names = ['csv files','image files','text files']
for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])


# In[15]:


#For all the files in file_name folder we will now use shutil.move()
# to move a file or directory to another location [shutil.move(source path,destination path)]
for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".png" in file and not os.path.exists(path + "png files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)
    else:
        print("These are the files in the folder that were not moved and remain at the same place!")

