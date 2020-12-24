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
            # print('Berhasil connect database')
        except mysql.connector.Error as e:
            print('Gagal connect dengan database {}'.format(e))
    
    #OVERLOADING
    def show(self, *argv):
        if len(argv)==1:
            self.showAll(argv[0])
        elif len(argv)==2:
            self.showCategory(argv[0],argv[1])
        elif len(argv)==3:
            self.showHarga(argv[0],argv[1],argv[2])
            

    def showAll(self,query):
        sql = query
        self.cursor.execute(sql)
        self.showData()
    
    def showCategory(self,query,param):
        sql = query
        val = (param,)
        self.cursor.execute(sql,val)
        self.showData()

    def showHarga(self,query,param1,param2):
        sql = query
        val = (param1,param2)
        self.cursor.execute(sql,val)
        self.showData()

    def showData(self):
        all = self.cursor.fetchall()
        print("||","  "*2,"ID","  "*2,"||",end="")
        print("  "*2,"JUDUL BUKU","  "*2,"||",end="")
        print("  "*2,"KATEGORI","  "*2,"||",end="")
        print("  "*2,"HARGA","  "*2,"||",end="")
        print("  "*2,"PENERBIT","  "*2,"||",end="")
        print()
        for i in all:
            print(" "*7,i[0], end=" "*4)
            print(" "*7,i[1], end=" "*4)
            print(" "*7,i[2], end=" "*4)
            print(" "*7,i[3], end=" "*4)
            print(" "*7,i[4], end=" "*4)
            print()

    def write(self,query,judul,kategori,harga,penerbit):
        try:
            sql = query
            val = (judul,kategori,harga,penerbit)
            self.cursor.execute(sql,val)
            self.conn.commit()
        except mysql.connector.Error as e:
            print("gagal memasukkan data : {}".format(e))

    def writeUser(self,nama,alamat,email,noHp,username,password):
        try:
            sql = "INSERT INTO CUSTOMER(Nama_Customer,Alamat,email,no_hp,username,password), VALUES(%s,%s,%s,%s,%s,%s)"
            val = (nama,alamat,email,noHp,username,password)
            self.cursor.execute(sql,val)
            self.conn.commit()
            print("Registrasi Berhasil, Silakan Login untuk melanjutkan")
        except mysql.connector.Error as e:
            print("gagal Mendaftar data : {}".format(e))

    def delete(self,query):
        try:
            id = input("masukkan id dari data yang akan di hapus : ")
            sql = query
            val = (id, )
            self.cursor.execute(sql,val)
            self.conn.commit()
            print("data dengan id : {} berhasil dihapus".format(id))
        except mysql.connector.Error as e:
            print('Gagal menghapus data : '.format(e))
    
    def update(self):
        try:
            sql = "UPDATE PENGGUNA SET nama=%s WHERE ID=%s"
            # val = (nama,id)
            # self.cursor.execute(sql,val)
            self.conn.commit()
            # print("data dengan id {} berhasil diperbarui")
        except mysql.connector.Error as e:
            print('gagal memperbarui data {}'.format(e))
            
db1 = dbConnection("localhost","root","Lowlight12","jual_buku")
db1.getConn()