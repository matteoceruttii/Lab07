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
        lista_epoche = []
        for row in cursor:
            epoca = Artefatto(row[3])
            lista_epoche.append(epoca)
        cursor.close()
        self.cnx.close()
        return lista_epoche