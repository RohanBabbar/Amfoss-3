from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QFileDialog, QWidget
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap
import os

class Gallery(QMainWindow):
    def __init__(self):
        super().__init__()
        background = QPixmap("assets/bg.jpeg") 
        background_label = QLabel(self)
        background_label.setPixmap(background)
        background_label.setGeometry(0, 0, 850, 600)

        self.initUI()
        
        image_folder = "/home/rohan/Poke-Search/Captures"  # Replace with the path to your folder
        image_paths = []

        for filename in os.listdir(image_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
                image_path = os.path.join(image_folder, filename)
                image_paths.append(image_path)

        # Initialize image slider variables
        self.image_paths = []
        self.current_image_index = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showNextImage)

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Pokemon")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setGeometry(50, 50, 700, 400)

        open_button = QPushButton("Open Images", self)
        open_button.clicked.connect(self.loadImages)
        open_button.setGeometry(50, 500, 120, 30)

        start_button = QPushButton("Start Slideshow", self)
        start_button.clicked.connect(self.startSlideshow)
        start_button.setGeometry(200, 500, 120, 30)

        stop_button = QPushButton("Stop Slideshow", self)
        stop_button.clicked.connect(self.stopSlideshow)
        stop_button.setGeometry(350, 500, 120, 30)

    def loadImages(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        image_folder = QFileDialog.getExistingDirectory(self, "Select Image Folder")
        if image_folder:
            self.image_paths = [os.path.join(image_folder, filename) for filename in os.listdir(image_folder) if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff'))]

    def showNextImage(self):
        if self.image_paths:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
            pixmap = QPixmap(self.image_paths[self.current_image_index])
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)

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
