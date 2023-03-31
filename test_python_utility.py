from python_utility import *

def testQuotedStr():
	x = r'hello cool "ac $12 $abc cool $a12" hello "hi $abc $a12 wow nice abcde $ad wowwww" hi'
	print fixQuotedStr(x)
	
def testQuotedStrDummy():
	x = '"abc" "def"'
	print fixQuotedStrDummy(x)

def testQuotedSingleVar():
	x = '"$abc"'
	print fixQuotedSingleVarStr(x)

def testQuotedVarStr():
	print fixQuotedStr(x)

def testFixVariables():
	x = 'AVERAGE=$[$SUM / $NUM]'
	print fixVariables(x)
	
def testBackticksAndEval():
	x = r'x=`ls - la` hello `cool` hi $(awesome) hi'
	print fixBackticksAndEval(x)
    
def testArguments():
	x = r'hello $12 cool $21abc $1 hello'
	print fixArguments(x)

def testFixString():
	#x = 'hello how are you "hello $abc $12 $536 cool $abc123"  hello "cool wow $1 $ab" hi neat'
	x = '"$1"'
	print fixString(x)

def test():
	testBackticksAndEval()
	testArguments()
	testQuotedStr()
	testQuotedStrDummy()
	testFixString()
	testFixVariables()
	testQuotedSingleVar()

if __name__ == "__main__":
    test()
