import os

from PySide6.QtWidgets import (QWidget,
                               QListWidget,
                               QVBoxLayout,
                               QProgressBar,
                               QPushButton)

from PySide6.QtCore import QThread, Signal

class MovieBrowser(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        self.progress_bar = QProgressBar()
        # amíg nem indul el a letöltés, addig ez maradjon láthatatlan
        self.progress_bar.setVisible(False)
        main_layout.addWidget(self.progress_bar)

        self.movie_list = MovieList()
        main_layout.addWidget(self.movie_list)

        self.movie_list.movie_downloader.download_started.connect(self.start_progress)
        self.movie_list.movie_downloader.download_progress.connect(self.download_progress)
        self.movie_list.movie_downloader.download_progress_finished.connect(self.progress_bar.setVisible)

    def start_progress(self, movie_list_length):
        self.progress_bar.setMaximum(movie_list_length)
        self.progress_bar.setValue(0)
        self.progress_bar.setVisible(True)

    def download_progress(self, download_data):
        self.progress_bar.setValue(download_data['Downloading'])
        self.progress_bar.setFormat(download_data['Movie'])


class MovieList(QListWidget):

    def __init__(self):
        super().__init__()

        self.movie_downloader = DownloadWorker()
        # letöltésnek itt kell megtörténnie
        # a letöltött adatokból itt kellene objektumokat létrehozni
        # és folyamatosan hozzáadni a list widgethez az objektumokat
        self.movie_downloader.download_finished.connect(self.update_movie_list)

    def update_movie_list(self, movie_object):
        print(f"valami: {movie_object}")

    def start_downloader(self):
        self.movie_downloader.start()

class DownloadWorker(QThread):
    download_started = Signal(int)
    download_finished = Signal(object)

    download_progress = Signal(dict)
    download_progress_finished = Signal(bool)

    def __init__(self):
        super().__init__()
        self.file_list = ["Ricsi", "Roland", "Karcsi", "Matil", "Jolán"]

    def run(self):
        import time
        self.download_started.emit(len(self.file_list))
        for idx, item in enumerate(self.file_list):
            self.download_progress.emit({"Downloading": idx, "Movie": f"{item}"})
            # itt kell majd "ténylegesen" az API letöltést elondítani

            self.download_finished.emit(item)
            time.sleep(2)

        self.download_progress_finished.emit(False)



if __name__ == '__main__':
    print()