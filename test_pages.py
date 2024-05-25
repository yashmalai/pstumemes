import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # Основной макет
        self.layout = QVBoxLayout()
        
        # Кнопки для переключения между страницами
        self.button1 = QPushButton('Go to Page 1')
        self.button2 = QPushButton('Go to Page 2')
        self.button3 = QPushButton('Go to Page 3')
        
        self.button1.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        self.button2.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        self.button3.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        
        # QStackedWidget для хранения страниц
        self.stacked_widget = QStackedWidget()
        
        # Создание страниц
        self.page1 = QWidget()
        self.page1_layout = QVBoxLayout()
        self.page1_layout.addWidget(QPushButton('This is Page 1'))
        self.page1.setLayout(self.page1_layout)
        
        self.page2 = QWidget()
        self.page2_layout = QVBoxLayout()
        self.page2_layout.addWidget(QPushButton('This is Page 2'))
        self.page2.setLayout(self.page2_layout)
        
        self.page3 = QWidget()
        self.page3_layout = QVBoxLayout()
        self.page3_layout.addWidget(QPushButton('This is Page 3'))
        self.page3.setLayout(self.page3_layout)
        
        # Добавление страниц в QStackedWidget
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)
        
        # Добавление QStackedWidget в основной макет
        self.layout.addWidget(self.stacked_widget)
        
        # Установка основного макета
        self.setLayout(self.layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
