from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLineEdit,
                             QPushButton, QDial, QLabel, QMessageBox)
from PyQt5 import uic
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        uic.loadUi("countdown.ui", self)
        self.setWindowTitle("Countdown Timer")

        self.dial = self.findChild(QDial, "dial")
        self.setButton = self.findChild(QPushButton, "pushButton")
        self.setButton.clicked.connect(self.set_timer)

        self.pauseButton = self.findChild(QPushButton, "pushButton_2")
        self.pauseButton.clicked.connect(self.pause_resume)

        self.resetButton = self.findChild(QPushButton, "pushButton_3")
        self.resetButton.clicked.connect(self.reset_timer)

        self.timeEdit = self.findChild(QLineEdit, "lineEdit")
        self.dial.setEnabled(False)

        self.timeLabel = self.findChild(QLabel, "label")

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)


        self.paused = False


        self.show()

    def set_timer(self):
        self.time = self.timeEdit.text()
        self.total_seconds = int(self.time.split(":")[0])*60 +int(self.time.split(":")[1])
        self.dial.setEnabled(True)
        self.dial.setMinimum(0)
        self.dial.setMaximum(self.total_seconds)
        self.dial.setValue(self.total_seconds)
        self.dial.setNotchesVisible(True)

        self.timeLabel.setText(self.time)

        self.timer.start(1000)
    def update_timer(self):
        time = self.dial.value()

        if time > 0:
            self.dial.setValue(time - 1)

            m, s = divmod(time - 1, 60)
            self.label.setText(f"{m:02}:{s:02}")

        else:
            self.timer.stop()
            self.label.setText("00:00")
            QMessageBox.information(self, "Time's up!", "The timer has finished!⏰")

    def pause_resume(self):
        if not self.paused:
            self.timer.stop()
            self.pauseButton.setText("Resume")
            self.paused = True
        else:
            self.timer.start(1000)
            self.pauseButton.setText("Pause")
            self.paused = False

    def reset_timer(self):

        self.timer.stop()
        self.dial.setValue(self.total_seconds)
        self.timeLabel.setText(self.time)


app = QApplication(sys.argv)
window = MainWindow()
app.exec_()