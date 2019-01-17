import re


def filename_prompt():
    filename = input("Please enter the name of your file: ")
    regex = input("Please enter your regular expression: ")
    replacement = input("Now, enter what to replace it with: ")
    return filename, regex, replacement

def regex_this(filename, regex, replacement):
    file = open(filename)
    file_content = file.read()
    print(file_content)
    file_content_after = re.sub(str(regex), str(replacement), file_content)
    file.close()
    new_filename = (filename+"_1")
    new_file = open(new_filename, "w")
    new_file.write(file_content_after)
    new_file.close()


def main():
    filename, regex, replacement = filename_prompt()
    regex_this(filename, regex, replacement)


if __name__ == '__main__':
    main()