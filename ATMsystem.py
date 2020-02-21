#!/usr/bin/env python
# coding: utf-8

# In[3]:


amount = int(input("enter ur amount: "))
notes = [2000,500,100,50]
rem_amt = amount
note_count = []
for note in notes:
    if rem_amt >= note:
        c = rem_amt // note
        note_count.append(c)
        rem_amt %= note
    else:
        note_count.append(0)
else:
    for note in zip(notes,note_count):
        if note[1]:
            print(*note)
       


# In[ ]:




