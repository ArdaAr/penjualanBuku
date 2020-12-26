from pembelian import pembelian
from buku import buku
from person import user
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
            print("admin soon")
        else:
            self.daftar(db,objRun)

    def menuUser(self,objRun,db,objUser):
        objBuku = buku()
        pilihan = int(input('===== Menu Books Console Store =====\n1. Lihat Daftar Semua Buku\n2. Daftar Buku Berdasarkan kategori\n3. Daftar Buku Berdasarkan Harga\n4. Keluar\n= '))
        if pilihan==1:
            objBuku.show()
            return self.opsiBeli(objRun,db,objUser)
        elif pilihan==2:
            objBuku.showCategory()
            return self.opsiBeli(objRun,db,objUser)
        elif pilihan==3:
            objBuku.showHarga()
            return self.opsiBeli(objRun,db,objUser)
        elif pilihan==4:
            self.keluar(objRun,db,objUser)
        else:
            print("maaf pilihan anda tidak dikenali")
            self.menuUser(objRun,db,objUser)
    
    def keluar(self, objRun, db, objUser):
        print("="*20+"Sampai Jumpa {}".format(objUser.nama)+"="*20)
        self.login(db, objRun)
    
    def opsiBeli(self,objRun,db,objUser):
        opsi = int(input("1. Beli Buku\n2. kembali\n= "))
        if opsi == 1:
            return self.beli(objUser,objRun,db)
        else:
            return self.menuUser(objRun,db,objUser)

    def beli(self,objUser,objRun,db):
        id = int(input("Masukkan ID Buku : "))
        objBuku = buku()
        buy = pembelian()
        objBuku.getDataBuku(id)
        buy.getDataPembelian(objUser,objBuku)
        buy.catatPesanan(db)
        buy.showPembelian(objUser,objBuku)
        beliLagi = int(input("Apa ada membeli lagi ?\n1. ya\n2. tidak\n= "))
        if beliLagi==1:
            buy.nominal += self.menuUser(objRun,db,objUser)
        print("Total yang harus anda adalah : ",buy.nominal)
        return buy.nominal

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
            if pw == objUser.password:
                print("SELAMAT DATANG KEMBALI {}".format(objUser.nama))
                print(objUser.email)
                return self.menuUser(objRun,db,objUser)
            else:
                print("Maaf kata sandi yang anda masukkan salah!")
                return self.loginUser(db,objRun)
        else:
            print("Maaf Username yang anda masukkan salah, silakan ulangi...")
            self.loginUser(db,objRun)

    def loginAdmin(self):
        # coding ndek kene jul
        ''

    def daftar(self,db,objRun):
        print("="*20+"Register Books Console Store"+"="*20)
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