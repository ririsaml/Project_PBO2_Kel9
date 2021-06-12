import wx
import sqlite3
from MiApp import Login
from MiApp import Register
from MiApp import Penjual

class LoginController (Login):
    def __init__(self, parent):
        Login.__init__(self,parent)
        self.SetTitle ('Login')
        img = wx.Image("abstract.png", wx.BITMAP_TYPE_PNG)
        img = img.Scale(320, 309, wx.IMAGE_QUALITY_HIGH)
        self.c.SetBitmap(wx.Bitmap(img))

    def btn_login_onclick( self, event ):
        username = self.inp_usn.GetValue()
        password = self.inp_pass.GetValue()
        if username == "":
            wx.MessageBox('Username tidak boleh kosong','Warning',wx.OK | wx.ICON_WARNING)
        elif password == "":
            wx.MessageBox('Password tidak boleh kosong','Warning',wx.OK | wx.ICON_WARNING)
        else :
            con = sqlite3.connect("MiApp.db")
            cursor = con.cursor()
            data = []
            query = "SELECT * FROM user WHERE username = ? AND pass = ?"
            cursor.execute(query,(username, password))
            con.commit()
            result = cursor.fetchone()
            if (result):
                data.append(result)
                if username == "admin":
                    penjual = PenjualController(parent=self)
                    penjual.Show()
                else :
                    pembeli = PembeliController(parent=self)
                    pembeli.Show()
            else:
                wx.MessageBox('Akun tidak terdaftar, silahkan melakukan registrasi','Warning',wx.OK | wx.ICON_WARNING)
                register = RegisterController(parent=self)
                register.Show()
                return result
            con.close()

    def btn_toRegister_onclick( self, event ):
        register = RegisterController(parent=self)
        register.Show()

class RegisterController (Register):
    def __init__(self, parent):
        Register.__init__(self,parent)
        self.SetTitle ('Register')
        img = wx.Image("abstract.png", wx.BITMAP_TYPE_PNG)
        img = img.Scale(320, 309, wx.IMAGE_QUALITY_HIGH)
        self.c.SetBitmap(wx.Bitmap(img))

    def btn_regist_onclick( self, event ):
        nama = self.nama_input.GetValue()
        usn = self.usn1_input.GetValue()
        psw = self.pass1_input.GetValue()
        konfirmasi = self.kon_input.GetValue()
        if usn == "":
            wx.MessageBox('Username tidak boleh kosong','Warning',wx.OK | wx.ICON_WARNING)
        elif psw == "":
            wx.MessageBox('Password tidak boleh kosong','Warning',wx.OK | wx.ICON_WARNING)
        elif nama == "":
            wx.MessageBox('Nama tidak boleh kosong','Warning',wx.OK | wx.ICON_WARNING)
        elif konfirmasi == "":
            wx.MessageBox('Konfirmasi password tidak boleh kosong','Warning',wx.OK | wx.ICON_WARNING)
        elif konfirmasi != psw:
            wx.MessageBox('Password dan konfirmasi password tidak sesuai','Warning',wx.OK | wx.ICON_WARNING)
        else :
            con = sqlite3.connect("MiApp.db")
            cursor = con.cursor()
            cursor.execute("INSERT INTO user (username, nama, pass) VALUES (?,?,?)", (usn, nama, psw))
            con.commit()
            con.close()
            wx.MessageBox('Registrasi Berhasil!')
            login = LoginController(parent=self)
            login.Show()

