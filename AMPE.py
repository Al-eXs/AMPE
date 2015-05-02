#!/usr/bin/env python
# -*- coding: UTF-8 -*-
version = u'1.1.0'

import os, sys
from subprocess import Popen
from platform import system
from time import sleep
from PySide.QtCore import *
from PySide.QtGui import *
try:
	from win32api import GetShortPathName
except:
	pass

FNULL = open(os.devnull, 'w')
if system() == 'Windows':
	folderrun = GetShortPathName(unicode(os.getcwd(), 'utf-8'))
if system() == 'Linux':
	folderrun = unicode(os.getcwd(), 'utf-8')
	
class BarWork(QThread):
	setProg = Signal(int, int)
	def __init__(self, parent):
		super(BarWork, self).__init__(parent)
		self.parent = parent

	def run(self):
		while True:
			sleep(2)
			prs = open(logfile[ii], 'r')
			for last in prs:
				prs2 = last
			prs2 = str(prs2)
			a = prs2[-80:-10].split(u'(')
			try:
				b = a[1].split(u'%')
			except IndexError:
				break
			try:
				if self.parent.comboFormat.currentIndex() == 1:
					c = float(b[0])/(2*len(filenames))
					self.setProg.emit(float(b[0])+1, c+(50*ii/len(filenames))+1)
				else:
					c = float(b[0])/(len(filenames))
					self.setProg.emit(float(b[0])+1, c+(100*ii/len(filenames))+1)
			except:
				break

class EncodeWork(QThread):
	setBtn = Signal(str)
	setLbl = Signal(str)
	def __init__(self, parent):
		super(EncodeWork, self).__init__(parent)
		self.parent = parent
	def run(self):
		global ii
		ii = 0
		while not stopConvert:
			try:
				os.remove(logfile[ii])
			except:
				pass
			process = Popen(encodes[ii].encode('utf-8'), stdout = open(logfile[ii], 'a'), stderr = open(logfile[ii], 'a'), shell = True)
			if self.parent.comboFormat.currentIndex() == 1:
				self.setLbl.emit(filenames[ii/2])
			else:
				self.setLbl.emit(filenames[ii])
			process.wait()
			
			f = open(logfile[ii], 'a')
			f.write(u'\n\n')
			f.write(encodes[ii].encode('utf-8'))
			f.close()
			if system() == 'Windows':
				if self.parent.comboFormat.currentIndex() == 1:
					try:
						os.remove(unicode(paths[ii/2][:-4], 'utf-8') + u'_converted.avi')
					except:
						pass
					try:
						if ii & 1: os.rename(folderrun + u'\\logs\\output' + str(ii/2) + u'_converted.avi', unicode(paths[ii/2][:-4], u'utf-8') + u'_converted.avi')
					except:
						pass
				else:
					try:
						os.remove(unicode(paths[ii][:-4], 'utf-8') + u'_converted.mp4')
					except:
						pass
					try:
						os.rename(folderrun + u'\\logs\\output' + str(ii) + u'_converted.mp4', unicode(paths[ii][:-4], 'utf-8') + u'_converted.mp4')
					except:
						pass
			sleep(2)
			if ii == (len(encodes) - 1):
				break
			ii += 1
		self.parent.bars.quit()
		if not stopConvert:
			self.setBtn.emit(u'ok')
		else:
			self.setBtn.emit(u'not')

	def stop(self):
		global stopConvert
		stopConvert = True
		self.parent.bars.quit()
		try:
			if system() == 'Linux': kill = Popen(u'killall mpv', shell = True)
			if system() == 'Windows': kill = Popen(u'taskkill /F /IM mpv.exe', stdout=FNULL, stderr=FNULL, shell = True)
		except:
			pass

