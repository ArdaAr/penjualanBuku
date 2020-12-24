class buku():
    def __init__(self,  judul, kategori, penerbit, harga):
        self.judul = judul
        self.kategori = kategori
        self.penerbit = penerbit
        self.harga = harga
    
    def stokNambah(self,db1):
        query = "INSERT INTO BUKU(nama_buku,kategori_buku,harga,penerbit) VALUES(%s,%s,%s,%s)"
        db1.write(query,self.judul,self.kategori,self.harga,self.penerbit)