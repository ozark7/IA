import sys
import reconocimientoScript
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
import interfazUsuario

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Interfaz con 4 botones")
        self.setGeometry(100, 100, 300, 200)

        # Centrar la ventana en la pantalla
        self.center_window()

        # Crear un layout vertical
        layout = QVBoxLayout()

        # Etiqueta que cambiará al presionar los botones
        self.label = QLabel("Presiona un botón", self)
        layout.addWidget(self.label)

        # Crear 4 botones
        self.button1 = QPushButton("INGRESAR", self)
        self.button2 = QPushButton("NUEVO USUARIO", self)
        self.button3 = QPushButton("Botón 3", self)
        self.button4 = QPushButton("Botón 4", self)

        # Conectar los botones a las funciones correspondientes
        self.button1.clicked.connect(self.on_button1_click)
        self.button2.clicked.connect(self.on_button2_click)
        self.button3.clicked.connect(self.on_button3_click)
        self.button4.clicked.connect(self.on_button4_click)

        # Agregar los botones al layout
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)

        # Establecer el layout en la ventana
        self.setLayout(layout)

    # Función para centrar la ventana en la pantalla
    def center_window(self):
        screen_geometry = QApplication.desktop().screenGeometry()
        window_geometry = self.geometry()
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        self.move(x, y)

    # Funciones para manejar los clics de los botones
    def on_button1_click(self):
        self.label.setText("Has presionado el Botón 1")
        self.hide()
        interfazUsuario.window()
        #reconocimientoScript.recognize()
        self.show()

    def on_button2_click(self):
        self.label.setText("Has presionado el Botón 2")
        self.hide()
        reconocimientoScript.recognize()
        self.show()

    def on_button3_click(self):
        self.label.setText("Has presionado el Botón 3")

    def on_button4_click(self):
        self.label.setText("Has presionado el Botón 4")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
