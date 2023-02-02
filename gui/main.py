from gui_v1 import *
from playsound import playsound



#se hereda de la clase Ui_MainWindow #setupUI se encarga de generar la interfaz

class MainWindow (QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btn_config.clicked.connect(self.config)
        self.btn_menu.clicked.connect(self.sidebar)

    def sidebar(self):
        if self.frameizq.width() > 0:
            self.frameizq.setMaximumWidth(0)
            playsound('boing1.mp3')
        else:
            self.frameizq.setMaximumWidth(270)
            playsound('boing1.mp3')

    def config(self):
        print("UD esta en config!!!")
        
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    application = MainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    application.show()
    sys.exit(app.exec_())
