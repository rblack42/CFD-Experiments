import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget


class MainWindow(object):

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.setWindowTitle("CFD Explorer")
        self.window.setGeometry(100, 100, 280, 80)
        self.window.move(60,15)

        helloMsg = QLabel('<h1>Hello World!</h1>', parent=self.window)
        helloMsg.move(60, 15)

    def show(self):
        self.window.show()

    def run(self):
        sys.exit(self.app.exec_())

def main():
    mw = MainWindow()
    mw.show()
    mw.run()



if __name__ == '__main__':
    main()