class AMPEapp(QMainWindow):
	def __init__(self):
		super(AMPEapp, self).__init__()
		self.initUI()
		
		global filenames, paths
		filenames = []
		paths = []
		
	def initUI(self):
		# Menu Actions
		self.openAction = QAction(self.style().standardIcon(QStyle.SP_DirOpenIcon), u'&Abrir', self)
		self.delAction = QAction(self.style().standardIcon(QStyle.SP_TrashIcon), u'&Eliminar', self)
		self.exitAction = QAction(self.style().standardIcon(QStyle.SP_DialogCancelButton), u'&Salir', self)
		self.optnsAction = QAction(self.style().standardIcon(QStyle.SP_TitleBarNormalButton), u'&Opciones', self)
		self.delLogsAction = QAction(self.style().standardIcon(QStyle.SP_MessageBoxWarning), u'&Borrar Logs', self)
		self.aboutAction = QAction(self.style().standardIcon(QStyle.SP_MessageBoxInformation), u'A&cerca de...', self)
		self.aboutQtAction = QAction(u'A&cerca de Qt', self)
		self.licenceAction = QAction(u'Licencia', self)
		# Menu Shortcuts
		self.openAction.setShortcut(u'Ctrl+A')
		self.delAction.setShortcut(u'Ctrl+E')
		self.exitAction.setShortcut(u'Ctrl+Q')
		self.optnsAction.setShortcut(u'Ctrl+O')
		self.delLogsAction.setShortcut(u'F12')
		self.aboutAction.setShortcut(u'F1')
		# Menu Statustip
		self.openAction.setStatusTip(u'Agregar un archivo')
		self.delAction.setStatusTip(u'Eliminar un archivo')
		self.exitAction.setStatusTip(u'Salir de la aplicación')
		self.optnsAction.setStatusTip(u'Opciones')
		self.delLogsAction.setStatusTip(u'Borrar Logs de conversiones')
		self.aboutAction.setStatusTip(u'Información de la aplicación')
		self.aboutQtAction.setStatusTip(u'Información acerca de Qt')
		self.licenceAction.setStatusTip(u'Información acerca de la Licencia')
		# Menu Connects
		self.openAction.triggered.connect(self.onOpen)
		self.delAction.triggered.connect(self.onDel)
		self.exitAction.triggered.connect(self.close)
		self.optnsAction.triggered.connect(self.onOptions)
		self.delLogsAction.triggered.connect(self.onDelLogs)
		self.aboutAction.triggered.connect(self.onAbout)
		self.aboutQtAction.triggered.connect(self.onQtAbout)
		self.licenceAction.triggered.connect(self.onLicence)
		# Menu properties
		self.delAction.setDisabled(True)
		self.optnsAction.setDisabled(True)
		# Menu Layout
		self.menubar = self.menuBar()
		self.fileMenu = self.menubar.addMenu(u'&Archivo')
		self.fileMenu.addAction(self.openAction)
		self.fileMenu.addAction(self.delAction)
		self.fileMenu.addSeparator()
		self.fileMenu.addAction(self.exitAction)
		self.toolsMenu = self.menubar.addMenu(u'&Herramientas')
		self.toolsMenu.addAction(self.optnsAction)
		self.toolsMenu.addSeparator()
		self.toolsMenu.addAction(self.delLogsAction)
		self.helpMenu = self.menubar.addMenu(u'A&yuda')
		self.helpMenu.addAction(self.aboutAction)
		self.helpMenu.addAction(self.aboutQtAction)
		self.helpMenu.addAction(self.licenceAction)

		# Widgets
		self.convertBtn = QPushButton(self.style().standardIcon(QStyle.SP_MediaPlay), u'&Convertir')
		self.stopBtn = QPushButton(self.style().standardIcon(QStyle.SP_MediaStop), u'&Detener')
		self.exitBtn = QPushButton(self.style().standardIcon(QStyle.SP_DialogCancelButton), u'&Salir')
		self.openBtn = QPushButton(self.style().standardIcon(QStyle.SP_DialogOpenButton), u'&Abrir')
		self.delBtn = QPushButton(self.style().standardIcon(QStyle.SP_DialogDiscardButton), u'&Eliminar')
		self.list = QListWidget()
		self.slid = QSlider(Qt.Horizontal)
		self.spin = QSpinBox()
		self.pbar1 = QProgressBar()
		self.pbar2 = QProgressBar()
		self.comboFormat = QComboBox()
		self.comboRes = QComboBox()
		self.comboAudio = QComboBox()
		self.resVal = QLineEdit()
		self.formatLabel = QLabel(u'Formato:')
		self.resLabel = QLabel(u'Resolución:')
		self.crfLabel = QLabel(u'CRF:')
		self.pxLabel = QLabel(u'px')
		self.audioLabel = QLabel(u'Audio:')
		self.statusLabel = QLabel()
		self.filesBox = QGroupBox(u'Archivos a Convertir')
		self.optBox = QGroupBox(u'Opciones')
		self.videoBox = QGroupBox(u'Video')
		self.audioBox = QGroupBox(u'Audio')
		# Widgets Properties
		self.pbar1.setMinimum(0)
		self.pbar1.setMaximum(100)
		self.pbar2.setMinimum(0)
		self.pbar2.setMaximum(100)
		self.comboFormat.addItem(u'MP4')
		self.comboFormat.addItem(u'AVI')
		self.comboRes.addItem(u'Mantener Original')
		self.comboRes.addItem(u'Ajustar Alto')
		self.comboRes.addItem(u'Ajustar Ancho')
		self.comboRes.addItem(u'720x400')
		self.comboRes.addItem(u'720x576')
		self.comboRes.addItem(u'848x480')
		self.comboRes.addItem(u'640x480')
		self.comboAudio.addItem(u'Stereo (2 canales)')
		self.comboAudio.addItem(u'5.1 (6 canales)')
		self.resVal.setText(u'500')
		self.resVal.setDisabled(True)
		self.slid.setRange(10, 30)
		self.slid.setValue(23)
		self.spin.setRange(10, 30)
		self.spin.setValue(23)
		self.spin.setSuffix(u'')
		self.spin.setSingleStep(1)
		self.delBtn.setDisabled(True)
		self.stopBtn.setDisabled(True)
		self.convertBtn.setDisabled(True)
		# Widgets Tooltips
		# Widgets Connects
		self.exitBtn.clicked.connect(self.close)
		self.openBtn.clicked.connect(self.onOpen)
		self.delBtn.clicked.connect(self.onDel)
		self.convertBtn.clicked.connect(self.onConvert)
		self.stopBtn.clicked.connect(self.onStop)
		self.slid.valueChanged.connect(self.onSlid)
		self.spin.valueChanged.connect(self.onSpin)
		self.comboRes.activated.connect(self.onSelRes)
		self.comboFormat.activated.connect(self.onSelFormat)
		# Widgetss Layout
		self.vbox1 = QVBoxLayout()
		self.vbox1.addWidget(self.openBtn)
		self.vbox1.addSpacing(10)
		self.vbox1.addWidget(self.delBtn)
		self.vbox1.addStretch(1)
		self.hbox1 = QHBoxLayout()
		self.hbox1.addWidget(self.list, 1)
		self.hbox1.addLayout(self.vbox1)
		self.filesBox.setLayout(self.hbox1)
		self.hbox2 = QHBoxLayout()
		self.hbox2.addWidget(self.formatLabel, 1)
		self.hbox2.addWidget(self.comboFormat, 1)
		self.hbox2.addStretch(8)
		self.hbox3 = QHBoxLayout()
		self.hbox3.addWidget(self.resLabel, 1)
		self.hbox3.addWidget(self.comboRes, 2)
		self.hbox3.addWidget(self.resVal, 1)
		self.hbox3.addWidget(self.pxLabel, 1)
		self.hbox3.addStretch(5)
		self.hbox4 = QHBoxLayout()
		self.hbox4.addWidget(self.crfLabel, 1)
		self.hbox4.addWidget(self.slid, 7)
		self.hbox4.addWidget(self.spin, 2)
		self.vbox2 = QVBoxLayout()
		self.vbox2.addLayout(self.hbox2)
		self.vbox2.addLayout(self.hbox3)
		self.vbox2.addLayout(self.hbox4)
		self.videoBox.setLayout(self.vbox2)
		self.hbox5 = QHBoxLayout()
		self.hbox5.addWidget(self.audioLabel, 1)
		self.hbox5.addWidget(self.comboAudio, 2)
		self.hbox5.addStretch(7)
		self.audioBox.setLayout(self.hbox5)
		self.vbox3 = QVBoxLayout()
		self.vbox3.addWidget(self.videoBox)
		self.vbox3.addWidget(self.audioBox)
		self.optBox.setLayout(self.vbox3)
		self.hbox6 = QHBoxLayout()
		self.hbox6.addStretch(5)
		self.hbox6.addWidget(self.convertBtn, 3)
		self.hbox6.addSpacing(20)
		self.hbox6.addWidget(self.stopBtn, 3)
		self.hbox6.addSpacing(20)
		self.hbox6.addWidget(self.exitBtn, 3)
		self.hbox6.addStretch(5)
		self.vbox = QVBoxLayout()
		self.vbox.addWidget(self.filesBox)
		self.vbox.addWidget(self.optBox)
		self.vbox.addLayout(self.hbox6)
		self.form = QWidget()
		self.form.setLayout(self.vbox)
		self.setCentralWidget(self.form)

		# Window settings
		self.setAcceptDrops(True)
		self.setFixedSize(600,550)
		self.setWindowTitle(u'AMPE - Al_eXs\' MPV Encoder ' + version)
		self.setWindowIcon(QIcon('img/AMPE.png'))
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
		# Status Bar
		self.statBar = QStatusBar()
		self.statBar.addWidget(self.statusLabel, 4)
		self.statBar.addWidget(self.pbar1, 2)
		self.statBar.addWidget(self.pbar2, 2)
		self.statBar.showMessage(u"En espera...", 2000)
		self.pbar1.setValue(0)
		self.pbar2.setValue(0)
		self.setStatusBar(self.statBar)
		# Show Window			
		self.show()
	
	def closeEvent(self, event):
		try:
			self.convert.stop()
		except:
			pass
		if system() == 'Windows':
			for each in os.listdir(folderrun + '\\logs'):
				try:
					if each.endswith('.mp4') or each.endswith('.avi') or each.startswith('output'):
						os.remove(folderrun + '\\logs\\' + each)
				except:
					pass
	def onConvert(self):
		self.convertBtn.setDisabled(True)
		self.onLock()
		if self.comboFormat.currentIndex() == 0:
			format1 = u'_converted.mp4" -ofps 23.976 -ovfirst -ovc libx264 -ovcopts preset=medium,profile=high,crf='
			bit2 = u' --audio-channels='
			format = u'mp4'
		elif self.comboFormat.currentIndex() == 1:
			format1 = u'_converted.avi" -ofps 23.976 -ovfirst -of avi -no-audio -ovc libxvid -ovcopts flags=+pass1,threads=4'
			format2 = u'_converted.avi" -ofps 23.976 -ovfirst -of avi -ovc libxvid -oac libmp3lame -ovcopts flags=+pass2,threads=4,b='
			bit2 = u'k -oacopts ab=192k -srate=44100 --audio-channels='
			format = u'avi'
		if self.comboRes.currentIndex() == 0:
			resol = u' -vf scale=-1:-10'
		elif self.comboRes.currentIndex() == 1:
			resol = u' -vf scale=-10:' + self.resVal.value() + u':-10'
		elif self.comboRes.currentIndex() == 2:
			resol = u' -vf scale=' + self.resVal.value() + u':-10'
		elif self.comboRes.currentIndex() == 3:
			resol = u' -vf scale=720:400'
		elif self.comboRes.currentIndex() == 4:
			resol = u' -vf scale=720:576'
		elif self.comboRes.currentIndex() == 5:
			resol = u' -vf scale=848:480'
		elif self.comboRes.currentIndex() == 6:
			resol = u' -vf scale=640:480'
		bit1 = str(self.spin.value())
		if self.comboAudio.currentIndex() == 0: chan = u'2'
		if self.comboAudio.currentIndex() == 1: chan = u'6'
		if system() == 'Windows': mpv = folderrun + u'\\bin\\mpv.exe'
		if system() == 'Linux': mpv = u'mpv'
		global encodes, logfile
		encodes = []
		logfile = []
		for i in range(len(paths)):
			paths[i] = paths[i].encode('utf-8')
			filenames[i] = filenames[i].encode('utf-8')
			infile = paths[i]
			output = paths[i][:-4]
			if self.comboFormat.currentIndex() == 1:
				if system() == 'Windows':
					encodes.append(mpv + u' "' + GetShortPathName(unicode(infile, 'utf-8')) + u'" -o "' + folderrun + u'\\logs\\output' + str(i) + format1 + resol)
					encodes.append(mpv + u' "' + GetShortPathName(unicode(infile, 'utf-8')) + u'" -o "' + folderrun + u'\\logs\\output' + str(i) + format2 + bit1 + bit2 + chan + resol)
					logfile.append(folderrun + u'\\logs\\' + unicode(filenames[i], 'utf-8') + u'-to-' + format + u'.pass1.log')
					logfile.append(folderrun + u'\\logs\\' + unicode(filenames[i], 'utf-8') + u'-to-' + format + u'.pass2.log')
				if system() == 'Linux':
					encodes.append(mpv + u' "' + unicode(infile, 'utf-8') + u' -o "' + unicode(output, 'utf-8') + format1 + resol)
					encodes.append(mpv + u' "' + unicode(infile, 'utf-8') + u' -o "' + unicode(output, 'utf-8') + format2 + bit1 + bit2 + chan + resol)
					logfile.append(folderrun + u'/logs/' + unicode(filenames[i], 'utf-8') + u'-to-' + format + u'.pass1.log')
					logfile.append(folderrun + u'/logs/' + unicode(filenames[i], 'utf-8') + u'-to-' + format + u'.pass2.log')
			else:
				if system() == 'Windows':
					encodes.append(mpv + u' "' + GetShortPathName(unicode(infile, 'utf-8')) + u'" -o "' + folderrun + u'\\logs\\output' + str(i) + format1 + bit1 + bit2 + chan + resol)
					logfile.append(folderrun + u'\\logs\\' + unicode(filenames[i], 'utf-8') + u'-to-' + format + u'.log')
				if system() == 'Linux':
					encodes.append(mpv + u' "' + unicode(infile, 'utf-8') + u'" -o "' + unicode(output, 'utf-8') + format1 + bit1 + bit2 + chan + resol)
					logfile.append(folderrun + u'/logs/' + unicode(filenames[i], 'utf-8') + u'-to-' + format + u'.log')
		global stopConvert
		stopConvert = False
		self.stopBtn.setDisabled(False)
		self.bars = BarWork(self)
		self.bars.setProg.connect(self.onProgress)
		self.bars.start()
		self.convert = EncodeWork(self)
		self.convert.setBtn.connect(self.onBtn)
		self.convert.setLbl.connect(self.onLbl)
		self.convert.start()

	def onLock(self):
		self.openAction.setDisabled(True)
		self.openBtn.setDisabled(True)
		self.delAction.setDisabled(True)
		self.delBtn.setDisabled(True)
		self.delLogsAction.setDisabled(True)
		self.comboAudio.setDisabled(True)
		self.comboFormat.setDisabled(True)
		self.comboRes.setDisabled(True)
		self.spin.setDisabled(True)
		self.slid.setDisabled(True)
	def onUnlock(self):
		self.openAction.setDisabled(False)
		self.openBtn.setDisabled(False)
		self.delAction.setDisabled(False)
		self.delBtn.setDisabled(False)
		self.delLogsAction.setDisabled(False)
		self.comboAudio.setDisabled(False)
		self.comboFormat.setDisabled(False)
		self.comboRes.setDisabled(False)
		self.spin.setDisabled(False)
		self.slid.setDisabled(False)
	def onBtn(self, e):
		self.convert.quit()
		self.onUnlock()
		self.list.clear()
		del paths[:]
		del filenames[:]
		self.pbar2.setValue(0)
		self.pbar1.setValue(0)
		self.stopBtn.setDisabled(True)
		self.delAction.setDisabled(True)
		self.delBtn.setDisabled(True)
		if e == u'ok':
			QMessageBox.information(self, u'Info', u'Terminó la conversión.')
		elif e == u'not':
			QMessageBox.information(self, u'Info', u'Se canceló la conversión.')
	def onProgress(self, progress1, progress2):
		self.pbar2.setValue(progress1)
		self.pbar1.setValue(progress2)
	def onLbl(self, text):
		self.statusLabel.setText(text)
	def onStop(self):
		enc = EncodeWork(self)
		enc.stop()
		del paths[:]
		del filenames[:]
	def onFinish(self):
		self.stopBtn.setDisabled(True)
		self.delAction.setDisabled(True)
		self.delBtn.setDisabled(True)
		self.pbar2.setValue(100)
		self.pbar1.setValue(100)
		self.list.clear()
		del paths[:]
		del filenames[:]
		QMessageBox.information(self, u'Info', u'Terminó la conversión.')
		self.pbar2.setValue(0)
		self.pbar1.setValue(0)
	def onOpen(self):
		#self.select = self.list.selected()
		files, nul = QFileDialog.getOpenFileNames(self, u'Agregar un Archivo de Video', u'', u'Video (*.mkv; *.mp4; *.avi);;MKV (*.mkv);;MP4 (*.mp4);;AVI (*.avi)')
		for index in range(len(files)):
			path, filename = os.path.split(files[index])
			if filename[-4:] == '.mkv' or filename[-4:] == '.mp4' or filename[-4:] == '.avi':
				filenames.append(filename)
				paths.append(files[index])
				self.list.addItem(files[index])
		if self.list.count() > 0:
			self.delAction.setDisabled(False)
			self.delBtn.setDisabled(False)
			self.convertBtn.setDisabled(False)
			self.list.setCurrentItem(0)
	def onDel(self):
		self.list.takeItem(self.list.currentRow())
		del filenames[self.list.currentRow()]
		del paths[self.list.currentRow()]
		if self.list.count() == 0:
			self.delAction.setDisabled(True)
			self.delBtn.setDisabled(True)
			self.convertBtn.setDisabled(True)
	def dropEvent(self, event):
		for index in range(len(self.dropFile)):
			path, filename = os.path.split(self.dropFile[index])
			if filename[-4:] == '.mkv' or filename[-4:] == '.mp4' or filename[-4:] == '.avi':
				filenames.append(filename)
				paths.append(self.dropFile[index])
				self.list.addItem(self.dropFile[index])
		if self.list.count() > 0:
			self.delAction.setDisabled(False)
			self.delBtn.setDisabled(False)
			self.convertBtn.setDisabled(False)
	def dragEnterEvent(self, event):
		if event.mimeData().hasUrls:
			self.dropFile = []
			for index in range(len(event.mimeData().urls())):
				self.dropFile.append(event.mimeData().urls()[index].toLocalFile())
			event.acceptProposedAction()
	def onOptions(self):
		print u"Opciones\nNo hay nada aún."
	def onSelFormat(self):
		if self.comboFormat.currentIndex() == 0:
			self.crfLabel.setText(u'CRF:')
			self.slid.setRange(10, 30)
			self.slid.setValue(23)
			self.slid.setSingleStep(1)
			self.spin.setRange(10, 30)
			self.spin.setValue(23)
			self.spin.setSuffix(u'')
			self.spin.setSingleStep(1)
			self.comboAudio.setDisabled(False)
		else:
			self.crfLabel.setText(u'Bitrate:')
			self.slid.setRange(500, 10000)
			self.slid.setValue(2000)
			self.slid.setSingleStep(50)
			self.spin.setRange(500, 10000)
			self.spin.setValue(2000)
			self.spin.setSuffix(u' Kb/s')
			self.spin.setSingleStep(50)
			self.comboAudio.setCurrentIndex(0)
			self.comboAudio.setDisabled(True)
	def onSelRes(self):
		if self.comboRes.currentIndex() == 1 or self.comboRes.currentIndex() == 2:
			self.resVal.setDisabled(False)
		else:
			self.resVal.setDisabled(True)
	def onSlid(self):
		self.spin.setValue(self.slid.value())
	def onSpin(self):
		self.slid.setValue(self.spin.value())
	def onDelLogs(self):
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
		QMessageBox.information(self, u'Info', u'Los archivos de Log\nhan sido borrados.')
	def onAbout(self):
		description = u"""
<b>Acerca de AMPE """ + version + u"""</b><br/>

<img src="img/logo.png" /><br/><br/>

AMPE (Al_eXs MPV Encoder) es una Interfaz Gráfica de
Usuario(GUI) para encodear videos MKV, MP4 o AVI en MP4 o
AVI compatibles con las consolas usando como fuente para
encodear el MPV.<br/><br/>

Acepta estilos y enlaza los capitulos con
Ordered Chapters Externos(Segment Linking).<br/><br/>

Agradecimientos:<br/>
- Al equipo de desarrollo de MPV, fork del MPlayer/MPlayer2.<br/>
- ErunamoJAZZ(AnS) por su apoyo en mejorar mi codigo python.<br/>
- Batousay(BB) por su tip para las barras de progreso.<br/>
- A todos los que probaron las betas.<br/>
- A los que sugirieron cambios.<br/><br/>

<img src="img/orange.png"> Las Mandarinas Nazis dominarán el mundo.<br/><br/>
<center><a href="https://github.com/Al-eXs/AMPE">https://github.com/Al-eXs/AMPE</a><br/><br/>
© 2011-2015 <a href="https://twitter.com/al_exs_">Al_eXs</a></center>"""
		QMessageBox.about(self, u'Acerca de...', description)
	def onQtAbout(self):
		QMessageBox.aboutQt(self, u'Acerca de Qt')
	def onLicence(self):
		licence = u"""
<b>Licencia</b><br/><br/>
AMPE es un sofware libre; se puede redistribuir y/o modificar
bajo los terminos de la Licencia Publica General GNU Version 3.
AMPE es distribuido con la esperanza de ser un software util
pero SIN GARANTIA ALGUNA."""
		QMessageBox.about(self, u'Licencia', licence)
	
if __name__ == '__main__':
	app = QApplication(sys.argv)
	amp = AMPEapp()
	sys.exit(app.exec_())