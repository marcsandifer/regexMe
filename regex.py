import re


def filename_prompt():
        file_name = ""
        while "." not in file_name or len(file_name) < 3:                               # to-do: replace with regEx
            file_name = input("Please enter the name of your file.\n" 
                              "Files must have an extension and the name must be at least 3 characters long: ")
        return file_name


def regex_prompt():
    regex = []
    regex.append(input("Please enter your regular expression: "))
    yes_no = input("Would you like to add another regular expression to apply?")
    while yes_no.lower() not in {"n", "y"}:
        yes_no = input("Please answer with 'n' or 'y': ")
    while yes_no.lower() == "y":
        regex.append(input("Please enter your regular expression: "))
        yes_no = input("Would you like to add another regular expression to apply?")
    print(f"You've entered {len(regex)} regular expression(s).")
    return regex


def replacement_prompt(regex):
    replacement = []
    for expression in regex:
        replacement.append(input(f"Please enter what you'd like to replace {expression} with: "))
    return replacement


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
    file_name = filename_prompt()
    regex = regex_prompt()
    replacement = replacement_prompt(regex)
    regex_this(file_name, regex, replacement)


if __name__ == '__main__':
    main()
