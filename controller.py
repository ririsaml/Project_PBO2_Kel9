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

app = wx.App()
run = LoginController(parent=None)
run.Show()
app.MainLoop()