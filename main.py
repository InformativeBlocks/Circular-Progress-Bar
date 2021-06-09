
# IMPORTS
###########################################################
from PyQt5 import QtWidgets, QtCore, QtGui
from splashScreenWindow import Ui_SplashScreen
import sys

# WINDOW THAT OPEN AFTER SPLASH SCREEN
from win import Ui_MainWindow

# GLOBALS
COUNTER = 0


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class SplashScreen(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # FRAMELESS WINDOW
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SHADOW
        ########################################################################
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 150))
        self.ui.progressBar.setGraphicsEffect(self.shadow)

        # START PROGRESS BAR
        ########################################################################
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(15)

        # SHOW WINDOW
        self.show()

    def progress(self):
        global COUNTER
        value = COUNTER

        # WHEN VALUE REACHED 100 THAN stop timer and close splash Screen
        if COUNTER > 100:
            # STOP TIMER
            self.timer.stop()

            # Show MainWindow
            self.main = MainWindow()
            self.main.show()

            # Close Splash Screen
            self.close()
        else:
            self.progressBarV(value)
            COUNTER += 0.4


    def progressBarV(self, value):
        stylesheet = """
        QFrame {
            border-radius: 125px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_V1} rgba(0, 0, 0, 0), stop:{STOP_V2} rgba(229, 229, 220, 255));
        }
        """

        # Calculate progress value
        progress = (100 - value) / 100.0

        # Get Stops Value
        stop_v1 = str(progress - 0.001)
        stop_v2 = str(progress)

        newStyleSheet = stylesheet.replace("{STOP_V1}", stop_v1).replace("{STOP_V2}", stop_v2)

        # APPLY NEW STYLESHEET
        self.ui.progressBar.setStyleSheet(newStyleSheet)
        self.ui.label.setText(str(int(value)) + " %")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
