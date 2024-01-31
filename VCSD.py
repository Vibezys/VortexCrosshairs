import sys
import os
import subprocess
import pygetwindow as gw
from PyQt5 import QtCore, QtGui, QtWidgets
from colorama import Fore

if os.path.exists("config.ini") == False:
    f = open("config.ini", "w")
    f.write("[RGB]\n")
    f.write("[R]\n")
    f.write("255\n")
    f.write("[G]\n")
    f.write("0\n")
    f.write("[B]\n")
    f.write("0\n")
    f.write("\n[Other]\n")
    f.write("[Crosshair Type]\n")
    f.write("1\n")
    f.close()

# Config
f = open("config.ini", "r")
n = f.readline()
n = f.readline()
R = f.readline()
n = f.readline()
G = f.readline()
n = f.readline()
B = f.readline()
n = f.readline()
n = f.readline()
n = f.readline()
ctype = f.readline()

R = int(R)
G = int(G)
B = int(B)
transparency = 0.0
ctype = int(ctype)

def display_crosshair():
    class Crosshair(QtWidgets.QWidget):
        def __init__(self, parent=None, windowSize=24, penWidth=2):
            QtWidgets.QWidget.__init__(self, parent)
            self.ws = windowSize
            self.resize(windowSize + 1, windowSize + 1)
            self.setWindowFlags(
                QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Tool)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

            # Pick your crosshair color
            self.pen = QtGui.QPen(QtGui.QColor(R, G, B, 150))  # 150 is the alpha value for transparency
            self.pen.setWidth(penWidth)

            self.move(
                QtWidgets.QApplication.desktop().screen().rect().center() - self.rect().center() + QtCore.QPoint(1, 1))

            self.vcsd_process = None  # Variable to store the VCSD.py process

        # these are not needed, the process will be started and stopped from the main script
        # def run_start_process(self):
        #     if self.vcsd_process is None or self.vcsd_process.poll() is not None:
        #         # Start VCSD.py only if it's not already running or has terminated
        #         self.vcsd_process = subprocess.Popen(["python", "VCSD.py"])

        # def stop_vcsd_process(self):
        #     if self.vcsd_process is not None and self.vcsd_process.poll() is None:
        #         #Terminate VCSD.py if it's currently running
        #         self.vcsd_process.terminate()
        #         self.vcsd_process = None

        def paintEvent(self, event):
            ws = self.ws
            res = int(ws / 2)
            red = int(ws / 10)
            painter = QtGui.QPainter(self)

            # Update pen color
            self.pen.setColor(QtGui.QColor(R, G, B, 150))  # 150 is the alpha value for transparency
            painter.setPen(self.pen)

            if ctype == 1:
                # Draw the crosshair
                painter.drawLine(res, 0, res, res - red)
                painter.drawLine(res, res + red + 1, res, ws)
                painter.drawLine(0, res, res - red, res)
                painter.drawLine(res + red, res, int(ws - 0.5), res)
            elif ctype == 2:
                # Draw a filled dot in the middle of the screen
                dot_size = 5
                painter.setBrush(QtGui.QBrush(QtGui.QColor(R, G, B, 150)))  # 150 is the alpha value for transparency
                painter.drawEllipse(int(res - dot_size / 2), int(res - dot_size / 2), int(dot_size), int(dot_size))

    app = QtWidgets.QApplication(sys.argv)
    widget = Crosshair(windowSize=16, penWidth=2)
    widget.show()

    # Get the active game window
    screen_rect = QtWidgets.QApplication.desktop().screen().rect()
    widget.move(screen_rect.center() - widget.rect().center())

    sys.exit(app.exec_())
if __name__ == '__main__':
    display_crosshair()