# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MargaritaMixer.ui'
#
# Created: Sun Jul 31 13:22:56 2011
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui

class Ui_MargaritaMixer(object):
    def setupUi(self, MargaritaMixer):
        MargaritaMixer.setObjectName("MargaritaMixer")
        MargaritaMixer.resize(536, 368)
        self.gridLayout = QtGui.QGridLayout(MargaritaMixer)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(MargaritaMixer)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(MargaritaMixer)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.tripleSecSpinBox = QtGui.QSpinBox(MargaritaMixer)
        self.tripleSecSpinBox.setMaximum(11)
        self.tripleSecSpinBox.setProperty("value", 4)
        self.tripleSecSpinBox.setObjectName("tripleSecSpinBox")
        self.gridLayout.addWidget(self.tripleSecSpinBox, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(MargaritaMixer)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.limeJuiceLineEdit = QtGui.QLineEdit(MargaritaMixer)
        self.limeJuiceLineEdit.setObjectName("limeJuiceLineEdit")
        self.gridLayout.addWidget(self.limeJuiceLineEdit, 2, 1, 1, 2)
        self.label_4 = QtGui.QLabel(MargaritaMixer)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.iceHorizontalSlider = QtGui.QSlider(MargaritaMixer)
        self.iceHorizontalSlider.setMinimum(0)
        self.iceHorizontalSlider.setMaximum(20)
        self.iceHorizontalSlider.setProperty("value", 12)
        self.iceHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.iceHorizontalSlider.setObjectName("iceHorizontalSlider")
        self.gridLayout.addWidget(self.iceHorizontalSlider, 3, 2, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(MargaritaMixer)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 1)
        self.tequilaScrollBar = QtGui.QScrollBar(MargaritaMixer)
        self.tequilaScrollBar.setEnabled(True)
        self.tequilaScrollBar.setMaximum(11)
        self.tequilaScrollBar.setProperty("value", 8)
        self.tequilaScrollBar.setSliderPosition(8)
        self.tequilaScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.tequilaScrollBar.setObjectName("tequilaScrollBar")
        self.gridLayout.addWidget(self.tequilaScrollBar, 0, 1, 1, 2)
        self.groupBox = QtGui.QGroupBox(MargaritaMixer)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.speedButton1 = QtGui.QRadioButton(self.groupBox)
        self.speedButton1.setObjectName("speedButton1")
        self.speedButtonGroup = QtGui.QButtonGroup(MargaritaMixer)
        self.speedButtonGroup.setObjectName("speedButtonGroup")
        self.speedButtonGroup.addButton(self.speedButton1)
        self.gridLayout_2.addWidget(self.speedButton1, 0, 0, 1, 1)
        self.speedButton3 = QtGui.QRadioButton(self.groupBox)
        self.speedButton3.setObjectName("speedButton3")
        self.speedButtonGroup.addButton(self.speedButton3)
        self.gridLayout_2.addWidget(self.speedButton3, 0, 2, 1, 1)
        self.speedButton4 = QtGui.QRadioButton(self.groupBox)
        self.speedButton4.setObjectName("speedButton4")
        self.speedButtonGroup.addButton(self.speedButton4)
        self.gridLayout_2.addWidget(self.speedButton4, 1, 0, 1, 1)
        self.speedButton5 = QtGui.QRadioButton(self.groupBox)
        self.speedButton5.setChecked(True)
        self.speedButton5.setObjectName("speedButton5")
        self.speedButtonGroup.addButton(self.speedButton5)
        self.gridLayout_2.addWidget(self.speedButton5, 1, 1, 1, 1)
        self.speedButton6 = QtGui.QRadioButton(self.groupBox)
        self.speedButton6.setObjectName("speedButton6")
        self.speedButtonGroup.addButton(self.speedButton6)
        self.gridLayout_2.addWidget(self.speedButton6, 1, 2, 1, 1)
        self.speedButton9 = QtGui.QRadioButton(self.groupBox)
        self.speedButton9.setObjectName("speedButton9")
        self.speedButtonGroup.addButton(self.speedButton9)
        self.gridLayout_2.addWidget(self.speedButton9, 3, 2, 1, 1)
        self.speedButton8 = QtGui.QRadioButton(self.groupBox)
        self.speedButton8.setObjectName("speedButton8")
        self.speedButtonGroup.addButton(self.speedButton8)
        self.gridLayout_2.addWidget(self.speedButton8, 3, 1, 1, 1)
        self.speedButton7 = QtGui.QRadioButton(self.groupBox)
        self.speedButton7.setObjectName("speedButton7")
        self.speedButtonGroup.addButton(self.speedButton7)
        self.gridLayout_2.addWidget(self.speedButton7, 3, 0, 1, 1)
        self.speedButton2 = QtGui.QRadioButton(self.groupBox)
        self.speedButton2.setObjectName("speedButton2")
        self.speedButtonGroup.addButton(self.speedButton2)
        self.gridLayout_2.addWidget(self.speedButton2, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 4, 0, 1, 3)

        self.retranslateUi(MargaritaMixer)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), MargaritaMixer.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), MargaritaMixer.reject)
        QtCore.QMetaObject.connectSlotsByName(MargaritaMixer)
        MargaritaMixer.setTabOrder(self.buttonBox, self.tripleSecSpinBox)
        MargaritaMixer.setTabOrder(self.tripleSecSpinBox, self.limeJuiceLineEdit)
        MargaritaMixer.setTabOrder(self.limeJuiceLineEdit, self.iceHorizontalSlider)
        MargaritaMixer.setTabOrder(self.iceHorizontalSlider, self.speedButton1)
        MargaritaMixer.setTabOrder(self.speedButton1, self.speedButton2)
        MargaritaMixer.setTabOrder(self.speedButton2, self.speedButton3)

    def retranslateUi(self, MargaritaMixer):
        MargaritaMixer.setWindowTitle(QtGui.QApplication.translate("MargaritaMixer", "Margarita Mixer", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MargaritaMixer", "Tequila", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MargaritaMixer", "Triple Sec", None, QtGui.QApplication.UnicodeUTF8))
        self.tripleSecSpinBox.setToolTip(QtGui.QApplication.translate("MargaritaMixer", "Jiggers of triple sec", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MargaritaMixer", "Lime Juice", None, QtGui.QApplication.UnicodeUTF8))
        self.limeJuiceLineEdit.setToolTip(QtGui.QApplication.translate("MargaritaMixer", "Jiggers of lime juice", None, QtGui.QApplication.UnicodeUTF8))
        self.limeJuiceLineEdit.setText(QtGui.QApplication.translate("MargaritaMixer", "12.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MargaritaMixer", "Ice", None, QtGui.QApplication.UnicodeUTF8))
        self.iceHorizontalSlider.setToolTip(QtGui.QApplication.translate("MargaritaMixer", "Chunks of ice", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonBox.setToolTip(QtGui.QApplication.translate("MargaritaMixer", "Press OK to make the drinks", None, QtGui.QApplication.UnicodeUTF8))
        self.tequilaScrollBar.setToolTip(QtGui.QApplication.translate("MargaritaMixer", "Jiggers of tequila", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setToolTip(QtGui.QApplication.translate("MargaritaMixer", "Speed of the blender", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MargaritaMixer", "Blender Speed", None, QtGui.QApplication.UnicodeUTF8))
        self.speedButton1.setText(QtGui.QApplication.translate("MargaritaMixer", "&Mix", None, QtGui.QApplication.UnicodeUTF8))
        self.speedButton3.setText(QtGui.QApplication.translate("MargaritaMixer", "&Puree", None, QtGui.QApplication.UnicodeUTF8))
        self.speedButton4.setText(QtGui.QApplication.translate("MargaritaMixer", "&Chop", None, QtGui.QApplication.UnicodeUTF8))
        self.speedButton5.setText(QtGui.QApplication.translate("MargaritaMixer", "&Karate Chop", None, QtGui.QApplication.UnicodeUTF8))
        self.speedButton6.setText(QtGui.QApplication.translate("MargaritaMixer", "&Beat", None, QtGui.QApplication.UnicodeUTF8))
        self.speedButton9.setText(QtGui.QApplication.translate("MargaritaMixer", "&Vaporize", None, QtGui.QApplication.UnicodeUTF8))
        self.speedButton8.setText(QtGui.QApplication.translate("MargaritaMixer", "&Liquefy", None, QtGui.QApplication.UnicodeUTF8))
        self.speedButton7.setText(QtGui.QApplication.translate("MargaritaMixer", "&Smash", None, QtGui.QApplication.UnicodeUTF8))
        self.speedButton2.setText(QtGui.QApplication.translate("MargaritaMixer", "&Whip", None, QtGui.QApplication.UnicodeUTF8))

