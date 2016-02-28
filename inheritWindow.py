import sys
from PyQt4 import QtGui, QtCore
import lyricslib

class Window(QtGui.QMainWindow):

	
	def __init__(self):
		super(Window,self).__init__()
		# Constants
		windowWidth = 1500
		windowHeight = 450
		self.height = 50
		self.btnWidth = 150
		self.btnFormat = "background:  qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0 #88c9aa, stop:1 #7eb299); border-style: outset; border-radius: 5px; border-width: 2px; border-color: black; padding: 6px"

		self.setGeometry(50,50,windowWidth,windowHeight)
		self.setWindowTitle("Project Firenze")
		self.setMinimumSize(windowWidth, windowHeight)
		self.setMaximumSize(windowWidth, windowHeight)

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
		# Constants
		labelWidth = 500
		xPosLeft = 100
		yPosBottom = 300
		xPosRight = 800
		yPosTop = 100
		yPosTopLabel = 50
		yPosBottomLabel = 250

		# Your Melody Button
		firstMelodyFile = QtGui.QPushButton("Attach Your Melody", self)
		firstMelodyFile.clicked.connect(self.openFirstMelodyFile)
		firstMelodyFile.setStyleSheet(self.btnFormat)
		firstMelodyFile.setGeometry(xPosLeft, yPosTop, self.btnWidth, self.height)
		firstMelodyFile.setFont(self.labelFont)

		# Your Melody Label
		self.firstMelodyLabel = QtGui.QLabel("", self)
		self.firstMelodyLabel.setStyleSheet("color: white")
		self.firstMelodyLabel.setGeometry(xPosLeft, yPosTopLabel, labelWidth, self.height)
		self.firstMelodyLabel.setFont(self.labelFont)

		# Other Melody Button
		secondMelodyFile = QtGui.QPushButton("Attach Other Melody", self)
		secondMelodyFile.clicked.connect(self.openSecondMelodyFile)
		secondMelodyFile.setStyleSheet(self.btnFormat)
		secondMelodyFile.setGeometry(xPosLeft, yPosBottom, self.btnWidth, self.height)
		secondMelodyFile.setFont(self.labelFont)

		# Other Melody Label
		self.secondMelodyLabel = QtGui.QLabel("", self)
		self.secondMelodyLabel.setStyleSheet("color: white")
		self.secondMelodyLabel.setGeometry(xPosLeft, yPosBottomLabel, labelWidth, self.height)
		self.secondMelodyLabel.setFont(self.labelFont)

		# Your Lyrics Button
		firstFile = QtGui.QPushButton("Attach Your Lyrics", self)
		firstFile.clicked.connect(self.openFirstLyricFile)
		firstFile.setStyleSheet(self.btnFormat)
		firstFile.setGeometry(xPosRight, yPosTop, self.btnWidth, self.height)
		firstFile.setFont(self.labelFont)

		# Your Lyrics Label
		self.firstLyricsLabel = QtGui.QLabel(self)
		self.firstLyricsLabel.setStyleSheet("color: white")
		self.firstLyricsLabel.setGeometry(xPosRight, yPosTopLabel, labelWidth, self.height)
		self.firstLyricsLabel.setFont(self.labelFont)

		# Other Lyrics Button
		secondFile = QtGui.QPushButton("Attach Other Lyrics", self)
		secondFile.clicked.connect(self.openSecondLyricFile)
		secondFile.setStyleSheet(self.btnFormat)
		secondFile.setGeometry(xPosRight, yPosBottom, self.btnWidth, self.height)
		secondFile.setFont(self.labelFont)

		# Other Lyrics Label
		self.secondLyricsLabel = QtGui.QLabel(self)
		self.secondLyricsLabel.setStyleSheet("color: white")
		self.secondLyricsLabel.setGeometry(xPosRight, yPosBottomLabel, labelWidth, self.height)
		self.secondLyricsLabel.setFont(self.labelFont)

	def setupCompareButtons(self):
		# Constants
		yPos = 200
		xPosLeft = 275
		xPosRight = 975

		# Compare Melody button
		compareMelodies = QtGui.QPushButton("Compare Melody", self)
		compareMelodies.clicked.connect(self.melodyCompare)
		compareMelodies.setStyleSheet(self.btnFormat)
		compareMelodies.setGeometry(xPosLeft, yPos, self.btnWidth, self.height)
		compareMelodies.setFont(self.labelFont)

		# Compare Lyrics button
		compareLyrics = QtGui.QPushButton("Compare Lyrics", self)
		compareLyrics.clicked.connect(self.lyricCompare)
		compareLyrics.setStyleSheet(self.btnFormat)
		compareLyrics.setGeometry(xPosRight, yPos, self.btnWidth, self.height)
		compareLyrics.setFont(self.labelFont)

	def setupProgressBars(self):
		# Constants
		yPos = 175
		height = 250
		width = 20
		xPosLeft = 245
		xPosRight = 945

		# Melody Progress bar
		self.melodyProgress = QtGui.QProgressBar(self)
		self.melodyProgress.setGeometry(xPosLeft, yPos, height, width)
		self.melodyProgress.hide()

		# Lyrics Progress bar
		self.progress = QtGui.QProgressBar(self)
		self.progress.setGeometry(xPosRight, yPos, height, width)
		self.progress.hide()

	def setupSimilarityLabelS(self):
		# Constants
		yPos = 120
		height = 200
		width = 200
		xPosLeft = 550
		xPosRight = 1250


		# Melody Similarity label
		self.melodyScore = QtGui.QLabel("", self)
		self.melodyScore.setStyleSheet("color: white")
		self.melodyScore.setFont(self.scoreFont)
		self.melodyScore.setGeometry(xPosLeft, yPos, height, width)
		self.melodyScore.setFont(self.scoreFont)
		self.melodyScore.setWordWrap(True)
		self.melodyScore.setAlignment(QtCore.Qt.AlignCenter)

		# Lyrics Similarity label
		self.lyricsScore = QtGui.QLabel("", self)
		self.lyricsScore.setStyleSheet("color: white")
		self.lyricsScore.setFont(self.scoreFont)
		self.lyricsScore.setGeometry(xPosRight, yPos, height, width)
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
			self.lyricsScore.setText("Your song lyrics are %s similar to the other song's lyrics" %(trimmedLyricScore))
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
			self.melodyScore.setText("Your song melody is %s similar to the other song's melody" %(trimmedMelodyScore))
		else:
			self.melodyScore.setText("Please select two MIDI files")



def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()