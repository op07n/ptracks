# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './dlg_fix_edit_new.ui'
#
# Created: Tue Jan 26 11:33:06 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_dlgFixEditNEW(object):
    def setupUi(self, dlgFixEditNEW):
        dlgFixEditNEW.setObjectName(_fromUtf8("dlgFixEditNEW"))
        dlgFixEditNEW.resize(369, 388)
        dlgFixEditNEW.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        dlgFixEditNEW.setSizeGripEnabled(True)
        dlgFixEditNEW.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(dlgFixEditNEW)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frmGrpID = QtGui.QFrame(dlgFixEditNEW)
        self.frmGrpID.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frmGrpID.setFrameShadow(QtGui.QFrame.Raised)
        self.frmGrpID.setObjectName(_fromUtf8("frmGrpID"))
        self.gridLayout = QtGui.QGridLayout(self.frmGrpID)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lblNome = QtGui.QLabel(self.frmGrpID)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblNome.sizePolicy().hasHeightForWidth())
        self.lblNome.setSizePolicy(sizePolicy)
        self.lblNome.setObjectName(_fromUtf8("lblNome"))
        self.gridLayout.addWidget(self.lblNome, 0, 0, 1, 1)
        self.qleNome = QtGui.QLineEdit(self.frmGrpID)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qleNome.sizePolicy().hasHeightForWidth())
        self.qleNome.setSizePolicy(sizePolicy)
        self.qleNome.setObjectName(_fromUtf8("qleNome"))
        self.gridLayout.addWidget(self.qleNome, 0, 1, 1, 1)
        self.lblDesc = QtGui.QLabel(self.frmGrpID)
        self.lblDesc.setObjectName(_fromUtf8("lblDesc"))
        self.gridLayout.addWidget(self.lblDesc, 1, 0, 1, 1)
        self.widget = QtGui.QWidget(self.frmGrpID)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setMargin(3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.qleIndc = QtGui.QLineEdit(self.widget)
        self.qleIndc.setObjectName(_fromUtf8("qleIndc"))
        self.horizontalLayout_2.addWidget(self.qleIndc)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addWidget(self.widget, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.frmGrpID)
        self.frame_3 = QtGui.QFrame(dlgFixEditNEW)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.groupBox_2 = QtGui.QGroupBox(self.frame_3)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ckxVOR = QtGui.QCheckBox(self.groupBox_2)
        self.ckxVOR.setObjectName(_fromUtf8("ckxVOR"))
        self.horizontalLayout.addWidget(self.ckxVOR)
        self.ckxNDB = QtGui.QCheckBox(self.groupBox_2)
        self.ckxNDB.setObjectName(_fromUtf8("ckxNDB"))
        self.horizontalLayout.addWidget(self.ckxNDB)
        self.ckxDME = QtGui.QCheckBox(self.groupBox_2)
        self.ckxDME.setObjectName(_fromUtf8("ckxDME"))
        self.horizontalLayout.addWidget(self.ckxDME)
        self.horizontalLayout_8.addWidget(self.groupBox_2)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtGui.QFrame(dlgFixEditNEW)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.gbxCrd = QtGui.QGroupBox(self.frame_2)
        self.gbxCrd.setObjectName(_fromUtf8("gbxCrd"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gbxCrd)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lblLat = QtGui.QLabel(self.gbxCrd)
        self.lblLat.setObjectName(_fromUtf8("lblLat"))
        self.gridLayout_3.addWidget(self.lblLat, 0, 0, 1, 1)
        self.lblLng = QtGui.QLabel(self.gbxCrd)
        self.lblLng.setObjectName(_fromUtf8("lblLng"))
        self.gridLayout_3.addWidget(self.lblLng, 1, 0, 1, 1)
        self.qleLat = QtGui.QLineEdit(self.gbxCrd)
        self.qleLat.setObjectName(_fromUtf8("qleLat"))
        self.gridLayout_3.addWidget(self.qleLat, 0, 1, 1, 1)
        self.qleLng = QtGui.QLineEdit(self.gbxCrd)
        self.qleLng.setObjectName(_fromUtf8("qleLng"))
        self.gridLayout_3.addWidget(self.qleLng, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 1, 1)
        self.horizontalLayout_5.addWidget(self.gbxCrd)
        self.verticalLayout.addWidget(self.frame_2)
        self.bbxEditPrf = QtGui.QWidget(dlgFixEditNEW)
        self.bbxEditPrf.setObjectName(_fromUtf8("bbxEditPrf"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.bbxEditPrf)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.btnCancel = QtGui.QPushButton(self.bbxEditPrf)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancel.setIcon(icon)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.horizontalLayout_6.addWidget(self.btnCancel)
        self.btnOk = QtGui.QPushButton(self.bbxEditPrf)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOk.setIcon(icon1)
        self.btnOk.setObjectName(_fromUtf8("btnOk"))
        self.horizontalLayout_6.addWidget(self.btnOk)
        self.verticalLayout.addWidget(self.bbxEditPrf)
        self.lblNome.setBuddy(self.qleNome)
        self.lblDesc.setBuddy(self.qleIndc)
        self.lblLat.setBuddy(self.qleLat)
        self.lblLng.setBuddy(self.qleLng)

        self.retranslateUi(dlgFixEditNEW)
        QtCore.QMetaObject.connectSlotsByName(dlgFixEditNEW)
        dlgFixEditNEW.setTabOrder(self.qleNome, self.qleIndc)
        dlgFixEditNEW.setTabOrder(self.qleIndc, self.ckxVOR)
        dlgFixEditNEW.setTabOrder(self.ckxVOR, self.ckxNDB)
        dlgFixEditNEW.setTabOrder(self.ckxNDB, self.ckxDME)
        dlgFixEditNEW.setTabOrder(self.ckxDME, self.qleLat)
        dlgFixEditNEW.setTabOrder(self.qleLat, self.qleLng)
        dlgFixEditNEW.setTabOrder(self.qleLng, self.btnCancel)
        dlgFixEditNEW.setTabOrder(self.btnCancel, self.btnOk)

    def retranslateUi(self, dlgFixEditNEW):
        dlgFixEditNEW.setWindowTitle(_translate("dlgFixEditNEW", "TrackS - Edição de Fixos", None))
        self.lblNome.setText(_translate("dlgFixEditNEW", "Nome:", None))
        self.lblDesc.setText(_translate("dlgFixEditNEW", "Indicativo:", None))
        self.qleIndc.setInputMask(_translate("dlgFixEditNEW", ">AAA; ", None))
        self.groupBox_2.setTitle(_translate("dlgFixEditNEW", "Navaids", None))
        self.ckxVOR.setText(_translate("dlgFixEditNEW", "VOR", None))
        self.ckxNDB.setText(_translate("dlgFixEditNEW", "NDB", None))
        self.ckxDME.setText(_translate("dlgFixEditNEW", "DME", None))
        self.gbxCrd.setTitle(_translate("dlgFixEditNEW", "Posicão", None))
        self.lblLat.setText(_translate("dlgFixEditNEW", "Latitude:", None))
        self.lblLng.setText(_translate("dlgFixEditNEW", "Longitude:", None))
        self.btnCancel.setText(_translate("dlgFixEditNEW", "Cancela", None))
        self.btnOk.setText(_translate("dlgFixEditNEW", "Ok", None))

import qrc_resources_rc
