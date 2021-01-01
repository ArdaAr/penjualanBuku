class private():
    def __init__(self,bil1):
        self.__bil1 = bil1

    def cetak(self):
        return self.__bil1

    def jumlah(self,x):
        pass    

class turunan(private):
    def __init__(self, password):
        super().__init__(password)

    def x(self):
        print(5 +self.cetak())

a = private('addssda')
turun = turunan(1)
# print('class parent')
# a.cetak()
# print('class turunan')
# turun.cetak()
print(turun.x())