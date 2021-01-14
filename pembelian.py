from datetime import date
from database import db1
today = date.today()

class pembelian():
    def __init__(self):
        self.idPesanan = None
        self.idBuku = None
        self.idCustomer = None
        self.tanggal = None
        self.nominal = 0
        self.quantity = None
    
    def setQuantity(self):
        qty = int(input("Masukkan jumlah : "))
        while qty <= 0:
            print("!!! Maaf jumlah yang anda masukkan tidak valid !!!")
            qty = int(input("Masukkan jumlah : "))
        self.quantity = qty
        
    
    def setTanggal(self):
        today = date.today()
        self.tanggal = today.strftime("%b-%d-%Y")

    def setID(self,db):
        query = "select ID_PESANAN from PESANAN order by ID_PESANAN DESC limit 1"
        db.cursor.execute(query)
        id = db.cursor.fetchone()
        if id==None:
            self.idPesanan = 1
            return self.idPesanan
        self.idPesanan = id[0] +1
        return self.idPesanan
    
    def getTanggal(self):
        return self.tanggal

    def catatPesanan(self, db):
        sql = "INSERT INTO Pesanan(ID_PESANAN,ID_Buku,ID_Customer,quantity) VALUES(%s,%s,%s,%s)"
        val = (self.idPesanan,self.idBuku,self.idCustomer,self.quantity)
        db.cursor.execute(sql,val)
        db.conn.commit()

    def showPembelian(self,db):
        query = "SELECT ID_pesanan,Nama_Customer,Nama_Buku,Tanggal,quantity,Harga FROM Customer c join PESANAN p on c.id_customer=p.id_customer join buku b on p.id_buku=b.id_buku where ID_PESANAN=%s"
        val = (self.idPesanan,)
        db.cursor.execute(query,val)
        data = db.cursor.fetchall()
        print("===== REKAP DATA PEMBELIAN =====")
        print("Id Pembelian : {}".format(data[0][0]))
        print("Nama : {}".format(data[0][1]))
        print("Judul Buku yang akan dipesan : ")
        for i in range(len(data)):
            print("- {}".format(data[i][2]))
            print("  jumlah : {}".format(data[i][4]))
            # self.nominal += data[i][5]
        print("Tanggal : {}".format(self.tanggal))
        print("Jumlah yang harus dibayar : {}".format(self.nominal))

    def getDataPembelian(self,objUser,objBuku):
        self.setTanggal()
        self.setQuantity()
        while self.quantity > objBuku.stok:
            print("Maaf Stok buku tidak mencukupi")
            self.setQuantity()
        self.idCustomer = objUser.id
        self.idBuku = objBuku.id
        self.nominal += self.quantity*objBuku.harga
        return self.nominal
buy = pembelian()