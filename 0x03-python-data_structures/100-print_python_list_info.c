#include <stdio.h>
#include <stdlib.h>
#include "listobject.h"

/**
 * print_python_list_info - print info about python list
 * p: pointer to object
 */
void print_python_list_info(PyObject *p)
{
	printf("%p", p);
}
