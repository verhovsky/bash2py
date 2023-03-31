//#include "python_functions.h"
#include <stdio.h>

char *cstrret= NULL;

char* arg_file = "temp_file";

/* Create a function to handle errors when they occur */
void error(char* errstring) {
	printf("%s\n", errstring);
	FILE *fp;
	fp=fopen("error", "w");
	fprintf(fp, "%s", errstring);
	fclose(fp);
	exit(1);
}


void log_stuff(char* input, char* log_file){
	FILE* fp = fopen(log_file, "a");
	fprintf(fp, "%s\n", input);
	fclose(fp);
}

void write_to_file(char* input){
	FILE* fp = fopen(arg_file, "w");
	fprintf(fp, "%s", input);
	fclose(fp);
}

//char* readFromFile1(){
//	int BUFF_SIZE = 1024;
//	char buff[BUZZ_SIZE];
//	FILE *f = fopen(arg_file, "r");
//	fgets(buff, BUZZ_SIZE, f);
//	//printf("String read: %s\n", buff);
//	fclose(f);
//	return 0;
//}

//char* readFromFile(){
//	
//	char * buffer = 0;
//	long length;
//	FILE * f = fopen (arg_file, "r");
//
//	if (f)
//	{
//	  fseek (f, 0, SEEK_END);
//	  length = ftell (f);
//	  fseek (f, 0, SEEK_SET);
//	  buffer = malloc (length);
//	  if (buffer)
//	  {
//	    fread (buffer, 1, length, f);
//	  }
//	  fclose (f);
//	}
//
//	if (buffer)
//	{
//	  // start to process your data / extract strings here...
//	}
//	return buffer;
//}

int count_chars(){
	FILE *fp = fopen(arg_file, "r+");
	char nextChar = getc(fp);
	int numCharacters = 0;

	while (nextChar != EOF) {
	    //Do something else, like collect statistics
	    numCharacters++;
	    nextChar = getc(fp);
	}
	fclose(fp);
	return numCharacters;

}

void read_file(char* output, int size){
	FILE *f = fopen(arg_file, "r+");
	fgets(output, size+1, f);
	//printf("String read: %s\n", buff);
	fclose(f);
	//return 0;
	
}

char* fix_string(char* input) {
	//return input;
	if (input == NULL)
		return NULL;
	write_to_file(input);
	//free(input);
	log_stuff(input, "logStuff");
	//free(input);
	system("python python_utility.py");
	FILE *fp;
	//char* output = (char *)malloc(1024*sizeof(char));
	//fp = popen("python python_utility.py", "r");
	//fgets(output, sizeof(output), fp);
//	    printf("%s", path);
	//pclose(fp);
	//char* output = readFromFile();
	int num_chars = count_chars();
	char* output = (char*)(malloc((num_chars+1)*sizeof(char)));
	read_file(output, num_chars);
	log_stuff(output, "logStuff");
	return output;
//	FILE *fp;
//	int status;
//	char path[1035];
//
//	/* Open the command for reading. */
//	//char cmd[100];
//	//sprintf("python python_utility.py %s", )
//	fp = popen("python python_utility.py", "r");
//	if (fp == NULL) {
//		printf("Failed to run command\n");
//		exit;
//	}
//
//	/* Read the output a line at a time - output it. */
//	while (fgets(path, sizeof(path)-1, fp) != NULL) {
//		printf("%s", path);
//	}
//
//	/* close */
//	pclose(fp);
//
//	return 0;
}

//int main(){
//	char * input = "abcde";
//	char * output = fix_string(input);
//	printf("%s", output);
//}
