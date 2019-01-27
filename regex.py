import re
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QPushButton, QFileDialog, qApp
from testqt5 import Ui_MainWindow
from regex_entry import Ui_regexEntry
from replace_entry import Ui_replaceEntry


class AppWindow(QMainWindow, Ui_MainWindow):
    regex = []
    filename = ""
    replacement = []

    def __init__(self, parent=None):
        super(AppWindow, self).__init__(parent)
        qApp.installEventFilter(self)
        self.setupUi(self)
        self.show()
        self.regexdialog = RegexWindow()
        self.replacedialog = ReplaceWindow()

    def clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        AppWindow.filename, extension_filter = QFileDialog.getOpenFileName()
        print(AppWindow.filename)
        self.textLog.append("Selected File Name: " + AppWindow.filename)
        self.regexdialog.exec()
        self.textLog.append("You entered the following regular expressions:")
        for i in self.regex:
            self.textLog.append("> " + i)
        self.replacedialog.exec()
        self.textLog.append("You entered the following replacement terms:")
        for i in range(0,len(self.regex)):
            self.textLog.append(f"{self.regex[i]} with {self.replacement[i]}")

    def replaceall(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        filename = AppWindow.filename
        regex = AppWindow.regex
        replacement = AppWindow.replacement
        regex_this(filename, regex, replacement)


class RegexWindow(QDialog, Ui_regexEntry):
    def __init__(self, parent=AppWindow):
        super(RegexWindow, self).__init__()
        self.setupUi(self)

    def accept(self):
        AppWindow.regex = self.plainTextEdit.toPlainText().split("\n")
        print("accepted")
        print(AppWindow.regex)
        self.close()
        super(RegexWindow, self).accept()   # call the accept method, as we're overwriting it

    def reject(self):
        print("declined")
        self.close()
        super(RegexWindow, self).reject()   # call the reject method, as we're overwriting it


class ReplaceWindow(QDialog, Ui_replaceEntry):
    def __init__(self, parent=AppWindow):
        super(ReplaceWindow, self).__init__()
        self.setupUi(self)

    def accept(self):
        AppWindow.replacement = self.plainTextEdit.toPlainText().split("\n")
        print("accepted")
        print(AppWindow.replacement)
        self.close()
        super(ReplaceWindow, self).accept()   # call the accept method, as we're overwriting it

    def reject(self):
        print("declined")
        self.close()
        super(ReplaceWindow, self).reject()   # call the reject method, as we're overwriting it

# def filename_prompt():
#        file_name = ""
#        while "." not in file_name or len(file_name) < 3:                               # to-do: replace with regEx
#            file_name = input("Please enter the name of your file.\n"
#                              "Files must have an extension and the name must be at least 3 characters long: ")
#        return file_name


# def regex_prompt():
#    regex = []
#    regex.append(input("Please enter your regular expression: "))
#    yes_no = input("Would you like to add another regular expression to apply?")
#    while yes_no.lower() not in {"n", "y"}:
#        yes_no = input("Please answer with 'n' or 'y': ")
#    while yes_no.lower() == "y":
#        regex.append(input("Please enter your regular expression: "))
#        yes_no = input("Would you like to add another regular expression to apply?")
#    print(f"You've entered {len(regex)} regular expression(s).")
#    return regex


# def replacement_prompt(regex):
#    replacement = []
#    for expression in regex:
#        replacement.append(input(f"Please enter what you'd like to replace {expression} with: "))
#    return replacement


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
                replacements_done = replacements_done + 1   # to-do: figure out how to get rid of this count variable
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
    # regex = regex_prompt()
    # replacement = replacement_prompt(regex)
    # regex_this(filename, regex, replacement)


if __name__ == '__main__':
    main()
