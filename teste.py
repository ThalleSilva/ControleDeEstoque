import sys
from PyQt5 import QtWidgets, uic

class AuditoriaWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("auditoria.ui", self)  # Carrega a UI

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AuditoriaWindow()
    window.show()
    sys.exit(app.exec_())
