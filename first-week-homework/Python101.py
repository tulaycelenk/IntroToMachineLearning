#!/usr/bin/env python
# coding: utf-8

# In[1]:


num=1
num2=2
print(num)


# In[4]:


myList=[1,2,3]
type(myList)


# In[3]:


myList[1]


# In[5]:


myList[1:3]


# In[7]:


myList.append(4)


# In[8]:


print(myList)


# In[9]:


myList.reverse()


# In[10]:


print(myList)


# In[11]:


myList.sort()
print(myList)


# In[12]:


myList.remove(2)
print(myList)


# In[14]:


for each in range (1,6):
	print(each)


# In[15]:


min=myList[0]
for i in myList:
    if min>i:
        min=i
print(min)


# In[16]:


a=0
while(a<4):
    a+=1
    print(a)
 


# In[17]:


def circle(r,pi=3.14):
    output=2*pi*r
    return output
circle(3)


# In[21]:


def calc(x):
    out=x*x*x
    return out
ans=calc(6)
print(ans)


# In[22]:


ans2 = lambda x: x*x
print(ans2(2))


# In[25]:


dictionary = {'tulay':22, 'ali':22 ,'mehmet':22}
print(dictionary)


# In[26]:


dictionary.keys()


# In[27]:


dictionary.values()


# In[29]:


keys = dictionary.keys()
if 'ali' in keys:
    print("olala")
else:
    print("idc")


# In[ ]:





# In[ ]:




