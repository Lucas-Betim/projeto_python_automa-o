# pyautogui

import pyautogui
import time

# pyautogui.click clica
# pyautogui.write escreve
# pyautogui.press pressiona uma tecla
# pyautogui.hotkey pressiona uma combinação de teclas

pyautogui.PAUSE = 0.5 # tempo de espera entre cada comando para não encavalar os comandos

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login' # link do sistema

# Passos do programa
# Passo 1 entrar no sistema da empresa
# Abrir navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

pyautogui.write(link)
pyautogui.press('enter')
# Pausa maior para carregar site 
time.sleep(3)

# Passo 2 fazer login
# clicar no campo de e-mail
pyautogui.click(x=786, y=376) 
pyautogui.write('lucas@gmail.com')
# clicar no campo de senha
pyautogui.press('tab')
pyautogui.write('senhadificilparacaramba')
# clicar no botão de login
pyautogui.press('tab')
pyautogui.press('enter')
# Pausa maior para carregar site 
time.sleep(3)

# Passo 3 abrir base de dados 
# Pandas e openpyxl
import pandas 

tabela_produtos = pandas.read_csv('produtos.csv')
print(tabela_produtos)

# para cada linha da tabela executar o passo 4 
for linha in tabela_produtos.index:  # .index para pegar o número de linhas da tabela
    # Passo 4 cadastrar um produto
    # clicar no botão de cadastrar produto   
    pyautogui.click(x=756, y=263) 
    codigo = tabela_produtos.loc[linha, 'codigo'] # pegar o código da linha atual
    pyautogui.write(codigo)
    pyautogui.press('tab') # passar para o próximo campo

    # marca
    marca = tabela_produtos.loc[linha, 'marca'] # pegar a marca da linha atual
    pyautogui.write(marca)
    pyautogui.press('tab') 

    # tipo
    tipo = tabela_produtos.loc[linha, 'tipo'] # pegar o tipo da linha atual
    pyautogui.write(str(tipo))
    pyautogui.press('tab') 

    # tipcategoria
    categoria = tabela_produtos.loc[linha, 'categoria'] # pegar a categoria da linha atual
    pyautogui.write(str(categoria))
    pyautogui.press('tab') 

    # preco_unitario
    preco = tabela_produtos.loc[linha, 'preco_unitario'] # pegar o preço da linha atual
    pyautogui.write(str(preco))
    pyautogui.press('tab') 

    # custo
    custo = tabela_produtos.loc[linha, 'custo'] # pegar o custo da linha atual
    pyautogui.write(str(custo))
    pyautogui.press('tab') 

    # obs
    obs = tabela_produtos.loc[linha, 'obs'] # pegar a obs da linha atual
    if obs != 'nan': # verificar se a obs não é nula
        pyautogui.write(str(obs))
    pyautogui.press('tab') 

    # clicar no botão de salvar produto
    pyautogui.press('enter')
    # voltar par o inicio da tela
    pyautogui.scroll(1000) # scroll para cima

# Passo 5 repetir passo 4 ate o fim da lista de produtos

