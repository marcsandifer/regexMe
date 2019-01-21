# to-do: add CSV functionality

import re


def filename_prompt():
    file_name = input("Please enter the name of your file: ")
    return file_name


def regex_prompt():
    regex = []
    regex_counter = 0
    regex.append(input("Please enter your regular expression: "))
    yes_no = input("Would you like to add another regular expression to apply?")
    while yes_no.lower() not in {"n", "y"}:
        yes_no = input("Please answer with 'n' or 'y': ")
    while yes_no.lower() == "y":
        regex.append(input("Please enter your regular expression: "))
        regex_counter = regex_counter + 1
        yes_no = input("Would you like to add another regular expression to apply?")
    print(f"You've entered {regex_counter + 1} regular expression(s).")
    return regex_counter, regex


def replacement_prompt(regex_counter, regex):
    replacement = []
    replacement_counter = 0
    while regex_counter >= 0:
        replacement.append(input(f"Please enter what you'd like to replace {regex[replacement_counter]} with: "))
        replacement_counter = replacement_counter + 1
        regex_counter = regex_counter - 1
    return replacement


def regex_this(file_name, regex, replacement, regex_counter):
    file_handler = open(file_name)
    file_content = file_handler.read()
    split_filename, split_extension = file_name.split(".")
    new_filename = (split_filename + "_processed." + split_extension)
    replacements_done = 0
    while regex_counter >= 0:
        print(f"Replacing {regex[replacements_done]} with {replacement[replacements_done]}")
        file_content_after = re.sub(regex[replacements_done], str(replacement[replacements_done]), file_content)
        regex_counter = regex_counter - 1
        replacements_done = replacements_done + 1
        file_handler.close()
        new_file = open(new_filename, "w+")
        new_file.write(file_content_after)
        new_file.close()
        file_content = file_content_after
    print("All replacement jobs applied successfully.")


def main():
    file_name = filename_prompt()
    regex_counter, regex = regex_prompt()
    replacement = replacement_prompt(regex_counter, regex)
    regex_this(file_name, regex, replacement, regex_counter)


if __name__ == '__main__':
    main()
