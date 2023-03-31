 #!/usr/bin/env python

import sys

def readFile(inputFile):
	return data

def fixFile(filename):
	inputFileName = filename
	inputFile = open(inputFileName, "r")
	inputText=inputFile.read()
	inputFile.close()
	commentsFileName = "TEMP_COMMENTS"
	commentsFile = open(commentsFileName, "r")
	comments = commentsFile.readlines()
	commentsFile.close()
	#outputFileName = "output.py"
	outputFile = open(outputFileName, "w")
	#outputFile.truncate(0)
	for i in range(len(comments)-1, -1, -1):
		inputText = inputText.replace("BASH2PY_COMMENT_" + str(i), "#"+comments[i][:len(comments[i])-1])
	outputFile.write(inputText)
	outputFile.close()
	commentsFile.close()
	
if __name__ == "__main__":
	filename = 'output.py'
	outputFileName = sys.argv[1]
	fixFile(filename)

	
