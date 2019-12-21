#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1
number = int(input("write a number: "))
fact = 1
for i in range(1,number+1):
    fact = fact *i
print(f'the factorial of {number} is {fact}')


# In[14]:


#Q2
uppercase,lowercase = 0,0
def f(x):
    global uppercase
    global lowercase
    for i in x:
        if str.isupper(i) == True:
            uppercase += 1
            
        else:
            lowercase += 1 
    print(f'the number of uppercase letters is :{uppercase}')
    print(f'the number of lowercase letters is :{lowercase}')
f('Asad')


# In[17]:


#Q5
num = int(input("write a number: "))
def f(a):
    for i in range(2,a):
        if (a % i) == 0:
            print("its not a prime numer")
            break
        else:
            print('its a prime number')
f(num)


# In[19]:


#Q6
def shopping(*items):
    for i in items:
        print("The user bought {i} from the market")
shopping(["shirt","pent","watch"])


# In[ ]:




