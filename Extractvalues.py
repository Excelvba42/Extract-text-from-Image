#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import easyocr
from PIL import Image
import numpy as nm


# In[3]:


st.set_page_config("Welcome to Application",layout='wide')
st.header("📄 AI-Powered Image to Text Extractor")
st.caption(
    "📌 Note: This application currently extracts text written in English (EN) and Hindi (HI) only."
)
path=st.file_uploader("Upload Image..")
if st.button("Extract text"):
    img=Image.open(path)
    img=nm.array(img)
    reader=easyocr.Reader(['hi','en'])
    txt=reader.readtext(img)
    for x in txt:
        st.write(x[1])
    st.success("Done")


# In[ ]:





# In[ ]:




