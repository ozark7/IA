import cv2
import os
import interfaz

user = "pepi"
dataPath = 'D:/UPC2024-2/IA/2 corte/reconocimientoFacial/data'  # Cambia a la ruta donde hayas almacenado Data
imagePaths = os.listdir(dataPath)
print('imagePaths=', imagePaths)
# reconocimiento de rostro

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
# Leyendo el modelo
face_recognizer.read('D:/UPC2024-2/IA/2 corte/reconocimientoFacial/modeloLBPHFace.xml')
def recognize():
    
    # ============================================================================
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # VIDEO CAMARA
    #cap = cv2.VideoCapture(f'D:/UPC2024-2/IA/2 corte/reconocimientoFacial/users/{user}.mp4')#USUARIOS EXISTENTES
    #cap = cv2.VideoCapture(f'D:/UPC2024-2/IA/2 corte/reconocimientoFacial/test/{user}.MP4')#PRUEBA
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Configuración de la ventana
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    screen_width = 1376  # Cambia según la resolución de tu pantalla
    screen_height = 768  # Cambia según la resolución de tu pantalla
    window_width = 600  # Ancho de la ventana de OpenCV
    window_height = 600  # Alto de la ventana de OpenCV

    # Calcula la posición para centrar la ventana
    pos_x = (screen_width - window_width) // 2
    pos_y = (screen_height - window_height) // 2

    # Mueve la ventana al centro
    cv2.resizeWindow('frame', window_width, window_height)
    cv2.moveWindow('frame', pos_x, pos_y)

    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()

        faces = faceClassif.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

        for (x, y, w, h) in faces:
            rostro = auxFrame[y:y + h, x:x + w]
            rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
            result = face_recognizer.predict(rostro)

            cv2.putText(frame, '{}'.format(result), (x, y - 5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)

            # LBPHFace
            if result[1] < 70:
                cv2.putText(frame, '{}'.format(imagePaths[result[0]]), (x, y - 25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            else:
                cv2.putText(frame, 'Desconocido', (x, y - 20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow('frame', frame)
        k = cv2.waitKey(1)
        if k == 27:
            
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recognize()
