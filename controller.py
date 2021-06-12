import wx
import sqlite3
from MiApp import Login

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

app = wx.App()
run = LoginController(parent=None)
run.Show()
app.MainLoop()