#got inspiration from here: http://stackoverflow.com/questions/17791143/removing-hash-comments-that-are-not-inside-quotes

#commentExpr = r'(?:"[^"]*"|\'[^\']*\'|\{[^\}]*\}|\([^\)]*\)|\\\#|\$\#|\#\!|\#\*|\#\@|[^\"\#\'\(\)\{\}])*((?<!(\\|\$))#(?!(\!|\*|\@)))'

commentExpr = r'''
				  (?:                            # Non-capturing group
				  "[^"]*"                        # A double-quote, followed by not-double-quotes, followed by a double quote
				  |           					 # or
				  \'[^\']*\' 					 # A single quote, followed by not-single-quotes, followed by a single quote
				  |
				  \{[^}]*\}  					 # An opening curly brackets, followed by not-closing curly bracket,  followed by a closing curly bracket
				  |
				  \([^\)]*\)  					 # Etc. for parenthesis
				  |
				  \\\#   						 # Blackslash hash
				  |
				  \$\#   						 # Dollar hash
				  |
				  \#\!                           # Hash followed by exclamation point
				  |
				  \#\*  						 # Hash followed by star
				  |
				  \#\@  						 # Hash followed by at sign
				  |
				  [^\#"'{(]     # stuff to exclude. should i include hash here?
				  )*    						 # Match any number of this big group... consume as much as possible
				  ((?<!(\\|\$))\#(?!(\!|\*|\@)))  # For the final character, try to match a hash that is not proceeded nor followed by forbidden character, using negative lookahead/behind
				  '''
				  
'''
				  |
				  [^\#\}\{]   			 # Anything that is NOT a quote, hash, parenthesis, etc.
				  
'''
#[^\"\#\'\}\)\{\(]

import sys, re
import pdb

def makeTempComments(filename):
	inputFileName = filename
	inputFile = open(inputFileName, "r")
	lines=inputFile.readlines()
	inputFile.close()
	outputFileName = "FILE_TO_TRANSLATE"
	outputFile = open(outputFileName, "a")
	commentsFileName = "TEMP_COMMENTS"
	commentsFile = open(commentsFileName, "a")
	outputFile.truncate(0)
	commentsFile.truncate(0)
	#outputFile.write(lines[0])
	i = 0
	commentsRegex = re.compile(commentExpr, re.VERBOSE)
	#pdb.set_trace()
	for line in lines:
		m = commentsRegex.match(line)
		#newLine = line
		if (m != None):
			hashStart = m.start(1)
			code = line[:hashStart]
			comment = line[hashStart+1:]
			commentRepl = 'BASH2PY_COMMENT_' + str(i)
			commentsFile.write(comment)
			if code.strip() != '':
				outputFile.write(code + '\n')
			outputFile.write(commentRepl + '\n')
			i += 1
			#outputFile.write('\n')
		else:
			outputFile.write(line)
	outputFile.close()
	commentsFile.close()
	
if __name__ == "__main__":
	filename = sys.argv[1]
	makeTempComments(filename)
