# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_point_dialog.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_PointEditDialog(object):
    def setupUi(self, PointEditDialog):
        if not PointEditDialog.objectName():
            PointEditDialog.setObjectName(u"PointEditDialog")
        PointEditDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(PointEditDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.xInputHorizontalLayout = QHBoxLayout()
        self.xInputHorizontalLayout.setObjectName(u"xInputHorizontalLayout")
        self.xLabel = QLabel(PointEditDialog)
        self.xLabel.setObjectName(u"xLabel")
        font = QFont()
        font.setPointSize(13)
        self.xLabel.setFont(font)

        self.xInputHorizontalLayout.addWidget(self.xLabel)

        self.xLineEdit = QLineEdit(PointEditDialog)
        self.xLineEdit.setObjectName(u"xLineEdit")

        self.xInputHorizontalLayout.addWidget(self.xLineEdit)


        self.verticalLayout.addLayout(self.xInputHorizontalLayout)

        self.yInputHorizontalLayout = QHBoxLayout()
        self.yInputHorizontalLayout.setObjectName(u"yInputHorizontalLayout")
        self.yLabel = QLabel(PointEditDialog)
        self.yLabel.setObjectName(u"yLabel")
        font1 = QFont()
        font1.setPointSize(11)
        self.yLabel.setFont(font1)

        self.yInputHorizontalLayout.addWidget(self.yLabel)

        self.yLineEdit = QLineEdit(PointEditDialog)
        self.yLineEdit.setObjectName(u"yLineEdit")

        self.yInputHorizontalLayout.addWidget(self.yLineEdit)


        self.verticalLayout.addLayout(self.yInputHorizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(PointEditDialog)
        self.buttonBox.setObjectName(u"buttonBox")
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
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush1)
        brush3 = QBrush(QColor(225, 255, 176, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush3)
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
        brush9 = QBrush(QColor(255, 170, 255, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        brush10 = QBrush(QColor(255, 0, 255, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush10)
        brush11 = QBrush(QColor(255, 170, 0, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush11)
        brush12 = QBrush(QColor(255, 255, 127, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush12)
        brush13 = QBrush(QColor(170, 255, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush13)
        brush14 = QBrush(QColor(0, 255, 127, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush14)
        brush15 = QBrush(QColor(255, 85, 127, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush15)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush13)
        brush16 = QBrush(QColor(255, 0, 127, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush16)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush12)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush13)
        brush17 = QBrush(QColor(0, 120, 215, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush17)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.buttonBox.setPalette(palette)
        self.buttonBox.setFont(font1)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(PointEditDialog)
        self.buttonBox.accepted.connect(PointEditDialog.accept)
        self.buttonBox.rejected.connect(PointEditDialog.reject)

        QMetaObject.connectSlotsByName(PointEditDialog)
    # setupUi

    def retranslateUi(self, PointEditDialog):
        PointEditDialog.setWindowTitle(QCoreApplication.translate("PointEditDialog", u"Edit Point", None))
        self.xLabel.setText(QCoreApplication.translate("PointEditDialog", u"X", None))
        self.yLabel.setText(QCoreApplication.translate("PointEditDialog", u"Y", None))
    # retranslateUi

