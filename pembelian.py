from datetime import date, datetime
today = date.today()

class pembelian():
    def __init__(self):
        self.idBuku = None
        self.idCustomer = None
        self.tanggal = None
        self.nominal = 0
        self.quantity = None
    
    def setQuantity(self):
        qty = int(input("Masukkan jumlah : "))
        self.quantity = qty
    
    def setTanggal(self):
        today = date.today()
        self.tanggal = today.strftime("%b-%d-%Y")
    
    def getTanggal(self):
        return self.tanggal
    
    def showPembelian(self,objUser,objBuku):
        print("=========== Rekap Pembelian ===========")
        print("Id buku : {}".format(self.idBuku))
        print("Judul Buku : {}".format(objBuku.judul))
        print("Id Customer : {}".format(self.idCustomer))
        print("Nama Customer : {}".format(objUser.nama))
        print("Alamat : {}".format(objUser.alamat))
        print("Jumlah pembelian : {}".format(self.quantity))
        print("Jumlah Harga : {} x {} = {}".format(objBuku.harga,self.quantity,self.nominal))
        print("Tanggal Pembelian : {}".format(self.getTanggal()))
        return self.nominal

    def catatPesanan(self, db):
        sql = "INSERT INTO Pesanan(ID_Buku,ID_Customer,Tanggal,quantity) VALUES(%s,%s,%s,%s)"
        val = (self.idBuku,self.idCustomer,self.tanggal,self.quantity)
        db.cursor.execute(sql,val)
        db.conn.commit()

    def getDataPembelian(self,objUser,objBuku):
        self.setTanggal()
        self.setQuantity()
        self.idCustomer = objUser.id
        self.idBuku = objBuku.id
        self.nominal = self.quantity*objBuku.harga
        return self.nominal
        