#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Sun Oct 16 19:24:52 2011

import wx
import os, platform, subprocess
import threading, time

folderrun = os.getcwd()
# begin wxGlade: extracode
# end wxGlade

class AMPEclass(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: AMPEclass.__init__
        kwds["style"] = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |	wx.CLOSE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.sizer_9_staticbox = wx.StaticBox(self, -1, "Video")
        self.sizer_10_staticbox = wx.StaticBox(self, -1, "Audio")
        self.sizer_6_staticbox = wx.StaticBox(self, -1, "Opciones")
        self.sizer_7_staticbox = wx.StaticBox(self, -1, "Archivos a Convertir")
        self.select = 0
                
        # Menu Bar
        self.Menu = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        self.open = wxglade_tmp_menu.Append(wx.NewId(), "Abrir", "", wx.ITEM_NORMAL)
        self.elim = wxglade_tmp_menu.Append(wx.NewId(), "Eliminar", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        self.quit = wxglade_tmp_menu.Append(wx.NewId(), "Salir", "", wx.ITEM_NORMAL)
        self.Menu.Append(wxglade_tmp_menu, "Archivo")
        wxglade_tmp_menu = wx.Menu()
        self.about = wxglade_tmp_menu.Append(wx.NewId(), "Acerca de...", "", wx.ITEM_NORMAL)
        self.Menu.Append(wxglade_tmp_menu, "Ayuda")
        self.SetMenuBar(self.Menu)
        # Menu Bar end
        global Lista
        Lista = wx.ListBox(self, -1)
        self.button_abrir = wx.Button(self, -1, "Abrir")
        self.button_eliminar = wx.Button(self, -1, "Eliminar")
        self.label_3 = wx.StaticText(self, -1, "Formato:")
        self.combo_formato = wx.ComboBox(self, -1, choices=[" MP4", " AVI"], style=wx.CB_DROPDOWN)
        self.label_4 = wx.StaticText(self, -1, u"Resolución:")
        self.combo_resolucion = wx.ComboBox(self, -1, choices=["Mantener Original", " 640 x 480 (4:3)", " 1280 x 720 (16:9)", " 480p (Mismo Aspect Ratio)", " 720p (Mismo Aspect Ratio)"], style=wx.CB_DROPDOWN)
        self.label_5 = wx.StaticText(self, -1, "CRF:")
        self.slider_bitrate = wx.Slider(self, -1, 23, 10, 40)
        self.spin_bitrate = wx.SpinCtrl(self, -1, "23", (40, 10))
        self.radio_128 = wx.RadioButton(self, -1, "128 Kb/s")
        self.radio_160 = wx.RadioButton(self, -1, "160 Kb/s")
        self.radio_192 = wx.RadioButton(self, -1, "192 Kb/s")
        self.button_convertir = wx.Button(self, -1, "Convertir")
        self.button_salir = wx.Button(self, -1, "Salir")

        self.Bind(wx.EVT_SPINCTRL, self.OnSpin)
        self.Bind(wx.EVT_SLIDER, self.OnSlider)
        self.Bind(wx.EVT_MENU, self.OnOpen, self.open)
        self.Bind(wx.EVT_MENU, self.OnElim, self.elim)
        self.Bind(wx.EVT_MENU, self.OnQuit, self.quit)
        self.Bind(wx.EVT_MENU, self.OnAbout, self.about)
        self.Bind(wx.EVT_BUTTON, self.OnOpen, self.button_abrir)
        self.Bind(wx.EVT_BUTTON, self.OnElim, self.button_eliminar)
        self.Bind(wx.EVT_BUTTON, self.OnQuit, self.button_salir)
        self.Bind(wx.EVT_BUTTON, self.OnConvert, self.button_convertir)
        self.Bind(wx.EVT_LISTBOX, self.SelList, Lista)
        self.Bind(wx.EVT_COMBOBOX, self.SelFormat, self.combo_formato)
        self.Bind(wx.EVT_CLOSE, self.OnQuit)
        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: AMPEclass.__set_properties
        if platform.system() == 'Windows':
            self.SetTitle("AMPE - Al_eXs MPlayer2 Encoder para Windows")
        elif platform.system() == 'Linux':
            self.SetTitle("AMPE - Al_eXs MPlayer2 Encoder para Linux")
        else:
            self.SetTitle("AMPE - Al_eXs MPlayer2 Encoder")
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("./img/icon.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((600, 520))
        Lista.SetMinSize((400, 200))
        self.elim.Enable(False)
        self.button_eliminar.Enable(False)
        self.combo_formato.SetSelection(0)
        self.combo_resolucion.SetSelection(0)
        self.slider_bitrate.SetMinSize((250, -1))
        self.spin_bitrate.SetMinSize((60, -1))
        self.radio_160.SetValue(1)
        self.button_convertir.Enable(False)
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
        grid_sizer_9.Add(self.combo_formato, 0, wx.TOP, 5)
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

    def SelFormat(self, e):
        if  self.combo_formato.GetSelection() == 1:
            self.label_5.Label = "Bitrate:"
            self.slider_bitrate.SetRange(500, 6000)
            self.slider_bitrate.SetValue(1500)
            self.spin_bitrate.SetRange(500, 6000)
            self.spin_bitrate.SetValueString("1500")
        else:
            self.label_5.Label = "CRF:"
            self.slider_bitrate.SetRange(10, 40)
            self.slider_bitrate.SetValue(23)
            self.spin_bitrate.SetRange(10, 40)
            self.spin_bitrate.SetValueString("23")

    def OnQuit(self, e):
        self.Destroy()

    def OnOpen(self, e):
        self.select = Lista.GetSelection()
        dlg = wx.FileDialog(
            self, message=u"Añadir un Archivo",
            defaultFile="",
            wildcard="Video (*.mkv; *.mp4; *.avi)|*.mkv;*.mp4;*.avi|MKV|*.mkv|MP4|*.mp4|AVI|*.avi",
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
 #       print Lista.GetSelection()
        if Lista.GetCount() == 0:
            self.button_eliminar.Enable(False)
            self.elim.Enable(False)
            self.button_convertir.Enable(False)
        self.select = Lista.GetSelection()
        
    def SelList(self, e):
        self.select = Lista.GetSelection()
        
    def OnConvert(self, e):
        if self.combo_formato.GetSelection() == 0:
            formato = 'converted.mp4" -ofps 23.976 -ovc libx264 -oac aac -ovcopts preset=medium,profile=main,crf='
            bit2 = " -oacopts ab="
            format = "mp4"
        elif self.combo_formato.GetSelection() == 1:
            formato = 'converted.avi" -ofps 23.976 -ovc libxvid -oac libmp3lame -ovcopts b='
            bit2 = "k -oacopts ab="
            format = "avi"

        if self.combo_resolucion.GetSelection() == 0:
            resolucion = " -vf scale=-1"
        elif self.combo_resolucion.GetSelection() == 1:
            resolucion = " -vf scale="
        elif self.combo_resolucion.GetSelection() == 2:
            resolucion = " -vf scale="
        elif self.combo_resolucion.GetSelection() == 3:
            resolucion = " -vf scale="
        elif self.combo_resolucion.GetSelection() == 4:
            resolucion = " -vf scale="
        
        bitrate = str(self.spin_bitrate.Value)

        if self.radio_128.Value == 1: audio = "128k"
        if self.radio_160.Value == 1: audio = "160k"
        if self.radio_192.Value == 1: audio = "192k"
        
        if platform.system() == 'Windows': mp2 = "mplayer2.exe"
        if platform.system() == 'Linux' : mp2 = "mplayer2"
        
        global encodear
        encodear = []
        global logfile
        logfile = []
        
        for i in range(len(paths)):
            input = paths[i]
            output = paths[i][:-3]
            encodear.append(folderrun + u"\\bin\\" + mp2 + ' "' + input + '" -o "' + output + formato + bitrate + bit2 + audio + resolucion)
            logfile.append(folderrun + "\\logs\\" + filenames[i] + "-to-" + format + ".log")
        
        convertir = Encodeo(self)
        convertir.start()
        frame2 = ConvertDialog(self)
        frame2.ShowModal()
        

    def OnAbout(self, e):
        description1 = u"AMPE (Al_eXs MPlayer2 Encoder) es una Interfaz Gráfica de Usuario(GUI)\n"
        description2 = u"para encodear videos MKV, MP4 o AVI en MP4 o AVI compatibles con\n"
        description3 = u"las consolas usando como fuente para encodear el MPlayer2.\n\n"
        description4 = u"Acepta estilos y enlaza los capitulos con Ordered Chapters Externos.\n\n"
        description5 = u"Agradecimientos:\n-ErunamoJAZZ, por su apoyo en mejorar mi codigo python\n"
        description = description1 + description2 + description3 + description4 + description5
        licence1 = u"AMPE es un sofware libre; se puede redistribuir y/o modificar\n"
        licence2 = u"bajo los terminos de la Licencia Publica General GNU Version 3.\n"
        licence3 = u"AMPE es distribuido con la esperanza de ser un software util\n"
        licence4 = u"pero SIN GARANTIA ALGUNA."
        licence = licence1 + licence2 + licence3 + licence4
        info = wx.AboutDialogInfo()
        info.SetIcon(wx.Icon("./img/logo.png", wx.BITMAP_TYPE_PNG))
        info.SetName("AMPE")
        info.SetVersion("0.1.0")
        info.SetDescription(description)
        info.SetCopyright('(C) 2011 Al_eXs')
        info.SetLicence(licence)
        wx.AboutBox(info)

    def OnSlider(self, e):
        self.spin_bitrate.SetValue(self.slider_bitrate.GetValue())

    def OnSpin(self, e):
        self.slider_bitrate.SetValue(self.spin_bitrate.GetValue())
        
# end of class AMPEclass

class ConvertDialog(wx.Dialog):
    def __init__(self, parent, **kwds):
        # begin wxGlade: ConvertDialog.__init__
        kwds["style"] = wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX
        wx.Dialog.__init__(self, None, -1, title="Convirtiendo")
        self.label_1a = wx.StaticText(self, -1, "Convirtiendo:")
        global label_capi
        label_capi = wx.StaticText(self, -1, "")#nombre del capi
#        self.gauge_2a = wx.Gauge(self, -1, 10)
        self.label_2a = wx.StaticText(self, -1, "Progreso Total:")
        global label_total
        label_total = wx.StaticText(self, -1, "")
#        self.gauge_1a = wx.Gauge(self, -1, 10)
        global button_minimize
        button_minimize = wx.Button(self, -1, "Minimizar")
        global button_cancel
        button_cancel = wx.Button(self, -1, "Cancelar")
        self.padre = parent
        
        self.Bind(wx.EVT_BUTTON, self.OnCancel, button_cancel)
        self.Bind(wx.EVT_BUTTON, self.OnMin, button_minimize)
        self.Bind(wx.EVT_CLOSE, self.OnCancel)
        
        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: ConvertDialog.__set_properties
        self.SetTitle("Convirtiendo")
        self.SetSize((500, 200))
#        self.gauge_2a.SetMinSize((450, 15))
#        self.gauge_1a.SetMinSize((450, 15))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ConvertDialog.__do_layout
        sizer_1a = wx.BoxSizer(wx.VERTICAL)
        sizer_2a = wx.BoxSizer(wx.VERTICAL)
        sizer_5a = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4a = wx.BoxSizer(wx.VERTICAL)
        sizer_3a = wx.BoxSizer(wx.VERTICAL)
        sizer_3a.Add(self.label_1a, 0, wx.BOTTOM, 10)
        sizer_3a.Add(label_capi, 0, 0, 0)
#        sizer_3a.Add(self.gauge_2a, 0, 0, 0)
        sizer_2a.Add(sizer_3a, 0, wx.LEFT|wx.TOP, 20)
        sizer_4a.Add(self.label_2a, 0, wx.BOTTOM, 10)
        sizer_4a.Add(label_total, 0, 0, 0)
 #       sizer_4a.Add(self.gauge_1a, 0, 0, 0)
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
        if not button_cancel.Label == "Cerrar":
            enc = Encodeo(self)
            enc.stop()
        self.Destroy()
        
    def OnMin(self, e):
        self.Iconize(True)
        self.padre.Iconize(True)

        
class Encodeo(threading.Thread):
    def __init__(self, _wxText):
        threading.Thread.__init__(self)
 #       self.setDaemon(True)
        
    def run(self):
        salir = False
        i = 0
        while True:
           # print i
            time.sleep(3)
           # print i
            cap = "Capitulo: " + str(filenames[i])
            tot = str(i+1) + " de " + str(len(filenames))
            label_capi.Label = cap
            label_total.Label = tot
            self.proceso = subprocess.Popen(encodear[i], stdout = open(logfile[i], "a"), stderr = open(logfile[i], "a"), shell = True).wait()
           # print i
            if salir:
              #  print "out"
                break
            if i==len(filenames)-1:
               # print "fuera"
                break
            i +=1
        
        button_cancel.Label = "Cerrar"
        button_minimize.Enable(False)
        Lista.Clear()
    
    def stop(self):
        salir = True
        self.proceso.terminate()


'''        
class Barras(AMPEclass):
    def __init__(parent):
        self.padre = parent
        
    def run():
        while True:
            time.sleep(2)
            prs = open(self.padre.logfile, "r")
            for last in prs:
                porcentaje=last
            ConverDialog().gauge_2a.SetValue(porcentaje[-38:-36])
            print porcentaje[-38:-36]
            if not self.corriendo:
                break
    def kill():
        self.corriendo = False
'''

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