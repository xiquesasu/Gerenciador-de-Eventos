import tkinter as tk
from tkinter import *
from tkcalendar import DateEntry
from datetime import datetime
from database import *
import os
from telaEventos import *
from telaFinal import *


database = eventDb()


class EventManagerApp: #Classe principal do programa
    def tela_primaria():
        def saveDates(): #salva as datas num arquivo txt, depois fecha
            with open('dates.txt', 'a') as f:
                data_evento = date_event.get_date()
                f.write("{}".format(data_evento))
                f.close()

            with open('dates.txt', 'r') as f: #abre o txt e escreve as informações
                for linha in f.readlines():
                    data_db = linha.strip("\n").strip(":")[0:10]
            f.close()

            nome_organizador = criador_evento_entry.get()
            nome_evento = nome_evento_entry.get()
            database.insert_event(nome_organizador,data_db,nome_evento)
            os.remove("dates.txt")

            tela_inicial.destroy()
            finalScreen.tela_final()

        def viewEvents():
            with open('dates.txt', 'a') as f:
                data_evento = date_event.get_date()
                f.write("{}".format(data_evento))
                f.close()

            with open('dates.txt', 'r') as f:
                for linha in f.readlines():
                    data_db = linha.strip("\n").strip(":")[0:10]
            f.close()
        
            tela_inicial.destroy()
            allEvents.tela_eventos()
            os.remove("dates.txt")


        tela_inicial = tk.Tk()  #interface
        tela_inicial.geometry("250x400")
        tela_inicial.minsize(250,400)
        tela_inicial.maxsize(250,400)
        tela_inicial.title("Gerenciador de Eventos")
        estilo_titulo_tela_principal = Label(tela_inicial, bg="black", width=180, height=6)
        estilo_titulo_tela_principal.pack()
       
        titulo_tela1 = Label(tela_inicial, text="EVENTOS:", font=("EVENTOS:", 20), bg="black", fg="white",)
        titulo_tela1.pack()
        titulo_tela1.place(x=60, y=30)

        nome_evento = Label(tela_inicial,text ="NOME DO EVENTO:", font=("NOME DO EVENTO:",10))
        nome_evento.pack()
        nome_evento.place(x=60, y=100)
        nome_evento_entry = Entry(tela_inicial, width=22, font=("calibri", 10))
        nome_evento_entry.pack()
        nome_evento_entry.place(x=45, y=120)

        criador_evento = Label(tela_inicial,text ="ORGANIZADOR:", font=("ORGANIZADOR:",10))
        criador_evento.pack()
        criador_evento.place(x=70, y=170)
        criador_evento_entry = Entry(tela_inicial, width=22, font=("calibri", 10))
        criador_evento_entry.pack()
        criador_evento_entry.place(x=45, y=190)

        data_evento = Label(tela_inicial,text ="DATA DO EVENTO:", font=("DATA DO EVENTO:",10))
        data_evento.pack()
        data_evento.place(x=60, y=260)
        

        date_event = DateEntry(tela_inicial, width=12, background='green', foreground='white', borderwidth=5, mindate = datetime(2023,11,25),
                                  maxdate = datetime(2024,5,31), showweeknumbers = False, showothermonthdays = False)
        date_event.pack(padx=10, pady=10)
        date_event.place(x=70,y=280)

        add_event = Button(tela_inicial,text="Adicionar evento", bg="green",fg="white", width=14, height=2,command=saveDates)
        add_event.pack()
        add_event.place(x=10,y=320)

        existing_events = Button(tela_inicial,text="Ver eventos", bg="green",fg="white", width=14, height=2,command=viewEvents)
        existing_events.pack()
        existing_events.place(x=120,y=320)

        tela_inicial.mainloop() #mainloop
        

