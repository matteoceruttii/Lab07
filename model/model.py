from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        # TODO

    def get_epoche(self):
        lista_epoche = self._artefatto_dao.get_epoca()
        return lista_epoche

    # --- MUSEI ---
    def get_musei(self):
        lista_nomi = self._museo_dao.get_museum()
        lista_nomi_completa = []
        for i in range(len(lista_nomi)):
            lista_nomi_completa.append(lista_nomi[i][1])
        return lista_nomi_completa

