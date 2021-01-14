import mysql.connector
from mysql.connector.cursor import SQL_COMMENT

class dbConnection():
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None
    
    def getConn(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as e:
            print('Gagal connect dengan database {}'.format(e))
            
db1 = dbConnection("localhost","root","Lowlight12","jual_buku")
db1.getConn()