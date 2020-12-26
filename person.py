# from database import db1
from buku import buku

class Person():
    def __init__(self, nama):
        self.nama = nama
    
    def getNama(self):
        print(self.nama)

class admin(Person):
    def __init__(self,id,nama,username,password):
        super().__init__(nama)
        self.id = id
        self.username = username
        self.password = password

    def tambahStok(self):
        print("Silakan masukkan data buku yang ingin ditambah : ")
        id = input("Masukkan ID Buku : ")
        judul = input("Masukkan Judul Buku : ")
        kategori = input("Masukkan Kategori Buku : ")
        harga = int(input("Masukkan Harga Buku : "))
        penerbit = input("Masukkan Penerbit Buku : ")
        stok = int(input("Masukkan Stok Buku : "))
        buku1 = buku(id,judul,kategori,harga,penerbit,stok)
        buku1.stokNambah()
    
    def lihatPesanan(self,db1):
        query = "SELECT * FROM PESANAN"
        db1.cursor.execute(query)
        db1.cursor.fetchall()

    def hapusStok(self,db1):
        id = input("masukan id dari data yang akan dihapus : ")
        val =(id,)
        query = "DELETE FROM buku WHERE ID_BUKU=%s"
        db1.cursor.execute(query,val)
        
        
        
        


class user(Person):
    def __init__(self, nama, alamat, email, noHp, username, password):
        super().__init__(nama)
        self.id = None
        self.email = email
        self.noHp = noHp
        self.password = password
        self.username = username
        self.alamat = alamat

    def setId(self,id):
        self.id = id
    
    def beliBuku(self,all):
        no = int(input("Pilih Buku Berdasarkan Urutan : ")) - 1
        objBuku = buku(all[no][0],all[no][1],all[no][2],all[no][3],all[no][4])
        print(objBuku.judul)
