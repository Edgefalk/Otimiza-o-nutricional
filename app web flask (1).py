#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install Flask


# In[1]:


from flask import Flask

app = Flask(__name__)


# In[2]:


@app.route('/escolher-alimentos')
def escolher_alimentos():
    return '''
        <form method="POST" action="/resultado">
            <p>Escolha os alimentos para sua dieta:</p>
            <label>Refeição 1:</label><br>
            <input type="text" name="refeicao1"><br>
            <label>Refeição 2:</label><br>
            <input type="text" name="refeicao2"><br>
            <label>Refeição 3:</label><br>
            <input type="text" name="refeicao3"><br><br>
            <input type="submit" value="Enviar">
        </form>
    '''


# In[3]:


@app.route('/resultado', methods=['POST'])
def resultado():
    refeicao1 = request.form['refeicao1']
    refeicao2 = request.form['refeicao2']
    refeicao3 = request.form['refeicao3']
    
    # Aqui, podemos utilizar alguma lógica para calcular as refeições ideais para o objetivo de hipertrofia.
    # Por exemplo, podemos utilizar a fórmula de cálculo de calorias e macronutrientes:
    # Calorias totais = peso em kg x 30-40 kcal
    # Proteína = peso em kg x 1,8-2,2g
    # Carboidratos = calorias totais x 0,5-0,6 / 4
    # Gorduras = calorias totais x 0,2-0,3 / 9
    
    # Para simplificar, vamos apenas exibir as refeições escolhidas pelo usuário.
    return f'''
        <p>Sua dieta para hipertrofia:</p>
        <ul>
            <li>Refeição 1: {refeicao1}</li>
            <li>Refeição 2: {refeicao2}</li>
            <li>Refeição 3: {refeicao3}</li>
        </ul>
    '''


# In[4]:


if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




