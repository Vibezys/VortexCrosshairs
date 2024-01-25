import time
import colorama
import uuid
import datetime
import random
import sys
import os
import pygetwindow as gw
from PyQt5 import QtCore, QtGui, QtWidgets
from colorama import Fore, Back, Style
from datetime import datetime, timedelta
from time import sleep

# Function to edit configuration
def edit_config():
    global R, G, B, ctype

    # Get new values from the user or any other source
    print()
    new_R = int(input(Fore.MAGENTA + "Enter new R value: "))
    new_G = int(input(Fore.MAGENTA + "Enter new G value: "))
    new_B = int(input("Enter new B value: "))
    new_ctype = int(input(Fore.MAGENTA + "Enter new Crosshair Type (1 or 2): "))

    # Update the global variables
    R, G, B, ctype = new_R, new_G, new_B, new_ctype

    # Update the configuration file
    with open("config.ini", "w") as f:
        f.write("[RGB]\n[R]\n{}\n[G]\n{}\n[B]\n{}\n\n[Other]\n[Crosshair Type]\n{}\n".format(R, G, B, ctype))

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
    game_window_title = "Your Game Window Title"  # Replace with the actual title of your game window
    game_window = gw.getWindowsWithTitle(game_window_title)

    if game_window:
        game_window = game_window[0]
        game_window.activate()  # Bring the game window to the front

        # Position the crosshair over the game window
        widget.move(game_window.left + (game_window.width - widget.width()) // 2,
                    game_window.top + (game_window.height - widget.height()) // 2)

    sys.exit(app.exec_())
if __name__ == '__main__':
    display_crosshair()