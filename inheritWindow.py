import sys
from PyQt4 import QtGui, QtCore
import lyricslib

class Window(QtGui.QMainWindow):

	
	def __init__(self):
		super(Window,self).__init__()
		self.setGeometry(50,50,1500,450)
		self.setWindowTitle("Project Firenze")
		self.setMinimumSize(1500, 450)
		self.setMaximumSize(1500, 450)

		self.setWindowIcon(QtGui.QIcon("Images/logo.png"))
		palette = QtGui.QPalette()
		palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(QtGui.QPixmap("Images/background.png")))
		self.setPalette(palette)

		self.home()


	def home(self):
		self.setFonts()
		self.setupInputButtons()
		self.setupCompareButtons()
		self.setupProgressBars()
		self.setupSimilarityLabelS()
		self.show()

	def setFonts(self):
		self.scoreFont = QtGui.QFont("Arial", 15, QtGui.QFont.Bold)
		self.labelFont = QtGui.QFont("Arial", 9)

	# SETUP HELPERS

	def setupInputButtons(self):
		# Your Melody Labels
		firstMelodyFile = QtGui.QPushButton("Attach Your Melody", self)
		firstMelodyFile.clicked.connect(self.openFirstMelodyFile)
		firstMelodyFile.setStyleSheet("background: #5fa449; border-style: outset; border-radius: 5px; border-width: 2px; border-color: black; padding: 6px")
		firstMelodyFile.resize(150,50)
		firstMelodyFile.setFont(self.labelFont)
		firstMelodyFile.move(800,100)

		self.firstMelodyLabel = QtGui.QLabel("", self)
		self.firstMelodyLabel.setStyleSheet("color: white")
		self.firstMelodyLabel.setFont(self.labelFont)
		self.firstMelodyLabel.setGeometry(800, 50, 500, 50)

		# Other Melody Labels
		secondMelodyFile = QtGui.QPushButton("Attach Other Melody", self)
		secondMelodyFile.clicked.connect(self.openSecondMelodyFile)
		secondMelodyFile.setStyleSheet("background: #5fa449; border-style: outset; border-radius: 5px; border-width: 2px; border-color: black; padding: 6px")
		secondMelodyFile.resize(150,50)
		secondMelodyFile.setFont(self.labelFont)
		secondMelodyFile.move(800,300)

		self.secondMelodyLabel = QtGui.QLabel("", self)
		self.secondMelodyLabel.setStyleSheet("color: white")
		self.secondMelodyLabel.setFont(self.labelFont)
		self.secondMelodyLabel.setGeometry(800, 250, 500, 50)

		# Your Lyrics Labels
		firstFile = QtGui.QPushButton("Attach Your Lyrics", self)
		firstFile.clicked.connect(self.openFirstLyricFile)
		firstFile.setFont(self.labelFont)
		firstFile.setStyleSheet("background: #5fa449; border-style: outset; border-radius: 5px; border-width: 2px; border-color: black; padding: 6px")
		firstFile.resize(150,50)
		firstFile.move(100,100)

		self.firstLyricsLabel = QtGui.QLabel(self)
		self.firstLyricsLabel.setFont(self.labelFont)
		self.firstLyricsLabel.setStyleSheet("color: white")
		self.firstLyricsLabel.setGeometry(100, 50, 500, 50)

		# Other Lyrics Labels
		secondFile = QtGui.QPushButton("Attach Other Lyrics", self)
		secondFile.clicked.connect(self.openSecondLyricFile)
		secondFile.setFont(self.labelFont)
		secondFile.setStyleSheet("background: #5fa449; border-style: outset; border-radius: 5px; border-width: 2px; border-color: black; padding: 6px")
		secondFile.resize(150,50)
		secondFile.move(100,300)

		self.secondLyricsLabel = QtGui.QLabel(self)
		self.secondLyricsLabel.setStyleSheet("color: white")
		self.secondLyricsLabel.setGeometry(100, 250, 500, 50)

	def setupCompareButtons(self):
		# Compare Melody button
		compareMelodies = QtGui.QPushButton("Compare Melody", self)
		compareMelodies.clicked.connect(self.melodyCompare)
		compareMelodies.setStyleSheet("background: #5fa449; border-style: outset; border-radius: 5px; border-width: 2px; border-color: black; padding: 6px")
		compareMelodies.resize(150,50)
		compareMelodies.setFont(self.labelFont)
		compareMelodies.move(975,200)

		# Compare Lyrics button
		compareLyrics = QtGui.QPushButton("Compare Lyrics", self)
		compareLyrics.clicked.connect(self.lyricCompare)
		compareLyrics.setFont(self.labelFont)
		compareLyrics.setStyleSheet("background: #5fa449; border-style: outset; border-radius: 5px; border-width: 2px; border-color: black; padding: 6px")
		compareLyrics.resize(150,50)
		compareLyrics.move(275,200)

	def setupProgressBars(self):
		# Melody Progress bar
		self.melodyProgress = QtGui.QProgressBar(self)
		self.melodyProgress.setGeometry(945, 175, 250, 20)
		self.melodyProgress.hide()
		# Lyrics Progress bar
		self.progress = QtGui.QProgressBar(self)
		self.progress.setGeometry(245, 175, 250, 20)
		self.progress.hide()

	def setupSimilarityLabelS(self):
		# Melody Similarity label
		self.melodyScore = QtGui.QLabel("", self)
		self.melodyScore.setStyleSheet("color: white")
		self.melodyScore.setFont(self.scoreFont)
		self.melodyScore.setGeometry(1250, 120, 200, 200)
		self.melodyScore.setFont(self.scoreFont)
		self.melodyScore.setWordWrap(True)
		self.melodyScore.setAlignment(QtCore.Qt.AlignCenter)

		# Lyrics Similarity label
		self.lyricsScore = QtGui.QLabel("", self)
		self.lyricsScore.setStyleSheet("color: white")
		self.lyricsScore.setFont(self.scoreFont)
		self.lyricsScore.setGeometry(550, 120, 200, 200)
		self.lyricsScore.setWordWrap(True)
		self.lyricsScore.setAlignment(QtCore.Qt.AlignCenter)


	# BUTTON ACTIONS

	def openFirstLyricFile(self):
		self.firstLyricName = QtGui.QFileDialog.getOpenFileName(self, 'Open File', "", "Text Files (*.txt)")
		self.firstLyricsLabel.setText(self.firstLyricName)

	def openSecondLyricFile(self):
		self.secondLyricName = QtGui.QFileDialog.getOpenFileName(self, 'Open File', "", "Text Files (*.txt)")
		self.secondLyricsLabel.setText(self.secondLyricName)

	def openFirstMelodyFile(self):
		self.firstMelodyName = QtGui.QFileDialog.getOpenFileName(self, 'Open File', "", "Text Files (*.txt)")
		self.firstMelodyLabel.setText(self.firstMelodyName)

	def openSecondMelodyFile(self):
		self.secondMelodyName = QtGui.QFileDialog.getOpenFileName(self, 'Open File', "", "Text Files (*.txt)")
		self.secondMelodyLabel.setText(self.secondMelodyName)


	def lyricCompare(self):
		if self.firstLyricsLabel.text() != "" and self.secondLyricsLabel.text() != "":
			self.progress.show()
			lyricsCompareScore = str(lyricslib.compare(self.firstLyricName, self.secondLyricName))

			self.completed = 0
			while self.completed < 100:
				self.completed+= 0.0005
				self.progress.setValue(self.completed)
			self.progress.hide()
			trimmedLyricScore = lyricsCompareScore[:5] + "%"
			self.lyricsScore.setText("These song lyrics are %s similar" %(trimmedLyricScore))
		else:
			self.lyricsScore.setText("Please select two text files")

	def melodyCompare(self):
		if self.firstMelodyLabel.text() != "" and self.secondMelodyLabel.text() != "":
			self.melodyProgress.show()
			melodyCompareScore = str(lyricslib.compare(self.firstMelodyName, self.secondMelodyName))
			self.completed = 0
			while self.completed < 100:
				self.completed+= 0.0005
				self.melodyProgress.setValue(self.completed)
			self.melodyProgress.hide()
			trimmedMelodyScore = melodyCompareScore[:5] + "%"
			self.melodyScore.setText("These song melodies are %s similar" %(trimmedMelodyScore))
		else:
			self.melodyScore.setText("Please select two MIDI files")



def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()