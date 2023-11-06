from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap
from itertools import cycle


def button_style(button):
        button.setStyleSheet(
            "QPushButton {"
            "background-color: #222;"
            "background: linear-gradient(to right, red, purple);"
            "border: 2px solid red ;"
            "color: white;"
            "font-size: 16px;"
            "font-Weight: bold;"
            "padding: 5px 10px;"
            "border-radius: 15px;"
            "}"
            "QPushButton:hover {"
            "background: qlineargradient(to bottom, rgba(0, 0, 0, 0), red);"
            "background-color: #811331;"
            "color: black;"
            "}")

class Gallery(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.initUI()
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.image_label)
        background = QPixmap("assets/bg.jpeg") 
        background_label = QLabel(self)
        background_label.setPixmap(background)
        background_label.setGeometry(0, 0, 850, 500)
        #background
        

        #New Code
        # self.image_paths = []  
        # self.image_iterator = cycle(self.image_paths)  
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.nextImage)

        # open_button = QPushButton("Start Slideshow", self)
        # open_button.clicked.connect(self.startSlideshow)
        # open_button.setGeometry(10, 10, 120, 30)
        # button_style(open_button)
        # self.loadImages()  
        # self.loadNextImage()

        open_button = QPushButton("Previous", self)
        open_button.clicked.connect(self.openImage)
        open_button.setGeometry(80, 400, 220, 45)
        button_style(open_button)

        open_button = QPushButton("Next", self)
        open_button.clicked.connect(self.openImage)
        open_button.setGeometry(500, 400, 220, 45)
        button_style(open_button)
        # def loadImages(self):
            # Load image paths from a directory and populate self.image_paths
        # Replace this with your code to load images from a directory
        # For example, using os.listdir and checking file extensions
            # self.image_paths = ["image1.jpg", "image2.jpg", "image3.jpg"]

        # def loadNextImage(self):
        #     image_path = next(self.image_iterator)
        #     pixmap = QPixmap(image_path)
        #     self.image_label.setPixmap(pixmap)
        #     self.image_label.setScaledContents(True)
        # def startSlideshow(self):
        #     self.timer.start(2000)
        # def nextImage(self):
        #     self.loadNextImage()


    def initUI(self):
        self.setGeometry(0, 0, 800, 500)
        self.setWindowTitle("Image Viewer")

    def openImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.ppm *.xbm *.xpm);;All Files (*)", options=options)

        if file_path:
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)

def main():
    app = QApplication([])
    window = Gallery()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
