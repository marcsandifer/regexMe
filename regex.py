import re
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QPushButton, QFileDialog, qApp
from testqt5 import Ui_MainWindow


class AppWindow(QMainWindow, Ui_MainWindow):
    regex = []
    filename = ""
    replacement = []

    def __init__(self, parent=None):
        super(AppWindow, self).__init__(parent)
        qApp.installEventFilter(self)
        self.setupUi(self)
        self.show()

    def clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        AppWindow.filename, extension_filter = QFileDialog.getOpenFileName()
        print(AppWindow.filename)
        self.textLog.append("Selected File Name: " + AppWindow.filename)
        row_count = self.tableWidget.rowCount()
        for row in range(0, row_count):
            if self.tableWidget.item(row, 0) is not None:
                AppWindow.regex.append(self.tableWidget.item(row, 0).text())
                AppWindow.replacement.append(self.tableWidget.item(row, 1).text())
        print(AppWindow.regex)
        print(AppWindow.replacement)

    def replaceall(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        filename = AppWindow.filename
        regex = AppWindow.regex
        replacement = AppWindow.replacement
        regex_this(filename, regex, replacement)


def regex_this(file_name, regex, replacement):
    split_filename, split_extension = file_name.split(".")
    new_filename = (split_filename + "_processed." + split_extension)
    new_file = open(new_filename, "w")
    with open(file_name, "r") as file_handler:
        line = file_handler.readline()
        while line:
            replacements_done = 0
            line_content = line
            for expression in regex:
                print(f"Replaced {expression} with {replacement[replacements_done]} in line: '{line_content}'")
                file_content_after = re.sub(regex[replacements_done], str(replacement[replacements_done]), line_content)
                line_content = file_content_after
                replacements_done = replacements_done + 1  # to-do: figure out how to get rid of this count variable
            new_file.write(file_content_after)
            line = file_handler.readline()
        file_handler.close()
    new_file.close()
    print("All replacement jobs applied successfully.")


def main():
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
