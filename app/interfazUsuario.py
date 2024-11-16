import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ProfileWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Perfil de Usuario")
        self.setGeometry(100, 100, 300, 300)
        
        # Centrar la ventana
        self.center_window()

        # Layout principal
        layout = QVBoxLayout()

        # Imagen de perfil
        self.profile_image = QLabel(self)
        self.profile_image.setPixmap(QPixmap('path_to_image.jpg').scaled(100, 100, Qt.KeepAspectRatio))  # Asegúrate de poner la ruta correcta de la imagen
        self.profile_image.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.profile_image)

        # Información del usuario
        self.username_label = QLabel("Nombre de Usuario: Pepi", self)
        layout.addWidget(self.username_label)

        self.email_label = QLabel("Correo: pepi@example.com", self)
        layout.addWidget(self.email_label)

        self.bio_label = QLabel("Bio: Entusiasta de la IA y el terror.", self)
        layout.addWidget(self.bio_label)

        # Botón de edición
        self.edit_button = QPushButton("Editar Perfil", self)
        self.edit_button.clicked.connect(self.on_edit_click)
        layout.addWidget(self.edit_button)

        # Establecer el layout en la ventana
        self.setLayout(layout)

    def center_window(self):
        screen_geometry = QApplication.desktop().screenGeometry()
        window_geometry = self.geometry()
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        self.move(x, y)

    def on_edit_click(self):
        # Lógica para editar el perfil
        self.username_label.setText("Nombre de Usuario: Editado")
        self.email_label.setText("Correo: editado@example.com")
        self.bio_label.setText("Bio: Nueva bio editada.")
        self.edit_button.setText("Guardar Cambios")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProfileWindow()
    window.show()
    sys.exit(app.exec_())
