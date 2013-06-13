#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# generated by wxGlade 0.6.3 on Sun Oct 16 19:24:52 2011

import wx
import os, platform, subprocess
import threading, time
try:
    import win32api
except:
    pass


folderrun = unicode(os.getcwd(), 'utf8')
# begin wxGlade: extracode
# end wxGlade

class AMPEclass(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: AMPEclass.__init__
        kwds["style"] = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |	wx.CLOSE_BOX | wx.TRANSPARENT_WINDOW
        wx.Frame.__init__(self, *args, **kwds)
        self.sizer_9_staticbox = wx.StaticBox(self, -1, u"Video")
        self.sizer_10_staticbox = wx.StaticBox(self, -1, u"Audio")
        self.sizer_6_staticbox = wx.StaticBox(self, -1, u"Opciones")
        self.sizer_7_staticbox = wx.StaticBox(self, -1, u"Archivos a Convertir")
        self.select = 0
                
        # Menu Bar
        self.Menu = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        self.open = wxglade_tmp_menu.Append(wx.NewId(), u"Abrir", "", wx.ITEM_NORMAL)
        self.elim = wxglade_tmp_menu.Append(wx.NewId(), u"Eliminar", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        self.quit = wxglade_tmp_menu.Append(wx.NewId(), u"Salir", "", wx.ITEM_NORMAL)
        self.Menu.Append(wxglade_tmp_menu, u"Archivo")
        wxglade_tmp_menu = wx.Menu()
        self.optns = wxglade_tmp_menu.Append(wx.NewId(), u"Opciones", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        self.logdel = wxglade_tmp_menu.Append(wx.NewId(), u"Borrar Logs", "", wx.ITEM_NORMAL)
        self.Menu.Append(wxglade_tmp_menu, u"Herramientas")
        wxglade_tmp_menu = wx.Menu()
        self.about = wxglade_tmp_menu.Append(wx.NewId(), u"Acerca de...", "", wx.ITEM_NORMAL)
        self.Menu.Append(wxglade_tmp_menu, u"Ayuda")
        self.SetMenuBar(self.Menu)
        # Menu Bar end
        global Lista
        Lista = wx.ListBox(self, -1)
        self.button_abrir = wx.Button(self, -1, u"Abrir")
        self.button_eliminar = wx.Button(self, -1, u"Eliminar")
        self.label_3 = wx.StaticText(self, -1, u"Formato:")
        global combo_formato
        combo_formato = wx.ComboBox(self, -1, choices=[u" MP4", u" AVI"], style=wx.CB_DROPDOWN)
        self.label_4 = wx.StaticText(self, -1, u"Resolución:")
        self.combo_resolucion = wx.ComboBox(self, -1, choices=[u"Mantener Original", u" 480p", u" 720p", u" 1080p", u" W 640px", u" W 1280px", u" W 1920px"], style=wx.CB_DROPDOWN)
        self.label_5 = wx.StaticText(self, -1, u"CRF:")
        self.slider_bitrate = wx.Slider(self, -1, 23, 10, 40)
        self.spin_bitrate = wx.SpinCtrl(self, -1, u"23", (40, 10))
        self.radio_128 = wx.RadioButton(self, -1, u"128 Kb/s")
        self.radio_160 = wx.RadioButton(self, -1, u"160 Kb/s")
        self.radio_192 = wx.RadioButton(self, -1, u"192 Kb/s")
        self.button_convertir = wx.Button(self, -1, u"Convertir")
        self.button_salir = wx.Button(self, -1, u"Salir")

        self.Bind(wx.EVT_SPINCTRL, self.OnSpin)
        self.Bind(wx.EVT_SLIDER, self.OnSlider)
        self.Bind(wx.EVT_MENU, self.OnOpen, self.open)
        self.Bind(wx.EVT_MENU, self.OnElim, self.elim)
        self.Bind(wx.EVT_MENU, self.OnQuit, self.quit)
        self.Bind(wx.EVT_MENU, self.OnAbout, self.about)
        self.Bind(wx.EVT_MENU, self.OnLogDel, self.logdel)
        self.Bind(wx.EVT_BUTTON, self.OnOpen, self.button_abrir)
        self.Bind(wx.EVT_BUTTON, self.OnElim, self.button_eliminar)
        self.Bind(wx.EVT_BUTTON, self.OnQuit, self.button_salir)
        self.Bind(wx.EVT_BUTTON, self.OnConvert, self.button_convertir)
        self.Bind(wx.EVT_LISTBOX, self.SelList, Lista)
        self.Bind(wx.EVT_COMBOBOX, self.SelFormat, combo_formato)
        self.Bind(wx.EVT_CLOSE, self.OnQuit)
        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: AMPEclass.__set_properties
        if platform.system() == 'Windows':
            self.SetTitle(u"AMPE - Al_eXs MPlayer2 Encoder para Windows")
        elif platform.system() == 'Linux':
            self.SetTitle(u"AMPE - Al_eXs MPlayer2 Encoder para Linux")
        else:
            self.SetTitle(u"AMPE - Al_eXs MPlayer2 Encoder")
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap(u"./img/icon.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((600, 520))
        Lista.SetMinSize((400, 200))
        self.elim.Enable(False)
        self.button_eliminar.Enable(False)
        combo_formato.SetSelection(0)
        self.combo_resolucion.SetSelection(0)
        self.slider_bitrate.SetMinSize((250, -1))
        self.spin_bitrate.SetMinSize((60, -1))
        self.radio_128.SetValue(1)
        self.button_convertir.Enable(False)
        self.optns.Enable(False)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: AMPEclass.__do_layout
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.StaticBoxSizer(self.sizer_6_staticbox, wx.HORIZONTAL)
        sizer_10 = wx.StaticBoxSizer(self.sizer_10_staticbox, wx.HORIZONTAL)
        sizer_11_copy = wx.BoxSizer(wx.VERTICAL)
        sizer_9 = wx.StaticBoxSizer(self.sizer_9_staticbox, wx.HORIZONTAL)
        grid_sizer_9 = wx.FlexGridSizer(3, 2, 0, 0)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.StaticBoxSizer(self.sizer_7_staticbox, wx.HORIZONTAL)
        sizer_7.Add(Lista, 3, 0, 10)
        sizer_4.Add(sizer_7, 0, wx.LEFT|wx.TOP|wx.BOTTOM, 10)
        sizer_5.Add(self.button_abrir, 0, wx.ALL, 10)
        sizer_5.Add(self.button_eliminar, 0, wx.ALL, 10)
        sizer_4.Add(sizer_5, 0, wx.TOP, 20)
        sizer_3.Add(sizer_4, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_9.Add(self.label_3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_9.Add(combo_formato, 0, wx.TOP, 5)
        grid_sizer_9.Add(self.label_4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_9.Add(self.combo_resolucion, 0, wx.TOP, 5)
        grid_sizer_9.Add(self.label_5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_12.Add(self.slider_bitrate, 0, 0, 0)
        sizer_12.Add(self.spin_bitrate, 0, 0, 0)
        grid_sizer_9.Add(sizer_12, 0, wx.TOP|wx.BOTTOM, 5)
        sizer_9.Add(grid_sizer_9, 0, 0, 0)
        sizer_6.Add(sizer_9, 0, wx.ALL, 5)
        sizer_11_copy.Add(self.radio_128, 0, wx.TOP, 5)
        sizer_11_copy.Add(self.radio_160, 0, wx.TOP, 5)
        sizer_11_copy.Add(self.radio_192, 0, wx.TOP, 5)
        sizer_10.Add(sizer_11_copy, 0, wx.ALL, 10)
        sizer_6.Add(sizer_10, 0, wx.ALL, 5)
        sizer_3.Add(sizer_6, 0, wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 10)
        sizer_8.Add(self.button_convertir, 0, wx.RIGHT, 20)
        sizer_8.Add(self.button_salir, 0, wx.LEFT, 20)
        sizer_3.Add(sizer_8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10)
        sizer_11.Add(sizer_3, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        self.SetSizer(sizer_11)
        self.Layout()
        self.Centre()
        # end wxGlade


    def OnLogDel(self, e):
        if platform.system() == 'Windows':
            for each in os.listdir(folderrun + '\\logs'):
                try:
                    os.remove(folderrun + '\\logs\\' + each)
                except:
                    pass
        if platform.system() == 'Linux':
            for each in os.listdir(folderrun + '/logs'):
                try:
                    os.remove(folderrun + '/logs/' + each)
                except:
                    pass
        wx.MessageBox('Los archivos de Log\nhan sido borrados.', ' Info', wx.OK | wx.ICON_INFORMATION)

    def SelFormat(self, e):
        if  combo_formato.GetSelection() == 1:
            self.label_5.Label = u"Bitrate:"
            self.slider_bitrate.SetRange(500, 6000)
            self.slider_bitrate.SetValue(1500)
            self.spin_bitrate.SetRange(500, 6000)
            self.spin_bitrate.SetValueString(u"1500")
        else:
            self.label_5.Label = u"CRF:"
            self.slider_bitrate.SetRange(10, 40)
            self.slider_bitrate.SetValue(23)
            self.spin_bitrate.SetRange(10, 40)
            self.spin_bitrate.SetValueString(u"23")

    def OnQuit(self, e):
        print "Bye Bye"
        time.sleep(1)
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
            global filenames
            filenames = dlg.GetFilenames()
            global paths
            paths = dlg.GetPaths()
            for filename in filenames:
                if self.select == -1:
                    Lista.Append(filename)
                if Lista.FindString(filename) == -1:
                    Lista.Append(filename)
            if Lista.GetCount()> 0:
                self.button_eliminar.Enable(True)
                self.elim.Enable(True)
                self.button_convertir.Enable(True)
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
            self.button_eliminar.Enable(False)
            self.elim.Enable(False)
            self.button_convertir.Enable(False)
        self.select = Lista.GetSelection()
        
    def SelList(self, e):
        self.select = Lista.GetSelection()
        
    def OnConvert(self, e):
        if combo_formato.GetSelection() == 0:
            formato = u'converted.mp4" -ofps 23.976 -ovc libx264 -oac aac -ovcopts preset=medium,profile=main,crf='
            bit2 = u" -af channels=2,resample=44100 -oacopts ab="
            format = u"mp4"
        elif combo_formato.GetSelection() == 1:
            formato1 = u'converted.avi" -ofps 23.976 -of avi -nosound -ovc libxvid -oac libmp3lame -ovcopts flags=+pass1,threads=2'
            formato2 = u'converted.avi" -ofps 23.976 -of avi -ovc libxvid -oac libmp3lame -ovcopts flags=+pass2,threads=2,b='
            bit2 = u"k -af channels=2,resample=44100 -oacopts ab="
            format = u"avi"

        if self.combo_resolucion.GetSelection() == 0:
            resolucion = u" -vf scale=-1"
        elif self.combo_resolucion.GetSelection() == 1:
            resolucion = u" -vf scale=-3:480"
        elif self.combo_resolucion.GetSelection() == 2:
            resolucion = u" -vf scale=-3:720"
        elif self.combo_resolucion.GetSelection() == 3:
            resolucion = u" -vf scale=-3:1080"
        elif self.combo_resolucion.GetSelection() == 4:
            resolucion = u" -vf scale=640:-3"
        elif self.combo_resolucion.GetSelection() == 5:
            resolucion = u" -vf scale=1280:-3"
        elif self.combo_resolucion.GetSelection() == 6:
            resolucion = u" -vf scale=1920:-3"

        bitrate = unicode(self.spin_bitrate.GetValue())

        if self.radio_128.Value == 1: audio = u"128k"
        if self.radio_160.Value == 1: audio = u"160k"
        if self.radio_192.Value == 1: audio = u"192k"
        
        if platform.system() == 'Windows': mp2 = u"mplayer2.exe"
        if platform.system() == 'Linux' : mp2 = u"mplayer2-lavc"
        
        global encodear
        encodear = []
        global logfile
        logfile = []
        
        for i in range(len(paths)):
            paths[i] = paths[i].encode('utf-8')
            filenames[i] = filenames[i].encode('utf-8')
#            print paths[i]#
#            print filenames[i]#
            input = paths[i]
            output = paths[i][:-3]
            if combo_formato.GetSelection() == 1:
                if platform.system() == 'Windows':
                    encodear.append(u'"' + folderrun + u'\\bin\\' + mp2 + u'" "' + win32api.GetShortPathName(unicode(input,'utf-8')) + u'" -o "' + unicode(output,'utf-8') + formato1 + resolucion)
                    encodear.append(u'"' + folderrun + u'\\bin\\' + mp2 + u'" "' + win32api.GetShortPathName(unicode(input,'utf-8')) + u'" -o "' + unicode(output,'utf-8') + formato2 + bitrate + bit2 + audio + resolucion)
                    logfile.append(folderrun + u'\\logs\\' + unicode(filenames[i],'utf-8') + u'-to-' + format + u'.first_pass.log')
                    logfile.append(folderrun + u'\\logs\\' + unicode(filenames[i],'utf-8') + u'-to-' + format + u'.second_pass.log')
                if platform.system() == 'Linux':
                    encodear.append(u'"' + folderrun + u'/bin/' + mp2 + u'" "' + unicode(input,'utf-8') + u'" -o "' + unicode(output,'utf-8') + formato1 + resolucion)
                    encodear.append(u'"' + folderrun + u'/bin/' + mp2 + u'" "' + unicode(input,'utf-8') + u'" -o "' + unicode(output,'utf-8') + formato2 + bitrate + bit2 + audio + resolucion)
                    logfile.append(folderrun + u'/logs/' + unicode(filenames[i],'utf-8') + u'-to-' + format + u'.first_pass.log')
                    logfile.append(folderrun + u'/logs/' + unicode(filenames[i],'utf-8') + u'-to-' + format + u'.second_pass.log')
            else:
                if platform.system() == 'Windows':
                    encodear.append(u'"' + folderrun + u'\\bin\\' + mp2 + u'" "' + win32api.GetShortPathName(unicode(input,'utf-8')) + u'" -o "' + unicode(output,'utf-8') + formato + bitrate + bit2 + audio + resolucion)
                    logfile.append(folderrun + u'\\logs\\' + unicode(filenames[i],'utf-8') + u'-to-' + format + u'.log')
                if platform.system() == 'Linux':
                    encodear.append(u'"' + folderrun + u'/bin/' + mp2 + u'" "' + unicode(input,'utf-8') + u'" -o "' + unicode(output,'utf-8') + formato + bitrate + bit2 + audio + resolucion)
                    logfile.append(folderrun + u'/logs/' + unicode(filenames[i],'utf-8') + u'-to-' + format + u'.log')
        global salir
        salir = False
        convertir = Encodeo(self)
        convertir.start()
        frame2 = ConvertDialog(self)
        frame2.Show()
        

    def OnAbout(self, e):
        description = u"""
AMPE (Al_eXs MPlayer2 Encoder) es una Interfaz Gráfica de
Usuario(GUI) para encodear videos MKV, MP4 o AVI en MP4 o
AVI compatibles con las consolas usando como fuente para
encodear el MPlayer2.\n
Acepta estilos y enlaza los capitulos con
Ordered Chapters Externos(Segment Linking).\n
Agradecimientos:
-lash0r por el build del mplayer2 para windows.
-ErunamoJAZZ(AnS) por su apoyo en mejorar mi codigo python.
-Batousay(BB) por su tip para las barras de progreso.
-Xibalba, Seposi, ZeroTheBest por probar las versiones betas.\n"""
        
        licence = u"""
AMPE es un sofware libre; se puede redistribuir y/o modificar
bajo los terminos de la Licencia Publica General GNU Version 3.
AMPE es distribuido con la esperanza de ser un software util
pero SIN GARANTIA ALGUNA.\n"""

        info = wx.AboutDialogInfo()
        if platform.system() == 'Linux': info.SetIcon(wx.Icon(folderrun + '/img/logo.png', wx.BITMAP_TYPE_PNG))
        if platform.system() == 'Windows': info.SetIcon(wx.Icon(folderrun + '\\img\\logo.png', wx.BITMAP_TYPE_PNG))
        info.SetName(u"AMPE")
        info.SetVersion(u"1.0.9")
        info.SetDescription(description)
        info.SetCopyright(u'(C) 2013 Al_eXs')
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
        kwds["style"] = wx.CAPTION
        wx.Frame.__init__(self, None, -1, title = u"  Convirtiendo", **kwds)
        self.label_1a = wx.StaticText(self, -1, u"Convirtiendo:")
        global label_capi
        label_capi = wx.StaticText(self, -1, "")#nombre del capi
        global gauge_2a
        gauge_2a = wx.Gauge(self, -1, 100)
        self.label_2a = wx.StaticText(self, -1, u"Progreso Total:")
        global label_total
#        label_total = wx.StaticText(self, -1, "")
        global gauge_1a
        gauge_1a = wx.Gauge(self, -1, 100)
        global button_minimize
        button_minimize = wx.Button(self, -1, u"Minimizar")
        global button_cancel
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
        self.Centre()
        # end wxGlade
    
    def OnCancel(self, e):
        if not button_cancel.Label == u"Cerrar":
            salir = True
            enc = Encodeo(self)
            enc.stop()
            self.padre.button_eliminar.Enable(True)
            self.padre.elim.Enable(True)
            self.padre.button_convertir.Enable(True)
        self.padre.Show(True)
        self.Destroy()
        
    def OnMin(self, e):
        self.Iconize(True)
#        self.padre.Iconize(True)

        
class Encodeo(threading.Thread):
    def __init__(self, e):
        threading.Thread.__init__(self)
 #       self.setDaemon(True)
        
    def run(self):
        global i
        i = 0
        while not salir:
            try:
                os.remove(logfile[i])
            except:
                pass
            self.proceso = subprocess.Popen(encodear[i].encode('utf-8'), stdout = open(logfile[i], "a"), stderr = open(logfile[i], "a"), shell = True)
            if combo_formato.GetSelection() == 1:
                label_capi.SetLabel(filenames[i/2])
                print filenames[i/2]
            else:
                label_capi.SetLabel(filenames[i])
                print filenames[i]
            bars = Barras(self)
            bars.start()
            self.proceso.wait()
            time.sleep(1)
            if i == len(encodear)-1:
                break
            i +=1
        try:
            if not salir:
                label_capi.SetLabel(u" ")
                gauge_1a.SetValue(100)
                gauge_2a.SetValue(100)
                wx.MessageBox(u'Terminó la Conversión', 'Info', wx.OK | wx.ICON_INFORMATION)
            button_cancel.Label = u"Cerrar"
            button_minimize.Enable(False)
            Lista.Clear()
        except:
            pass
    
    def stop(self):
        global salir
        salir = True
        if platform.system() == 'Linux': self.kill = subprocess.Popen(u"killall mplayer2-lavc", shell = True)
        if platform.system() == 'Windows': self.kill = subprocess.Popen(u"taskkill /F /IM mplayer2.exe", shell = True)

       
class Barras(threading.Thread):
    def __init__(self, e):
        threading.Thread.__init__(self)
       
    def run(self):
        while True:
            time.sleep(3)
            prs = open(logfile[i], "r")
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
            print '{0}\r'.format(b[0]),
#            print b[0]#
            try:
                if combo_formato.GetSelection() == 1:
                    gauge_2a.SetValue(float(b[0])+1)
                    c = float(b[0])/(2*len(filenames))
                    gauge_1a.SetValue(c+(50*i/len(filenames))+1)
                else:
                    gauge_2a.SetValue(float(b[0])+1)
                    c = float(b[0])/len(filenames)
                    gauge_1a.SetValue(c+(100*i/len(filenames))+1)
            except:
                break

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