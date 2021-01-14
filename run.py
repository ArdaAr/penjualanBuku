from pembelian import pembelian
from buku import buku
from person import admin, user
from database import *
from getpass import getpass

class run():
    def login(self,db,objRun):
        print('='*10+'Selamat Datang di Books Console Store'+'='*10)
        print('Silakan Login Terlebih Dahulu')
        a = int(input('Anda akan login sebagai :\n1. Pembeli\n2. Admin\n3. Daftar Jika belum memiliki akun\n= '))
        if a==1:
            self.loginUser(db,objRun)
        elif a==2:
            self.loginAdmin(db,objRun)
        elif a==3:
            self.daftar(db,objRun)
        else:
            print("!!! Maaf pilihan anda tidak dikenali !!!")
            self.login(db,objRun)

    def menuUser(self,objRun,db,objUser):
        objBuku = buku()
        pilihan = int(input('========== Menu Books Console Store ==========\n1. Lihat Daftar Semua Buku\n2. Daftar Buku Berdasarkan kategori\n3. Daftar Buku Berdasarkan Harga\n4. Keluar\n= '))
        if pilihan==1:
            objBuku.show()
            self.opsiBeli(objRun,db,objUser)
        elif pilihan==2:
            objBuku.showCategory()
            self.opsiBeli(objRun,db,objUser)
        elif pilihan==3:
            objBuku.showHarga()
            self.opsiBeli(objRun,db,objUser)
        elif pilihan==4:
            self.keluar(objRun,db,objUser)
        else:
            print("maaf pilihan anda tidak dikenali")
            self.menuUser(objRun,db,objUser)

    def keluar(self, objRun, db, obj):
        print("="*10+" Sampai Jumpa {} ".format(obj.nama)+"="*10)
        self.login(db, objRun)
    
    def opsiBeli(self,objRun,db,objUser):
        opsi = int(input("1. Beli Buku\n2. Kembali\n= "))
        if opsi == 1:
            return self.beli(objUser,objRun,db)
        elif opsi ==2:
            return self.menuUser(objRun,db,objUser)
        else :
            self.opsiBeli(objRun,db,objUser)

    def beli(self,objUser,objRun,db):
        id = int(input("Masukkan ID Buku : "))
        query = "Select * from Buku where ID_BUKU=%s"
        val = (id,)
        db1.cursor.execute(query,val)
        data = db1.cursor.fetchone()
        while data == None:
            print("Maaf ID Buku tidak ada silakan masukkan kembali")
            id = input("Masukkan ID Buku : ")
            val = (id,)
            db1.cursor.execute(query,val)
            data = db1.cursor.fetchall()
        objBuku = buku()
        buy = pembelian()
        buy.setID(db)
        objBuku.getDataBuku(id)
        buy.getDataPembelian(objUser,objBuku)
        buy.catatPesanan(db)
        objBuku.stokBerkurang(buy.quantity)
        # buy.showPembelian(objUser,objBuku)
        beliLagi = int(input("Apa ada membeli lagi ?\n1. ya\n0. tidak\n= "))
        while beliLagi:
            id = int(input("Masukkan ID Buku : "))
            objBuku.getDataBuku(id)
            buy.getDataPembelian(objUser,objBuku)
            buy.catatPesanan(db)
            objBuku.stokBerkurang(buy.quantity)
            beliLagi = int(input("Apa ada membeli lagi ?\n1. ya\n0. tidak\n= "))
        buy.showPembelian(db)
        print("="*20)
        back = int(input("Tekan 1 Untuk Kembali ke Menu Utama = "))
        while back != 1:
            print(" !!! Inputan anda salah !!! ")
            back = int(input("Tekan 1 Untuk Kembali ke Menu Utama = "))
        self.menuUser(objRun,db,objUser)
        # print("Total yang harus anda adalah : ",buy.nominal)

    def loginUser(self,db,objRun):
        username = input("Masukkan Username\n= ")
        pw = getpass("Masukkan Password\n= ")
        val = (username,)
        query = "SELECT * FROM CUSTOMER WHERE username=%s"
        db.cursor.execute(query,val)
        dataUser = db.cursor.fetchone()
        db.conn.commit()
        if (dataUser):
            objUser = user(dataUser[1],dataUser[2],dataUser[3],dataUser[4],dataUser[5],dataUser[6])
            objUser.setId(dataUser[0])
            if objUser.cekPassword(pw):
                print("========== SELAMAT DATANG KEMBALI {} ==========".format(objUser.nama))
                print(objUser.email)
                self.menuUser(objRun,db,objUser)
            else:
                print("Maaf kata sandi yang anda masukkan salah!")
                self.loginUser(db,objRun)
        else:
            print("Maaf Username yang anda masukkan salah, silakan ulangi...")
            self.loginUser(db,objRun)

    def menuAdmin(self,db,objAdmin,objRun):
        pilihan = int(input("masukan pilihan \n 1. lihatPesanan \n 2. hapusStok \n 3. Tambah Buku \n 4. Tambah Jumlah Stok \n 5. Keluar \n = "))
        if pilihan==1 :
            objAdmin.lihatPesanan(db)
            self.menuAdmin(db,objAdmin,objRun)
        elif pilihan==2 :
            objAdmin.hapusStok(db)
            self.menuAdmin(db,objAdmin,objRun)
        elif pilihan==3 :
            objAdmin.tambahStok(db)
            self.menuAdmin(db,objAdmin,objRun)
        elif pilihan==4 :
            objAdmin.tambahJumlahStok(db)
            self.menuAdmin(db,objAdmin,objRun)
        elif pilihan==5:
            self.keluar(objRun,db,objAdmin)
        else:
            print("!!! Maaf Pilihan anda tidak dikenali !!!")
            self.menuAdmin(db,objAdmin,objRun)
               
    def loginAdmin(self,db,objRun):
        username = input("Masukkan Username\n= ")
        pw = getpass("Masukkan Password\n= ")
        val = (username,)
        query = "SELECT * FROM ADMIN WHERE username=%s"
        db.cursor.execute(query,val)
        dataAdmin = db.cursor.fetchone()
        db.conn.commit()
        if (dataAdmin):
            objAdmin = admin(dataAdmin[1],dataAdmin[2],dataAdmin[3])
            if objAdmin.cekPassword(pw):
                print("========== SELAMAT DATANG KEMBALI {} ==========".format(objAdmin.nama))
                self.menuAdmin(db,objAdmin,objRun)
            else:
                print("Maaf kata sandi yang anda masukkan salah!")
                return self.loginAdmin(db,objRun)
        else:
            print("Maaf Username yang anda masukkan salah, silakan ulangi...")
            self.loginAdmin(db,objRun)

    def daftar(self,db,objRun):
        print("="*20+" Register Books Console Store "+"="*20)
        nama = input("Nama : ")
        alamat = input("Alamat Lengkap : ")
        email = input("Email : ")
        noHp = input("Nomor Hp : ")
        username = input("Username (digunakan untuk login) : ")
        password = input("Password : ")
        while len(password)>8:
            print("Maaf kata sandi harus mengandung maksimal 8 karakter!")
            password = input("Password : ")
        try:
            sql = "INSERT INTO Customer(Nama_Customer,Alamat,email,no_hp,username,password) VALUES(%s,%s,%s,%s,%s,%s)"
            val = (nama,alamat,email,noHp,username,password)
            db.cursor.execute(sql,val)
            db.conn.commit()
            print("Registrasi Berhasil, Silakan Login untuk melanjutkan")
            self.loginUser(db,objRun)
        except mysql.connector.Error as e:
            print(e)
            self.daftar(db,objRun)

program1 = run()
program1.login(db1, program1)