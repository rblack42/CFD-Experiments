import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.Qt import QKeySequence
from PyQt5.Qt import Qt
from myapp import Window
from PyQt5.QtTest import QTest


########################################################################
class Test(unittest.TestCase):

    #----------------------------------------------------------------------
    def setUp(self):
        self.app = QApplication([])
        self.ui = Window()
        self.menu = self.ui.menuBar()
        QTest.qWaitForWindowExposed(self.ui)

    #----------------------------------------------------------------------
    def test_update_label_from_menu(self):
        self.assertEqual(self.ui.label.text(), 'Empty')
        self.menu.actions()[0].menu().actions()[0].trigger()
        self.assertEqual(self.ui.label.text(), 'Updated label')

    #----------------------------------------------------------------------
    def test_update_label_from_shortcut(self):
        self.assertEqual(self.ui.label.text(), 'Empty')
        QTest.keyClicks(self.ui, 'U', Qt.ControlModifier)
        print(self.ui.label.text())

        QTest.keyPress(self.ui, 'U', Qt.ControlModifier)
        print(self.ui.label.text())

        QTest.keyPress(self.ui, Qt.Key_U, Qt.ControlModifier)
        print(self.ui.label.text())

        self.assertEqual(self.ui.label.text(), 'Updated label')
        return

    #----------------------------------------------------------------------
    def tearDown(self):
        pass
