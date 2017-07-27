
# coding: utf-8

# In[1]:


import requests

url_suzhou = "https://api.darksky.net/forecast/3e5af14d3d36118b4d7eb9aa71b9771f/31.29897,120.58529"

response = requests.get(url_suzhou)
data = response.json()


# Right now it is TEMPERATURE degrees out and SUMMARY. Today will be TEMP_FEELING with a high of HIGH_TEMP and a low of LOW_TEMP. RAIN_WARNING.

# In[16]:


temperature = str(data['currently']['temperature'])
temperature


# In[3]:


summary = data['currently']['summary']
summary


# In[4]:


if temperature > 86:
    TEMP_FEELING = 'hot'
elif temperature > 68:
    TEMP_FEELING = 'warm'
elif temperature > 50:
    TEMP_FEELING = 'moderate'
else:
    TEMP_FEELING = 'cold'    


# In[17]:


high_temp = str(data['daily']['data'][0]['temperatureMax'])
high_temp


# In[18]:


low_temp = str(data['daily']['data'][0]['temperatureMin'])
low_temp


# In[12]:


if data['daily']['icon'] == 'rain':
    RAIN_WARNING = 'Bring your umbrella!'
else:
    RAIN_WARNING = 'Probably no rain today.'


# In[19]:


text = 'Right now it is '+temperature+' degrees out and '+summary+". Today will be "+TEMP_FEELING+' with a high of '+high_temp+' and a low of '+low_temp+'. '+RAIN_WARNING 


# In[20]:


text


# In[28]:


import datetime

data_time = datetime.datetime.fromtimestamp(int(data['daily']['data'][0]['time'])).strftime('%Y-%m-%d %H:%M:%S')[0:10]


# In[29]:


subject = "8AM Weather forecast: "+data_time


# In[30]:


subject


# In[33]:


key = 'key-f82e20099e7292ce61cae6fdcd478e85'


# In[35]:


requests.post(
        "https://api.mailgun.net/v3/sandbox11918e1a9deb4fa5bbe61daa6c1b04f8.mailgun.org/messages",
        auth=("api", key),
        data={"from": "Mailgun Sandbox <postmaster@sandbox11918e1a9deb4fa5bbe61daa6c1b04f8.mailgun.org>",
              "to": "Xinyi <xz2656@columbia.edu>",
              "subject": subject,
              "text": text})


# In[ ]:




