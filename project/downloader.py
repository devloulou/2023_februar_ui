from PySide6.QtWidgets import QMainWindow, QWidget, QApplication, QVBoxLayout, QPushButton
from PySide6.QtGui import QAction

from meta_downloader.helpers import APIHelper
from meta_downloader import MovieBrowser


class MetaDownloader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Meta Downloader")
        self.resize(400, 300)
        # self.showMaximized()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # margó beállítása a layouton
        main_layout.setContentsMargins(0, 0, 0, 0)

        menu = self.menuBar()
        action_menu = menu.addMenu("Downloader")

        add_folder_action = QAction("Add folder", action_menu)
        action_menu.addAction(add_folder_action)

        add_popular_movies = QAction("Add Popular Movies", action_menu)
        action_menu.addAction(add_popular_movies)

        add_folder_action.triggered.connect(self.fnc_add_folder)
        add_popular_movies.triggered.connect(self.fnc_add_popular_movies)

        self.movie_browser = MovieBrowser()
        main_layout.addWidget(self.movie_browser)


    def fnc_add_folder(self):
        print("Megkattintottam az Add folder menüt")

    def fnc_add_popular_movies(self):
        print("Megkattintottam az Add Popular Movies menüt")

if __name__ == '__main__':
    app = QApplication([])
    win = MetaDownloader()
    win.show()
    app.exec()