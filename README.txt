Current version: 2.0

Bash2py is a tool designed to automate the translation from Bash to Python.

WARNING: It is highly recommended that you backup any file/directory you wish to translate, before running bash2py on that file/directory.

Instructions for installation:

Download the latest version of this software from swag.uwaterloo.ca/bash2py

cd into the project

To setup, run this command:

	./install

Run bash2py in any of the following ways:

1. Using the front end interface to invoke bash2pyengine
	
	./bash2py -f <SCRIPT>
	./bash2py -d <DIRECTORY>
    ./bash2py <SCRIPT|DIRECTORY>

2. Invoking this engine directly

	./bash/bash2pyengine <SCRIPT>
	
<SCRIPT> is replaced by the name of the script you want to translate, and <DIRECTORY> is the name of the directory you want to recursively translate.

Bash2py will put the translated Python file in the same directory as the corresponding Bash file, with the same name, but with a .py extension.
	
Note: Bash2py is not perfect. You will have to review and edit the translated file by hand, to fix any errors that bash2py made in translation.
