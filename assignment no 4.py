#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question1:
person_dict={"first_name":"Muhammad Asad","last_name":"Ahmed","age":"22","city":"Sukkur"}
for key, value in person_dict.items():
    print(key+" : "+value)
print("\n Add qualification \n")
person_dict["qualification"]="Intermediate"
for key, value in person_dict.items():
    print(key+" : "+value)
print("\n New qualification \n")
person_dict["qualification"]="BCom"
for key, value in person_dict.items():
    print(key+" : "+value)


# In[8]:


#Q2
cities={
    "Lahore":{
        "country":"pakistan",
        "population":11188000,
        "fact":"Lahore is the  province of Punjab. It is the second largest and most beautiful city in Pakistan"
    },
    "Karachi":{
        "country":"pakistan",
        "population":14741000,
        "fact":"Karachi is contribute 70 per cent of income tax."
    },
    "Islamabad":{
        "country":"pakistan",
        "population":195049,
        "fact":"Islamabad is the capital of pakistan."
    },
}
for citykey,cityinfo in cities.items():
    print("\n"+citykey+"\n")
    for city in cityinfo:
        print(city+" : "+str(cityinfo[city]))


# In[11]:


#Q3
for i in range(1,4):
    age = int(input("Enter your age: "))
    if age>0 and age<3:
        print("The ticket for you is free.")
    elif age>3 and age<13:
        print("The tick for you us $10.")
    else:
        print("The ticket for you is $15.")


# In[13]:


#Q4
def favorite_book(title):
    print("One of my favorite books is", title)
favorite_book("Smart way to learn phyton")


# In[14]:


#Q5
import random
c=0
rNumber=0
while c<3:
    rNumber=int(random.randrange(1,30))
    userNumber=int(input("Enter number between 1 and 30: "))
    c=c+1
    if rNumber>userNumber:
        print("Hidden number is greater\n")
    elif rNumber<userNumber:
        print("Hidden number is Smaller\n")
    else:
        print("Hidden number is equal\n")


# In[ ]:




