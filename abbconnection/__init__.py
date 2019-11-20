
class AbbConnection:

    def __init__(self):
        server = "sql-svr\mssqlr2"
        database = 'wmis_ibm'
        driver = 'DRIVER={ODBC Driver 17 for SQL Server}'
        self.connection_string = driver + ';SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes;'
        return
