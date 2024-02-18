#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - prints info about python lists
 * @p: address of pyobject struct
 */
void print_python_list_info(PyObject *p)
{
	int num;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (num = 0; num < Py_SIZE(p); num++)
		printf("Element %d: %s\n", num, Py_TYPE(PyList_GetItem(p, num))->tp_name);
}
