import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def popola_dropdown_musei(self):
        for elemento in self._model.get_musei():
            self._view.selezione_musei.options.append(ft.dropdown.Option(elemento))

    def popola_dropdown_epoche(self):
        for elemento in self._model.get_epoche():
            self._view.epoca.options.append(ft.dropdown.Option(elemento))

    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA ARTEFATTI
    # TODO
