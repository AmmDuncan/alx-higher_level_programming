#include <python3.4/Python.h>

/**
 * print_python_list_info - print info about python list
 * p: pointer to object
 */
void print_python_list_info(PyObject *p)
{
	int size, allocated, i;

	size = sizeof(*p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of Python List = %d", size);
	printf("[*] Allocated = %d", allocated);
}
