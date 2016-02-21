import sys
import os
from PyQt4 import QtGui


__author__ = 'HashmalS'



class Window(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.initUI()

    def initUI(self):
        text = QtGui.QTextEdit(self)
        self.text = text
        self.setWindowIcon(QtGui.QIcon('C:\\Users\\1\\Pictures\\Notepad-icon.png'))

        self.setCentralWidget(self.text)

        close_action = QtGui.QAction('Close', self)
        close_action.setShortcut('Ctrl+Q')
        close_action.setStatusTip('Close Notepad')
        close_action.triggered.connect(self.close)

        new_action = QtGui.QAction('New', self)
        new_action.setShortcut('Ctrl+N')
        new_action.setStatusTip('Create new file')
        new_action.triggered.connect(self.newFile)

        save_action = QtGui.QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.setStatusTip('Save current file')
        save_action.triggered.connect(self.saveFile)

        open_action = QtGui.QAction('Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.setStatusTip('Open a file')
        open_action.triggered.connect(self.openFile)

        undo_action = QtGui.QAction('Undo', self)
        undo_action.setShortcut('Ctrl+Z')
        undo_action.setStatusTip('Undo previous event')
        undo_action.triggered.connect(text.undo)

        menubar = self.menuBar()

        filemenu = menubar.addMenu('&File')
        filemenu.addAction(new_action)
        filemenu.addAction(save_action)
        filemenu.addAction(open_action)
        filemenu.addSeparator()
        filemenu.addAction(close_action)

        edit_menu = menubar.addMenu('&Edit')
        edit_menu.addAction(undo_action)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Notepad')
        self.show()

    def newFile(self):
        self.text.clear()

    def saveFile(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save file', os.path.expanduser('~'), '.txt')
        file = open(filename.txt, 'w')
        filedata = self.text.toPlainText()
        file.write(filedata)
        file.close()

    def openFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', os.path.expanduser('~'))
        file = open(filename, 'r')
        filedata = file.read()
        self.text.setText(filedata)
        file.close()

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Quit', "Are you sure to quit?",
                                           QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QtGui.QApplication(sys.argv)
    notepad = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
