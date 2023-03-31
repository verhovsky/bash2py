#!/bin/bash


FILE="/some/file"
OPTION="0"

#The statement below gets interpreted incorrectly. The '!' character never gets translated to 'not' and the '-x' is overlooked entirely, with the varaible being tested printed out twice.
#believe the desired output would be:
#if not(os.access(str(FILE.val),X_OK) )

if [ ! -x "$FILE" ]; then
  echo "File is not executable"
fi


#The statement below also gets interpreted incorrectly. 
#believe the desired output would be:
#if (OPTION.val != "1")
if [ "$OPTION" != "1" ]; then
  echo "Option is disabled"
fi

