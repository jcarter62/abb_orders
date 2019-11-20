from abbconnection import AbbConnection
import pyodbc


class Laterals:

    def __init__(self):
        con_str = AbbConnection().connection_string
        self.connection = pyodbc.connect(con_str)
        self.cursor = self.connection.cursor()
        self.lats = self.getLaterals()
        return


    def getLaterals(self) -> []:
        result = []
        self.cursor.execute('select id, latname from lat;')
        rows = self.cursor.fetchall()
        for row in rows:
            result.append({'id': row[0], 'lat': row[1]})
        return result

