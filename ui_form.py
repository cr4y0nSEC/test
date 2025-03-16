# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTabWidget, QTextBrowser,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(922, 572)
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 611, 391))
        font = QFont()
        font.setBold(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setStyleSheet(u"QTabBar::tab {\n"
"    width: 200px;\n"
"    height: 130px;\n"
"    font-size: 14px; \n"
"    text-align: center; \n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: rgb(250, 250, 250); \n"
"}")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"QWidget{\n"
"    background: rgb(250, 250, 250);      \n"
"}\n"
"")
        self.pushButton_5 = QPushButton(self.tab)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(90, 250, 201, 71))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #a8c4ff, stop:1 #7aaaff);\n"
"\n"
"    border-radius: 5px;\n"
"    border: 2px solid #6a9cfd; \n"
"    color: white;\n"
"    font: bold 14px;\n"
"    padding: 10px 20px;\n"
"    box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #b8d4ff, stop:1 #8abaff);\n"
"    border: 2px solid #7aaaff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #7aaaff, stop:1 #a8c4ff);\n"
"    box-shadow: inset 2px 2px 5px rgba(0, 0, 0, 0.3);\n"
"}")
        self.pushButton_6 = QPushButton(self.tab)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(90, 130, 201, 71))
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #a8c4ff, stop:1 #7aaaff);\n"
"\n"
"    border-radius: 5px;\n"
"    border: 2px solid #6a9cfd; \n"
"    color: white;\n"
"    font: bold 14px;\n"
"    padding: 10px 20px;\n"
"    box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #b8d4ff, stop:1 #8abaff);\n"
"    border: 2px solid #7aaaff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #7aaaff, stop:1 #a8c4ff);\n"
"    box-shadow: inset 2px 2px 5px rgba(0, 0, 0, 0.3);\n"
"}")
        self.pushButton_14 = QPushButton(self.tab)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(230, 50, 111, 31))
        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 50, 151, 31))
        self.lineEdit.setStyleSheet(u"            QLineEdit {\n"
"                background-color: #f0f0f0;\n"
"                border: 2px solid #8f8f91;\n"
"                border-radius: 5px;\n"
"                padding: 5px;\n"
"                color: #333;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border-color: #0078d4;\n"
"                background-color: #ffffff;\n"
"            }")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"QWidget{\n"
"    background: rgb(250, 250, 250);      \n"
"}\n"
"")
        self.pushButton_8 = QPushButton(self.tab_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(220, 40, 111, 31))
        self.pushButton_9 = QPushButton(self.tab_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(220, 100, 111, 31))
        self.pushButton_10 = QPushButton(self.tab_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(220, 160, 111, 31))
        self.label_18 = QLabel(self.tab_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(360, 282, 20, 20))
        self.label_18.setStyleSheet(u"QLabel {\n"
"    background-color: red;\n"
"    border-radius: 10px; \n"
"\n"
"}")
        self.pushButton_15 = QPushButton(self.tab_2)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(40, 260, 201, 71))
        self.pushButton_15.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #a8c4ff, stop:1 #7aaaff);\n"
"\n"
"    border-radius: 5px;\n"
"    border: 2px solid #6a9cfd; \n"
"    color: white;\n"
"    font: bold 14px;\n"
"    padding: 10px 20px;\n"
"    box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #b8d4ff, stop:1 #8abaff);\n"
"    border: 2px solid #7aaaff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #7aaaff, stop:1 #a8c4ff);\n"
"    box-shadow: inset 2px 2px 5px rgba(0, 0, 0, 0.3);\n"
"}")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 282, 69, 19))
        self.lineEdit_2 = QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(50, 40, 151, 31))
        self.lineEdit_3 = QLineEdit(self.tab_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(50, 100, 151, 31))
        self.lineEdit_4 = QLineEdit(self.tab_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(50, 160, 151, 31))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setStyleSheet(u"QWidget{\n"
"    background: rgb(250, 250, 250);      \n"
"}\n"
"")
        self.label_21 = QLabel(self.tab_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(360, 290, 20, 20))
        self.label_21.setStyleSheet(u"QLabel {\n"
"    background-color: red;\n"
"    border-radius: 10px; \n"
"\n"
"}")
        self.pushButton_29 = QPushButton(self.tab_3)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setGeometry(QRect(210, 130, 111, 31))
        self.pushButton_30 = QPushButton(self.tab_3)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setGeometry(QRect(40, 260, 201, 71))
        self.pushButton_30.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #a8c4ff, stop:1 #7aaaff);\n"
