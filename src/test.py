from PyQt5.QtWidgets import QApplication, \
    QWidget, \
    QPushButton, \
    QVBoxLayout, \
    QMessageBox

def on_quit_clicked():
    alert = QMessageBox()
    alert.setText("You want to quit?")
    alert.exec()

def isVisible(widget):
    if not widget.visibleRegion().isEmpty():
        return true
    return false

def testClick(button):
    button.click()

def checkAlert(msg):
    if isVisible(msg):
        print("Alert is visible")
    else:
        print("Alert is not visible")

def testButton(msg,button):
    check(msg)
    testClick(button)
    check(msg)

def main():
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    button = QPushButton("Quit")
    button.clicked.connect(on_quit_clicked)
    layout.addWidget(button)
    window.setLayout(layout)
    window.show()

    app.exec_()

if __name__ == '__main__':
    main()
