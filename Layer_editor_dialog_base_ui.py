# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Layer_editor_dialog_base.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

from qgscolorbutton import QgsColorButton
from qgsspinbox import QgsSpinBox

class Ui_StylePluginDialogBase(object):
    def setupUi(self, StylePluginDialogBase):
        if not StylePluginDialogBase.objectName():
            StylePluginDialogBase.setObjectName(u"StylePluginDialogBase")
        StylePluginDialogBase.resize(429, 408)
        self.widgetContent = QWidget(StylePluginDialogBase)
        self.widgetContent.setObjectName(u"widgetContent")
        self.widgetContent.setGeometry(QRect(20, 10, 391, 391))
        self.gridLayout = QGridLayout(self.widgetContent)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, -1, 0, 8)
        self.pushButton_apply = QPushButton(self.widgetContent)
        self.pushButton_apply.setObjectName(u"pushButton_apply")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton_apply.setFont(font)

        self.gridLayout.addWidget(self.pushButton_apply, 3, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widgetContent)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.comboBoxLayers = QComboBox(self.widgetContent)
        self.comboBoxLayers.setObjectName(u"comboBoxLayers")

        self.verticalLayout.addWidget(self.comboBoxLayers)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.widgetContent)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayoutWidget_2 = QWidget(self.tab)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 381, 261))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widgetPoint = QWidget(self.verticalLayoutWidget_2)
        self.widgetPoint.setObjectName(u"widgetPoint")
        font1 = QFont()
        font1.setPointSize(10)
        self.widgetPoint.setFont(font1)
        self.horizontalLayout = QHBoxLayout(self.widgetPoint)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelPoint = QLabel(self.widgetPoint)
        self.labelPoint.setObjectName(u"labelPoint")
        self.labelPoint.setFont(font1)

        self.horizontalLayout.addWidget(self.labelPoint)

        self.comboBoxPoint = QComboBox(self.widgetPoint)
        self.comboBoxPoint.addItem("")
        self.comboBoxPoint.addItem("")
        self.comboBoxPoint.addItem("")
        self.comboBoxPoint.setObjectName(u"comboBoxPoint")

        self.horizontalLayout.addWidget(self.comboBoxPoint)


        self.verticalLayout_2.addWidget(self.widgetPoint)

        self.widgetPen = QWidget(self.verticalLayoutWidget_2)
        self.widgetPen.setObjectName(u"widgetPen")
        self.horizontalLayout_2 = QHBoxLayout(self.widgetPen)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelPen = QLabel(self.widgetPen)
        self.labelPen.setObjectName(u"labelPen")
        self.labelPen.setFont(font1)

        self.horizontalLayout_2.addWidget(self.labelPen)

        self.mColorButtonPen = QgsColorButton(self.widgetPen)
        self.mColorButtonPen.setObjectName(u"mColorButtonPen")

        self.horizontalLayout_2.addWidget(self.mColorButtonPen)


        self.verticalLayout_2.addWidget(self.widgetPen)

        self.widgetBrush = QWidget(self.verticalLayoutWidget_2)
        self.widgetBrush.setObjectName(u"widgetBrush")
        self.horizontalLayout_5 = QHBoxLayout(self.widgetBrush)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.labelBrush = QLabel(self.widgetBrush)
        self.labelBrush.setObjectName(u"labelBrush")
        self.labelBrush.setFont(font1)

        self.horizontalLayout_5.addWidget(self.labelBrush)

        self.mColorButtonBrush = QgsColorButton(self.widgetBrush)
        self.mColorButtonBrush.setObjectName(u"mColorButtonBrush")
        self.mColorButtonBrush.setEnabled(True)
        self.mColorButtonBrush.setMinimumSize(QSize(100, 16))

        self.horizontalLayout_5.addWidget(self.mColorButtonBrush)

        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 3)

        self.verticalLayout_2.addWidget(self.widgetBrush)

        self.widgetStroke = QWidget(self.verticalLayoutWidget_2)
        self.widgetStroke.setObjectName(u"widgetStroke")
        self.horizontalLayout_4 = QHBoxLayout(self.widgetStroke)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelStroke = QLabel(self.widgetStroke)
        self.labelStroke.setObjectName(u"labelStroke")
        self.labelStroke.setFont(font1)

        self.horizontalLayout_4.addWidget(self.labelStroke)

        self.comboBoxStroke = QComboBox(self.widgetStroke)
        self.comboBoxStroke.addItem("")
        self.comboBoxStroke.addItem("")
        self.comboBoxStroke.addItem("")
        self.comboBoxStroke.addItem("")
        self.comboBoxStroke.addItem("")
        self.comboBoxStroke.addItem("")
        self.comboBoxStroke.setObjectName(u"comboBoxStroke")

        self.horizontalLayout_4.addWidget(self.comboBoxStroke)


        self.verticalLayout_2.addWidget(self.widgetStroke)

        self.widgetSize = QHBoxLayout()
        self.widgetSize.setObjectName(u"widgetSize")
        self.widgetSize.setContentsMargins(9, 9, 9, 9)
        self.labelStroke_2 = QLabel(self.verticalLayoutWidget_2)
        self.labelStroke_2.setObjectName(u"labelStroke_2")
        self.labelStroke_2.setFont(font1)

        self.widgetSize.addWidget(self.labelStroke_2)

        self.mQgsSpinBox = QgsSpinBox(self.verticalLayoutWidget_2)
        self.mQgsSpinBox.setObjectName(u"mQgsSpinBox")
        self.mQgsSpinBox.setMinimum(1)
        self.mQgsSpinBox.setSingleStep(1)
        self.mQgsSpinBox.setDisplayIntegerBase(10)

        self.widgetSize.addWidget(self.mQgsSpinBox)


        self.verticalLayout_2.addLayout(self.widgetSize)

        self.widgetFill = QWidget(self.verticalLayoutWidget_2)
        self.widgetFill.setObjectName(u"widgetFill")
        self.horizontalLayout_3 = QHBoxLayout(self.widgetFill)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelFill = QLabel(self.widgetFill)
        self.labelFill.setObjectName(u"labelFill")
        self.labelFill.setFont(font1)

        self.horizontalLayout_3.addWidget(self.labelFill)

        self.comboBoxFill = QComboBox(self.widgetFill)
        self.comboBoxFill.addItem("")
        self.comboBoxFill.addItem("")
        self.comboBoxFill.addItem("")
        self.comboBoxFill.addItem("")
        self.comboBoxFill.addItem("")
        self.comboBoxFill.addItem("")
        self.comboBoxFill.addItem("")
        self.comboBoxFill.addItem("")
        self.comboBoxFill.addItem("")
        self.comboBoxFill.addItem("")
        self.comboBoxFill.addItem("")
        self.comboBoxFill.addItem("")
        self.comboBoxFill.addItem("")
        self.comboBoxFill.addItem("")
        self.comboBoxFill.addItem("")
        self.comboBoxFill.setObjectName(u"comboBoxFill")
        self.comboBoxFill.setMinimumSize(QSize(100, 16))

        self.horizontalLayout_3.addWidget(self.comboBoxFill)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 3)

        self.verticalLayout_2.addWidget(self.widgetFill)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayoutWidget_3 = QWidget(self.tab_2)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 381, 261))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.geometryLabel = QLabel(self.verticalLayoutWidget_3)
        self.geometryLabel.setObjectName(u"geometryLabel")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.geometryLabel.setFont(font2)

        self.verticalLayout_3.addWidget(self.geometryLabel)

        self.tableWidget = QTableWidget(self.verticalLayoutWidget_3)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        font3 = QFont()
        font3.setPointSize(11)
        self.tableWidget.setFont(font3)

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 1)


        self.retranslateUi(StylePluginDialogBase)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StylePluginDialogBase)
    # setupUi

    def retranslateUi(self, StylePluginDialogBase):
        StylePluginDialogBase.setWindowTitle(QCoreApplication.translate("StylePluginDialogBase", u"StylePlugin", None))
        self.pushButton_apply.setText(QCoreApplication.translate("StylePluginDialogBase", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("StylePluginDialogBase", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043b\u043e\u0439", None))
        self.labelPoint.setText(QCoreApplication.translate("StylePluginDialogBase", u"\u0421\u0442\u0438\u043b\u044c \u0442\u043e\u0447\u043a\u0438", None))
        self.comboBoxPoint.setItemText(0, QCoreApplication.translate("StylePluginDialogBase", u"diamond", None))
        self.comboBoxPoint.setItemText(1, QCoreApplication.translate("StylePluginDialogBase", u"dot", None))
        self.comboBoxPoint.setItemText(2, QCoreApplication.translate("StylePluginDialogBase", u"triangle", None))

        self.labelPen.setText(QCoreApplication.translate("StylePluginDialogBase", u"\u0426\u0432\u0435\u0442 \u043b\u0438\u043d\u0438\u0438/\u043e\u0431\u0432\u043e\u0434\u043a\u0438", None))
        self.mColorButtonPen.setText(QCoreApplication.translate("StylePluginDialogBase", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0446\u0432\u0435\u0442", None))
        self.labelBrush.setText(QCoreApplication.translate("StylePluginDialogBase", u"\u0426\u0432\u0435\u0442 \u0437\u0430\u043b\u0438\u0432\u043a\u0438", None))
        self.mColorButtonBrush.setText(QCoreApplication.translate("StylePluginDialogBase", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0446\u0432\u0435\u0442", None))
        self.labelStroke.setText(QCoreApplication.translate("StylePluginDialogBase", u"\u0421\u0442\u0438\u043b\u044c \u043b\u0438\u043d\u0438\u0438/\u043e\u0431\u0432\u043e\u0434\u043a\u0438", None))
        self.comboBoxStroke.setItemText(0, QCoreApplication.translate("StylePluginDialogBase", u"\u0421\u043f\u043b\u043e\u0448\u043d\u0430\u044f", None))
        self.comboBoxStroke.setItemText(1, QCoreApplication.translate("StylePluginDialogBase", u"\u0411\u0435\u0437 \u043e\u0431\u0432\u043e\u0434\u043a\u0438", None))
        self.comboBoxStroke.setItemText(2, QCoreApplication.translate("StylePluginDialogBase", u"\u0428\u0442\u0440\u0438\u0445\u043e\u0432\u0430\u044f", None))
        self.comboBoxStroke.setItemText(3, QCoreApplication.translate("StylePluginDialogBase", u"\u041f\u0443\u043d\u043a\u0442\u0438\u0440\u043d\u0430\u044f", None))
        self.comboBoxStroke.setItemText(4, QCoreApplication.translate("StylePluginDialogBase", u"\u0428\u0442\u0440\u0438\u0445\u043f\u0443\u043d\u043a\u0442\u0438\u0440\u043d\u0430\u044f", None))
        self.comboBoxStroke.setItemText(5, QCoreApplication.translate("StylePluginDialogBase", u"\u0428\u0442\u0440\u0438\u0445\u043f\u0443\u043d\u043a\u0442\u0438\u0440\u043d\u0430\u044f \u0441 \u0434\u0432\u0443\u043c\u044f \u0442\u043e\u0447\u043a\u0430\u043c\u0438", None))

        self.labelStroke_2.setText(QCoreApplication.translate("StylePluginDialogBase", u"\u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u043e\u0431\u0432\u043e\u0434\u043a\u0438", None))
        self.labelFill.setText(QCoreApplication.translate("StylePluginDialogBase", u"\u0421\u0442\u0438\u043b\u044c \u0437\u0430\u043b\u0438\u0432\u043a\u0438", None))
        self.comboBoxFill.setItemText(0, QCoreApplication.translate("StylePluginDialogBase", u"\u0421\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u0430\u044f", None))
        self.comboBoxFill.setItemText(1, QCoreApplication.translate("StylePluginDialogBase", u"\u0411\u0435\u0437 \u0437\u0430\u043b\u0438\u0432\u043a\u0438", None))
        self.comboBoxFill.setItemText(2, QCoreApplication.translate("StylePluginDialogBase", u"\u0413\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u0430\u044f", None))
        self.comboBoxFill.setItemText(3, QCoreApplication.translate("StylePluginDialogBase", u"\u0412\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u0430\u044f", None))
        self.comboBoxFill.setItemText(4, QCoreApplication.translate("StylePluginDialogBase", u"\u041f\u0435\u0440\u0435\u043a\u0440\u0435\u0441\u0442\u043d\u0430\u044f", None))
        self.comboBoxFill.setItemText(5, QCoreApplication.translate("StylePluginDialogBase", u"\u041f\u0440\u044f\u043c\u0430\u044f \u0434\u0438\u0430\u0433\u043e\u043d\u0430\u043b\u044c\u043d\u0430\u044f", None))
        self.comboBoxFill.setItemText(6, QCoreApplication.translate("StylePluginDialogBase", u"\u041e\u0431\u0440\u0430\u0442\u043d\u0430\u044f \u0434\u0438\u0430\u0433\u043e\u043d\u0430\u043b\u044c\u043d\u0430\u044f", None))
        self.comboBoxFill.setItemText(7, QCoreApplication.translate("StylePluginDialogBase", u"\u0414\u0438\u0430\u0433\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0435 \u043f\u0435\u0440\u0435\u043a\u0440\u0435\u0441\u0442\u0438\u0435", None))
        self.comboBoxFill.setItemText(8, QCoreApplication.translate("StylePluginDialogBase", u"\u0428\u0442\u0440\u0438\u0445\u043e\u0432\u043a\u0430 1", None))
        self.comboBoxFill.setItemText(9, QCoreApplication.translate("StylePluginDialogBase", u"\u0428\u0442\u0440\u0438\u0445\u043e\u0432\u043a\u0430 2", None))
        self.comboBoxFill.setItemText(10, QCoreApplication.translate("StylePluginDialogBase", u"\u0428\u0442\u0440\u0438\u0445\u043e\u0432\u043a\u0430 3", None))
        self.comboBoxFill.setItemText(11, QCoreApplication.translate("StylePluginDialogBase", u"\u0428\u0442\u0440\u0438\u0445\u043e\u0432\u043a\u0430 4", None))
        self.comboBoxFill.setItemText(12, QCoreApplication.translate("StylePluginDialogBase", u"\u0428\u0442\u0440\u0438\u0445\u043e\u0432\u043a\u0430 5", None))
        self.comboBoxFill.setItemText(13, QCoreApplication.translate("StylePluginDialogBase", u"\u0428\u0442\u0440\u0438\u0445\u043e\u0432\u043a\u0430 6", None))
        self.comboBoxFill.setItemText(14, QCoreApplication.translate("StylePluginDialogBase", u"\u0428\u0442\u0440\u0438\u0445\u043e\u0432\u043a\u0430 7", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("StylePluginDialogBase", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0441\u0442\u0438\u043b\u044f", None))
        self.geometryLabel.setText(QCoreApplication.translate("StylePluginDialogBase", u"\u041d\u0435\u0432\u0435\u0440\u043d\u044b\u0439 \u0442\u0438\u043f \u0433\u0435\u043e\u043c\u0435\u0442\u0440\u0438\u0438", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("StylePluginDialogBase", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("StylePluginDialogBase", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("StylePluginDialogBase", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0433\u0435\u043e\u043c\u0435\u0442\u0440\u0438\u0438", None))
    # retranslateUi

