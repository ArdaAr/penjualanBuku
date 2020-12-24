from main import user
from database import *

class run():
    def login(self,db,objRun):
        print('='*10+'Selamat Datang di Books Console Store'+'='*10)
        print('Silakan Login Terlebih Dahulu')
        a = int(input('Anda akan login sebagai :\n1. Pembeli\n2. Admin\n3. Daftar Jika belum memiliki akun\n= '))
        if a==1:
            self.loginUser(db,objRun)
        elif a==2:
            print("admin soon")
        else :
            self.daftar(db)
    
    def loginUser(self,db,objRun):
        username = input("Masukkan Username\n= ")
        pw = input("Masukkan Password\n= ")
        val = (username,)
        query = "SELECT * FROM CUSTOMER WHERE username=%s"
        try:
            db.cursor.execute(query,val)
            dataUser = db.cursor.fetchone()
            db.conn.commit()
            objUser = user(dataUser[1],dataUser[2],dataUser[3],dataUser[4],dataUser[5],dataUser[6])
            if pw == objUser.password:
                print("SELAMAT DATANG KEMBALI {}".format(objUser.nama))
                print(objUser.email)
                objUser.menuUser(objRun,db)
            else:
                print("Maaf kata sandi yang anda masukkan salah!")
                self.loginUser(db,objRun)
        except:
            print("Maaf Username yang anda masukkan salah, silakan ulangi...")
            self.loginUser(db,objRun)

    def loginAdmin(self):
        # coding ndek kene jul
        ''

    def daftar(self,db):
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
            self.loginUser(db)
        except mysql.connector.Error as e:
            print(e)
            self.daftar(db)

program1 = run()
program1.login(db1, program1)
