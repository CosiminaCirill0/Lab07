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
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown_biblioteche(self):
        #Popola i dropdown nella View prendendo i dati dal Model
        self._view.dd_biblioteca.options.clear()
        # Aggiunge l'opzione di default "Nessun Filtro" (chiave vuota = nessun filtro applicato)
        self._view.dd_biblioteca.options.append(ft.dropdown.Option(key="", text="Nessun Filtro"))

        biblioteche = self._model.get_biblioteche()

        if biblioteche is not None:
            for biblioteca in biblioteche:
                # Imposta l'ID come chiave (usato per le query SQL) e il Nome come testo visibile
                self._view.dd_biblioteca.options.append(ft.dropdown.Option(key=str(biblioteca.id), text=biblioteca.nome)
                )
        else:
            self._view.show_alert("Errore nel caricamento delle biblioteche.")

        self._view.update()

    def popola_dropdown_generi(self):
        self._view.dd_genere.options.clear()
        self._view.dd_genere.options.append(ft.dropdown.Option(key="", text="Nessun Filtro"))

        generi = self._model.get_generi()

        if generi is not None:
            for genere in generi:
                self._view.dd_genere.options.append(ft.dropdown.Option(key=genere, text=genere))
        else:
            self._view.show_alert("Errore nel caricamento dei generi.")

        self._view.update()

    # CALLBACKS DROPDOWN
    # TODO
    def on_biblioteca_change(self, e):
        valore = e.control.value
        self.biblioteca_selezionata = None if valore in (None, "", "None") else valore

    def on_genere_change(self, e):
        valore = e.control.value
        self.genere_selezionato = None if valore in (None, "", "None") else valore

    # AZIONE: MOSTRA LIBRI
    # TODO
    def handle_mostra_libri(self, e):
        """
                Viene eseguito al click sul pulsante 'Mostra Libri':
                1. Estrae le opzioni correntemente selezionate nei Dropdown.
                2. Normalizza i valori vuoti o 'Nessun Filtro' convertendoli in None.
                3. Valida la presenza di almeno un filtro attivo.
                4. Richiede al Model la lista dei libri corrispondenti e la mostra nella ListView.
                """
        val_biblio = self._view.dd_biblioteca.value
        val_genere = self._view.dd_genere.value

        biblioteca = None if val_biblio in (None, "", "None") else val_biblio
        genere = None if val_genere in (None, "", "None") else val_genere

        # Se entrambi i filtri sono disattivati, mostra un messaggio di alert
        if biblioteca is None and genere is None:
            self._view.show_alert("Selezionare almeno un filtro (Biblioteca o Genere).")
            return

        self._view.lista_libri.controls.clear()

        # Interrogazione del modello con i filtri applicati
        lista_libri = self._model.get_libri_filtrati(biblioteca, genere)

        if lista_libri is None:
            self._view.show_alert("Errore di connessione al database.")
        elif len(lista_libri) == 0:
            self._view.show_alert("Nessun libro trovato per i criteri selezionati.")
        else:
            for libro in lista_libri:
                self._view.lista_libri.controls.append(ft.Text(f"{libro}"))

        self._view.update()