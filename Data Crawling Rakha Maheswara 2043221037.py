#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install bs4


# In[4]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[5]:


page = requests.get('https://www.guinnessworldrecords.com/records/hall-of-fame/')


# In[6]:


page.content


# In[7]:


soup = BeautifulSoup(page.content, 'html.parser')


# In[8]:


soup


# In[15]:


rekor = soup.find_all('div', class_='carousel-item-caption')


# In[16]:


rekor


# In[21]:


data_nama = []
data_achive = []

for rekors in rekor:
    nama = rekors.find('h4').text
    achive = rekors.find('p').text
    data_nama.append(nama)
    data_achive.append(achive)


# In[24]:


data = {
    'Nama ' :data_nama,
    'penghargaan ':data_achive
}


# In[25]:


pd.DataFrame(data)


# In[26]:


pd.DataFrame(data).to_excel('TugasProkomDataCrawling.xlsx')


# In[ ]:




