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
    # funzione che prende il valore selezionato nel dropdown
    def on_museo_change(self, e):
        valore = e.control.value
        self.museo_selezionato = None if valore == "Nessun filtro" else valore

    def on_epoca_change(self, e):
        valore = e.control.value
        self.epoca_selezionata = None if valore == "Nessun filtro" else valore


    # AZIONE: MOSTRA ARTEFATTI
    def mostra_artefatti(self):
        (lista1, lista2) = self._model.get_artefatti_filtrati(self._view.selezione_musei.value, self._view.epoca.value)
        if len(lista1) == 1:
            # il museo è stato selezionato (uno solo)
            for artefatto in lista2:
                print(artefatto)
        elif lista1 is None and len(lista2) == 1:
            # nessuna selezione nel museo, ma epoca selezionata
            for museo in lista1:
                print(museo)
        else:
            for museo in lista1:
                print(museo)
            for artefatto in lista2:
                print(artefatto)