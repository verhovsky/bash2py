import os, sys
import pdb

def translate(bashFileName):
	os.system('bash/bash2pyengine ' + bashFileName)

def helpx():
	print("Usage:\n./bash2py -d <dir_name>\n./bash2py -f <file_name>\n./bash2py <name>\n")

def main():

	option = ' '
	if (len(sys.argv) == 2):
		bashFileName = sys.argv[1]
		if (os.path.isdir(bashFileName)) :
			option = '-d'
		else :
			option = '-f'
	elif (len(sys.argv) == 3):
		option = sys.argv[1]
		bashFileName = sys.argv[2]

	if (option == '-f'):
		translate(bashFileName)
		exit
		
	if(option == '-d'):
		for dirname, subDirs, files in os.walk(bashFileName):
			for f in files:
				if not f.endswith(".py"):
					bashFileName1 = os.path.join(dirname, f)
					translate(bashFileName1)
		exit

	helpx()

if __name__ == "__main__":
	main()
