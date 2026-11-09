from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    def get_generi(self):
        cnx = DBConnect.get_connection()
        results = []
        if cnx is not None:
            query = "SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL ORDER BY genere"
            cursor = cnx.cursor()
            cursor.execute(query)

            for (genere,) in cursor:
                results.append(genere)

            cursor.close()
            cnx.close()
            return results
        return None

    def get_libri_filtrati(self, id_biblioteca=None, genere=None):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore di connessione al database.")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """
                       SELECT * 
                       FROM libro 
                       WHERE id_biblioteca=COALESCE(%s, id_biblioteca) 
                       AND genere=COALESCE(%s, genere)
                   """
        cursor.execute(query, (id_biblioteca, genere))

        for row in cursor:
            result.append(row)

        cursor.close()
        cnx.close()
        return result