"\n"
"    border-radius: 5px;\n"
"    border: 2px solid #6a9cfd; \n"
"    color: white;\n"
"    font: bold 14px;\n"
"    padding: 10px 20px;\n"
"    box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #b8d4ff, stop:1 #8abaff);\n"
"    border: 2px solid #7aaaff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #7aaaff, stop:1 #a8c4ff);\n"
"    box-shadow: inset 2px 2px 5px rgba(0, 0, 0, 0.3);\n"
"}")
        self.label_7 = QLabel(self.tab_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(260, 290, 69, 19))
        self.pushButton_31 = QPushButton(self.tab_3)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setGeometry(QRect(210, 70, 111, 31))
        self.lineEdit_5 = QLineEdit(self.tab_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(40, 70, 151, 31))
        self.lineEdit_6 = QLineEdit(self.tab_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(40, 130, 151, 31))
        self.tabWidget.addTab(self.tab_3, "")
        self.pushButton_11 = QPushButton(Widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(10, 490, 201, 71))
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"    /* \u80cc\u666f\u6e10\u53d8 - \u6de1\u84dd\u8272 */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #a3d8f4, stop:1 #72c3f2);\n"
"\n"
"    border-radius: 5px;\n"
"    border: 2px solid #5cb0e6;  /* \u6de1\u84dd\u8272\u8fb9\u6846 */\n"
"    color: white;\n"
"    font: bold 14px;\n"
"    padding: 10px 20px;\n"
"    box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u6e10\u53d8 - \u66f4\u4eae\u7684\u6de1\u84dd\u8272 */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #b3e2f8, stop:1 #82d3f6);\n"
"    border: 2px solid #72c3f2;  /* \u60ac\u505c\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u6e10\u53d8 - \u53cd\u8f6c\u6de1\u84dd\u8272 */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                sto"
                        "p:0 #72c3f2, stop:1 #a3d8f4);\n"
