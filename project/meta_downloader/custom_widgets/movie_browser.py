import os

from PySide6.QtWidgets import (QWidget, QVBoxLayout, QProgressBar, QPushButton)


class MovieBrowser(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        self.progress_bar = QProgressBar()
        # amíg nem indul el a letöltés, addig ez maradjon láthatatlan
        self.progress_bar.setVisible(False)
        main_layout.addWidget(self.progress_bar)
