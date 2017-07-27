
# coding: utf-8

# In[4]:


from bs4 import BeautifulSoup
import requests


# In[5]:


response = requests.get('https://www.wsj.com/')
doc = BeautifulSoup(response.text, 'html.parser')


# In[6]:


headlines = doc.find_all('h3')
headlines


# In[8]:


email_text = ''
for headline in headlines[0:10]:
    email_text = email_text+"\n"+ headline.text.strip()
    
print(email_text)


# In[10]:


key = 'key-f82e20099e7292ce61cae6fdcd478e85'
requests.post(
        "https://api.mailgun.net/v3/sandbox11918e1a9deb4fa5bbe61daa6c1b04f8.mailgun.org/messages",
        auth=("api", key),
        data={"from": "Mailgun Sandbox <postmaster@sandbox11918e1a9deb4fa5bbe61daa6c1b04f8.mailgun.org>",
              "to": "Xinyi <xz2656@columbia.edu>",
              "subject": 'News headlines from WSJ',
              "text": email_text})


# In[ ]:




