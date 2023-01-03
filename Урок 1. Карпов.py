#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 1.4 Задания первого урока(шаг 2)
age = 34
name = "Dmitry"


# In[4]:


# 1.4 Задания первого урока(шаг 3)
user_info = ["Dmitry","Fedin",100000.00,5]


# In[5]:


# 1.4 Задания первого урока(шаг 4)
salaries = [42, 100, 70, 80]
first = salaries[0]


# In[6]:


# 1.4 Задания первого урока(шаг 5)
users=[]
users.extend(['Voronov',42])


# In[7]:


# 1.4 Задания первого урока(шаг 6)
user_ages = [10, 18, 21, 35, 42, 27, 12, 16]
for i in user_ages:
    if i > 18:
        print(i)


# In[3]:


# 1.4 Задания первого урока(шаг 7)
worker = ['Dmitry', 'Fedin', 350000, 1]
user_name = worker[0]
user_name = worker[0]
user_family = worker[1]
years = worker[3]
position = ''
if years < 2:
    position='junior'
elif years >= 2 and years < 5:
    position='middle'
else:
    position='senior'
    print (status.format(user_name=user_name,user_family=user_family,position=position))   


# In[4]:


# 1.4 Задания первого урока(шаг 8)
values = [12, 134, 10, 47, 100, 20, 50, 160, 210]
tens=[]
for i in values:
    if i%10==0:
        tens.append(i)
print(tens)


# In[5]:


# 1.4 Задания первого урока(шаг 9)
workers = [['Ivan', 'Ivanov', 100000, 1], ['Petr', 'Petrov', 150000, 2], ['Sidor', 'Sidorov', 200000, 5]]
for i in workers:
    status = '{user_name} {user_family} is {position}'
    user_name = i[0]
    user_family = i[1]
    years = i[3]
    position = ''
    if years < 2:
        position='junior'
    elif years >= 2 and years <= 5:
        position='middle'
    else:
        position='senior'
    print (status.format(user_name=user_name,user_family=user_family,position=position))


# In[6]:


# 1.4 Задания первого урока(шаг 9)

workers = [['Ivan', 'Ivanov', 100000, 2], ['Petr', 'Petrov', 150000, 2], ['Sidor', 'Sidorov', 200000, 3]]
for i in workers:
    status = '{} {} is {}'
    years = i[-1]
    if years < 2:
        position ='junior'
    elif years >= 2 and years <= 5:
        position ='middle'
    elif years > 5:
        position ='senior'
    status = status.format(i[0],i[1],position)
    print(status)


# In[11]:


# 1.4 Задания первого урока(шаг 10)
# Поместите в список lst числа от 0 (n = 0) до 10 включительно (N = 10) c шагом 2 (dn = 2). Для этого используйте условие while.
lst = []
n = 0
while n >= 0 and n <= 10:
    if n % 2 == 0:
        lst.append(n)
        n = n + 1
    else:
        n = n + 1


# In[12]:


lst


# In[15]:


# 1.4 Задания первого урока(шаг 11)
salaries_dict = {"name":"Masha","surname":"Volkova","age":25,"salary":60000,"position":"junior"}
print(salaries_dict["name"])


# In[18]:


# 1.4 Задания первого урока(шаг 12)

users_dict = {
    "mvolkova":{"name":"Masha","surname":"Volkova","age":25,"salary":60000,"position":"junior"},
    "pvoronov":{"name":"Peter","surname":"Voronov","age":27,"salary":100000,"position":"junior"},
    "pparker":{"name":"Peter","surname":"Parker","age":35,"salary":150000,"position":"middle"},
    "akarpov":{"name":"Anatoly","surname":"Karpov","age":30,"salary":250000,"position":"senior"}
}

