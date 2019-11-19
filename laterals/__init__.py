import pyodbc


class Laterals:

    def __init__(self):
        self.connection = pyodbc.connect(self.con_string())
        self.cursor = self.connection.cursor()
        self.lats = self.getLaterals()
        return

    @staticmethod
    def con_string() -> str:
        server = 'DESKTOP-PU1J78F\SQLSVR'
        database = 'wmis_ibm'
        driver = 'DRIVER={ODBC Driver 17 for SQL Server}'
        result = driver + ';SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes;'
        return result

    def getLaterals(self) -> []:
        result = []
        self.cursor.execute('select id, latname from lat;')
        rows = self.cursor.fetchall()
        for row in rows:
            result.append({'id': row[0], 'lat': row[1]})
        return result
