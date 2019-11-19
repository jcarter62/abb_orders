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


'''
declare @lat varchar(20) = '%';
declare @now datetime = '2/13/2019 08:00 am'

/*
  List active orders at specific time.
*/

select 
	l.LatName, 
	o.Turnout_ID, 
	f.FieldName,
	o.flow, o.EffectiveTime as Start, o.OffDateTime as Stop, 
	o.Name_ID as Account, isnull( n.fullname, '') as Account_Name
from orders o
join latTurnout lt on o.Turnout_ID = lt.turnout_id
join lat l on lt.latid = l.id 
left join NAME n on o.Name_ID = n.NAME_ID
left join fields f on o.Field_ID = f.FIELD_ID
where (@now between o.EffectiveTime and o.OffDateTime) and (l.LatName like @lat)
order by l.LatName, o.Turnout_ID
'''