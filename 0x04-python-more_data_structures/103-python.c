#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints information related to Python lists
 * @p: Pointer to the Python object.
 *
 * Return: Nothing.
 */

void print_python_list(PyObject *p)
{
	int i, size, alloc;
	PyVarObject *pvar = (PyVarObject *)p;
	PyListObject *plist = (PyListObject *)p;
	const char *type;

	size = pvar->ob_size;
	alloc = plist->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		type = plist->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(plist->ob_item[i]);
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
	unsigned char f, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", size);
	for (f = 0; f < size; f++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (f == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
