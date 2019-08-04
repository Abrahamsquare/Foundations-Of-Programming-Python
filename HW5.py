#!/usr/bin/env python
"""
Created on Tue Jul 28 19:44:04 2019

@author: Abraham G Abraham
Class:Foundations Of Programming: Python
Assignment 5
HW5.py
Dependencies : Python 3.7


Question

How Can I break my script if the user choices other than option 1-5 example 6,7,8,9

"""


infile = "C:\Foundations Of Programming Python\ToDo.txt"

# read in ToDo.txt
with open(infile, 'r') as todo_file:
    lines = todo_file.readlines()
  
task_dict = {}
    
for line in lines:
   task = line.split(",")[0].strip()
   priority = line.split(",")[1].strip()
   task_dict[task] = priority
   

while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()#adding a new line

    # Choice 1 -Show the current items in the table
    if (strChoice.strip() == '1'):
        # loop through the dictionary here and print items
        if (strChoice.strip() == '1'):
            for key,value in task_dict.items():
                print(key,value)
    
    # Choice 2 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        task_new = input("What is the task?: ")
        if task_new not in task_dict:
           priority_new = input("whats the priority of the task?: ") 
           task_dict[task_new] = priority_new
           print("\n",task_new, "has been added")
        else:
            print("That task already exists!")
   
    # Choice 3 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        remove_key = input("Enter the task name to remove: ")
        if remove_key in task_dict.keys():
            del task_dict[remove_key]
            print(remove_key,"has been deleted")
        else:
            print(remove_key,"doesn't exist in the dictionary")
   
    # Choice 4 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        # open a file handle
        user_save = input("Would you like to save your info? Type yes or no:")
         # loop through key, value and write to file
        if user_save.lower() == "yes":
            with open("ToDo.txt","w") as op:
                for key,value in task_dict.items():
                    outline = "{},{}\n".format(key,value)
                    op.write(outline)
                    
        else:
                        print("Have a lovely day!")
        
        # Chocie 5- end the program
    elif (strChoice == '5'):break



    

