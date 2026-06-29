#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import easyocr


# In[2]:


st.header("Welcome to Image Extraction....")
img=st.text_input("Please enter your image path....")
if st.button("Please click to extract text"):
    reader=easyocr.Reader(['hi','en'])
    txt=reader.readtext(img)
    for x in txt:
        st.write(x[1])
    st.success('This is done')


# In[ ]:




