# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/Erying_Eq.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Erying_Eq(object):
    def setupUi(self, Erying_Eq):
        Erying_Eq.setObjectName("Erying_Eq")
        Erying_Eq.resize(559, 380)
        self.verticalLayout = QtWidgets.QVBoxLayout(Erying_Eq)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.G_neq_lineEdit = QtWidgets.QLineEdit(Erying_Eq)
        self.G_neq_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.G_neq_lineEdit.setFont(font)
        self.G_neq_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.G_neq_lineEdit.setPlaceholderText("")
        self.G_neq_lineEdit.setObjectName("G_neq_lineEdit")
        self.gridLayout.addWidget(self.G_neq_lineEdit, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(Erying_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Erying_Eq)
        self.label_2.setMinimumSize(QtCore.QSize(67, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.kTST_lineEdit = QtWidgets.QLineEdit(Erying_Eq)
        self.kTST_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.kTST_lineEdit.setFont(font)
        self.kTST_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.kTST_lineEdit.setText("")
        self.kTST_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.kTST_lineEdit.setReadOnly(False)
        self.kTST_lineEdit.setPlaceholderText("")
        self.kTST_lineEdit.setObjectName("kTST_lineEdit")
        self.gridLayout.addWidget(self.kTST_lineEdit, 4, 1, 1, 1)
        self.conc1_label = QtWidgets.QLabel(Erying_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.conc1_label.setFont(font)
        self.conc1_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.conc1_label.setObjectName("conc1_label")
        self.gridLayout.addWidget(self.conc1_label, 1, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(Erying_Eq)
        self.label_8.setMinimumSize(QtCore.QSize(45, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(Erying_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 2, 1, 1)
        self.kTST_unit_label = QtWidgets.QLabel(Erying_Eq)
        self.kTST_unit_label.setMinimumSize(QtCore.QSize(45, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.kTST_unit_label.setFont(font)
        self.kTST_unit_label.setObjectName("kTST_unit_label")
        self.gridLayout.addWidget(self.kTST_unit_label, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(Erying_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.conc1_lineEdit = QtWidgets.QLineEdit(Erying_Eq)
        self.conc1_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.conc1_lineEdit.setFont(font)
        self.conc1_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.conc1_lineEdit.setObjectName("conc1_lineEdit")
        self.gridLayout.addWidget(self.conc1_lineEdit, 1, 6, 1, 1)
        self.label_6 = QtWidgets.QLabel(Erying_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.line = QtWidgets.QFrame(Erying_Eq)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 4, 5, 1)
        self.conversion_lineEdit = QtWidgets.QLineEdit(Erying_Eq)
        self.conversion_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.conversion_lineEdit.setFont(font)
        self.conversion_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.conversion_lineEdit.setObjectName("conversion_lineEdit")
        self.gridLayout.addWidget(self.conversion_lineEdit, 3, 6, 1, 1)
        self.line_2 = QtWidgets.QFrame(Erying_Eq)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 6, 0, 1, 8)
        self.temp_lineEdit = QtWidgets.QLineEdit(Erying_Eq)
        self.temp_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.temp_lineEdit.setFont(font)
        self.temp_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.temp_lineEdit.setObjectName("temp_lineEdit")
        self.gridLayout.addWidget(self.temp_lineEdit, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(Erying_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 7, 1, 1)
        self.label_10 = QtWidgets.QLabel(Erying_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 7, 1, 1)
        self.total_time_lineEdit = QtWidgets.QLineEdit(Erying_Eq)
        self.total_time_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.total_time_lineEdit.setFont(font)
        self.total_time_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.total_time_lineEdit.setPlaceholderText("")
        self.total_time_lineEdit.setObjectName("total_time_lineEdit")
        self.gridLayout.addWidget(self.total_time_lineEdit, 4, 6, 1, 1)
        self.label_4 = QtWidgets.QLabel(Erying_Eq)
        self.label_4.setMinimumSize(QtCore.QSize(67, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(Erying_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 5, 1, 1)
        self.label_12 = QtWidgets.QLabel(Erying_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 3, 7, 1, 1)
        self.conc2_lineEdit = QtWidgets.QLineEdit(Erying_Eq)
        self.conc2_lineEdit.setEnabled(False)
        self.conc2_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.conc2_lineEdit.setFont(font)
        self.conc2_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.conc2_lineEdit.setObjectName("conc2_lineEdit")
        self.gridLayout.addWidget(self.conc2_lineEdit, 2, 6, 1, 1)
        self.conc2_label = QtWidgets.QLabel(Erying_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.conc2_label.setFont(font)
        self.conc2_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.conc2_label.setObjectName("conc2_label")
        self.gridLayout.addWidget(self.conc2_label, 2, 5, 1, 1)
        self.conc2_unit_label = QtWidgets.QLabel(Erying_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.conc2_unit_label.setFont(font)
        self.conc2_unit_label.setObjectName("conc2_unit_label")
        self.gridLayout.addWidget(self.conc2_unit_label, 2, 7, 1, 1)
        self.sigma_lineEdit = QtWidgets.QLineEdit(Erying_Eq)
        self.sigma_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.sigma_lineEdit.setFont(font)
        self.sigma_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sigma_lineEdit.setObjectName("sigma_lineEdit")
        self.gridLayout.addWidget(self.sigma_lineEdit, 3, 1, 1, 1)
        self.calculate_pushButton = QtWidgets.QPushButton(Erying_Eq)
        self.calculate_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.calculate_pushButton.setFont(font)
        self.calculate_pushButton.setObjectName("calculate_pushButton")
        self.gridLayout.addWidget(self.calculate_pushButton, 7, 5, 1, 4)
        self.reset_all_pushButton = QtWidgets.QPushButton(Erying_Eq)
        self.reset_all_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.reset_all_pushButton.setFont(font)
        self.reset_all_pushButton.setObjectName("reset_all_pushButton")
        self.gridLayout.addWidget(self.reset_all_pushButton, 7, 0, 1, 4)
        self.clear_G_pushButton = QtWidgets.QPushButton(Erying_Eq)
        self.clear_G_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.clear_G_pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.clear_G_pushButton.setFont(font)
        self.clear_G_pushButton.setObjectName("clear_G_pushButton")
        self.gridLayout.addWidget(self.clear_G_pushButton, 1, 3, 1, 1)
        self.clear_sigma_pushButton = QtWidgets.QPushButton(Erying_Eq)
        self.clear_sigma_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.clear_sigma_pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.clear_sigma_pushButton.setFont(font)
        self.clear_sigma_pushButton.setObjectName("clear_sigma_pushButton")
        self.gridLayout.addWidget(self.clear_sigma_pushButton, 3, 3, 1, 1)
        self.clear_k_pushButton = QtWidgets.QPushButton(Erying_Eq)
        self.clear_k_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.clear_k_pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.clear_k_pushButton.setFont(font)
        self.clear_k_pushButton.setObjectName("clear_k_pushButton")
        self.gridLayout.addWidget(self.clear_k_pushButton, 4, 3, 1, 1)
        self.clear_T_pushButton = QtWidgets.QPushButton(Erying_Eq)
        self.clear_T_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.clear_T_pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.clear_T_pushButton.setFont(font)
        self.clear_T_pushButton.setObjectName("clear_T_pushButton")
        self.gridLayout.addWidget(self.clear_T_pushButton, 2, 3, 1, 1)
        self.clear_conc1_pushButton = QtWidgets.QPushButton(Erying_Eq)
        self.clear_conc1_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.clear_conc1_pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.clear_conc1_pushButton.setFont(font)
        self.clear_conc1_pushButton.setObjectName("clear_conc1_pushButton")
        self.gridLayout.addWidget(self.clear_conc1_pushButton, 1, 8, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Erying_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.unimolecular_radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.unimolecular_radioButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.unimolecular_radioButton.setFont(font)
        self.unimolecular_radioButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.unimolecular_radioButton.setChecked(True)
        self.unimolecular_radioButton.setObjectName("unimolecular_radioButton")
        self.horizontalLayout_3.addWidget(self.unimolecular_radioButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.bimolecular_AA_radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.bimolecular_AA_radioButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bimolecular_AA_radioButton.setFont(font)
        self.bimolecular_AA_radioButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.bimolecular_AA_radioButton.setObjectName("bimolecular_AA_radioButton")
        self.horizontalLayout_3.addWidget(self.bimolecular_AA_radioButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.bimolecular_AB_radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.bimolecular_AB_radioButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bimolecular_AB_radioButton.setFont(font)
        self.bimolecular_AB_radioButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.bimolecular_AB_radioButton.setObjectName("bimolecular_AB_radioButton")
        self.horizontalLayout_3.addWidget(self.bimolecular_AB_radioButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.horizontalLayout.addWidget(self.groupBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 9)
        self.clear_conc2_pushButton = QtWidgets.QPushButton(Erying_Eq)
        self.clear_conc2_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.clear_conc2_pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.clear_conc2_pushButton.setFont(font)
        self.clear_conc2_pushButton.setObjectName("clear_conc2_pushButton")
        self.gridLayout.addWidget(self.clear_conc2_pushButton, 2, 8, 1, 1)
        self.clear_t_pushButton = QtWidgets.QPushButton(Erying_Eq)
        self.clear_t_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.clear_t_pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.clear_t_pushButton.setFont(font)
        self.clear_t_pushButton.setObjectName("clear_t_pushButton")
        self.gridLayout.addWidget(self.clear_t_pushButton, 4, 8, 1, 1)
        self.clear_conv_pushButton = QtWidgets.QPushButton(Erying_Eq)
        self.clear_conv_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.clear_conv_pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.clear_conv_pushButton.setFont(font)
        self.clear_conv_pushButton.setObjectName("clear_conv_pushButton")
        self.gridLayout.addWidget(self.clear_conv_pushButton, 3, 8, 1, 1)
        self.total_time_display_label = QtWidgets.QLabel(Erying_Eq)
        self.total_time_display_label.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.total_time_display_label.setFont(font)
        self.total_time_display_label.setText("")
        self.total_time_display_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.total_time_display_label.setObjectName("total_time_display_label")
        self.gridLayout.addWidget(self.total_time_display_label, 5, 5, 1, 3)
        self.gridLayout.setRowStretch(0, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line_3 = QtWidgets.QFrame(Erying_Eq)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.line_3.setFont(font)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.status_label_2 = QtWidgets.QLabel(Erying_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.status_label_2.setFont(font)
        self.status_label_2.setObjectName("status_label_2")
        self.verticalLayout.addWidget(self.status_label_2)
        self.status_label_3 = QtWidgets.QLabel(Erying_Eq)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.status_label_3.setFont(font)
        self.status_label_3.setObjectName("status_label_3")
        self.verticalLayout.addWidget(self.status_label_3)

        self.retranslateUi(Erying_Eq)
        QtCore.QMetaObject.connectSlotsByName(Erying_Eq)
        Erying_Eq.setTabOrder(self.G_neq_lineEdit, self.temp_lineEdit)
        Erying_Eq.setTabOrder(self.temp_lineEdit, self.kTST_lineEdit)
        Erying_Eq.setTabOrder(self.kTST_lineEdit, self.conc1_lineEdit)
        Erying_Eq.setTabOrder(self.conc1_lineEdit, self.conc2_lineEdit)
        Erying_Eq.setTabOrder(self.conc2_lineEdit, self.conversion_lineEdit)
        Erying_Eq.setTabOrder(self.conversion_lineEdit, self.total_time_lineEdit)
        Erying_Eq.setTabOrder(self.total_time_lineEdit, self.calculate_pushButton)
        Erying_Eq.setTabOrder(self.calculate_pushButton, self.reset_all_pushButton)
        Erying_Eq.setTabOrder(self.reset_all_pushButton, self.sigma_lineEdit)

    def retranslateUi(self, Erying_Eq):
        _translate = QtCore.QCoreApplication.translate
        Erying_Eq.setWindowTitle(_translate("Erying_Eq", "Erying Equation Solver by LYH"))
        self.label_15.setText(_translate("Erying_Eq", "σ"))
        self.label_2.setText(_translate("Erying_Eq", "Temp."))
        self.conc1_label.setText(_translate("Erying_Eq", "Conc. 1"))
        self.label_8.setText(_translate("Erying_Eq", "kJ/mol"))
        self.label_9.setText(_translate("Erying_Eq", "°C"))
        self.kTST_unit_label.setText(_translate("Erying_Eq", "<html><head/><body><p>M<span style=\" vertical-align:super;\">-1</span>·s<span style=\" vertical-align:super;\">-1</span></p></body></html>"))
        self.label.setText(_translate("Erying_Eq", "<html><head/><body><p>ΔG<span style=\" vertical-align:super;\">≠</span></p></body></html>"))
        self.label_6.setText(_translate("Erying_Eq", "<html><head/><body><p>k<span style=\" vertical-align:sub;\">TST</span></p></body></html>"))
        self.conversion_lineEdit.setText(_translate("Erying_Eq", "98"))
        self.label_13.setText(_translate("Erying_Eq", "mol/L"))
        self.label_10.setText(_translate("Erying_Eq", "s"))
        self.label_4.setText(_translate("Erying_Eq", "Rxn Time"))
        self.label_5.setText(_translate("Erying_Eq", "Conv."))
        self.label_12.setText(_translate("Erying_Eq", "%"))
        self.conc2_label.setText(_translate("Erying_Eq", "Conc. 2"))
        self.conc2_unit_label.setText(_translate("Erying_Eq", "mol/L"))
        self.sigma_lineEdit.setText(_translate("Erying_Eq", "1"))
        self.calculate_pushButton.setText(_translate("Erying_Eq", "Calculate"))
        self.reset_all_pushButton.setText(_translate("Erying_Eq", "Reset All"))
        self.clear_G_pushButton.setText(_translate("Erying_Eq", "×"))
        self.clear_sigma_pushButton.setText(_translate("Erying_Eq", "×"))
        self.clear_k_pushButton.setText(_translate("Erying_Eq", "×"))
        self.clear_T_pushButton.setText(_translate("Erying_Eq", "×"))
        self.clear_conc1_pushButton.setText(_translate("Erying_Eq", "×"))
        self.groupBox.setTitle(_translate("Erying_Eq", "Reaction Type"))
        self.unimolecular_radioButton.setText(_translate("Erying_Eq", "A → P"))
        self.bimolecular_AA_radioButton.setText(_translate("Erying_Eq", "A + A → P"))
        self.bimolecular_AB_radioButton.setText(_translate("Erying_Eq", "A + B → P"))
        self.clear_conc2_pushButton.setText(_translate("Erying_Eq", "×"))
        self.clear_t_pushButton.setText(_translate("Erying_Eq", "×"))
        self.clear_conv_pushButton.setText(_translate("Erying_Eq", "×"))
        self.status_label_2.setText(_translate("Erying_Eq", "<html><head/><body><p>You can input any Python arithmetic expression, e.g. 2E3*4.18 (= 8360).</p></body></html>"))
        self.status_label_3.setText(_translate("Erying_Eq", "<html><head/><body><p>If the [Calculate] button is not enabled, check your number of parameters.</p></body></html>"))

