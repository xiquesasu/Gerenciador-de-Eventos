import tkinter as tk
from tkinter import *

class finalScreen(): #classe para a ultima tela

    def tela_final():

        tela_final = tk.Tk() #interface
        tela_final.geometry("250x400")
        tela_final.minsize(250,400)
        tela_final.maxsize(250,400)
        tela_final.title("TELA FINAL:")
        estilo_titulo_tela_final = Label(tela_final)
        estilo_titulo_tela_final.pack()

        event_name = Label(tela_final, text=('Agradecemos a preferência!'),font=("Agradecemos a preferência!", 12), fg="black",)
        event_name.pack()
        event_name.place(x=35, y=150)

        titulo_final = Label(tela_final, text=('Evento salvo.'),font=("Evento Salvo.", 12), fg="black", bg= "green",)
        titulo_final.pack()
        titulo_final.place(x=80, y=350)

        tela_final.mainloop() #mainloop