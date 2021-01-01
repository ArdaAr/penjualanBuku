# from database import db1
from buku import buku

class Person():
    def __init__(self, nama, username, password):
        self.nama = nama
        self.username = username
        self.__password = password
    
    def getNama(self):
        print(self.nama)
    
    def cekPassword(self, pw):
        if pw == self.__password:
            return True
        return False

class admin(Person):
    def __init__(self,nama,username,password):
        super().__init__(nama, username, password)
        self.id = None

    def tambahStok(self,db1):
        print("Silakan masukkan data buku yang ingin ditambah : ")
        judul = input("Masukkan Judul Buku : ")
        kategori = input("Masukkan Kategori Buku : ")
        harga = int(input("Masukkan Harga Buku : "))
        penerbit = input("Masukkan Penerbit Buku : ")
        stok = int(input("Masukkan Jumlah Stok Buku : "))
        # stok = int(input("Masukkan Stok Buku : "))
        # buku1 = buku(id,judul,kategori,harga,penerbit,stok)
        # buku1.stokNambah()
        query = "insert into BUKU(Nama_Buku,Kategori_buku,Harga,Penerbit,stok) values(%s,%s,%s,%s,%s)"
        val = (judul,kategori,harga,penerbit,stok)
        db1.cursor.execute(query,val)
        db1.conn.commit()
        print("====== Buku Berhasil Ditambahkan ======")

    def tambahJumlahStok(self):
        objBuku = buku()
        id = int(input("Masukkan ID Buku yang akan ditambahkan stok"))
        objBuku.getDataBuku(id)
        stok = int(input("Masukkan Jumlah Stok yang ditambahkan : "))
        objBuku.stokNambah(stok)

    def lihatPesanan(self,db1):
        query = "SELECT ID_pesanan,Nama_Customer,Nama_Buku,Tanggal,quantity FROM Customer c join PESANAN p on c.id_customer=p.id_customer join buku b on p.id_buku=b.id_buku"
        db1.cursor.execute(query)
        all = db1.cursor.fetchall()
        for i in all:
            for data in i:
                print(data, end=" ")
            print()

    def hapusStok(self,db1):
        id = input("masukkan id dari data yang akan di hapus : ")
        sql = "DELETE FROM BUKU WHERE ID_Buku=%s"
        val = (id,)
        db1.cursor.execute(sql,val)
        db1.conn.commit()
        print("====== Buku dengan ID {} Berhasil dihapus ======".format(id))
        
class user(Person):
    def __init__(self, nama, alamat, email, noHp, username, password):
        super().__init__(nama,username, password)
        self.id = None
        self.email = email
        self.noHp = noHp
        self.alamat = alamat

    def setId(self,id):
        self.id = id
    
    def beliBuku(self,all):
        no = int(input("Pilih Buku Berdasarkan Urutan : ")) - 1
        objBuku = buku(all[no][0],all[no][1],all[no][2],all[no][3],all[no][4])
        print(objBuku.judul)