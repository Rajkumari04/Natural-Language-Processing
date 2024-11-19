#!/usr/bin/env python
# coding: utf-8

# In[3]:


acronym = "NLP"
full_form ="Natural Language Processing"
print(f"{acronym}stands for {full_form }")


# In[5]:


with open('contats.txt', 'w') as file:
    file.write('Name,Phone,email\n')


# In[8]:


with open('contacts.txt', 'w') as file: 
    file.write('Name,Phone,email\n')
with open('contacts.txt','r') as file:
    field = file.read()
    print(field)


# In[11]:


get_ipython().system('pip install PyPDF2')
from PyPDF2 import PdfReader

pdf_path = "/Business_Proposal.pdf"

reader = PdfReader(pdf_path)

page_2_text = reader.pages[1].extract_text()
print(page_2_text)


# In[15]:


page_2_text = """<AUTHORS:
Amy Baker, Finance Chair, x345, abaker@ourcompany.com
Chris Donaldson, Accounting Dir., x621, cdonaldson@ourcompany.com
Erin Freeman, Sr. VP, x879, efreeman@ourcompany.com>"""

with open("contacts.txt", "a") as file:
    file.write("\n" + page_2_text)

print("Text successfully appended to contacts.txt")


# In[16]:


import re

page_2_text = """<AUTHORS:
Amy Baker, Finance Chair, x345, abaker@ourcompany.com
Chris Donaldson, Accounting Dir., x621, cdonaldson@ourcompany.com
Erin Freeman, Sr. VP, x879, efreeman@ourcompany.com>"""

email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

email_addresses = re.findall(email_pattern, page_2_text)

print(email_addresses)


# In[ ]:




