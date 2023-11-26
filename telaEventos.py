import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime
from database import *
import os

database = eventDb()

class allEvents: #classe dos eventos já existentes
    def tela_eventos():
        with open ('dates.txt', 'r') as f:
            for linhas in f.readlines():
                data = linhas.strip("\n").strip(":")[0:10]
            
                if not (database.select_event(data)): #caso não tenah recebido a data no banco de dados, envia mensagem de erro
                    f.close()
                    os.remove("dates.txt")
                    messagebox.showerror(title = 'Erro',message = 'Sem eventos neste dia.')
            
        tela_secundaria = tk.Tk() #interface
        tela_secundaria.geometry("250x400")
        tela_secundaria.minsize(250,400)
        tela_secundaria.maxsize(250,400)
        tela_secundaria.title("DIA DOS EVENTOS:")
        estilo_titulo_tela_secundaria = Label(tela_secundaria, bg="black", width=180, height=6)
        estilo_titulo_tela_secundaria.pack()

        titulo_secundaria = Label(tela_secundaria, text="EVENTOS DO DIA: "+data, font=("EVENTOS DO DIA:", 12), bg="black", fg="white",)
        titulo_secundaria.pack()
        titulo_secundaria.place(x=15, y=35)


        event_name_text = Label(tela_secundaria, text="Nome do evento:", font=("Nome do evento:",12), bg="green", fg="white",)
        event_name_text.place(x=60, y=110)

        event_name = Label(tela_secundaria, text=str(database.select_event(data)[0]),font=14,fg="black",)
        event_name.pack()
        event_name.place(x=50, y=150)

        event_nomes_text = Label(tela_secundaria, text="Nome do organizador:", font=("Nome do organizador:",12), bg="green", fg="white",) #texto pra aparecer "nome do criador do evento"
        event_nomes_text.place(x=45, y=200)

        nomes_secundaria = Label(tela_secundaria, text=str(database.select_name(data)[0]),font=14,fg="black",)
        nomes_secundaria.pack()
        nomes_secundaria.place(x=35, y=250)

        tela_secundaria.mainloop() #mainloop