class PembeliController (Pembeli):
    def __init__(self, parent):
        Pembeli.__init__(self,parent)
        self.SetTitle ('MiApp')
        self.tabel_listapk_pembeli.SetColLabelValue(0, "Kode Aplikasi")
        self.tabel_listapk_pembeli.SetColLabelValue(1, "Nama Aplikasi")
        self.tabel_listapk_pembeli.SetColLabelValue(2, "Durasi")
        self.tabel_listapk_pembeli.SetColLabelValue(3, "Harga")
        self.data()
        self.tabel_akun.SetColLabelValue(0, "Username")
        self.tabel_akun.SetColLabelValue(1, "Nama")
        self.tabel_akun.SetColLabelValue(2, "Password")
        self.akun()

    def data(self):
        con = sqlite3.connect("MiApp.db")
        cursor = con.cursor()
        data = cursor.execute("select * from produk").fetchall()
        for a in data:
            self.tabel_listapk_pembeli.AppendRows(1)
        for b in range (4):
            a = 0
            for row in data:
                self.tabel_listapk_pembeli.SetCellValue(a, b, str(row[b]))
                a = a + 1
        con.close()

    def btn_pesan_onclick( self, event ):
        nama_apk = self.inp_apkPembeli.GetValue()
        jumlah = int(self.inp_jml.GetValue())
        username = run.inp_usn.GetValue()
        wx.MessageBox(username)
        if nama_apk == "":
            wx.MessageBox('Masukkan nama aplikasi terlebih dahulu','Warning',wx.OK | wx.ICON_WARNING)
        elif jumlah == "":
            wx.MessageBox('Masukkan jumlah pemesanan terlebih dahulu','Warning',wx.OK | wx.ICON_WARNING)
        else :
            con = sqlite3.connect("MiApp.db")
            cursor = con.cursor()
            cursor.execute(
            """CREATE TABLE IF NOT EXISTS pemesanan (
                "id_order" INTEGER NOT NULL,
                "nama_apk" INT NOT NULL,
                "jumlah" TEXT NOT NULL,
                "username" TEXT NOT NULL,
                PRIMARY KEY("id_order" AUTOINCREMENT),
                FOREIGN KEY("username")REFERENCES user("username")
            )"""
            )
            cursor.execute("INSERT INTO pemesanan VALUES (NULL,?,?,?)", (nama_apk, jumlah, username))
            cursor.execute("SELECT harga FROM produk WHERE nama_app=?", (nama_apk,))
            con.commit()
            harga_perunit = cursor.fetchone()
            if (harga_perunit):
                harga = int(harga_perunit[0])
                total_pemesanan = jumlah * harga
                wx.MessageBox(f'Total pemesanan Anda senilai {total_pemesanan}')
                self.inp_apkPembeli.SetValue("")
                self.inp_jml.SetValue("")
            else:
                wx.MessageBox('Aplikasi tidak terdaftar, lakukan pemesanan ulang','Warning',wx.OK | wx.ICON_WARNING)
                self.inp_apkPembeli.SetValue("")
                self.inp_jml.SetValue("")
                return harga_perunit
            con.close()

    def akun(self):
        username = run.inp_usn.GetValue()
        con = sqlite3.connect("MiApp.db")
        data1 = con.cursor().execute("SELECT * FROM user where username=?", (username,)).fetchall()
        for a in data1:
            self.tabel_akun.AppendRows(1)
        for b in range (3):
            a = 0
            for row in data1:
                self.tabel_akun.SetCellValue(a, b, str(row[b]))
                a = a + 1
        con.close()

class PenjualController (Penjual):
    def __init__(self, parent):
        Penjual.__init__(self,parent)
        self.SetTitle ('MiApp')
        self.tabel_listapk_penjual.SetColLabelValue(0, "Kode Aplikasi")
        self.tabel_listapk_penjual.SetColLabelValue(1, "Nama Aplikasi")
        self.tabel_listapk_penjual.SetColLabelValue(2, "Durasi")
        self.tabel_listapk_penjual.SetColLabelValue(3, "Harga")
        self.data()
        self.tabel_riwayat.SetColLabelValue(0, "Kode Order")
        self.tabel_riwayat.SetColLabelValue(1, "Nama Aplikasi")
        self.tabel_riwayat.SetColLabelValue(2, "Jumlah")
        self.tabel_riwayat.SetColLabelValue(3, "Username")
        self.riwayat()

    def data(self):
        con = sqlite3.connect("MiApp.db")
        cursor = con.cursor()
        data = cursor.execute("select * from produk").fetchall()
        for a in data:
            self.tabel_listapk_penjual.AppendRows(1)
        for b in range (4):
            a = 0
            for row in data:
                self.tabel_listapk_penjual.SetCellValue(a, b, str(row[b]))
                a = a + 1
        con.close()
    
    def btn_tambah_onclick( self, event ):
        tambah = TambahController(parent=self)
        tambah.Show()

    def btn_edit1_onclick( self, event ):
        edit = EditController(parent=self)
        edit.Show()
    
    def btn_delete1_onclick( self, event ):
        delete = DeleteController(parent=self)
        delete.Show()
    
    def riwayat(self):
        con = sqlite3.connect("MiApp.db")
        cursor = con.cursor()
        data = cursor.execute("select * from pemesanan").fetchall()
        for a in data:
            self.tabel_riwayat.AppendRows(1)
        for b in range (4):
            a = 0
            for row in data:
                self.tabel_riwayat.SetCellValue(a, b, str(row[b]))
                a = a + 1
        con.close()

    def btn_logout_onclick( self, event ):
        login = LoginController(parent=self)
        login.Show()

app = wx.App()
run = LoginController(parent=None)
run.Show()
app.MainLoop()