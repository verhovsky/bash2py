Current version: 1.1

Bash2py is a tool designed to automate the translation from Bash to Python.

WARNING: It is highly recommended that you backup any file/directory you wish to translate, before running bash2py on that file/directory.

Instructions for installation:

Download and unzip the following zip file: https://bitbucket.org/mwexler/bash2py/get/v1.1.zip

cd into the project

To setup, run this command:

	./install

Run bash2py in either of the following two ways:

	
	./bash2py -f <SCRIPT>
	./bash2py -d <DIRECTORY>
	
<SCRIPT> is replaced by the name of the script you want to translate, and <DIRECTORY> is the name of the directory you want to recursively translate.

Bash2py will put the translated Python file in the same directory as the corresponding Bash file, with the same name, but with a .py extension.
	
Note: Bash2py is not perfect. You will have to review and edit the translated file by hand, to fix any errors that bash2py made in translation.
