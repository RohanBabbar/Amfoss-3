from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import os

def button_style(button):
        button.setStyleSheet(
            "QPushButton {"
            "background-color: #222;"
            "border: 1px solid red ;"
            "color: white;"
            "font-size: 16px;"
            "font-Weight: bold;"
            "padding: 5px 10px;"
            "border-radius: 20px;"
            "}"
            "QPushButton:hover {"
            "background-color: #811331;"
            "color: black;"
            "}"
        )

class Gallery(QMainWindow):
    def __init__(self):
        super().__init__()
        background = QPixmap("assets/bg.jpeg") 
        background_label = QLabel(self)
        background_label.setPixmap(background)
        background_label.setGeometry(0, 0, 850, 600)

        self.image_folder = "/home/rohan/Amfoss-3/Task8Captures"  
        self.image_paths = []
        self.image_names = []
        self.current_image_index = 0
        self.initUI()
        
        self.display_image(self.current_image_index)
        self.loadImages() 
        

        # for filename in os.listdir(self.image_folder):
        #     if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
        #         image_path = os.path.join(self.image_folder, filename)
        #         self.image_paths.append(image_path)
        

        # Initialize image slider variables

        # self.image_paths = []
        # self.current_image_index = 0
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.showNextImage)

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Pokemon")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setGeometry(50, 50, 700, 400)

        self.poke_name = QLabel(self)
        self.poke_name.setGeometry(100, 450, 180, 50)
        self.poke_name.setStyleSheet("color: white; font-size: 36px; font-weight: bold; text-transform: uppercase;")

        
        # open_button = QPushButton("Load Images", self)
        # open_button.clicked.connect(self.loadImages)
        # open_button.setGeometry(50, 500, 120, 30)

        start_button = QPushButton("Next Pokemon", self)
        start_button.clicked.connect(self.showNextImage)
        start_button.setGeometry(500, 500, 280, 28)
        button_style(start_button)
        
        

        stop_button = QPushButton("Previous Pokemon", self)
        stop_button.clicked.connect(self.showPreviousImage)
        stop_button.setGeometry(30, 500, 280, 28)
        button_style(stop_button)


    def loadImages(self):
        for filename in os.listdir(self.image_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
                image_path = os.path.join(self.image_folder, filename)
                self.image_paths.append(image_path)
                self.image_names.append(filename)                

    def display_image(self, index):
        if 0 <= index < len(self.image_paths):
            pixmap = QPixmap(self.image_paths[index])
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)

        if index < len(self.image_names):
            filename = self.image_names[index]
            filename = filename.split(".")[0]
            self.poke_name.setText(f"{filename}")

            

    def showNextImage(self):
        self.current_image_index += 1
        if self.current_image_index >= len(self.image_paths):
            self.current_image_index = 0
        self.display_image(self.current_image_index)

    def showPreviousImage(self):
        self.current_image_index -= 1
        if self.current_image_index < 0:
            self.current_image_index = len(self.image_paths) - 1
        self.display_image(self.current_image_index)



        # if self.image_paths:
        #     self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
        #     pixmap = QPixmap(self.image_paths[self.current_image_index])
        #     self.image_label.setPixmap(pixmap)
        #     self.image_label.setScaledContents(True)

    def startSlideshow(self):
        
        if self.image_paths:
            self.timer.start(2000)  # Change image every 2 seconds

    def stopSlideshow(self):
        self.timer.stop()

    

def main():
    app = QApplication([])
    window = Gallery()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
