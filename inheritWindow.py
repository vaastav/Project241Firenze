import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

	
	def __init__(self):
		super(Window,self).__init__()
		self.setGeometry(50,50,1300,500)
		self.setWindowTitle("Project Firenze")
		self.setWindowIcon(QtGui.QIcon("Images/archerlogo.png"))
		self.home()


	def home(self):
		firstFile = QtGui.QPushButton("Attach First Song", self)
		firstFile.clicked.connect(self.openFirstFile)
		firstFile.resize(150,50)
		firstFile.move(100,100)

		self.firstFileLabel = QtGui.QLabel("First Song", self)
		self.firstFileLabel.setGeometry(100, 50, 500, 50)

		secondFile = QtGui.QPushButton("Attach Second Song", self)
		secondFile.clicked.connect(self.openSecondFile)
		secondFile.resize(150,50)
		secondFile.move(100,300)

		self.secondFileLabel = QtGui.QLabel("Second Song", self)
		self.secondFileLabel.setGeometry(100, 250, 500, 50)

		compareSongs = QtGui.QPushButton("Compare Songs", self)
		compareSongs.clicked.connect(self.download)
		compareSongs.resize(150,50)
		compareSongs.move(275,200)

		self.progress = QtGui.QProgressBar(self)
		self.progress.setGeometry(245, 175, 250, 20)



		self.show()

	def openFirstFile(self):
		# self.fileDialog = QtGui.QFileDialog(self)
		# self.fileDialog.show()

		name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
		print(name)
		self.firstFileLabel.setText(name)

		file = open(name, 'r')

	def openSecondFile(self):

		name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
		print(name)
		self.secondFileLabel.setText(name)

		file = open(name, 'r')

	def download(self):
		self.completed = 0
		while self.completed < 100:
			self.completed+= 0.001
			self.progress.setValue(self.completed)



def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()