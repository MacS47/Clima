from tkinter import *
from tkinter import ttk
import info
import datetime


# Armazenando Horário, Localização, Temperatura, Sensação Térmica e Umidade
# dentro da tupla getting

city = "Porto Alegre"

getting = info.getData(city)

# Janela
root = Tk()
root.title("Clima")
root.configure(bg="lightgray")
frm = ttk.Frame(root, padding = 10)
frm.grid()

# Criando um objeto da classe photoimage de acordo com a hora do dia
time = datetime.datetime.now()
hour = time.hour

if (hour > 5 and hour < 19):
    window_icon = PhotoImage(file = 'sun.png')
else:
    window_icon = PhotoImage(file = 'moon.png')

# Definindo a imagem como ícone da janela
root.iconphoto(False,window_icon)

# Definindo a fonte utilizada em labels
font = "Roboto"


# Função responsável por atualizar os dados dos labels
def refresh():

    # getting = info.get_info()
    getting = info.getData(city)
    local_label = Label(frm, text =f"{getting[1]}", font =("font",11)).grid(column = 0, row = 0)
    temp_label = Label(frm, text =f"{getting[2]}ºC", font =("font",18)).grid(column = 0, row = 1)
    feels_label = Label(frm, text =f"Sensação: {getting[3]}ºC", font =("font",11)).grid(column = 0, row = 2)
    humid_label = Label(frm, text =f"Umidade: {getting[4]}%", font =("font",11)).grid(column = 0, row = 3)
    description_label = Label(frm, text =f"Descrição: {getting[5]}", font =("font",11)).grid(column = 0, row = 4)
    lstupd_label = Label(frm, text =f"Atualizado: {getting[0]}", font =("font",7)).grid(column = 0, row = 8)

# Criação da estrutura e labels

local_label = Label(frm, text =f"{getting[1]}", font =("font",11)).grid(row = 0)
temp_label = Label(frm, text =f"{getting[2]}ºC", font =("font",18)).grid(column = 0, row = 1)
feels_label = Label(frm, text =f"Sensação: {getting[3]}ºC", font =("font",11)).grid(column = 0, row = 2)
humid_label = Label(frm, text =f"Umidade: {getting[4]}%", font =("font",11)).grid(column = 0, row = 3)
description_label = Label(frm, text =f"Descrição: {getting[5]}", font =("font",11)).grid(column = 0, row = 4)
Label(frm, text =f"", font =("font",7)).grid(column = 0, row = 5)
button = Button(frm, text = f"Atualizar", command = refresh, font = ("font", 11) ).grid(column = 0, row = 6)
Label(frm, text =f"", font =("font",7)).grid(column = 0, row = 7)
lstupd_label = Label(frm, text =f"Atualizado: {getting[0]}", font =("font",7)).grid(column = 0, row = 8)
data_origin = Label(frm, text =f"openweathermap.org", font =("font",7)).grid(column = 0, row = 10)

root.mainloop()