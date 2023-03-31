import os, sys
import pdb

def translate(bashFileName):
	os.system('./bash2py_file ' + bashFileName)

def helpx():
	print("Usage:\n./bash2py -d <dir_name>\n./bash2py -f <file_name>")
	exit
def main():
	#print len(sys.argv)
	if (len(sys.argv) != 3):
		helpx()
	option = sys.argv[1]
	if (option == '-f'):
		bashFileName = sys.argv[2]
		translate(bashFileName)
	elif(option == '-d'):
		rootdir = sys.argv[2]
		for dirname, subDirs, files in os.walk(rootdir):
			for f in files:
				if not f.endswith(".py"):
					bashFileName = os.path.join(dirname, f)
					translate(bashFileName)
	else:
		helpx()
	#writeInfoToStatsFile(totalLines, numFiles, cmdDict)

if __name__ == "__main__":
	main()
