from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        self.cnx = ConnessioneDB.get_connection()

    # funzione che ricava i vari artefatti
    def get_epoca(self):
        cursor = self.cnx.cursor()
        query = """SELECT * FROM artefatto"""
        cursor.execute(query)
        lista_epoche = cursor.fetchall()
        cursor.close()
        self.cnx.close()
        return lista_epoche

    # funzione che restituisce gli artefatti scelti dall'utente
    def get_artefatto_utente(self, e):
        cursor = self.cnx.cursor()
        query = """SELECT nome 
                    FROM artefatto
                    WHERE epoca = COALESCE(%s, epoca)"""
        cursor.execute(query, (e,))  # , serve per evitare errore con un solo parametro
        self.cnx.close()
        lista_artefatto_utente = cursor.fetchall()
        cursor.close()
        return lista_artefatto_utente