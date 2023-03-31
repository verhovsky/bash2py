 #!/usr/bin/env python

import re, sys

arithmeticExpansionPattern = r'\$\((\(.*\))\)'   #maybe this should be more precise... cannot handle $((1+2+3(((4+3)+2)+1)) +3)
argumentPattern=r'\$(\d+)'
rangePatternNoStep=r' \{(\w+)\.\.(\w+)\}'
rangePatternStep=r' \{(\w+)\.\.(\w+)\.\.(\w+)\}'
quotedNumberPattern = r'"(\d+)"'
backticksPattern = r'`(.*?)`'
evalPattern = r'\$\((.*?)\)'
varPattern = r'\$([a-zA-Z_]\w*)'
bracketVarPattern = r'\$\{([a-zA-Z_]\w*)\}'
squareBracketPattern = r'\$\[(.*?)\]'
quotedVarPattern = r'(\$\{*\w*\}*)'
quotedPattern = r'"[^"]*"'
quotedSingleVarPattern = r'\"\$([a-zA-Z_]\w*?)\"'

errorMsg = "TRANSLATION_ERROR"

argFile = 'temp_file'
logFile = 'python_log_file'

def fixQuotedSection(matchObj):
	x = matchObj.group(0)
	replStr = r'" + str(\1) + "'
	output = re.sub(quotedVarPattern, replStr, x)
	return output

#This will fix any string with quoted sections... and will separate out any dollar signed variables, to avoid string interpolation
def fixQuotedStr(x):
	output = re.sub(quotedPattern, fixQuotedSection, x)
	output = output.replace('"" +', '')
	output = output.replace('+ ""', '')
	return output
	
def fixQuotedStrDummy(x):
	output = re.sub(quotedPattern, 'A', x)
	return output
	
def fixQuotedSingleVarStr(x):
	replStr = r'\1'
	output = re.sub(quotedSingleVarPattern, replStr, x)
	return output

def fixSquareBrackets(x):
	replStr = r'\1'
	output = re.sub(squareBracketPattern, replStr, x)
	return output

def fixBackticksAndEval(x):
	replStr = r" os.popen('\1').read() "
	output = re.sub(backticksPattern, replStr, x)
	output = re.sub(evalPattern, replStr, output)
	return output

def fixArguments(x):
	replStr = r"sys.argv[\1]"
	output = re.sub(argumentPattern, replStr, x)
	return output

def fixVariables(x):
	replStr = r"\1"
	output = re.sub(varPattern, replStr, x)
	return output

def fixBracketVariables(x):
	replStr = r"\1"
	output = re.sub(bracketVarPattern, replStr, x)
	return output

def fixArithmeticExpansion(x):
	replStr = r"\1"
	output = re.sub(arithmeticExpansionPattern, replStr, x)
	return output

def getInput():
	with open (argFile, "r") as myfile:
		data=myfile.read()
	return data

def writeToOutputFile(output):
	with open(argFile, "w") as text_file:
		text_file.write(output)
		
def writeToLogFile(output):
	with open(logFile, "a") as text_file:
		text_file.write(output + "\n")

def isQuoted(input):
	return input[0] == '"' and input[len(input)-1] == '"'

def fixRange(x):
	output = x
	matchNoStep = re.search(rangePatternNoStep, output)
	matchStep = re.search(rangePatternStep, output)
	replNoStep = r'range(\1, \2)'
	replStep = r'range(\1, \2, \3)'
	if matchNoStep != None:
		output = re.sub(rangePatternNoStep, replNoStep, output)
	if matchStep != None:
		output = re.sub(rangePatternStep, replStep, output)
	return output

def fixString(x):
	output = x.strip()
	if (len(output) < 2):
		return output
	#order matters here
	output = fixArithmeticExpansion(output)
	output = fixQuotedStr(output)   # should come early, to separate out all dollar signed variables
	output = fixBackticksAndEval(output)
	output = fixArguments(output)
	output = fixBracketVariables(output)
	output = fixVariables(output)
	output = fixRange(output)
	output = fixSquareBrackets(output)
	return output

def main():
	input = getInput()
	output = fixString(input)
	writeToOutputFile(output)
	writeToLogFile(output)

if __name__ == '__main__':
	main()
