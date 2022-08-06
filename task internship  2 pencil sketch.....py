#!/usr/bin/env python
# coding: utf-8

# # Image to pencil sketch using python

# # Task:4

# # Name:Shivani kadam

# In[26]:


import numpy as np


# In[27]:


import cv2
import matplotlib.pyplot as plt
plt.style.use('seaborn')


# # Original Image

# In[28]:


img = cv2.imread(r"C:\Users\shivu\Downloads\dog.webp")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure(figsize=(8,8))
plt.imshow(img)
plt.axis("off")
plt.title("Original Image")
plt.show()


# # GrayScale Image

# In[29]:


img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure(figsize=(8,8))
plt.imshow(img_gray,cmap="gray")
plt.axis("off")
plt.title("GrayScale Image")
plt.show()


# # Final Sketch Image

# In[30]:


img_invert = cv2.bitwise_not(img_gray)
img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
final = cv2.divide(img_gray, 255 - img_smoothing, scale=255)
plt.figure(figsize=(8,8))
plt.imshow(final,cmap="gray")
plt.axis("off")
plt.title("Final Sketch Image")
plt.show()


# # Concantenate two frames

# In[31]:



plt.figure(figsize=(20,20))
plt.subplot(1,2,1)
plt.imshow(img)
plt.axis("off")
plt.title("Original Image")
plt.subplot(1,2,2)
plt.imshow(final,cmap="gray")
plt.axis("off")
plt.title("Final Sketch Image")
plt.show()


# In[ ]:





# In[ ]:




