import re
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QPushButton, QFileDialog, qApp, QErrorMessage
from regexMeGUI import Ui_MainWindow


class AppWindow(QMainWindow, Ui_MainWindow):
    regex = []                              # array to store regular expressions
    source_filename = ""                    # name of source file
    replacement = []                        # array to store replacement terms

    def __init__(self, parent=None):
        super(AppWindow, self).__init__(parent)
        qApp.installEventFilter(self)
        self.setupUi(self)
        self.show()

    def picksourcefile(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        AppWindow.source_filename, extension_filter = QFileDialog.getOpenFileName()     # sets source file name
        print(AppWindow.source_filename)
        self.textLog.append("Selected Source File: " + AppWindow.source_filename)

    def pickrulefile(self):                                         # TODO: add csv -> table functionality
        self.statusBar().showMessage(self.sender().text() + ' was pressed')
        AppWindow.rule_filename, extension_filter = QFileDialog.getOpenFileName()
        print(AppWindow.rule_filename)
        self.textLog.append("Selected Rule File: " + AppWindow.rule_filename)
        print(AppWindow.regex)
        print(AppWindow.replacement)

    def replaceall(self):
        self.statusBar().showMessage(self.sender().text() + ' was pressed')
        row_count = self.tableWidget.rowCount()                                         # checks how many rows there are
        for row in range(0, row_count):                                                 # for every row, checks first
                                                                                        # two columns:
            if self.tableWidget.item(row, 0) not in [None, ""]:                         # Is it empty or has never been
                                                                                        # touched? Then add it to the
                AppWindow.regex.append(self.tableWidget.item(row, 0).text())            # matching array. Else don't.
            if self.tableWidget.item(row, 1) not in [None, ""]:                         # ("") is important to include
                AppWindow.replacement.append(self.tableWidget.item(row, 1).text())      # because previously filled
        print(AppWindow.regex)                                                          # cells are "", not None
        print(AppWindow.replacement)
        filename = AppWindow.source_filename
        regex = AppWindow.regex
        replacement = AppWindow.replacement
        if filename == "":
            self.textLog.append("No source file selected. Please select a source file.")
            return
        if not regex:
            self.textLog.append("No regular expressions found. Please enter at least one regular expression")
            return
        if not replacement:
            self.textLog.append("No replacements found.")
            return
        regex_this(filename, regex, replacement)

    def cleartable(self):
        self.tableWidget.clearContents()
        self.textLog.append("Table cleared.")


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
                line_content = file_content_after           # not-to-do: load the entire file into one variable.
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
