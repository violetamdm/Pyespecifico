import sys
from PyQt5.QtWidgets import QMainWindow, Q , QLabel, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'Meow'
        self.left = 500
        self.top = 500
        self.width = 500
        self.height = 300
        self.initUI()
 
    def initUI(self):
        #Titulo de la ventana:
        self.setWindowTitle(self.title)

        #self.setStyleSheet("background-color:yellow")
        #self.setStyleSheet("background-image:url(.\gato.png)")  ##### NO QUIERE FUNCIONAR
        #Tamaño de la ventana
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Crear texto nombre
        self.labelnombre = QLabel("Nombre" , self)
        self.labelnombre.move(20, 0)
        # Crear cuadro de texto para nombre
        self.textboxnombre = QLineEdit(self)
        self.textboxnombre.move(20, 30)
        self.textboxnombre.resize(200,30)

        # Crear texto para mensaje
        self.labelmensaje = QLabel("Mensaje" , self)
        self.labelmensaje.move(20, 70)

       # Crear cuadro de texto mensaje
        self.textboxmensaje = QLineEdit(self)
        self.textboxmensaje.move(20, 100)
        self.textboxmensaje.resize(300,100)

        # Crea un botón en la ventana
        self.button = QPushButton('Enviar', self)
        self.button.move(20,220)
        self.button.setStyleSheet("background-image:\gato.jpg")
        #self.button.setStyleSheet("background-color:red")

        # botón de conexión para funcionar on_click
        self.button.clicked.connect(self.on_click)
        self.show()

        self.imagen = QIcon() 
        self.imagen
 
    def on_click(self):
        textboxnombreValue = self.textboxnombre.text()
        textboxmensajeValue =  self.textboxmensaje.text()
        QMessageBox.question(self, 'Resumen', "Escribiste: \n" + "Nombre: \n" + textboxnombreValue + "Mensaje: \n" + textboxmensajeValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textboxnombre.setText("")
        self.textboxmensaje.setText("")
        diccionario = {"nombre":textboxnombreValue, "mensaje":textboxmensajeValue}
        send_code(message=textboxmensajeValue)
        return diccionario

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    
    #################################

 
