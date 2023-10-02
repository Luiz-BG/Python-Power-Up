# importar bibliotecas necessárias
import pyautogui
import time
pyautogui.PAUSE = 0.5 #Setar uma pausa para o computador carregar

# abrir o opera
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

# espera o opera abrir
time.sleep(5)

# entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# esperar o site carregar
time.sleep(3)

# fazer login
pyautogui.click(x=998, y=487)
pyautogui.write("luizeduardobritogomes@gmail.com")

# escrever senhapera
pyautogui.press("tab")
pyautogui.write("sua senha aqui")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(5)

# importar base da dados
import pandas 

tabela = pandas.read_csv('produtos.csv') #importar o banco de dados de um arquivo csv
print(tabela)

for linha in tabela.index:  #para cada linha dentro da lista, execute X
 # for coluna in tabela.columns:  para cada coluna dentro da lista, execute x

    # cadastrar um produto manualmente
    pyautogui.press("tab")

    codigo = tabela.loc[linha, "codigo"]  # linha, coluna


    # preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))


    #apertar para enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(50000)