"""
https://stackoverflow.com/questions/34419926/how-to-make-qtgui-window-process-events-whenever-it-is-brought-forward-on-the-sc
"""
import sys
import time
import threading

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QProgressBar, QWidget


def singleRun(pb, timer):
    pb.setValue(pb.value() + 1)
    if pb.value() >= pb.maximum():
        timer.stop()


def loopRun(pb, delay):
    timer = QTimer(window)
    timer.start(delay)
    timer.timeout.connect(lambda: singleRun(pb, timer))


def printer(num):
    for i in range(num):
        print(i)
        time.sleep(0.1)


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Window")
window.setFixedWidth(1000)
window.setFixedHeight(600)
window.move(100, 50)

window.setStyleSheet("background-color: rgb(208, 208, 208);")


ProgressBar1 = QProgressBar(window)
ProgressBar1.setGeometry(400, 50, 200, 24)
ProgressBar1.setValue(0)
ProgressBar1.setStyleSheet(
    "QProgressBar {"
    "background-color: rgb(0, 33, 68);"
    "font: 11pt 'Trebuchet MS';"
    "font-weight: bold;"
    "color: rgb(255, 75, 20);"
    "text-align: center;"
    "border: 1px solid;"
    "border-color: rgb(195, 195, 195);"
    "}"
    "\n"
    "QProgressBar:chunk {"
    "background-color: rgb(245, 219, 15);"
    "}"
)


loopRun(ProgressBar1, 75)
threading.Thread(target=printer, args=(65,), daemon=True).start()


window.show()
sys.exit(app.exec_())