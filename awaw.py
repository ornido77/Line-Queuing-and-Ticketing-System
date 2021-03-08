import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QTextDocument
from PyQt5.QtPrintSupport import QPrintPreviewWidget, QPrinter
from PyQt5.QtWidgets import QMainWindow, QApplication

html = """<html><body>%s</body></html>""" % """
<p><span style=" font-size:20pt; font-weight:600;">QTextEdit</span></p>
""" * 20

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.document = QTextDocument(self)
        self.document.setHtml(html)
        self.preview = QPrintPreviewWidget(self)
        self.preview.paintRequested.connect(self.handlePaintRequest)
        self.setCentralWidget(self.preview)

    def handlePaintRequest(self, printer):
        printer.setOrientation(QPrinter.Landscape)
        printer.setPageSize(QPrinter.A3)
        printer.setPageMargins(QMargin(0, 0, 0, 0))
        self.document.setPageSize(
            QtCore.QSizeF(printer.width(), printer.height()))
        self.document.print_(printer)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.setGeometry(600, 100, 1200, 800)
    window.show()
    sys.exit(app.exec_())