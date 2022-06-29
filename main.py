# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QIODevice
from PySide2.QtCore import SIGNAL, QObject

import Window_Logic as WL
if __name__ == "__main__":
    app = QApplication([])
#    Basing on: https://doc.qt.io/qtforpython/tutorials/basictutorial/uifiles.html
    ui_file_name = "mainwindow.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()
    WindowManager = WL.GUI_Logic(window)

    sys.exit(app.exec_())