"    box-shadow: inset 2px 2px 5px rgba(0, 0, 0, 0.3);\n"
"}")
        self.pushButton_12 = QPushButton(Widget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(340, 490, 201, 71))
        self.pushButton_12.setStyleSheet(u"QPushButton {\n"
"    /* \u80cc\u666f\u6e10\u53d8 - \u6de1\u84dd\u8272 */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #a3d8f4, stop:1 #72c3f2);\n"
"\n"
"    border-radius: 5px;\n"
"    border: 2px solid #5cb0e6;  /* \u6de1\u84dd\u8272\u8fb9\u6846 */\n"
"    color: white;\n"
"    font: bold 14px;\n"
"    padding: 10px 20px;\n"
"    box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u6e10\u53d8 - \u66f4\u4eae\u7684\u6de1\u84dd\u8272 */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #b3e2f8, stop:1 #82d3f6);\n"
"    border: 2px solid #72c3f2;  /* \u60ac\u505c\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u6e10\u53d8 - \u53cd\u8f6c\u6de1\u84dd\u8272 */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                sto"
                        "p:0 #72c3f2, stop:1 #a3d8f4);\n"
"    box-shadow: inset 2px 2px 5px rgba(0, 0, 0, 0.3);\n"
"}")
        self.pushButton_13 = QPushButton(Widget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(660, 490, 201, 71))
        self.pushButton_13.setStyleSheet(u"QPushButton {\n"
"    /* \u80cc\u666f\u6e10\u53d8 - \u6de1\u7ea2\u8272 */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #ff8a80, stop:1 #ff5252);\n"
"\n"
"    border-radius: 5px;\n"
"    border: 2px solid #ff1744;  /* \u6de1\u7ea2\u8272\u8fb9\u6846 */\n"
"    color: white;\n"
"    font: bold 14px;\n"
"    padding: 10px 20px;\n"
"    box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u6e10\u53d8 - \u66f4\u4eae\u7684\u6de1\u7ea2\u8272 */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #ff9e80, stop:1 #ff6e6e);\n"
"    border: 2px solid #ff5252;  /* \u60ac\u505c\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u6e10\u53d8 - \u53cd\u8f6c\u6de1\u7ea2\u8272 */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                sto"
                        "p:0 #ff5252, stop:1 #ff8a80);\n"
"    box-shadow: inset 2px 2px 5px rgba(0, 0, 0, 0.3);\n"
"}")
        self.label_10 = QLabel(Widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 420, 91, 20))
        self.label_11 = QLabel(Widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 460, 81, 19))
        self.label_12 = QLabel(Widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(700, 440, 69, 19))
        self.label_13 = QLabel(Widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(390, 440, 69, 19))
        self.label_14 = QLabel(Widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(140, 420, 20, 20))
        self.label_14.setStyleSheet(u"QLabel {\n"
"    background-color: red;\n"
"    border-radius: 10px; \n"
"}")
        self.label_15 = QLabel(Widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(140, 460, 20, 20))
        self.label_15.setStyleSheet(u"QLabel {\n"
"    background-color: red;\n"
"    border-radius: 10px; \n"
"\n"
"}")
        self.label_16 = QLabel(Widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(790, 440, 20, 20))
        self.label_16.setStyleSheet(u"QLabel {\n"
"    background-color: red;\n"
"    border-radius: 10px; \n"
"\n"
"}")
        self.label_17 = QLabel(Widget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(470, 440, 20, 20))
        self.label_17.setStyleSheet(u"QLabel {\n"
"    background-color: red;\n"
"    border-radius: 10px; \n"
"\n"
"}")
        self.graphicsView_2 = QGraphicsView(Widget)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(630, 10, 281, 181))
        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(640, 215, 69, 19))
        self.label_6 = QLabel(Widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(640, 265, 69, 19))
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(640, 315, 69, 19))
        self.textBrowser_9 = QTextBrowser(Widget)
        self.textBrowser_9.setObjectName(u"textBrowser_9")
        self.textBrowser_9.setGeometry(QRect(720, 310, 170, 29))
        self.textBrowser_10 = QTextBrowser(Widget)
        self.textBrowser_10.setObjectName(u"textBrowser_10")
        self.textBrowser_10.setGeometry(QRect(720, 260, 170, 29))
        self.textBrowser_8 = QTextBrowser(Widget)
        self.textBrowser_8.setObjectName(u"textBrowser_8")
        self.textBrowser_8.setGeometry(QRect(720, 210, 170, 29))

        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButton_5.setText(QCoreApplication.translate("Widget", u"\u4e0b\u964d", None))
        self.pushButton_6.setText(QCoreApplication.translate("Widget", u"\u4e0a\u5347", None))
        self.pushButton_14.setText(QCoreApplication.translate("Widget", u"\u70b9\u51fb\u8bbe\u5b9a\u901f\u5ea6", None))
        self.lineEdit.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"\u70b9\u52a8\u6a21\u5f0f", None))
        self.pushButton_8.setText(QCoreApplication.translate("Widget", u"\u8fd0\u884c\u901f\u5ea6", None))
        self.pushButton_9.setText(QCoreApplication.translate("Widget", u"\u4e0a\u5347\u8ddd\u79bb", None))
        self.pushButton_10.setText(QCoreApplication.translate("Widget", u"\u4e0b\u964d\u8ddd\u79bb", None))
        self.label_18.setText("")
        self.pushButton_15.setText(QCoreApplication.translate("Widget", u"\u63a5\u8fd1", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u63a5\u8fd1\u72b6\u6001", None))
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"\u8ddd\u79bb\u6a21\u5f0f", None))
        self.label_21.setText("")
        self.pushButton_29.setText(QCoreApplication.translate("Widget", u"\u538b\u529b\u8bbe\u7f6e", None))
        self.pushButton_30.setText(QCoreApplication.translate("Widget", u"\u63a5\u8fd1", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"\u63a5\u8fd1\u72b6\u6001", None))
        self.pushButton_31.setText(QCoreApplication.translate("Widget", u"\u8fd0\u884c\u901f\u5ea6", None))
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Widget", u"\u538b\u529b\u6a21\u5f0f", None))
        self.pushButton_11.setText(QCoreApplication.translate("Widget", u"\u521d\u59cb\u5316", None))
        self.pushButton_12.setText(QCoreApplication.translate("Widget", u"\u56de\u539f", None))
        self.pushButton_13.setText(QCoreApplication.translate("Widget", u"\u6025\u505c", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"\u4e0a\u9650\u4f4d\u8b66\u544a", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"\u4e0b\u9650\u4f4d\u8b66\u544a", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"\u6025\u505c\u72b6\u6001", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"\u56de\u539f\u72b6\u6001", None))
        self.label_14.setText("")
        self.label_15.setText("")
        self.label_16.setText("")
        self.label_17.setText("")
        self.label_5.setText(QCoreApplication.translate("Widget", u"\u5b9e\u65f6\u4f4d\u7f6e", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"\u5b9e\u65f6\u538b\u529b", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u5b9e\u65f6\u901f\u5ea6", None))
    # retranslateUi

