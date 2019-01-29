## regexMe
"regexMe" is a script I'm writing as I learn Python. It serves a practical use, but should not be assumed to be even remotely bug free. Use it at your own risk.

## Who needs this?
I'm learning Python and started looking for real-world problems to solve. One such problem is that I frequently need to replace strings matching one or more regular expressions. Colleagues have mentioned that they frequently need to search and replace strings via Excel, which doesn't handle large file sizes well. I aim to make this a reliable solution for them as well.

## Features
I'm planning to add further features as I learn the language. 
At the moment, the script works as follows: 
* You can select a source file.
    * Only plaintext files are supported at the moment. CSV support will be added shortly.
* You can select a rule file to import your regular expressions and replacements from.
    * Oh wait, you can't. The button is there but the script currently does nothing with the file. This will be added 
    shortly. Instead:
* You can enter your regular expressions and replacement terms directly into the table.
    * Up to 50 pairs are supported right now.
* There is very basic input validation. 
    
## Limitations 
- It can currently only read and write plain text files. I'm planning to add CSV support in the very near future.
- You will, without a doubt, be able to break this. If you're actually planning on using this on files you care about, make backups of those files. 

###### Last changed: 22:55 CET - Jan 29, 2018