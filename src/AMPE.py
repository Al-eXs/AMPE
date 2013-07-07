#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx, os, threading
from sys import stdout
from subprocess import Popen
from platform import system
from time import sleep
try:
    from win32api import GetShortPathName
except:
    pass


folderrun = unicode(os.getcwd(), 'utf-8')
# begin wxGlade: extracode
# end wxGlade

class AMPEclass(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: AMPEclass.__init__
        kwds["style"] = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |	wx.CLOSE_BOX | wx.TAB_TRAVERSAL
        wx.Frame.__init__(self, *args, **kwds)
        self.sizer_6_staticbox = wx.StaticBox(self, 0, u"Opciones")
        self.sizer_7_staticbox = wx.StaticBox(self, 0, u"Archivos a Convertir")
        self.sizer_9_staticbox = wx.StaticBox(self, 0, u"Video")
        self.sizer_10_staticbox = wx.StaticBox(self, 0, u"Audio")
        self.select = 0

        global elim, Lista, button_eliminar, combo_formato, button_convertir, filenames, paths
        
        filenames = []
        paths = []
        print ""
        
        # Menu Bar
        self.Menu = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        self.open = wxglade_tmp_menu.Append(wx.ID_OPEN, u"&Abrir\tCtrl+A", "Añadir un archivo", wx.ITEM_NORMAL)
        elim = wxglade_tmp_menu.Append(wx.ID_CLOSE, u"&Eliminar\tCtrl+E", "Eliminar seleccionado", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        self.quit = wxglade_tmp_menu.Append(wx.ID_EXIT, u'&Salir\tCtrl+Q', u'Salir de AMPE')
        self.Menu.Append(wxglade_tmp_menu, u"Ar&chivo")
        wxglade_tmp_menu = wx.Menu()
        self.optns = wxglade_tmp_menu.Append(wx.ID_PROPERTIES, u"&Opciones\tF8", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        self.logdel = wxglade_tmp_menu.Append(wx.ID_CLEAR, u"&Borrar Logs\tF12", "Borra todo", wx.ITEM_NORMAL)
        self.Menu.Append(wxglade_tmp_menu, u"&Herramientas")
        wxglade_tmp_menu = wx.Menu()
        self.about = wxglade_tmp_menu.Append(wx.ID_ABOUT, u"&Acerca de...\tF1", "", wx.ITEM_NORMAL)
        self.Menu.Append(wxglade_tmp_menu, u"A&yuda")
        self.SetMenuBar(self.Menu)
        # Menu Bar end
        file_drop_target = MyFileDropTarget(self)
        Lista = wx.ListBox(self, -1)
        Lista.SetDropTarget(file_drop_target)
        self.button_abrir = wx.Button(self, -1, u"&Abrir")
        button_eliminar = wx.Button(self, -1, u"&Eliminar")
        self.label_3 = wx.StaticText(self, -1, u"&Formato:")
        combo_formato = wx.ComboBox(self, -1, choices=[u" MP4", u" AVI"], style=wx.CB_DROPDOWN)
        self.label_4 = wx.StaticText(self, -1, u"&Resolución:")
        self.combo_resolucion = wx.ComboBox(self, -1, choices=[u" Mantener Original", u" Alto", u" Ancho"], style=wx.CB_DROPDOWN)
        self.text_res = wx.TextCtrl(self, -1, u"500", style=wx.ALIGN_RIGHT)
        self.label_2 = wx.StaticText(self, -1, u"px")
        self.label_5 = wx.StaticText(self, -1, u"&CRF:")
        self.slider_bitrate = wx.Slider(self, -1, 23, 10, 40)
        self.spin_bitrate = wx.SpinCtrl(self, -1, u"23", (40, 10))
        self.radio_128 = wx.RadioButton(self, -1, u"1&28 Kb/s")
        self.radio_160 = wx.RadioButton(self, -1, u"1&60 Kb/s")
        self.radio_192 = wx.RadioButton(self, -1, u"1&92 Kb/s")
        button_convertir = wx.Button(self, -1, u"Con&vertir")
        self.button_salir = wx.Button(self, -1, u"&Salir")
                
        self.Bind(wx.EVT_SPINCTRL, self.OnSpin)
        self.Bind(wx.EVT_SLIDER, self.OnSlider)
        self.Bind(wx.EVT_COMBOBOX, self.SelRes, self.combo_resolucion)
        self.Bind(wx.EVT_MENU, self.OnOpen, self.open)
        self.Bind(wx.EVT_MENU, self.OnElim, elim)
        self.Bind(wx.EVT_MENU, self.OnQuit, self.quit)
        self.Bind(wx.EVT_MENU, self.OnAbout, self.about)
        self.Bind(wx.EVT_MENU, self.OnLogDel, self.logdel)
        self.Bind(wx.EVT_BUTTON, self.OnOpen, self.button_abrir)
        self.Bind(wx.EVT_BUTTON, self.OnElim, button_eliminar)
        self.Bind(wx.EVT_BUTTON, self.OnQuit, self.button_salir)
        self.Bind(wx.EVT_BUTTON, self.OnConvert, button_convertir)
        self.Bind(wx.EVT_LISTBOX, self.SelList, Lista)
        self.Bind(wx.EVT_COMBOBOX, self.SelFormat, combo_formato)
        self.Bind(wx.EVT_CLOSE, self.OnQuit)
        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: AMPEclass.__set_properties
        if system() == 'Windows':
            self.SetTitle(u"AMPE - Al_eXs MPV Encoder para Windows")
        elif system() == 'Linux':
            self.SetTitle(u"AMPE - Al_eXs MPV Encoder para Linux")
        else:
            self.SetTitle(u"AMPE - Al_eXs MPV Encoder")
        global _icon
        _icon = wx.EmptyIcon()
        _icon = wx.Icon(u"./img/AMPE.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(_icon)
        self.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_3DLIGHT))
        self.SetSize((600, 520))
        Lista.SetMinSize((400, 200))
        elim.Enable(False)
        button_eliminar.Enable(False)
        combo_formato.SetSelection(0)
        self.combo_resolucion.SetSelection(0)
        self.slider_bitrate.SetMinSize((250, -1))
        self.spin_bitrate.SetMinSize((60, -1))
        self.text_res.SetMinSize((50,-1))
        self.radio_128.SetValue(1)
        button_convertir.Enable(False)
        self.optns.Enable(False)
        self.text_res.Enable(False)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: AMPEclass.__do_layout
        sizer_10 = wx.StaticBoxSizer(self.sizer_10_staticbox, wx.HORIZONTAL)
        sizer_7 = wx.StaticBoxSizer(self.sizer_7_staticbox, wx.HORIZONTAL)
        sizer_6 = wx.StaticBoxSizer(self.sizer_6_staticbox, wx.HORIZONTAL)
        sizer_9 = wx.StaticBoxSizer(self.sizer_9_staticbox, wx.HORIZONTAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11_copy = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_9 = wx.FlexGridSizer(3, 2, 0, 0)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_7.Add(Lista, 3, 0, 10)
        sizer_4.Add(sizer_7, 0, wx.LEFT|wx.TOP|wx.BOTTOM, 10)
        sizer_5.Add(self.button_abrir, 0, wx.ALL, 10)
        sizer_5.Add(button_eliminar, 0, wx.ALL, 10)
        sizer_4.Add(sizer_5, 0, wx.TOP, 20)
        sizer_3.Add(sizer_4, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_9.Add(self.label_3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_9.Add(combo_formato, 0, wx.TOP, 5)
        grid_sizer_9.Add(self.label_4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_1.Add(self.combo_resolucion, 0, 0, 0)
        sizer_1.Add(self.text_res, 0, wx.LEFT, 10)
        sizer_1.Add(self.label_2, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 2)
        grid_sizer_9.Add(sizer_1, 0, wx.TOP|wx.BOTTOM, 5)
        grid_sizer_9.Add(self.label_5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_12.Add(self.slider_bitrate, 0, 0, 0)
        sizer_12.Add(self.spin_bitrate, 0, 0, 0)
        grid_sizer_9.Add(sizer_12, 0, wx.TOP|wx.BOTTOM, 5)
        sizer_9.Add(grid_sizer_9, 0, 0, 0)
        sizer_6.Add(sizer_9, 0, wx.ALL, 5)
        sizer_11_copy.Add(self.radio_128, 0, wx.ALL, 4)
        sizer_11_copy.Add(self.radio_160, 0, wx.ALL, 4)
        sizer_11_copy.Add(self.radio_192, 0, wx.ALL, 4)
        sizer_10.Add(sizer_11_copy, 0, wx.ALL, 10)
        sizer_6.Add(sizer_10, 0, wx.ALL, 5)
        sizer_3.Add(sizer_6, 0, wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 10)
        sizer_8.Add(button_convertir, 0, wx.RIGHT, 20)
        sizer_8.Add(self.button_salir, 0, wx.LEFT, 20)
        sizer_3.Add(sizer_8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10)
        sizer_11.Add(sizer_3, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        self.SetSizer(sizer_11)
        self.Layout()
        self.Centre()
        # end wxGlade        

    def OnLogDel(self, e):
        if system() == 'Windows':
            for each in os.listdir(folderrun + '\\logs'):
                try:
                    if each.endswith(".log"):
                        os.remove(folderrun + '\\logs\\' + each)
                except:
                    pass
        if system() == 'Linux':
            for each in os.listdir(folderrun + '/logs'):
                try:
                    if each.endswith(".log"):
                        os.remove(folderrun + '/logs/' + each)
                except:
                    pass
        wx.MessageBox('Los archivos de Log\nhan sido borrados.', ' Info', wx.OK | wx.ICON_INFORMATION)

    def SelFormat(self, e):
        if combo_formato.GetSelection() == 1:
            self.label_5.Label = u"&Bitrate:"
            self.slider_bitrate.SetRange(500, 6000)
            self.slider_bitrate.SetValue(1500)
            self.spin_bitrate.SetRange(500, 6000)
            self.spin_bitrate.SetValueString(u"1500")
        else:
            self.label_5.Label = u"&CRF:"
            self.slider_bitrate.SetRange(10, 40)
            self.slider_bitrate.SetValue(23)
            self.spin_bitrate.SetRange(10, 40)
            self.spin_bitrate.SetValueString(u"23")

    def SelRes(self, e):
        if self.combo_resolucion.GetSelection() == 0:
            self.text_res.Enable(False)
        else:
            self.text_res.Enable(True)

    def OnQuit(self, e):
        print "\n\nBye Bye"
        if system() == 'Windows':
            for each in os.listdir(folderrun + '\\logs'):
                try:
                    if each.endswith('.mp4') or each.endswith('.avi') or each.startswith('output'):
                        os.remove(folderrun + '\\logs\\' + each)
                except:
                    pass
        self.Destroy()

    def OnOpen(self, e):
        self.select = Lista.GetSelection()
        dlg = wx.FileDialog(
            self, message = u"Añadir un Archivo",
            defaultFile = "",
            wildcard = u"Video (*.mkv; *.mp4; *.avi)|*.mkv;*.mp4;*.avi|MKV|*.mkv|MP4|*.mp4|AVI|*.avi",
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK: 
            filename = dlg.GetFilenames()
            path = dlg.GetPaths()
            for index in range(len(filename)):
                filenames.append(filename[index])
                paths.append(path[index])
                if self.select == -1:
                    Lista.Append(filename[index])
                if Lista.FindString(filename[index]) == -1:
                    Lista.Append(filename[index])
            if Lista.GetCount()> 0:
                button_eliminar.Enable(True)
                elim.Enable(True)
                button_convertir.Enable(True)
            Lista.SetSelection(Lista.GetCount() - 1)
            self.select = Lista.GetSelection()
        dlg.Destroy()

    def OnElim(self, e):
        Lista.Delete(self.select)
        if Lista.GetCount() - 1 == self.select:
            Lista.SetSelection(self.select)
        else:
            Lista.SetSelection(self.select - 1)
#        print Lista.GetSelection()
        if Lista.GetCount() == 0:
            button_eliminar.Enable(False)
            elim.Enable(False)
            button_convertir.Enable(False)
        self.select = Lista.GetSelection()
        
    def SelList(self, e):
        self.select = Lista.GetSelection()
        
    def OnConvert(self, e):
        if combo_formato.GetSelection() == 0:
            formato = u'converted.mp4" -ofps 23.976 -ovfirst -ovc libx264 -oac aac -ovcopts preset=medium,profile=main,crf='
            bit2 = u" -af lavrresample=srate=44100,pan=2:1:0:0:1:1:1:1:1:1:0:0:1,format=s16le -oacopts ab="
            format = u"mp4"
        elif combo_formato.GetSelection() == 1:
            formato1 = u'converted.avi" -ofps 23.976 -ovfirst -of avi -no-audio -ovc libxvid -ovcopts flags=+pass1,threads=2'
            formato2 = u'converted.avi" -ofps 23.976 -ovfirst -of avi -ovc libxvid -oac libmp3lame -ovcopts flags=+pass2,threads=2,b='
            bit2 = u"k -af lavrresample=srate=44100,pan=2:1:0:0:1:1:1:1:1:1:0:0:1,format=s16le -oacopts ab="
            format = u"avi"

        if self.combo_resolucion.GetSelection() == 0:
            resolucion = u" -vf scale=-1"
        elif self.combo_resolucion.GetSelection() == 1:
            res = self.text_res.GetValue()
            resolucion = u" -vf scale=-3:" + res
        elif self.combo_resolucion.GetSelection() == 2:
            res = self.text_res.GetValue()
            resolucion = u" -vf scale=" + res + ":-3"

        bitrate = unicode(self.spin_bitrate.GetValue())

        if self.radio_128.Value == 1: audio = u"128k"
        if self.radio_160.Value == 1: audio = u"160k"
        if self.radio_192.Value == 1: audio = u"192k"
        
        if system() == 'Windows': mp2 = u"mpv2.exe"
        if system() == 'Linux' : mp2 = u"mpv-lavc"
        
        global encodear
        encodear = []
        del encodear[:]
        global logfile
        logfile = []
        del logfile[:]
        
        for i in range(len(paths)):
            paths[i] = paths[i].encode('utf-8')
            filenames[i] = filenames[i].encode('utf-8')
            #print paths[i]#
            #print filenames[i]#
            infile = paths[i]
            output = paths[i][:-3]
            if combo_formato.GetSelection() == 1:
                if system() == 'Windows':
                    encodear.append(u'"' + folderrun + u'\\bin\\' + mp2 + u'" "' + GetShortPathName(unicode(infile,'utf-8')) + u'" -o "' + folderrun + '\\logs\\output' + str(i) + formato1 + resolucion)
                    encodear.append(u'"' + folderrun + u'\\bin\\' + mp2 + u'" "' + GetShortPathName(unicode(infile,'utf-8')) + u'" -o "' + folderrun + '\\logs\\output' + str(i) + formato2 + bitrate + bit2 + audio + resolucion)
                    logfile.append(folderrun + u'\\logs\\' + unicode(filenames[i],'utf-8') + u'-to-' + format + u'.pass1.log')
                    logfile.append(folderrun + u'\\logs\\' + unicode(filenames[i],'utf-8') + u'-to-' + format + u'.pass2.log')
                if system() == 'Linux':
                    encodear.append(u'"' + folderrun + u'/bin/' + mp2 + u'" "' + unicode(infile,'utf-8') + u'" -o "' + unicode(output,'utf-8') + formato1 + resolucion)
                    encodear.append(u'"' + folderrun + u'/bin/' + mp2 + u'" "' + unicode(infile,'utf-8') + u'" -o "' + unicode(output,'utf-8') + formato2 + bitrate + bit2 + audio + resolucion)
                    logfile.append(folderrun + u'/logs/' + unicode(filenames[i],'utf-8') + u'-to-' + format + u'.pass1.log')
                    logfile.append(folderrun + u'/logs/' + unicode(filenames[i],'utf-8') + u'-to-' + format + u'.pass2.log')
            else:
                if system() == 'Windows':
                    encodear.append(u'"' + folderrun + u'\\bin\\' + mp2 + u'" "' + GetShortPathName(unicode(infile,'utf-8')) + u'" -o "' + folderrun + '\\logs\\output' + str(i) + formato + bitrate + bit2 + audio + resolucion)
                    logfile.append(folderrun + u'\\logs\\' + unicode(filenames[i],'utf-8') + u'-to-' + format + u'.log')
                if system() == 'Linux':
                    encodear.append(u'"' + folderrun + u'/bin/' + mp2 + u'" "' + unicode(infile,'utf-8') + u'" -o "' + unicode(output,'utf-8') + formato + bitrate + bit2 + audio + resolucion)
                    logfile.append(folderrun + u'/logs/' + unicode(filenames[i],'utf-8') + u'-to-' + format + u'.log')
        global salir
        salir = False
        convertir = Encodeo(self)
        convertir.start()
        frame2 = ConvertDialog(self)
        frame2.Show()
        

    def OnAbout(self, e):
        description = u"""
AMPE (Al_eXs MPlayer2/MPV Encoder) es una Interfaz Gráfica de
Usuario(GUI) para encodear videos MKV, MP4 o AVI en MP4 o
AVI compatibles con las consolas usando como fuente para
encodear el MPlayer2/MPV.\n
Acepta estilos y enlaza los capitulos con
Ordered Chapters Externos(Segment Linking).\n

Agradecimientos:
- Al equipo de desarrollo de MPV, fork del MPlayer/MPlayer2.
- ErunamoJAZZ(AnS) por su apoyo en mejorar mi codigo python.
- Batousay(BB) por su tip para las barras de progreso.
- A todos los que probaron las betas.\n"""
        
        licence = u"""
AMPE es un sofware libre; se puede redistribuir y/o modificar
bajo los terminos de la Licencia Publica General GNU Version 3.
AMPE es distribuido con la esperanza de ser un software util
pero SIN GARANTIA ALGUNA.\n"""

        info = wx.AboutDialogInfo()
        if system() == 'Linux': info.SetIcon(wx.Icon(folderrun + '/img/logo.png', wx.BITMAP_TYPE_PNG))
        if system() == 'Windows': info.SetIcon(wx.Icon(folderrun + '\\img\\logo.png', wx.BITMAP_TYPE_PNG))
        info.SetName(u"AMPE")
        info.SetVersion(u"1.0.10")
        info.SetDescription(description)
        info.SetCopyright(u'(C) 2011-2013 Al_eXs')
        info.SetWebSite(u'https://github.com/Al-eXs/AMPE')
#        info.AddDeveloper('-')
#        info.AddDocWriter('-')
#        info.AddArtist('-')
#        info.AddTranslator('-')
        info.SetLicence(licence)
        wx.AboutBox(info)

    def OnSlider(self, e):
        self.spin_bitrate.SetValue(self.slider_bitrate.GetValue())

    def OnSpin(self, e):
        self.slider_bitrate.SetValue(self.spin_bitrate.GetValue())
        
# end of class AMPEclass

class ConvertDialog(wx.Frame):
    def __init__(self, parent, *args, **kwds):
        # begin wxGlade: ConvertDialog.__init__
        kwds["style"] = wx.CAPTION | wx.MINIMIZE_BOX
        kwds["pos"] = parent.GetPosition()
        wx.Frame.__init__(self, None, -1, title = u"  Convirtiendo", **kwds)
        self.label_1a = wx.StaticText(self, -1, u"Convirtiendo:")
        
        global label_capi, gauge_2a, label_total, gauge_1a, button_minimize, button_cancel
        label_capi = wx.StaticText(self, -1, "")#nombre del capi
        gauge_2a = wx.Gauge(self, -1, 100)
        self.label_2a = wx.StaticText(self, -1, u"Progreso Total:")
#        label_total = wx.StaticText(self, -1, "")
        gauge_1a = wx.Gauge(self, -1, 100)
        button_minimize = wx.Button(self, -1, u"Minimizar")
        button_cancel = wx.Button(self, -1, u"Cancelar")
        self.padre = parent
        
        self.Bind(wx.EVT_BUTTON, self.OnCancel, button_cancel)
        self.Bind(wx.EVT_BUTTON, self.OnMin, button_minimize)
        self.Bind(wx.EVT_CLOSE, self.OnCancel)

        self.padre.Show(False)
        
        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: ConvertDialog.__set_properties
        self.SetTitle(u"Convirtiendo")
        self.SetSize((500, 220))
        self.SetIcon(_icon)
        gauge_2a.SetMinSize((450, 15))
        gauge_1a.SetMinSize((450, 15))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ConvertDialog.__do_layout
        sizer_1a = wx.BoxSizer(wx.VERTICAL)
        sizer_2a = wx.BoxSizer(wx.VERTICAL)
        sizer_5a = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4a = wx.BoxSizer(wx.VERTICAL)
        sizer_3a = wx.BoxSizer(wx.VERTICAL)
        sizer_3a.Add(self.label_1a, 0, 0, 0)
        sizer_3a.Add(label_capi, 0, wx.BOTTOM, 10)
        sizer_3a.Add(gauge_2a, 0, 0, 0)
        sizer_2a.Add(sizer_3a, 0, wx.LEFT|wx.TOP, 20)
        sizer_4a.Add(self.label_2a, 0, wx.BOTTOM, 10)
#        sizer_4a.Add(label_total, 0, 0, 0)
        sizer_4a.Add(gauge_1a, 0, 0, 0)
        sizer_2a.Add(sizer_4a, 0, wx.LEFT|wx.TOP|wx.BOTTOM, 20)
        sizer_5a.Add(button_minimize, 0, 0, 0)
        sizer_5a.Add(button_cancel, 0, wx.LEFT, 120)
        sizer_2a.Add(sizer_5a, 0, wx.RIGHT|wx.ALIGN_RIGHT, 20)
        sizer_1a.Add(sizer_2a, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1a)
        self.Layout()
        # end wxGlade
    
    def OnCancel(self, e):
        if not button_cancel.Label == u"Cerrar":
#            global salir
            salir = True
            enc = Encodeo(self)
            enc.stop()
        self.padre.Show(True)
        Lista.Clear()
        del paths[:]
        del filenames[:]
        if Lista.GetCount() == 0:
            button_eliminar.Enable(False)
            elim.Enable(False)
            button_convertir.Enable(False)  
        self.Destroy()
        
    def OnMin(self, e):
        self.Iconize(True)
#        self.padre.Iconize(True)

        
class Encodeo(threading.Thread):
    def __init__(self, e):
        threading.Thread.__init__(self)
 #       self.setDaemon(True)
        
    def run(self):
        global ii
        ii = 0
        while not salir:
            try:
                os.remove(logfile[ii])
            except:
                pass
            stdout.write('\n\n')
            print encodear[ii].encode('cp1252')
            self.proceso = Popen(encodear[ii].encode('utf-8'), stdout = open(logfile[ii], "a"), stderr = open(logfile[ii], "a"), shell = True)
            if combo_formato.GetSelection() == 1:
                wx.CallAfter(label_capi.SetLabel, filenames[ii/2])
                stdout.write('\n')
                print filenames[ii/2]
            else:
                wx.CallAfter(label_capi.SetLabel, filenames[ii])
                stdout.write('\n')
                print filenames[ii]
            bars = Barras(self)
            bars.start()
            self.proceso.wait()

            #Windows unicode fix
            if system() == 'Windows':
                if combo_formato.GetSelection() == 1:
                    try:
                        os.remove(unicode(paths[ii/2][:-3], 'utf-8') + u'converted.avi')
                    except:
                        pass
                    try:
                        if ii & 1: os.rename(folderrun + u'\\logs\\output' + str(ii/2) + u'converted.avi', unicode(paths[ii/2][:-3], 'utf-8') + u'converted.avi')
                    except:
                        pass
                else:
                    try:
                        os.remove(unicode(paths[ii][:-3], 'utf-8') + u'converted.mp4')
                    except:
                        pass
                    try:
                        os.rename(folderrun + u'\\logs\\output' + str(ii) + u'converted.mp4', unicode(paths[ii][:-3], 'utf-8') + u'converted.mp4')
                    except:
                        pass

            sleep(2)
            if ii == len(encodear)-1:
                break
            ii +=1
        try:
            if not salir:
                bars._Thread__stop()
                sleep(2)
                wx.CallAfter(label_capi.SetLabel, u" ")
                gauge_2a.SetValue(100)
                gauge_1a.SetValue(100)
                wx.CallAfter(wx.MessageBox, u'Terminó la Conversión', u'Info', wx.OK | wx.ICON_INFORMATION)
            button_cancel.Label = u"Cerrar"
            button_minimize.Enable(False)
            Lista.Clear()
            del paths[:]
            del filenames[:]
        except:
            pass
    
    def stop(self):
        global salir
        salir = True
        stdout.write('\n\n')
        if system() == 'Linux': self.kill = Popen(u"killall mpv-lavc", shell = True)
        if system() == 'Windows': self.kill = Popen(u"taskkill /F /IM mpv2.exe", shell = True)

       
class Barras(threading.Thread):
    def __init__(self, e):
        threading.Thread.__init__(self)
       
    def run(self):
        while True:
            sleep(2)
            prs = open(logfile[ii], "r")
            for last in prs:
                porcentaje = last
            porcentaje = str(porcentaje)
#            print porcentaje[-80:-10]
            a = porcentaje[-80:-10].split(u'{')
#            print a
            try:
                b = a[1].split(u'%')
            except IndexError:
                break
            stdout.flush()
            stdout.write('\r')
            stdout.write(b[0])
            try:
                if combo_formato.GetSelection() == 1:
                    gauge_2a.SetValue(float(b[0])+1)
                    c = float(b[0])/(2*len(filenames))
                    gauge_1a.SetValue(c+(50*ii/len(filenames))+1)
                else:
                    gauge_2a.SetValue(float(b[0])+1)
                    c = float(b[0])/len(filenames)
                    gauge_1a.SetValue(c+(100*ii/len(filenames))+1)
            except:
                break

class MyFileDropTarget(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, files):
        #self.window.SetInsertionPointEnd()
        self.select = Lista.GetSelection()
        for index in range(len(files)):
            path, filename = os.path.split(files[index])
            if filename[-4:] == '.mkv' or filename[-4:] == '.mp4' or filename[-4:] == '.avi':
                filenames.append(filename)
                paths.append(files[index])
                if self.select == -1:
                    Lista.Append(filename)
                if Lista.FindString(filename) == -1:
                    Lista.Append(filename)
        if Lista.GetCount()> 0:
            button_eliminar.Enable(True)
            elim.Enable(True)
            button_convertir.Enable(True)
        Lista.SetSelection(Lista.GetCount() - 1)
        self.select = Lista.GetSelection()


class AMPEapp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        AMPEbody = AMPEclass(None, -1, "")
        self.SetTopWindow(AMPEbody)
        AMPEbody.Show()
        return 1

# end of class AMPEapp

if __name__ == "__main__":
    AMPE = AMPEapp(0)
    AMPE.MainLoop()
