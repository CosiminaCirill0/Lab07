from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO
    def read_biblioteca_from_db(self):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            query = "SELECT * FROM biblioteca ORDER BY nome"
            cursor = cnx.cursor()
            cursor.execute(query)

            results = []
            for row in cursor:
                biblioteca = Biblioteca(*row)
                results.append(biblioteca)

            cursor.close()
            cnx.close()
            return results
        return None

