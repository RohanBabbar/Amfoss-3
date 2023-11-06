
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QApplication, QDialog
import requests
from PySide6.QtGui import QPixmap
from PySide6.QtGui import QPalette, QColor, QFont, QBrush
from Gallery import Gallery


# response = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
# print(response.status_code)
# print(response.json())
# data = response.json()
# name = data['name']
# pokemon_type = data['types']
# print("Name:", name)
# print("Type:", pokemon_type)


# abilities = [ability['ability']['name'] for ability in data['abilities']]
# print(f'Ability: {abilities}')

# types = [type_data['type']['name'] for type_data in data['types']]
# print(f'Type: {types}')
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
            "}"
        )

class SearchWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.pokemon_name = "" # Initialize the pokemon_name variable
        self.w = None        
        self.setFixedSize(850, 500)
        background = QPixmap("assets/landing.jpg") #background
        background_label = QLabel(self)
        background_label.setPixmap(background)

        self.pokemon_info_label = QLabel(self)   # Create a label for displaying Pokemon information
        self.pokemon_info_label.setGeometry(450, 250, 400, 240)  # Set label's position and size
        

        #Pokemon Image
        self.pokemon_pic = QLabel(self)
        self.pokemon_pic.setGeometry(350, -50, 400, 300)
        # self.pokemon_pic.setPixmap(pixmap.scaled(200, 200))

        #Pokemon Background
        self.poke_back = QLabel(self)
        self.poke_back.setGeometry(0, 0, 850, 500)
        
        
        # Set the position and size of the background label to cover the entire window
        background_label.setGeometry(0, 0, 850, 500)
        
        self.textbox = QLineEdit(self) #input box
        self.textbox.move(20, 20) 
        self.textbox.setGeometry(50, 50, 280, 40)
      
        
        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 5, 600, 70)
        

        font = QFont()
        font.setPointSize(16) 
        font.setBold(True)     
        label1.setFont(font)
        self.pokemon_info_label.setFont(font)

        palette = QPalette()
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))  # White color 

# Apply the palette to the QLabel
        label1.setPalette(palette)
        self.pokemon_info_label.setPalette(palette)

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)
        button_style(enter_button)
        
        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        button_style(capture_button)
        capture_button.clicked.connect(self.showPopup)

        # capture_button.clicked.connect(self.)
        # capture_button.setGeometry(10, 10, 120, 30)

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        button_style(display_button)

        enter_button.clicked.connect(self.search_pokemon)

        capture_button.clicked.connect(self.capture)

        display_button.clicked.connect(self.Gallery)
    
    def capture(self):
        pokemon_name = self.textbox.text().strip().lower()
        if pokemon_name:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/")
            if response.status_code == 200:
                data = response.json()
                sprite_url = data['sprites']['front_default']
                pixmap = QPixmap()
                pixmap.loadFromData(requests.get(sprite_url).content)
                pixmap = pixmap.scaled(400, 400)

                #image download
                pokemon_filename = f"Captures/{pokemon_name}.png"
                pixmap.save(pokemon_filename)
                print(f"Image for {pokemon_name} downloaded successfully!") 
                # self.file_name_label.setText(f"File Name: {pokemon_filename}")



                # pokemon_uuid = str(uuid.uuid4())  # Convert the UUID to a string
                # pokemon_filename = "Captures/" + pokemon_uuid + ".png"  # Add directory path and file extension
                # pixmap.save(pokemon_filename)
                # print("Image downloaded successfully!")

    def search_pokemon(self):
        pokemon_name = self.textbox.text().strip().lower()
        if pokemon_name:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/")
            if response.status_code == 200:
                print("OK")
                data = response.json()
                name = data['name'].capitalize()

                sprite_url = data['sprites']['front_default']
                pixmap = QPixmap()
                pixmap.loadFromData(requests.get(sprite_url).content)
                pixmap = pixmap.scaled(400, 400)  # Corrected line to assign the scaled pixmap
                
                

                abilities = [ability['ability']['name'] for ability in data['abilities']]
                abilities_str = ", ".join(abilities)

                # new_background_label = QLabel(self)
                # new_background = QPixmap("assets/bg.jpeg")
                
                # new_background_label.setGeometry(0, 0, 850, 500)


                types = [type_data['type']['name'] for type_data in data['types']]
                types_str = ", ".join(types)

                stats = data['stats']
                stats_info = '\n'.join([f"{stat['stat']['name'].capitalize()}: {stat['base_stat']}" for stat in stats])


                info_str = f"Name: {name}\nAbilities: {abilities_str}\nType(s): {types_str}\nStats:\n{stats_info}"
                self.pokemon_info_label.setText(info_str)
                self.pokemon_pic.setPixmap(pixmap)
    def Gallery(self):
        if self.w is None:
            self.w = Gallery()
        self.w.show()
    def showPopup(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("POKÉMON CAPTURED")
        msg.setWindowTitle("Popup")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()


    


    ## TO-DO ##

    # 1 #
    # Fetch the data from from the API.
    # Display the name, official artwork (image), abilities, types and stats when queried with a Pokémon name.
    # Add the background provided in assets

    # 2 #
    # Capture the Pokémon i.e. download the image.

    # 3 #
    # Display all the Pokémon captured with their respective names using a new window.

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
