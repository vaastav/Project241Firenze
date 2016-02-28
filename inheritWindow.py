import sys
from PyQt4 import QtGui, QtCore
import lyricslib

class Window(QtGui.QMainWindow):

	
	def __init__(self):
		super(Window,self).__init__()
		self.setGeometry(50,50,900,500)
		self.setWindowTitle("Project Firenze")
		self.setWindowIcon(QtGui.QIcon("Images/logo.png"))

		palette = QtGui.QPalette()
		palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(QtGui.QPixmap("Images/background.png")))
		self.setPalette(palette)
		self.home()


	def home(self):
		# Your Song Labels
		firstFile = QtGui.QPushButton("Attach Your Song", self)
		firstFile.clicked.connect(self.openFirstFile)
		firstFile.setStyleSheet("background: #5fa449; border-style: outset; border-radius: 6px; border-width: 2px; border-color: black; padding: 6px")
		firstFile.resize(150,50)
		firstFile.move(100,100)

		self.firstFileLabel = QtGui.QLabel("Your Song", self)
		self.firstFileLabel.setGeometry(100, 50, 500, 50)

		# Other Song Labels
		secondFile = QtGui.QPushButton("Attach Other Song", self)
		secondFile.clicked.connect(self.openSecondFile)
		secondFile.setStyleSheet("background: #5fa449; border-style: outset; border-radius: 6px; border-width: 2px; border-color: black; padding: 6px")
		secondFile.resize(150,50)
		secondFile.move(100,300)

		self.secondFileLabel = QtGui.QLabel("Other Song", self)
		self.secondFileLabel.setGeometry(100, 250, 500, 50)

		# Compare songs button
		compareSongs = QtGui.QPushButton("Compare Songs", self)
		compareSongs.clicked.connect(self.download)
		compareSongs.setStyleSheet("background: #5fa449; border-style: outset; border-radius: 6px; border-width: 2px; border-color: black; padding: 6px")
		compareSongs.resize(150,50)
		compareSongs.move(275,200)

		# Progress bar
		self.progress = QtGui.QProgressBar(self)
		self.progress.setGeometry(245, 175, 250, 20)
		self.progress.hide()

		# Similarity label
		self.lyricsScore = QtGui.QLabel("", self)
		scoreFont = QtGui.QFont("Courier", 15, QtGui.QFont.Bold)
		self.lyricsScore.setFont(scoreFont)
		self.lyricsScore.setGeometry(550, 120, 200, 200)
		self.lyricsScore.setWordWrap(True)
		self.lyricsScore.setAlignment(QtCore.Qt.AlignCenter)


		self.show()

	def openFirstFile(self):
		self.firstFileName = QtGui.QFileDialog.getOpenFileName(self, 'Open File', "", "Text Files (*.txt)")

		self.firstFileLabel.setText(self.firstFileName)

	def openSecondFile(self):
		self.secondFileName = QtGui.QFileDialog.getOpenFileName(self, 'Open File', "", "Text Files (*.txt)")
		self.secondFileLabel.setText(self.secondFileName)


	def download(self):
		self.progress.show()
		lyricsCompareScore = str(lyricslib.compare(self.firstFileName, self.secondFileName))

		self.completed = 0
		while self.completed < 100:
			self.completed+= 0.0001
			self.progress.setValue(self.completed)
		self.progress.hide()
		trimmedLyricScore = lyricsCompareScore[:5] + "%"
		self.lyricsScore.setText("These song lyrics are %s similar" %(trimmedLyricScore))

def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()