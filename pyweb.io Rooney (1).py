#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pywebio


# In[2]:


from pywebio import start_server
from pywebio.input import *

def perder_peso():
    put_text("Escolha suas refeições para perder peso")

def ganhar_massa():
    put_text("Escolha suas refeições para ganhar massa muscular")

def cafe_da_manha():
    put_text("Escolha seu café da manhã")

def almoco():
    put_text("Escolha seu almoço")

def jantar():
    put_text("Escolha seu jantar")

def dieta():
    objetivo = radio("Qual o seu objetivo?", options=["Perder peso", "Ganhar massa muscular"])
    
    if objetivo == "Perder peso":
        perder_peso()
    else:
        ganhar_massa()
        
    refeicao = select("Qual refeição você deseja escolher?", options=["Café da manhã", "Almoço", "Jantar"])
    
    if refeicao == "Café da manhã":
        cafe_da_manha()
    elif refeicao == "Almoço":
        almoco()
    else:
        jantar()

if __name__ == '__main__':
    start_server(dieta, port=80)


# In[ ]:




