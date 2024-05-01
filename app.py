import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Weather App')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.location_input = QLineEdit()
        layout.addWidget(self.location_input)

        self.get_weather_button = QPushButton('Get Weather')
        self.get_weather_button.clicked.connect(self.get_weather)
        layout.addWidget(self.get_weather_button)

        self.weather_label = QLabel()
        layout.addWidget(self.weather_label)

        self.setLayout(layout)

        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
            }
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #cccccc;
                padding: 5px;
            }
            QPushButton {
                background-color: #4CAF50;
                border: none;
                color: white;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QLabel {
                color: #333333;
                font-size: 16px;
            }
        """)

    def get_weather(self):
        location = self.location_input.text()
        if not location:
            QMessageBox.warning(self, 'Warning', 'Please enter a location.')
            return

        api_key = 'e317aeb2e793f4a0831b141cb7f637b6'  # Replace with your API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'

        try:
            response = requests.get(url)
            data = response.json()

            if data['cod'] == 200:
                weather_info = f"Weather in {location}: {data['weather'][0]['description']}, Temperature: {data['main']['temp']}°C"
                self.weather_label.setText(weather_info)
            else:
                QMessageBox.warning(self, 'Error', f'Error fetching weather data: {data["message"]}')
        except Exception as e:
            QMessageBox.warning(self, 'Error', f'An error occurred: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())
