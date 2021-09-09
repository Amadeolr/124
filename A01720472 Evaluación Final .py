#!/usr/bin/env python
# coding: utf-8

# # Welcome to an example Binder

# We need `seaborn`, which shall be included it in `requirements.txt` file

# In[3]:


#Se importan las librerías y se llama a la base de datos en la que se trabajara
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance.csv')
df.head()


# In[4]:


#Esta función da información general de la base de datos y sus columnas 
df.info()


# In[5]:


#Esta función analiza las columnas con valores numéricos 
df.describe()


# In[6]:


#Aquí renombre las columnas a mi preferencia 
df.rename(columns=({'gender':'Gender','race/ethnicity':'Race/Ethnicity'
                     ,'parental level of education':'Parental_Level_of_Education'
                     ,'lunch':'Lunch','test preparation course':'Test_Preparation_Course'
                      ,'math score':'Math_Score','reading score':'Reading_Score'
                     ,'writing score':'Writing_Score'}),inplace=True)


# In[7]:


#Resultados de exámenes en base al nivel educativo
plt.figure(figsize=(10,10))
sns.catplot(x="Gender", y="Math_Score",
                 hue="Parental_Level_of_Education",
                 data=df, kind="bar")
plt.title('Resultados en base al nivel educativo')
plt.show()


# In[8]:


#Resultados de exámenes dependiendo de la preparación previa
sns.lmplot(x='Reading_Score',y='Writing_Score',hue='Test_Preparation_Course',data=df)
plt.xlabel('Reading Score')
plt.ylabel('Writing Score')
plt.title('Resultados en base a la preparacion previa')
plt.show()


# In[9]:


#Resultados dependiendo de la alimentación previa 
sns.boxplot(x=df['Lunch'],y=df['Math_Score'])
plt.show()


# In[ ]:




