"""
  Demo for EventLoop.py - interactive GUI development

  This assumes you have PyQt4 installed on your system.

  Make sure that you have enabled the Event Loop under "Shell"
  and "Use Qt4".

  The "GUI: ON/OFF" button in the status bar is clickable.

"""

## import once
import sys
from PyQt4 import Qt
app = Qt.QApplication(sys.argv)   # running this subcode twice may crash 

##
def clicked():
    print('Click received.')

w = Qt.QWidget()
w.resize(300, 200)
w.setWindowTitle('IdleX GUI Event Loop Demo')

b = Qt.QPushButton('Click Me', w)
b.clicked.connect(clicked)
w.show()


#app.exec_()
