import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

	
	def __init__(self):
		super(Window,self).__init__()
		self.setGeometry(50,50,700,400)
		self.setWindowTitle("Project Firenze")
		self.setWindowIcon(QtGui.QIcon("Images/archerlogo.png"))
		self.home()


	def home(self):
		firstFile = QtGui.QPushButton("Attach First Song", self)
		firstFile.clicked.connect(QtCore.QCoreApplication.instance().quit)
		firstFile.resize(150,50)
		firstFile.move(100,100)

		secondFile = QtGui.QPushButton("Attach Second Song", self)
		secondFile.clicked.connect(QtCore.QCoreApplication.instance().quit)
		secondFile.resize(150,50)
		secondFile.move(450,100)

		self.show()




def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()