# from person import user
# from getpass import getpass

# class login():

#     def login(self,db,objRun):
#         username = input("Masukkan Username\n= ")
#         pw = getpass("Masukkan Password\n= ")
#         val = (username,)
#         query = "SELECT * FROM CUSTOMER WHERE username=%s"
#         db.cursor.execute(query,val)
#         dataUser = db.cursor.fetchone()
#         db.conn.commit()
#         if (dataUser):
#             objUser = user(dataUser[1],dataUser[2],dataUser[3],dataUser[4],dataUser[5],dataUser[6])
#             objUser.setId(dataUser[0])
#             if pw == objUser.password:
#                 print("SELAMAT DATANG KEMBALI {}".format(objUser.nama))
#                 print(objUser.email)
#                 return self.menuUser(objRun,db,objUser)
#             else:
#                 print("Maaf kata sandi yang anda masukkan salah!")
#                 return self.loginUser(db,objRun)
#         else:
#             print("Maaf Username yang anda masukkan salah, silakan ulangi...")
#             self.loginUser(db,objRun)

#     def loginAdmin(self,db,objRun):
#         username = input("Masukkan Username\n= ")
#         pw = getpass("Masukkan Password\n= ")
#         val = (username,)
#         query = "SELECT * FROM ADMIN WHERE username=%s"
#         db.cursor.execute(query,val)
#         dataAdmin = db.cursor.fetchone()
#         db.conn.commit()
#         if (dataAdmin):
#             objAdmin = admin(dataAdmin[0],dataAdmin[1],dataAdmin[2],dataAdmin[3])
#             if pw == objAdmin.password:
#                 print("SELAMAT DATANG KEMBALI {}".format(objAdmin.nama))
#                 return self.menuAdmin(db,objAdmin)
#             else:
#                 print("Maaf kata sandi yang anda masukkan salah!")
#                 return self.loginAdmin(db,objRun)
#         else:
#             print("Maaf Username yang anda masukkan salah, silakan ulangi...")
#             self.loginAdmin(db,objRun)