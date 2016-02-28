import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

	
	def __init__(self):
		super(Window,self).__init__()
		self.setGeometry(50,50,700,300)
		self.setWindowTitle("Project Firenze")
		self.setWindowIcon(QtGui.QIcon("Images/archerlogo.png"))
		self.home()


	def home(self):
		firstFile = QtGui.QPushButton("Attach First Song", self)
		firstFile.clicked.connect(self.openFile)
		firstFile.resize(150,50)
		firstFile.move(100,100)

		secondFile = QtGui.QPushButton("Attach Second Song", self)
		secondFile.clicked.connect(self.openFile)
		secondFile.resize(150,50)
		secondFile.move(450,100)

		compareSongs = QtGui.QPushButton("Compare Songs", self)
		compareSongs.clicked.connect(self.download)
		compareSongs.resize(150,50)
		compareSongs.move(275,200)

		self.progress = QtGui.QProgressBar(self)
		self.progress.setGeometry(245, 175, 250, 20)


		

		# lbl = QtGui.QLabel('No file selected')
		# self.addWidget(self.lbl)

		self.show()

	def openFile(self):
		# self.fileDialog = QtGui.QFileDialog(self)
		# self.fileDialog.show()

		name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
		print(name)
		file = open(name, 'r')

	def download(self):
		self.completed = 0
		while self.completed < 100:
			self.completed+= 0.001
			self.progress.setValue(self.completed)

    #     # Create a label which displays the path to our chosen file
    #     self.lbl = QtGui.QLabel('No file selected')
    #     self.vbox.addWidget(self.lbl)

    #     # Create a push button labelled 'choose' and add it to our layout
    #     btn = QtGui.QPushButton('Choose file', self)
    #     self.vbox.addWidget(btn)
        
    #     # Connect the clicked signal to the get_fname handler
    #     self.connect(btn, QtCore.SIGNAL('clicked()'), self.get_fname)

    # def get_fname(self):
    #     """
    #     Handler called when 'choose file' is clicked
    #     """
    #     # When you call getOpenFileName, a file picker dialog is created
    #     # and if the user selects a file, it's path is returned, and if not
    #     # (ie, the user cancels the operation) None is returned
    #     fname = QtGui.QFileDialog.getOpenFileName(self, 'Select file')
    #     if fname:
    #         self.lbl.setText(fname)
    #     else:
    #         self.lbl.setText('No file selected')



def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()