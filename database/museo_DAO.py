from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        self.cnx = ConnessioneDB.get_connection()

    # funzione che ricava tutti i musei presenti dal database
    def get_museum(self):
        cursor = self.cnx.cursor()
        query = """SELECT * FROM museo"""
        cursor.execute(query)
        lista_musei = cursor.fetchall()
        cursor.close()
        self.cnx.close()
        return lista_musei

    # funzione che restituisce i musei scelti dall'utente
    def get_museo_utente(self, m):
        cursor = self.cnx.cursor()
        query = """SELECT nome 
                    FROM museo
                    WHERE nome = COALESCE(%s, nome)"""
        cursor.execute(query, (m,))  # , serve per evitare errore con un solo parametro
        self.cnx.close()
        lista_museo_utente = cursor.fetchall()
        cursor.close()
        return lista_museo_utente