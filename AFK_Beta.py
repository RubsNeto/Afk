import pyautogui
import time
from datetime import datetime
from tkinter import *
import schedule

'''
Sistemas_digitais = 'http://meet.google.com/bbo-vnbe-dvb'
#Geometria_analitica = 'https://meet.google.com/rqi-todf-hrg'
Algoritmos = 'https://meet.google.com/jzy-awks-yhx'
#Matematica_discreta = 'meet.google.com/pqz-tskn-rhb'

'''

aulas = list
aulas = ['https://meet.google.com/jzy-awks-yhx',#Ap2
'http://meet.google.com/bbo-vnbe-dvb', # sistemas
'http://meet.google.com/bbo-vnbe-dvb' # sistemas
]
hoje = 1

parar = 0

root = Tk()

def abrir_aula_automatico():

    #pyautogui.alert('Código vai começar.')
    pyautogui.PAUSE = 0.5

    pyautogui.press('winleft')

    pyautogui.write('Google Chrome')
    pyautogui.press('enter')

    time.sleep(1)

    pyautogui.moveTo(270,17)
    pyautogui.mouseDown()
    pyautogui.mouseUp()

    pyautogui.write(f'{aulas[hoje-1]}')
    pyautogui.press('enter')


    time.sleep(10)

    pyautogui.moveTo(686,736)
    pyautogui.mouseDown()
    pyautogui.mouseUp()

    pyautogui.moveTo(1254,601)
    pyautogui.mouseDown()
    pyautogui.mouseUp()

    time.sleep(1)

    pyautogui.alert('Aula iniciada com sucesso!')


def abrir_aula():
    
    with open("link.txt",'r') as file:
        link = file.read()

    pyautogui.moveTo(1254,601)
    pyautogui.mouseDown()
    pyautogui.mouseUp()

    pyautogui.moveTo(1254,601)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    
    #pyautogui.alert('Código vai começar.')
    pyautogui.PAUSE = 0.5

    pyautogui.press('winleft')

    pyautogui.write('Google Chrome')
    pyautogui.press('enter')

    time.sleep(1)

    pyautogui.moveTo(270,17)
    pyautogui.mouseDown()
    pyautogui.mouseUp()

    pyautogui.write(f'{link}')
    pyautogui.press('enter')

    time.sleep(10)

    pyautogui.moveTo(686,736)
    pyautogui.mouseDown()
    pyautogui.mouseUp()

    time.sleep(5)

    pyautogui.hotkey('ctrl','e')

    time.sleep(5)

    pyautogui.moveTo(1254,601)
    pyautogui.mouseDown()
    pyautogui.mouseUp()

    time.sleep(1)

    pyautogui.alert('Aula iniciada com sucesso!')


def dia():
    hoje = datetime.today().isoweekday()
    print('entrou')

    with open("link.txt",'w') as file:
        file.write(Link_aula.get())

    hora_aula = StringVar()
    hora_aula.set(horario_aula.get())
    hora_aula_str = str(horario_aula.get())
    print(hora_aula_str)

    
    #if(hoje < 4):
    schedule.every().day.at(hora_aula_str).do(abrir_aula)



root.title('AFK')
root.iconbitmap('Imagem/Icone.ico')
root.geometry('350x300')

img = PhotoImage(file="Imagem/logo1.png")

Escrita_Link_aula = Label(root,
text='Digite o link da aula')

Escrita_horario_aula = Label(root,text='Digite o horario da aula')

Link_aula = Entry(root,width=35)
horario_aula = Entry(root)

espaco_branco1 = Label()
espaco_branco2 = Label()

Botao = Button(root,
text='Entrar na aula',
command=dia)

espaco_branco1.grid(row=0)
espaco_branco2.grid(row=1)
imagem_logo = Label(root,image= img).grid(columnspan=2)
Escrita_Link_aula.grid(row=5,column=0,sticky=W)
Link_aula.grid(row=5,column=1,sticky=W)
Escrita_horario_aula.grid(row=6,column=0,sticky=W)
horario_aula.grid(row=6,column=1,sticky=W)
Botao.grid(row=7,column=1,sticky= E)

root.mainloop()

while True:
    schedule.run_pending()
    time.sleep(1)




