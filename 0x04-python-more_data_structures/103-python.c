#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
#include <stdio.h>

/**
 * print_python_list - prints information related to Python lists
 * @p: Pointer to the Python object.
 *
 * Return: Nothing.
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	Py_ssize_t allocated = 0;
	Py_ssize_t i;

	PyObject **items = NULL;
	PyObject *item = NULL;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid Python List\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	allocated = ((PyListObject *)p)->allocated;
	items = ((PyListObject *)p)->ob_item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = items[i];
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - prints information related to Python bytes
 * @p: Pointer to the Python object.
 *
 * Return: Nothing.
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0;
	Py_ssize_t i;
	char *bytes = NULL;

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Python Bytes object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	bytes = ((PyBytesObject *)p)->ob_sval;

	printf("[.] Bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes);
	printf("  first %ld bytes: ", (size < 10) ? size + 1 : 10);

	for (i = 0; i < size && i < 10; i++)
		printf("%02hhx%c", bytes[i], (i == 9 || i == size - 1) ? '\n' : ' ');
}
