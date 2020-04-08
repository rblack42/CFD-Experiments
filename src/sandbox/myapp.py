import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QLabel


########################################################################
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)

        action1 = QAction("&Action1", self)
        action1.setShortcut("Ctrl+U")
        action1.triggered.connect(self.update_label)

        self.label = QLabel('Empty', self)
        self.setCentralWidget(self.label)

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu("&File")
        file_menu.addAction(action1)

        self.show()

    def update_label(self):
        print("updating label")
        self.label.setText('Updated label')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
