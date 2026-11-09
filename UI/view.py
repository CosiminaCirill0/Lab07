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
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # TODO
        # Menu a tendina per la selezione della biblioteca
        self.dd_biblioteca = ft.Dropdown(
            label="Biblioteca",
            width=400
        )
        # Popola le opzioni del menu chiamando il controller
        self.controller.popola_dropdown_biblioteche()

        # Menu a tendina per la selezione del genere
        self.dd_genere = ft.Dropdown(
            label="Genere",
            width=220
        )
        # Popola le opzioni del menu chiamando il controller
        self.controller.popola_dropdown_generi()

        # Sezione 3: Libri
        # TODO
        # Pulsante che attiva il filtraggio
        btn_mostra_libri = ft.Button(
            "Mostra Libri",
            on_click=self.controller.handle_mostra_libri
        )
        # Contenitore scorrevole per la visualizzazione dinamica dei libri trovati
        self.lista_libri = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)


        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            # TODO
            ft.Row(spacing=20,
                   controls=[self.dd_biblioteca, self.dd_genere],
                   alignment= ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            # Sezione 3: Libri
            # TODO
            ft.Row(spacing=200,
                   controls=[btn_mostra_libri],
                   alignment=ft.MainAxisAlignment.CENTER),

            # Contenitore bordato per delimitare visivamente la ListView
            ft.Container(
                content=self.lista_libri,
                height=250,
                border=ft.Border.all(1, ft.Colors.BLACK),
                padding=5,
            )
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
