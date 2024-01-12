# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_line_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHeaderView, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_LineEditDialog(object):
    def setupUi(self, LineEditDialog):
        if not LineEditDialog.objectName():
            LineEditDialog.setObjectName(u"LineEditDialog")
        LineEditDialog.resize(328, 347)
        palette = QPalette()
        brush = QBrush(QColor(0, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        brush3 = QBrush(QColor(255, 255, 127, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush3)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        brush4 = QBrush(QColor(200, 151, 255, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Link, brush4)
        brush5 = QBrush(QColor(245, 220, 230, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush5)
        brush6 = QBrush(QColor(255, 185, 192, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        brush7 = QBrush(QColor(185, 167, 226, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
        brush8 = QBrush(QColor(255, 221, 252, 128))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        brush9 = QBrush(QColor(255, 0, 255, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush9)
        brush10 = QBrush(QColor(255, 170, 0, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        brush11 = QBrush(QColor(170, 255, 255, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush11)
        brush12 = QBrush(QColor(0, 255, 127, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush11)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush1)
        brush13 = QBrush(QColor(225, 255, 176, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush13)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        brush14 = QBrush(QColor(255, 170, 255, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        LineEditDialog.setPalette(palette)
        self.verticalLayout = QVBoxLayout(LineEditDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.coordsTable = QTableWidget(LineEditDialog)
        if (self.coordsTable.columnCount() < 2):
            self.coordsTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.coordsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.coordsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.coordsTable.setObjectName(u"coordsTable")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.coordsTable.setPalette(palette1)

        self.verticalLayout.addWidget(self.coordsTable)

        self.buttonBox = QDialogButtonBox(LineEditDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(LineEditDialog)
        self.buttonBox.accepted.connect(LineEditDialog.accept)
        self.buttonBox.rejected.connect(LineEditDialog.reject)

        QMetaObject.connectSlotsByName(LineEditDialog)
    # setupUi

    def retranslateUi(self, LineEditDialog):
        LineEditDialog.setWindowTitle(QCoreApplication.translate("LineEditDialog", u"Edit Line", None))
        ___qtablewidgetitem = self.coordsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("LineEditDialog", u"X", None));
        ___qtablewidgetitem1 = self.coordsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("LineEditDialog", u"Y", None));
    # retranslateUi

