#include <Python.h>
int main() {
	PyObject *strret, *mymod, *strfunc, *strargs;
	char *cstrret;
	Py_Initialize();
	PySys_SetPath(".");
	mymod = PyImport_ImportModule("pytest");
	strfunc = PyObject_GetAttrString(mymod, "getWord");
	//strargs = Py_BuildValue("(s)", "Hello World");
	strret = PyEval_CallObject(strfunc, NULL);
	PyArg_Parse(strret, "s", &cstrret);
	printf("Reversed string: %s\n", cstrret);
	Py_Finalize();
	return 0;

}


//	printf("Prefix: %s\nExec Prefix: %s\nPython Path: %s\n",
//			Py_GetPrefix(),
//			Py_GetExecPrefix(),
//			Py_GetProgramFullPath());
//	printf("Module Path: %s\n",
//			Py_GetPath());
//	printf("Version: %s\nPlatform: %s\nCopyright: %s\n",
//			Py_GetVersion(),
//			Py_GetPlatform(),
//			Py_GetCopyright());
//	printf("Compiler String: %s\nBuild Info: %s\n",
//			Py_GetCompiler(),
//			Py_GetBuildInfo());
//	Py_Finalize();
//	return 0;