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
