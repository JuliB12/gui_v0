# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_v1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(836, 544)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#frameizq{\n"
"border-image: url(:/img/imagenes1/fondo bolita.png);\n"
"}\n"
"\n"
"#buscador_widget{\n"
"border-radius:10px;\n"
"border:2px solid #FF6A62;\n"
"}\n"
"\n"
"#parametro_widget{\n"
"border-radius:10px;\n"
"border:2px solid #FF6A62;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frameizq = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameizq.sizePolicy().hasHeightForWidth())
        self.frameizq.setSizePolicy(sizePolicy)
        self.frameizq.setMaximumSize(QtCore.QSize(270, 16777215))
        self.frameizq.setStyleSheet("*{\n"
"border:none;\n"
"}")
        self.frameizq.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameizq.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameizq.setLineWidth(0)
        self.frameizq.setObjectName("frameizq")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameizq)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logoizq_label = QtWidgets.QLabel(self.frameizq)
        self.logoizq_label.setMaximumSize(QtCore.QSize(16777215, 180))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        self.logoizq_label.setFont(font)
        self.logoizq_label.setStyleSheet("border-image: url(:/img/imagenes1/Recurso 1.png);")
        self.logoizq_label.setText("")
        self.logoizq_label.setTextFormat(QtCore.Qt.PlainText)
        self.logoizq_label.setObjectName("logoizq_label")
        self.verticalLayout_2.addWidget(self.logoizq_label)
        self.nombrecam_label = QtWidgets.QLabel(self.frameizq)
        self.nombrecam_label.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Sunrise Morning")
        font.setPointSize(63)
        self.nombrecam_label.setFont(font)
        self.nombrecam_label.setStyleSheet("")
        self.nombrecam_label.setObjectName("nombrecam_label")
        self.verticalLayout_2.addWidget(self.nombrecam_label)
        self.btn_config = QtWidgets.QPushButton(self.frameizq)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_config.setFont(font)
        self.btn_config.setStyleSheet("#btn_config {\n"
"border:2px solid #B5D9F7;  /*Color del borde*/\n"
"/*border-radius:20px; borde redondo*/\n"
"padding:5px; /*Expane el cuadro*/\n"
"text-align:center; /*centra el texto*/\n"
"border-top-left-radius:30px; /* borde superior del cuadro izq*/\n"
"border-top-right-radius:30px; /* borde superior del cuadro der*/\n"
"border-bottom-left-radius: 5px; /* borde inferior del cuadro der*/\n"
"border-bottom-right-radius: 5px;\n"
"border-style: dotted;\n"
"}\n"
"#btn_config:hover{ /* cambia de color cuando el mouse para por encima*/\n"
"background-color:#B5D9F7;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/iconos1/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_config.setIcon(icon)
        self.btn_config.setIconSize(QtCore.QSize(42, 32))
        self.btn_config.setObjectName("btn_config")
        self.verticalLayout_2.addWidget(self.btn_config)
        self.btn_ejecucion = QtWidgets.QPushButton(self.frameizq)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_ejecucion.setFont(font)
        self.btn_ejecucion.setStyleSheet("#btn_ejecucion {\n"
"border:2px solid #B5D9F7;  /*Color del borde*/\n"
"/*border-radius:20px; borde redondo*/\n"
"padding:5px; /*Expane el cuadro*/\n"
"text-align:center; /*centra el texto*/\n"
"border-top-left-radius:30px; /* borde superior del cuadro izq*/\n"
"border-top-right-radius:30px; /* borde superior del cuadro der*/\n"
"border-bottom-left-radius: 5px; /* borde inferior del cuadro der*/\n"
"border-bottom-right-radius: 5px;\n"
"border-style: dotted;\n"
"}\n"
"#btn_ejecucion:hover{ /* cambia de color cuando el mouse para por encima*/\n"
"background-color:#B5D9F7;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("iconos1/loader.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ejecucion.setIcon(icon1)
        self.btn_ejecucion.setIconSize(QtCore.QSize(42, 32))
        self.btn_ejecucion.setObjectName("btn_ejecucion")
        self.verticalLayout_2.addWidget(self.btn_ejecucion)
        self.btn_info = QtWidgets.QPushButton(self.frameizq)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_info.setFont(font)
        self.btn_info.setStyleSheet("#btn_info {\n"
"border:2px solid #B5D9F7;  /*Color del borde*/\n"
"/*border-radius:20px; borde redondo*/\n"
"padding:5px; /*Expane el cuadro*/\n"
"text-align:center; /*centra el texto*/\n"
"border-top-left-radius:30px; /* borde superior del cuadro izq*/\n"
"border-top-right-radius:30px; /* borde superior del cuadro der*/\n"
"border-bottom-left-radius: 5px; /* borde inferior del cuadro der*/\n"
"border-bottom-right-radius: 5px;\n"
"border-style: dotted;\n"
"}\n"
"#btn_info:hover{ /* cambia de color cuando el mouse para por encima*/\n"
"background-color:#B5D9F7;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("iconos1/info.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_info.setIcon(icon2)
        self.btn_info.setIconSize(QtCore.QSize(42, 32))
        self.btn_info.setObjectName("btn_info")
        self.verticalLayout_2.addWidget(self.btn_info)
        self.gridLayout_2.addWidget(self.frameizq, 0, 0, 1, 1)
        self.frameder = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameder.sizePolicy().hasHeightForWidth())
        self.frameder.setSizePolicy(sizePolicy)
        self.frameder.setStyleSheet("*{\n"
"border:none;\n"
"}")
        self.frameder.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameder.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameder.setLineWidth(1)
        self.frameder.setObjectName("frameder")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frameder)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.encabezado_widget = QtWidgets.QWidget(self.frameder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.encabezado_widget.sizePolicy().hasHeightForWidth())
        self.encabezado_widget.setSizePolicy(sizePolicy)
        self.encabezado_widget.setMaximumSize(QtCore.QSize(16777215, 60))
        self.encabezado_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.encabezado_widget.setObjectName("encabezado_widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.encabezado_widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.menu_widget = QtWidgets.QWidget(self.encabezado_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_widget.sizePolicy().hasHeightForWidth())
        self.menu_widget.setSizePolicy(sizePolicy)
        self.menu_widget.setMaximumSize(QtCore.QSize(90, 16777215))
        self.menu_widget.setStyleSheet("")
        self.menu_widget.setObjectName("menu_widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.menu_widget)
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_menu = QtWidgets.QPushButton(self.menu_widget)
        self.btn_menu.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_menu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_menu.setFont(font)
        self.btn_menu.setStyleSheet("#btn_menu {\n"
"border:2px solid #trasparent;  /*Color del borde*/\n"
"/*border-radius:20px; borde redondo*/\n"
"padding:3px; /*Expane el cuadro*/\n"
"text-align:center; /*centra el texto*/\n"
"border-top-left-radius:10px; /* borde superior del cuadro izq*/\n"
"border-top-right-radius:10px; /* borde superior del cuadro der*/\n"
"border-style: dotted;\n"
"}\n"
"#btn_menu:hover{ /* cambia de color cuando el mouse para por encima*/\n"
"background-color:#B5D9F7;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("iconos1/align-justify.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_menu.setIcon(icon3)
        self.btn_menu.setIconSize(QtCore.QSize(34, 34))
        self.btn_menu.setAutoDefault(False)
        self.btn_menu.setObjectName("btn_menu")
        self.horizontalLayout_5.addWidget(self.btn_menu)
        self.horizontalLayout_4.addWidget(self.menu_widget)
        spacerItem = QtWidgets.QSpacerItem(48, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.logos_widget = QtWidgets.QWidget(self.encabezado_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logos_widget.sizePolicy().hasHeightForWidth())
        self.logos_widget.setSizePolicy(sizePolicy)
        self.logos_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.logos_widget.setStyleSheet("")
        self.logos_widget.setObjectName("logos_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.logos_widget)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cam_label = QtWidgets.QLabel(self.logos_widget)
        self.cam_label.setMaximumSize(QtCore.QSize(70, 16777215))
        self.cam_label.setStyleSheet("border-image: url(:/img/imagenes1/Recurso 1.png);")
        self.cam_label.setText("")
        self.cam_label.setObjectName("cam_label")
        self.horizontalLayout_2.addWidget(self.cam_label)
        self.psi_label = QtWidgets.QLabel(self.logos_widget)
        self.psi_label.setMaximumSize(QtCore.QSize(120, 16777215))
        self.psi_label.setStyleSheet("border-image: url(:/img/imagenes1/logo psi.png);")
        self.psi_label.setText("")
        self.psi_label.setObjectName("psi_label")
        self.horizontalLayout_2.addWidget(self.psi_label)
        self.uv_label = QtWidgets.QLabel(self.logos_widget)
        self.uv_label.setMaximumSize(QtCore.QSize(40, 50))
        self.uv_label.setStyleSheet("border-image: url(:/img/imagenes1/logo uv.png);")
        self.uv_label.setText("")
        self.uv_label.setObjectName("uv_label")
        self.horizontalLayout_2.addWidget(self.uv_label)
        self.horizontalLayout_4.addWidget(self.logos_widget)
        spacerItem1 = QtWidgets.QSpacerItem(48, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.ctrl_enc_widget = QtWidgets.QWidget(self.encabezado_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctrl_enc_widget.sizePolicy().hasHeightForWidth())
        self.ctrl_enc_widget.setSizePolicy(sizePolicy)
        self.ctrl_enc_widget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.ctrl_enc_widget.setStyleSheet("")
        self.ctrl_enc_widget.setObjectName("ctrl_enc_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.ctrl_enc_widget)
        self.horizontalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_minimizar = QtWidgets.QPushButton(self.ctrl_enc_widget)
        self.btn_minimizar.setMaximumSize(QtCore.QSize(32, 32))
        self.btn_minimizar.setStyleSheet("#btn_minimizar {\n"
"border:2px solid #trasparent;  /*Color del borde*/\n"
"/*border-radius:20px; borde redondo*/\n"
"padding:3px; /*Expane el cuadro*/\n"
"text-align:center; /*centra el texto*/\n"
"border-top-left-radius:10px; /* borde superior del cuadro izq*/\n"
"border-top-right-radius:10px; /* borde superior del cuadro der*/\n"
"border-style: dotted;\n"
"}\n"
"#btn_minimizar:hover{ /* cambia de color cuando el mouse para por encima*/\n"
"background-color:#E6EEFF;\n"
"}")
        self.btn_minimizar.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("iconos1/minimize-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimizar.setIcon(icon4)
        self.btn_minimizar.setIconSize(QtCore.QSize(26, 28))
        self.btn_minimizar.setObjectName("btn_minimizar")
        self.horizontalLayout_3.addWidget(self.btn_minimizar)
        self.btn_expandir = QtWidgets.QPushButton(self.ctrl_enc_widget)
        self.btn_expandir.setMaximumSize(QtCore.QSize(32, 32))
        self.btn_expandir.setStyleSheet("#btn_expandir{\n"
"border:2px solid #trasparent;  /*Color del borde*/\n"
"/*border-radius:20px; borde redondo*/\n"
"padding:3px; /*Expane el cuadro*/\n"
"text-align:center; /*centra el texto*/\n"
"border-top-left-radius:10px; /* borde superior del cuadro izq*/\n"
"border-top-right-radius:10px; /* borde superior del cuadro der*/\n"
"border-style: dotted;\n"
"}\n"
"#btn_expandir:hover{ /* cambia de color cuando el mouse para por encima*/\n"
"background-color:#E6EEFF;\n"
"}")
        self.btn_expandir.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/iconos1/maximize-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_expandir.setIcon(icon5)
        self.btn_expandir.setIconSize(QtCore.QSize(26, 26))
        self.btn_expandir.setObjectName("btn_expandir")
        self.horizontalLayout_3.addWidget(self.btn_expandir)
        self.btn_cerrar = QtWidgets.QPushButton(self.ctrl_enc_widget)
        self.btn_cerrar.setMaximumSize(QtCore.QSize(32, 32))
        self.btn_cerrar.setStyleSheet("#btn_cerrar {\n"
"border:2px solid #trasparent;  /*Color del borde*/\n"
"/*border-radius:20px; borde redondo*/\n"
"padding:3px; /*Expane el cuadro*/\n"
"text-align:center; /*centra el texto*/\n"
"border-top-left-radius:10px; /* borde superior del cuadro izq*/\n"
"border-top-right-radius:10px; /* borde superior del cuadro der*/\n"
"border-style: dotted;\n"
"}\n"
"#btn_cerrar:hover{ /* cambia de color cuando el mouse para por encima*/\n"
"background-color:#F34F1B;\n"
"}")
        self.btn_cerrar.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("iconos1/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cerrar.setIcon(icon6)
        self.btn_cerrar.setIconSize(QtCore.QSize(26, 26))
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.horizontalLayout_3.addWidget(self.btn_cerrar)
        self.horizontalLayout_4.addWidget(self.ctrl_enc_widget)
        self.verticalLayout.addWidget(self.encabezado_widget)
        self.main_frame = QtWidgets.QWidget(self.frameder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setStyleSheet("background-color: rgb(255, 255, 255)\n"
"\n"
"")
        self.main_frame.setObjectName("main_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.main_frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.East)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName("tabWidget")
        self.config_tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.config_tab.sizePolicy().hasHeightForWidth())
        self.config_tab.setSizePolicy(sizePolicy)
        self.config_tab.setStyleSheet("#buscador_widget{\n"
"border:2px solid #B5D9F7;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"#parametro_widget{\n"
"border:2px solid #B5D9F7;\n"
"border-radius:20px\n"
"}\n"
"\n"
"#imgmuestra_widget{\n"
"border:2px solid #B5D9F7;\n"
"border-radius:20px\n"
"}\n"
"")
        self.config_tab.setObjectName("config_tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.config_tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.parametro_widget = QtWidgets.QWidget(self.config_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parametro_widget.sizePolicy().hasHeightForWidth())
        self.parametro_widget.setSizePolicy(sizePolicy)
        self.parametro_widget.setMaximumSize(QtCore.QSize(16777215, 250))
        self.parametro_widget.setObjectName("parametro_widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.parametro_widget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.btn_fr3 = QtWidgets.QRadioButton(self.parametro_widget)
        self.btn_fr3.setObjectName("btn_fr3")
        self.gridLayout_5.addWidget(self.btn_fr3, 0, 4, 1, 1)
        self.logofre_label = QtWidgets.QLabel(self.parametro_widget)
        self.logofre_label.setText("")
        self.logofre_label.setPixmap(QtGui.QPixmap(":/icon/iconos1/activity.svg"))
        self.logofre_label.setAlignment(QtCore.Qt.AlignCenter)
        self.logofre_label.setObjectName("logofre_label")
        self.gridLayout_5.addWidget(self.logofre_label, 0, 0, 1, 1)
        self.descrfre_label = QtWidgets.QLabel(self.parametro_widget)
        self.descrfre_label.setTextFormat(QtCore.Qt.RichText)
        self.descrfre_label.setObjectName("descrfre_label")
        self.gridLayout_5.addWidget(self.descrfre_label, 1, 0, 1, 5)
        self.namefrec_label = QtWidgets.QLabel(self.parametro_widget)
        self.namefrec_label.setObjectName("namefrec_label")
        self.gridLayout_5.addWidget(self.namefrec_label, 0, 1, 1, 1)
        self.btn_fr2 = QtWidgets.QRadioButton(self.parametro_widget)
        self.btn_fr2.setObjectName("btn_fr2")
        self.gridLayout_5.addWidget(self.btn_fr2, 0, 3, 1, 1)
        self.btn_guardar = QtWidgets.QPushButton(self.parametro_widget)
        self.btn_guardar.setStyleSheet("#btn_guardar{\n"
"background-color: rgba(210, 232, 250, 211);\n"
"border-radius: 10px;\n"
"border-style: dotted;\n"
"}\n"
"#btn_guardar:hover{ \n"
"background-color:#B5D9F7;\n"
"}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/iconos1/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_guardar.setIcon(icon7)
        self.btn_guardar.setIconSize(QtCore.QSize(32, 32))
        self.btn_guardar.setObjectName("btn_guardar")
        self.gridLayout_5.addWidget(self.btn_guardar, 3, 0, 1, 5)
        self.btn_fr1 = QtWidgets.QRadioButton(self.parametro_widget)
        self.btn_fr1.setObjectName("btn_fr1")
        self.gridLayout_5.addWidget(self.btn_fr1, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.parametro_widget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 2, 0, 1, 5)
        self.gridLayout_4.addWidget(self.parametro_widget, 0, 1, 1, 1)
        self.imgmuestra_widget = QtWidgets.QWidget(self.config_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgmuestra_widget.sizePolicy().hasHeightForWidth())
        self.imgmuestra_widget.setSizePolicy(sizePolicy)
        self.imgmuestra_widget.setObjectName("imgmuestra_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.imgmuestra_widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.imgmuestra_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_3.addWidget(self.widget)
        self.imgvidselect_label = QtWidgets.QLabel(self.imgmuestra_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgvidselect_label.sizePolicy().hasHeightForWidth())
        self.imgvidselect_label.setSizePolicy(sizePolicy)
        self.imgvidselect_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.imgvidselect_label.setFont(font)
        self.imgvidselect_label.setStyleSheet("#imgvidselect_label{\n"
"background-color: rgba(210, 232, 250, 211);\n"
"border-radius: 10px;\n"
"border-style: dotted;\n"
"}")
        self.imgvidselect_label.setAlignment(QtCore.Qt.AlignCenter)
        self.imgvidselect_label.setObjectName("imgvidselect_label")
        self.verticalLayout_3.addWidget(self.imgvidselect_label)
        self.gridLayout_4.addWidget(self.imgmuestra_widget, 1, 0, 1, 2)
        self.buscador_widget = QtWidgets.QWidget(self.config_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buscador_widget.sizePolicy().hasHeightForWidth())
        self.buscador_widget.setSizePolicy(sizePolicy)
        self.buscador_widget.setMaximumSize(QtCore.QSize(250, 250))
        self.buscador_widget.setStyleSheet("")
        self.buscador_widget.setObjectName("buscador_widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.buscador_widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_buscador = QtWidgets.QPushButton(self.buscador_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_buscador.setFont(font)
        self.btn_buscador.setStyleSheet("#btn_buscador{\n"
"border:2px solid rgba(210, 232, 250, 211);  \n"
"\n"
"border-style: dotted;\n"
"border-radius: 10px;\n"
"border-style: dotted;\n"
"}\n"
"#btn_buscador:hover{ \n"
"background-color: rgba(181, 217, 247, 116);\n"
"}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/iconos1/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_buscador.setIcon(icon8)
        self.btn_buscador.setIconSize(QtCore.QSize(26, 26))
        self.btn_buscador.setObjectName("btn_buscador")
        self.gridLayout_3.addWidget(self.btn_buscador, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.buscador_widget)
        self.label_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icon/iconos1/archive.svg"))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.nombrefold_lineEdit = QtWidgets.QLineEdit(self.buscador_widget)
        self.nombrefold_lineEdit.setObjectName("nombrefold_lineEdit")
        self.gridLayout_3.addWidget(self.nombrefold_lineEdit, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.buscador_widget)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/icon/iconos1/hard-drive.svg"))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.dirfold_lineEdit = QtWidgets.QLineEdit(self.buscador_widget)
        self.dirfold_lineEdit.setObjectName("dirfold_lineEdit")
        self.gridLayout_3.addWidget(self.dirfold_lineEdit, 2, 1, 1, 1)
        self.btn_visualizador = QtWidgets.QPushButton(self.buscador_widget)
        self.btn_visualizador.setStyleSheet("#btn_visualizador{\n"
"background-color: rgba(210, 232, 250, 211);\n"
"border-radius: 10px;\n"
"border-style: dotted;\n"
"}\n"
"\n"
"#btn_visualizador:hover{ \n"
"background-color:#B5D9F7;\n"
"}")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("iconos1/eye.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_visualizador.setIcon(icon9)
        self.btn_visualizador.setIconSize(QtCore.QSize(42, 42))
        self.btn_visualizador.setObjectName("btn_visualizador")
        self.gridLayout_3.addWidget(self.btn_visualizador, 3, 0, 1, 2)
        self.gridLayout_4.addWidget(self.buscador_widget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.config_tab, icon, "")
        self.ejecucion_tab = QtWidgets.QWidget()
        self.ejecucion_tab.setStyleSheet("#tray_widget{\n"
"border:2px solid #B5D9F7;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"#imgder_widget{\n"
"border:2px solid #B5D9F7;\n"
"border-radius:20px\n"
"}\n"
"\n"
"#imgizq_widget{\n"
"border:2px solid #B5D9F7;\n"
"border-radius:20px\n"
"}")
        self.ejecucion_tab.setObjectName("ejecucion_tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.ejecucion_tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_3 = QtWidgets.QLabel(self.ejecucion_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 13))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 7, 0, 1, 5)
        self.widget_2 = QtWidgets.QWidget(self.ejecucion_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.imgizq_widget = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgizq_widget.sizePolicy().hasHeightForWidth())
        self.imgizq_widget.setSizePolicy(sizePolicy)
        self.imgizq_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.imgizq_widget.setObjectName("imgizq_widget")
        self.horizontalLayout_6.addWidget(self.imgizq_widget)
        self.imgder_widget = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgder_widget.sizePolicy().hasHeightForWidth())
        self.imgder_widget.setSizePolicy(sizePolicy)
        self.imgder_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.imgder_widget.setObjectName("imgder_widget")
        self.horizontalLayout_6.addWidget(self.imgder_widget)
        self.gridLayout_6.addWidget(self.widget_2, 1, 0, 1, 5)
        self.label_5 = QtWidgets.QLabel(self.ejecucion_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(130, 18))
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 2, 1, 1, 1)
        self.tray_widget = QtWidgets.QWidget(self.ejecucion_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tray_widget.sizePolicy().hasHeightForWidth())
        self.tray_widget.setSizePolicy(sizePolicy)
        self.tray_widget.setObjectName("tray_widget")
        self.gridLayout_6.addWidget(self.tray_widget, 6, 0, 1, 5)
        self.ctrltray_widget = QtWidgets.QWidget(self.ejecucion_tab)
        self.ctrltray_widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.ctrltray_widget.setObjectName("ctrltray_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ctrltray_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(190, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_play = QtWidgets.QPushButton(self.ctrltray_widget)
        self.btn_play.setStyleSheet("#btn_play{\n"
"background-color: rgba(210, 232, 250, 211);\n"
"border-radius: 10px;\n"
"border-style: dotted;\n"
"}\n"
"#btn_play:hover{ \n"
"background-color:#B5D9F7;\n"
"}")
        self.btn_play.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icon/iconos1/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_play.setIcon(icon10)
        self.btn_play.setIconSize(QtCore.QSize(36, 36))
        self.btn_play.setObjectName("btn_play")
        self.horizontalLayout.addWidget(self.btn_play)
        self.btn_resume = QtWidgets.QPushButton(self.ctrltray_widget)
        self.btn_resume.setStyleSheet("#btn_resume{\n"
"background-color: rgba(210, 232, 250, 211);\n"
"border-radius: 10px;\n"
"border-style: dotted;\n"
"}\n"
"#btn_resume:hover{ \n"
"background-color:#B5D9F7;\n"
"}")
        self.btn_resume.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icon/iconos1/pause.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_resume.setIcon(icon11)
        self.btn_resume.setIconSize(QtCore.QSize(36, 36))
        self.btn_resume.setObjectName("btn_resume")
        self.horizontalLayout.addWidget(self.btn_resume)
        self.btn_stop = QtWidgets.QPushButton(self.ctrltray_widget)
        self.btn_stop.setStyleSheet("#btn_stop{\n"
"background-color: rgba(210, 232, 250, 211);\n"
"border-radius: 10px;\n"
"border-style: dotted;\n"
"}\n"
"#btn_stop:hover{ \n"
"background-color:#B5D9F7;\n"
"}")
        self.btn_stop.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icon/iconos1/square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_stop.setIcon(icon12)
        self.btn_stop.setIconSize(QtCore.QSize(36, 36))
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout.addWidget(self.btn_stop)
        spacerItem3 = QtWidgets.QSpacerItem(189, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout_6.addWidget(self.ctrltray_widget, 8, 0, 1, 5)
        self.label_6 = QtWidgets.QLabel(self.ejecucion_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QtCore.QSize(130, 18))
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 2, 3, 1, 1)
        self.tabWidget.addTab(self.ejecucion_tab, icon1, "")
        self.info_tab = QtWidgets.QWidget()
        self.info_tab.setStyleSheet("#error_widget{\n"
"border:2px solid #B5D9F7;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"#trayfinal_widget{\n"
"border:2px solid #B5D9F7;\n"
"border-radius:20px\n"
"}")
        self.info_tab.setObjectName("info_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.info_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_expinfo = QtWidgets.QPushButton(self.info_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_expinfo.sizePolicy().hasHeightForWidth())
        self.btn_expinfo.setSizePolicy(sizePolicy)
        self.btn_expinfo.setStyleSheet("#btn_expinfo {\n"
"border:2px solid #B5D9F7;  /*Color del borde*/\n"
"background-color:#E6EEFF;\n"
"border-radius:20px; \n"
"text-align:center; /*centra el texto*/\n"
"\n"
"\n"
"}\n"
"#btn_expinfo:hover{ /* cambia de color cuando el mouse para por encima*/\n"
"background-color:#B5D9F7;\n"
"}")
        self.btn_expinfo.setIcon(icon2)
        self.btn_expinfo.setIconSize(QtCore.QSize(20, 20))
        self.btn_expinfo.setObjectName("btn_expinfo")
        self.verticalLayout_4.addWidget(self.btn_expinfo)
        self.trayfinal_widget = QtWidgets.QWidget(self.info_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trayfinal_widget.sizePolicy().hasHeightForWidth())
        self.trayfinal_widget.setSizePolicy(sizePolicy)
        self.trayfinal_widget.setObjectName("trayfinal_widget")
        self.verticalLayout_4.addWidget(self.trayfinal_widget)
        self.label_10 = QtWidgets.QLabel(self.info_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 14))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.error_widget = QtWidgets.QWidget(self.info_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_widget.sizePolicy().hasHeightForWidth())
        self.error_widget.setSizePolicy(sizePolicy)
        self.error_widget.setObjectName("error_widget")
        self.verticalLayout_4.addWidget(self.error_widget)
        self.label_9 = QtWidgets.QLabel(self.info_tab)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 13))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icon/iconos1/info.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.info_tab, icon13, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.main_frame)
        self.gridLayout_2.addWidget(self.frameder, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.btn_cerrar.clicked.connect(MainWindow.close)
        self.btn_expandir.clicked.connect(MainWindow.showMaximized)
        self.btn_minimizar.clicked.connect(MainWindow.showNormal)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nombrecam_label.setText(_translate("MainWindow", "Camvision"))
        self.btn_config.setText(_translate("MainWindow", "Configuracion "))
        self.btn_ejecucion.setText(_translate("MainWindow", "Ejecucion "))
        self.btn_info.setText(_translate("MainWindow", "Informacion "))
        self.btn_menu.setText(_translate("MainWindow", "Menu"))
        self.btn_fr3.setText(_translate("MainWindow", "50"))
        self.descrfre_label.setText(_translate("MainWindow", "La frecuencia varia la velocidad de las imagenes."))
        self.namefrec_label.setText(_translate("MainWindow", "Frecuencia img:"))
        self.btn_fr2.setText(_translate("MainWindow", "100"))
        self.btn_guardar.setText(_translate("MainWindow", "Guardar"))
        self.btn_fr1.setText(_translate("MainWindow", "200"))
        self.imgvidselect_label.setText(_translate("MainWindow", "Imagen-Video seleccionado"))
        self.btn_buscador.setText(_translate("MainWindow", "buscador folder"))
        self.nombrefold_lineEdit.setPlaceholderText(_translate("MainWindow", "Nombre folder"))
        self.dirfold_lineEdit.setPlaceholderText(_translate("MainWindow", "Direccion folder"))
        self.btn_visualizador.setText(_translate("MainWindow", "Visualizar"))
        self.label_3.setText(_translate("MainWindow", "Estimacion de la trayectoria"))
        self.label_5.setText(_translate("MainWindow", "imagen izquierda"))
        self.label_6.setText(_translate("MainWindow", "imagen derecha"))
        self.btn_expinfo.setText(_translate("MainWindow", "Exportar información"))
        self.label_10.setText(_translate("MainWindow", "Trayectoria recorrida"))
        self.label_9.setText(_translate("MainWindow", "Curva de error"))
import iconos
import imagenes


"""if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())"""
