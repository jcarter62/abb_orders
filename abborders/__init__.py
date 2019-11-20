from abbconnection import AbbConnection
import pyodbc


class AbbOrders:

    def __init__(self):
        con_str = AbbConnection().connection_string
        self.connection = pyodbc.connect(con_str)
        self.cursor = self.connection.cursor()
        return

    def get_orders(self, lateral='') -> []:
        result = []
        qt = "'"
        if lateral == '':
            cmd = 'sp_abb_orders_detail;'
        else:
            cmd = 'sp_abb_orders_detail @lateral=' + qt + lateral + qt + ';'

        self.cursor.execute(cmd)
        rows = self.cursor.fetchall()
        for row in rows:
            result.append({
                'latname': row[0],
                'turnout': row[1],
                'field': row[2],
                'flow': row[3],
                'account': row[6],
                'name': row[7],
                'active': row[13]
            })
        return result

    def get_orders_summary(self, lateral='') -> []:
        result = []
        qt = "'"
        if lateral == '':
            cmd = 'sp_abb_orders_detail @summary=1;'
        else:
            cmd = 'sp_abb_orders_detail @summary=1, @lateral=' + qt + lateral + qt + ';'

        self.cursor.execute(cmd)
        rows = self.cursor.fetchall()
        for row in rows:
            result.append({
                'latname': row[0],
                'flow': row[1]
            })
        return result

    def getLaterals(self) -> []:
        result = []
        self.cursor.execute('select id, latname from lat;')
        rows = self.cursor.fetchall()
        for row in rows:
            result.append({'id': row[0], 'lat': row[1]})
        return result

