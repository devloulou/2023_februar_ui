import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from pdf_export_ui import Ui_Form
from PySide6.QtCore import QFileInfo
from PySide6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.printButton.clicked.connect(self.print_file)
        self.ui.previewButton.clicked.connect(self.preview_file)
        self.ui.exportButton.clicked.connect(self.export_pdf)

    def print_file(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintDialog(printer)

        if dialog.exec() == QPrintDialog.accepted:
            self.ui.textEdit.print_(printer)

    def preview_file(self):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintPreviewDialog(printer)

        dialog.paintRequested.connect(self.print_preview)

        dialog.exec()
    
    def print_preview(self, printer):
        self.ui.textEdit.print_(printer)

    def export_pdf(self):
        fn, _ = QFileDialog.getSaveFileName(self, "Export PDF")

        if fn != "":
            if QFileInfo(fn).suffix() == "":
                fn += '.pdf'
            
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(fn)
            self.ui.textEdit.document().print_(printer)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())