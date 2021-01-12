#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


img = cv2.imread('lena.jpg', 1) # -1 = color; 0 = grey ; 1 = apha channel ; image as array


# #print (img)

# In[3]:


cv2.imshow('image', img)
cv2.waitKey(5000)
cv2.destroyAllWindows()


# In[9]:


A = input ("Do you want to save this image? t = true ; f = false")

if A == "t":
    cv2.imwrite('lena_copy.png', img) #salva como você quer 
elif A =="f":
    print ("Picture not saved")
else:
    print ("You din't put a valid key")


# In[ ]:




