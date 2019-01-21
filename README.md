## regexMe
"regexMe" is a script I'm writing as I learn Python. It serves a practical use, but should not be assumed to be even remotely bug free. Use it at your own risk.

## Who needs this?
I'm learning Python and started looking for real-world problems to solve. One such problem is that I frequently need to replace strings matching one or more regular expressions. Colleagues have mentioned that they frequently need to search and replace strings via Excel, which doesn't handle large file sizes well. I aim to make this a reliable solution for them as well.

## Features
I'm planning to add further features as I learn the language. 
At the moment, the script is quite simple:
1) It asks for a filename (file must be located in the same folder)
2) It then asks for at least one regular expression to apply.
3) For each entered expression, it asks the user for a replacement string.
4) It checks the file line by line (to save memory and allow for larger files) and replaces all strings matching the entered regular expressions with their respective replacement strings.
5) After applying all replacement jobs to a line, it writes the resulting new line into a new file named {your_original_file_name}_processed.{your_extension}.

## Limitations
- It can currently only read and write plain text files. I'm planning to add CSV support in the very near future.
- You will, without a doubt, be able to break this. If you're actually planning on using this on files you care about, make backups of those files. 

###### Last changed: 23:26 CET - Jan 21, 2018