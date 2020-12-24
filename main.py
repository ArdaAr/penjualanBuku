from database import db1
import buku

class Person():
    def __init__(self, nama):
        self.nama = nama
    
    def getNama(self):
        print(self.nama)

class admin(Person):
    def __init__(self, nama, umur,):
        self.umur = umur
        super().__init__(nama)

    def tambahStok(self):
        print("Silakan masukkan data buku yang ingin ditambah : ")
        judul = input("Masukkan Judul Buku : ")
        kategori = input("Masukkan Kategori Buku : ")
        harga = int(input("Masukkan Harga Buku : "))
        penerbit = input("Masukkan Penerbit Buku : ")
        buku1 = buku(judul,kategori,penerbit,harga)
        buku1.stokNambah()
    
    def lihatPesanan(self):
        query = "SELECT * FROM PESANAN"
        db1.show(query)
    
    def hapusStok(self):
        query = "DELETE FROM buku WHERE ID=%s"
        db1.delete(query)

# class buku():
#     def __init__(self,  judul, kategori, penerbit, harga):
#         self.judul = judul
#         self.kategori = kategori
#         self.penerbit = penerbit
#         self.harga = harga
    
#     def stokNambah(self):
#         query = "INSERT INTO BUKU(nama_buku,kategori_buku,harga,penerbit) VALUES(%s,%s,%s,%s)"
#         db1.write(query,self.judul,self.kategori,self.harga,self.penerbit)


class user(Person):
    def __init__(self, nama, alamat, email, noHp, username, password):
        super().__init__(nama)
        self.email = email
        self.noHp = noHp
        self.password = password
        self.username = username
        self.alamat = alamat
    
    def menuUser(self,objRun,db):
        pilihan = int(input('===== Menu Books Console Store =====\n1. Lihat Daftar Semua Buku\n2. Daftar Buku Berdasarkan kategori\n3. Daftar Buku Berdasarkan Harga\n4. Keluar\n= '))
        if pilihan==1:
            self.lihatDaftarBuku(db)
        elif pilihan==2:
            self.listByCategory(db)
        elif pilihan==3:
            self.listByPrice(db)
        elif pilihan==4:
            self.keluar(objRun,db)
        else:
            print("maaf pilihan anda tidak dikenali")
            self.menuUser()
    
    def beliBuku(self):
        pass

    def lihatDaftarBuku(self,db):
        sql = "select * from buku"
        db.show(sql)
    
    def listByCategory(self,db):
        kategori = input("Masukkan Kategori Buku : ")
        query = "Select * from Buku where kategori_buku=%s"
        db.show(query,kategori)
    
    def listByPrice(self,db):
        hargaMin = int(input("Masukkan Harga Minimal : "))
        hargaMax = int(input("Masukkan Harga Maksimal : "))
        query = "Select * from Buku where Harga between %s and %s"
        db.show(query,hargaMin,hargaMax)
    
    def isiData(self):
        pass

    def keluar(self, objRun, db):
        print("="*20+"Sampai Jumpa {}".format(self.nama)+"="*20)
        objRun.login(db, objRun)