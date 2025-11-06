import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.LIGHT

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    # funzione che gestisce il messaggio di alert
    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    # funzione che gestisce il controller e lo setta
    def set_controller(self, controller):
        self.controller = controller

    # funzione per fare l'update della pagina
    def update(self):
        self.page.update()

    # FUNZIONE CHE GESTISCE L'INTERFACCIA GRAFICA CON L'UTENTE
    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
# dropdown per selezionare il museo da vedere
        self.selezione_musei = ft.Dropdown(label = "Museo",
                                          width = 400,
                                          hint_text = "Seleziona il nome del museo",
                                          on_change = self.controller.popola_dropdown_musei()
                                          )

# dropdown per selezionare l'epoca dell'artefatto
        self.epoca = ft.Dropdown(label = "Epoca",
                                 width = 200,
                                 hint_text = "Seleziona l'epoca dell'artefatto",
                                 on_change=self.controller.popola_dropdown_epoche()
                                 )

        # --- Sezione 3: Artefatti ---
# bottone per confermare il filtraggio degli artefatti
        self.mostra_artefatti = ft.ElevatedButton(text = "Mostra Artefatti")

# listview per mostrare i risultati richiesti (in caso di mancanza viene sollecitato l'alert)
        self.list_view = ft.ListView()


        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)


        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            ft.Row([self.selezione_musei, self.epoca],
                   alignment = ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            # Sezione 3: Artefatti
            self.mostra_artefatti
        )

        self.page.scroll = "adaptive"
        self.page.update()

    # funzione che cambia il tema della pagina
    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
