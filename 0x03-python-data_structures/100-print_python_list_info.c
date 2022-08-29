#include <python3.4/Python.h>

/**
 * print_python_list_info - print info about python list
 * @p: pointer to object
 */
void print_python_list_info(PyObject *p)
{
	int size, allocated, i;

	size = sizeof(*p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *obj = PyList_GetItem(p, i);

		printf("Element %d: %s", i, Py_TYPE(obj)->tp_name));
	}
}
