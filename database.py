import sqlite3


class eventDb: #padrão de banco de dados, criando quatro querys: create event table, insert event, select event, select manager
    CREATE_EVENT_TABLE_QUERY = ('CREATE TABLE IF NOT EXISTS events(name text, day date, event_name text)')
    INSERT_EVENT_QUERY = 'INSERT INTO events (name, day, event_name) VALUES (?,?,?)'
    SELECT_EVENT_QUERY = 'SELECT event_name FROM events WHERE day = ?'
    SELECT_MANAGER_QUERY = 'SELECT name FROM events WHERE day = ?'
    
    
    def __init__(self): #inicia o banco de dados
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.CREATE_EVENT_TABLE_QUERY)
        self.connection.commit()
    
    def insert_event(self,name,day,event_name): #insere os valores com o commit
        self.cursor.execute(self.INSERT_EVENT_QUERY,(name,day,event_name))
        self.connection.commit()

    def select_event(self,day): #fetchall
        self.cursor.execute(self.SELECT_EVENT_QUERY,(day,))
        return self.cursor.fetchall()

    def select_name(self,day): #fetchall
        self.cursor.execute(self.SELECT_MANAGER_QUERY,(day,))
        return self.cursor.fetchall()

    def __del__(self): #fecha o banco de dados
        self.connection.close()