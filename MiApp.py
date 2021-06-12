# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class Login
###########################################################################

class Login ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 640,360 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Poppins" ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )


		bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 26, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Poppins" ) )
		self.m_staticText3.SetForegroundColour( wx.Colour( 211, 187, 221 ) )

		bSizer3.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )

		fgSizer1.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.inp_usn = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inp_usn.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )

		fgSizer1.Add( self.inp_usn, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )

		fgSizer1.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.inp_pass = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inp_pass.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )

		fgSizer1.Add( self.inp_pass, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer3.Add( fgSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.btn_login = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_login.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )
		self.btn_login.SetBackgroundColour( wx.Colour( 211, 187, 221 ) )

		gSizer3.Add( self.btn_login, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.btn_toRegister = wx.Button( self, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_toRegister.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )

		gSizer3.Add( self.btn_toRegister, 0, wx.ALL, 5 )


		bSizer3.Add( gSizer3, 1, wx.EXPAND, 5 )


		bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer2.Add( bSizer3, 1, wx.EXPAND|wx.ALL, 5 )

		self.c = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.c.SetMinSize( wx.Size( 320,309 ) )

		gSizer2.Add( self.c, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( gSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.login_onclose )
		self.btn_login.Bind( wx.EVT_BUTTON, self.btn_login_onclick )
		self.btn_toRegister.Bind( wx.EVT_BUTTON, self.btn_toRegister_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def login_onclose( self, event ):
		event.Skip()

	def btn_login_onclick( self, event ):
		event.Skip()

	def btn_toRegister_onclick( self, event ):
		event.Skip()


###########################################################################
## Class Register
###########################################################################

class Register ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 640,360 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Poppins" ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )


		bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.staticText = wx.StaticText( self, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText.Wrap( -1 )

		self.staticText.SetFont( wx.Font( 26, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Poppins" ) )
		self.staticText.SetForegroundColour( wx.Colour( 211, 187, 221 ) )

		bSizer3.Add( self.staticText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Nama Lengkap", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )

		fgSizer1.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.nama_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nama_input.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )

		fgSizer1.Add( self.nama_input, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )

		fgSizer1.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.usn1_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.usn1_input.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )

		fgSizer1.Add( self.usn1_input, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )

		fgSizer1.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.pass1_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pass1_input.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )

		fgSizer1.Add( self.pass1_input, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Konfirmasi Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )

		fgSizer1.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.kon_input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kon_input.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )

		fgSizer1.Add( self.kon_input, 0, wx.ALL, 5 )


		bSizer3.Add( fgSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.btn_regist = wx.Button( self, wx.ID_ANY, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_regist.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )
		self.btn_regist.SetBackgroundColour( wx.Colour( 211, 187, 221 ) )

		bSizer3.Add( self.btn_regist, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer2.Add( bSizer3, 1, wx.EXPAND|wx.ALL, 5 )

		self.c = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.c.SetMinSize( wx.Size( 320,309 ) )

		gSizer2.Add( self.c, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( gSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.regist__onclose )
		self.btn_regist.Bind( wx.EVT_BUTTON, self.btn_regist_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def regist__onclose( self, event ):
		event.Skip()

	def btn_regist_onclick( self, event ):
		event.Skip()


###########################################################################
## Class Tambah
###########################################################################

class Tambah ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 640,360 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		isi_formpemesanan = wx.BoxSizer( wx.VERTICAL )


		isi_formpemesanan.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Tambah Aplikasi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Poppins" ) )
		self.m_staticText9.SetForegroundColour( wx.Colour( 211, 187, 221 ) )

		isi_formpemesanan.Add( self.m_staticText9, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 5 )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Nama Aplikasi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		fgSizer3.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.inp_apkPenjual = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.inp_apkPenjual, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Durasi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		fgSizer3.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.inp_durasi = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.inp_durasi, 0, wx.ALL, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		fgSizer3.Add( self.m_staticText33, 0, wx.ALL, 5 )

		self.inp_harga = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.inp_harga, 0, wx.ALL, 5 )


		isi_formpemesanan.Add( fgSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )

		self.btn_tambah = wx.Button( self, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_tambah.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )
		self.btn_tambah.SetBackgroundColour( wx.Colour( 210, 187, 221 ) )

		isi_formpemesanan.Add( self.btn_tambah, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		isi_formpemesanan.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( isi_formpemesanan )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.tambah_onclose )
		self.btn_tambah.Bind( wx.EVT_BUTTON, self.btn_tambah_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tambah_onclose( self, event ):
		event.Skip()

	def btn_tambah_onclick( self, event ):
		event.Skip()


###########################################################################
## Class Edit
###########################################################################

class Edit ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 640,360 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		isi_formpemesanan = wx.BoxSizer( wx.VERTICAL )


		isi_formpemesanan.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Edit Data Aplikasi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Poppins" ) )
		self.m_staticText9.SetForegroundColour( wx.Colour( 211, 187, 221 ) )

		isi_formpemesanan.Add( self.m_staticText9, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 5 )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Kode Aplikasi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )

		fgSizer3.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.inp_kodeApk = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.inp_kodeApk, 0, wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Nama Aplikasi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )

		fgSizer3.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.inp_apkPenjual = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.inp_apkPenjual, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Durasi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )

		fgSizer3.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.inp_durasi = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.inp_durasi, 0, wx.ALL, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )

		fgSizer3.Add( self.m_staticText33, 0, wx.ALL, 5 )

		self.inp_harga = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.inp_harga, 0, wx.ALL, 5 )


		isi_formpemesanan.Add( fgSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )

		self.m_btnEdit = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_btnEdit.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )
		self.m_btnEdit.SetBackgroundColour( wx.Colour( 210, 187, 221 ) )

		isi_formpemesanan.Add( self.m_btnEdit, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		isi_formpemesanan.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( isi_formpemesanan )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.edit_onclose )
		self.m_btnEdit.Bind( wx.EVT_BUTTON, self.btn_simpan_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def edit_onclose( self, event ):
		event.Skip()

	def btn_simpan_onclick( self, event ):
		event.Skip()


###########################################################################
## Class Delete
###########################################################################

class Delete ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 640,360 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		isi_formpemesanan = wx.BoxSizer( wx.VERTICAL )


		isi_formpemesanan.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Delete Data Aplikasi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Poppins" ) )
		self.m_staticText9.SetForegroundColour( wx.Colour( 211, 187, 221 ) )

		isi_formpemesanan.Add( self.m_staticText9, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 5 )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Kode Aplikasi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		fgSizer3.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.inp_apkPenjual = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.inp_apkPenjual, 0, wx.ALL, 5 )


		isi_formpemesanan.Add( fgSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )

		self.m_btnDelete = wx.Button( self, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_btnDelete.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )
		self.m_btnDelete.SetBackgroundColour( wx.Colour( 210, 187, 221 ) )

		isi_formpemesanan.Add( self.m_btnDelete, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		isi_formpemesanan.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( isi_formpemesanan )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.delete_onclose )
		self.m_btnDelete.Bind( wx.EVT_BUTTON, self.btn_delete_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def delete_onclose( self, event ):
		event.Skip()

	def btn_delete_onclick( self, event ):
		event.Skip()


###########################################################################
## Class Pembeli
###########################################################################

class Pembeli ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 640,360 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_pembeli = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_beranda = wx.Panel( self.m_pembeli, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer15 = wx.BoxSizer( wx.VERTICAL )


		bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_home = wx.StaticText( self.m_beranda, wx.ID_ANY, u"Daftar Aplikasi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_home.Wrap( -1 )

		self.m_home.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Poppins" ) )
		self.m_home.SetForegroundColour( wx.Colour( 211, 187, 221 ) )

		bSizer15.Add( self.m_home, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tabel_listapk_pembeli = wx.grid.Grid( self.m_beranda, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabel_listapk_pembeli.CreateGrid( 4, 4 )
		self.tabel_listapk_pembeli.EnableEditing( True )
		self.tabel_listapk_pembeli.EnableGridLines( True )
		self.tabel_listapk_pembeli.EnableDragGridSize( False )
		self.tabel_listapk_pembeli.SetMargins( 0, 0 )

		# Columns
		self.tabel_listapk_pembeli.EnableDragColMove( False )
		self.tabel_listapk_pembeli.EnableDragColSize( True )
		self.tabel_listapk_pembeli.SetColLabelSize( 25 )
		self.tabel_listapk_pembeli.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabel_listapk_pembeli.AutoSizeRows()
		self.tabel_listapk_pembeli.EnableDragRowSize( True )
		self.tabel_listapk_pembeli.SetRowLabelSize( 50 )
		self.tabel_listapk_pembeli.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabel_listapk_pembeli.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.tabel_listapk_pembeli.SetMinSize( wx.Size( -1,200 ) )

		bSizer15.Add( self.tabel_listapk_pembeli, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )


		bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_beranda.SetSizer( bSizer15 )
		self.m_beranda.Layout()
		bSizer15.Fit( self.m_beranda )
		self.m_pembeli.AddPage( self.m_beranda, u"Beranda", False )
		self.m_pemesanan = wx.Panel( self.m_pembeli, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		isi_formpemesanan = wx.BoxSizer( wx.VERTICAL )


		isi_formpemesanan.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText9 = wx.StaticText( self.m_pemesanan, wx.ID_ANY, u"Form Pemesanan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Poppins" ) )
		self.m_staticText9.SetForegroundColour( wx.Colour( 211, 187, 221 ) )

		isi_formpemesanan.Add( self.m_staticText9, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 5 )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText13 = wx.StaticText( self.m_pemesanan, wx.ID_ANY, u"Nama Aplikasi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )

		fgSizer3.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.inp_apkPembeli = wx.TextCtrl( self.m_pemesanan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.inp_apkPembeli, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self.m_pemesanan, wx.ID_ANY, u"Jumlah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )

		fgSizer3.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.inp_jml = wx.TextCtrl( self.m_pemesanan, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.inp_jml, 0, wx.ALL, 5 )


		isi_formpemesanan.Add( fgSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )

		self.btn_pesan = wx.Button( self.m_pemesanan, wx.ID_ANY, u"Pesan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_pesan.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )
		self.btn_pesan.SetBackgroundColour( wx.Colour( 210, 187, 221 ) )

		isi_formpemesanan.Add( self.btn_pesan, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		isi_formpemesanan.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_pemesanan.SetSizer( isi_formpemesanan )
		self.m_pemesanan.Layout()
		isi_formpemesanan.Fit( self.m_pemesanan )
		self.m_pembeli.AddPage( self.m_pemesanan, u"Pemesanan", False )
		self.m_akun = wx.Panel( self.m_pembeli, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )


		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText24 = wx.StaticText( self.m_akun, wx.ID_ANY, u"Akun Saya", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		self.m_staticText24.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Poppins" ) )
		self.m_staticText24.SetForegroundColour( wx.Colour( 211, 187, 221 ) )

		bSizer12.Add( self.m_staticText24, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tabel_akun = wx.grid.Grid( self.m_akun, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabel_akun.CreateGrid( 1, 3 )
		self.tabel_akun.EnableEditing( True )
		self.tabel_akun.EnableGridLines( True )
		self.tabel_akun.EnableDragGridSize( False )
		self.tabel_akun.SetMargins( 0, 0 )

		# Columns
		self.tabel_akun.EnableDragColMove( False )
		self.tabel_akun.EnableDragColSize( True )
		self.tabel_akun.SetColLabelSize( 30 )
		self.tabel_akun.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabel_akun.EnableDragRowSize( True )
		self.tabel_akun.SetRowLabelSize( 80 )
		self.tabel_akun.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabel_akun.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.tabel_akun.SetMinSize( wx.Size( -1,70 ) )

		bSizer12.Add( self.tabel_akun, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.btn_akun = wx.Button( self.m_akun, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_akun.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )
		self.btn_akun.SetBackgroundColour( wx.Colour( 211, 187, 221 ) )

		bSizer12.Add( self.btn_akun, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_akun.SetSizer( bSizer12 )
		self.m_akun.Layout()
		bSizer12.Fit( self.m_akun )
		self.m_pembeli.AddPage( self.m_akun, u"Akun", True )

		bSizer10.Add( self.m_pembeli, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.pembeli_onclose )
		self.btn_pesan.Bind( wx.EVT_BUTTON, self.btn_pesan_onclick )
		self.btn_akun.Bind( wx.EVT_BUTTON, self.btn_logout_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def pembeli_onclose( self, event ):
		event.Skip()

	def btn_pesan_onclick( self, event ):
		event.Skip()

	def btn_logout_onclick( self, event ):
		event.Skip()


###########################################################################
## Class Penjual
###########################################################################

class Penjual ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 640,360 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook5 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_beranda = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer15 = wx.BoxSizer( wx.VERTICAL )


		bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_home = wx.StaticText( self.m_beranda, wx.ID_ANY, u"Daftar Aplikasi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_home.Wrap( -1 )

		self.m_home.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Poppins" ) )
		self.m_home.SetForegroundColour( wx.Colour( 211, 187, 221 ) )

		bSizer15.Add( self.m_home, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tabel_listapk_penjual = wx.grid.Grid( self.m_beranda, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabel_listapk_penjual.CreateGrid( 4, 4 )
		self.tabel_listapk_penjual.EnableEditing( True )
		self.tabel_listapk_penjual.EnableGridLines( True )
		self.tabel_listapk_penjual.EnableDragGridSize( False )
		self.tabel_listapk_penjual.SetMargins( 0, 0 )

		# Columns
		self.tabel_listapk_penjual.EnableDragColMove( False )
		self.tabel_listapk_penjual.EnableDragColSize( True )
		self.tabel_listapk_penjual.SetColLabelSize( 25 )
		self.tabel_listapk_penjual.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabel_listapk_penjual.AutoSizeRows()
		self.tabel_listapk_penjual.EnableDragRowSize( True )
		self.tabel_listapk_penjual.SetRowLabelSize( 50 )
		self.tabel_listapk_penjual.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabel_listapk_penjual.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.tabel_listapk_penjual.SetMinSize( wx.Size( -1,150 ) )

		bSizer15.Add( self.tabel_listapk_penjual, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )

		self.btn_tambah = wx.Button( self.m_beranda, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.btn_tambah.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_OTHER ) )
		self.btn_tambah.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )
		self.btn_tambah.SetBackgroundColour( wx.Colour( 211, 187, 221 ) )

		bSizer15.Add( self.btn_tambah, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		self.btn_edit1 = wx.Button( self.m_beranda, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_edit1.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )
		self.btn_edit1.SetBackgroundColour( wx.Colour( 211, 187, 221 ) )

		gSizer4.Add( self.btn_edit1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.btn_delete1 = wx.Button( self.m_beranda, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_delete1.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )
		self.btn_delete1.SetBackgroundColour( wx.Colour( 211, 187, 221 ) )

		gSizer4.Add( self.btn_delete1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer15.Add( gSizer4, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer15.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_beranda.SetSizer( bSizer15 )
		self.m_beranda.Layout()
		bSizer15.Fit( self.m_beranda )
		self.m_notebook5.AddPage( self.m_beranda, u"Beranda", False )
		self.m_pemesanan = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer151 = wx.BoxSizer( wx.VERTICAL )


		bSizer151.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_home1 = wx.StaticText( self.m_pemesanan, wx.ID_ANY, u"Riwayat Pemesanan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_home1.Wrap( -1 )

		self.m_home1.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Poppins" ) )
		self.m_home1.SetForegroundColour( wx.Colour( 211, 187, 221 ) )

		bSizer151.Add( self.m_home1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tabel_riwayat = wx.grid.Grid( self.m_pemesanan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabel_riwayat.CreateGrid( 4, 4 )
		self.tabel_riwayat.EnableEditing( True )
		self.tabel_riwayat.EnableGridLines( True )
		self.tabel_riwayat.EnableDragGridSize( False )
		self.tabel_riwayat.SetMargins( 0, 0 )

		# Columns
		self.tabel_riwayat.EnableDragColMove( False )
		self.tabel_riwayat.EnableDragColSize( True )
		self.tabel_riwayat.SetColLabelSize( 25 )
		self.tabel_riwayat.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabel_riwayat.AutoSizeRows()
		self.tabel_riwayat.EnableDragRowSize( True )
		self.tabel_riwayat.SetRowLabelSize( 50 )
		self.tabel_riwayat.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabel_riwayat.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.tabel_riwayat.SetMinSize( wx.Size( -1,200 ) )

		bSizer151.Add( self.tabel_riwayat, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )


		bSizer151.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer151.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_pemesanan.SetSizer( bSizer151 )
		self.m_pemesanan.Layout()
		bSizer151.Fit( self.m_pemesanan )
		self.m_notebook5.AddPage( self.m_pemesanan, u"Pemesanan", True )
		self.m_logout = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )


		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText24 = wx.StaticText( self.m_logout, wx.ID_ANY, u"Klik logout untuk keluar sistem", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		self.m_staticText24.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )

		bSizer12.Add( self.m_staticText24, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.btn_logout = wx.Button( self.m_logout, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_logout.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Poppins Medium" ) )
		self.btn_logout.SetBackgroundColour( wx.Colour( 211, 187, 221 ) )

		bSizer12.Add( self.btn_logout, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_logout.SetSizer( bSizer12 )
		self.m_logout.Layout()
		bSizer12.Fit( self.m_logout )
		self.m_notebook5.AddPage( self.m_logout, u"Logout", False )

		bSizer23.Add( self.m_notebook5, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer23 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.penjual_onclose )
		self.btn_tambah.Bind( wx.EVT_BUTTON, self.btn_tambah_onclick )
		self.btn_edit1.Bind( wx.EVT_BUTTON, self.btn_edit1_onclick )
		self.btn_delete1.Bind( wx.EVT_BUTTON, self.btn_delete1_onclick )
		self.btn_logout.Bind( wx.EVT_BUTTON, self.btn_logout_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def penjual_onclose( self, event ):
		event.Skip()

	def btn_tambah_onclick( self, event ):
		event.Skip()

	def btn_edit1_onclick( self, event ):
		event.Skip()

	def btn_delete1_onclick( self, event ):
		event.Skip()

	def btn_logout_onclick( self, event ):
		event.Skip()


