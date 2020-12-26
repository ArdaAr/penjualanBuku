from database import db1

class buku():
    def __init__(self):
        self.id = None
        self.judul = None
        self.kategori = None
        self.harga = None
        self.penerbit = None
    
    def stokNambah(self):
        query = "INSERT INTO BUKU(nama_buku,kategori_buku,harga,penerbit) VALUES(%s,%s,%s,%s)"
        db1.write(query,self.judul,self.kategori,self.harga,self.penerbit)

    def getDataBuku(self,id):
        data = self.getByID(id)
        for i in data:
            self.id = i[0]
            self.judul = i[1]
            self.kategori = i[2]
            self.harga = i[3]
            self.penerbit = i[4]
    
    def getByID(self,id):
        db1.getConn()
        sql = "Select * from Buku where ID_Buku=%s"       
        val = (id,)
        db1.cursor.execute(sql,val)    
        return self.showData()

    def show(self, *argv):
        if len(argv)==0:
            buku = self.showAll()
        elif len(argv)==1:
            buku = self.showCategory(argv[0])
        else:
            buku = self.showHarga(argv[0],argv[1])
        return buku

    def showAll(self):
        db1.getConn()
        sql = "select * from buku"
        db1.cursor.execute(sql)
        return self.showData()
    
    def showCategory(self):
        kategori = input("Masukkan Kategori Buku : ")
        db1.getConn()
        sql = "Select * from Buku where kategori_buku=%s"       
        val = (kategori,)
        db1.cursor.execute(sql,val)    
        return self.showData()
        
    def showHarga(self):
        hargaMin = int(input("Masukkan Harga Minimal : "))
        hargaMax = int(input("Masukkan Harga Maksimal : "))
        db1.getConn()
        sql = "Select * from Buku where Harga between %s and %s"       
        val = (hargaMin,hargaMax)
        db1.cursor.execute(sql,val)
        return self.showData()

    def showData(self):
        all = db1.cursor.fetchall()    
        if len(all)>0:
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
            return all
        else:
            print("Maaf Kategori yang anda inputkan tidak ada !")

# b1 = buku()
# b1.getDataBuku()
# print(b1.judul)