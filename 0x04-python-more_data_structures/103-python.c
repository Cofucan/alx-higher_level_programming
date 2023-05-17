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
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
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
	Py_ssize_t size;
	Py_ssize_t i;
	char *bytes;
	PyObject *bytes_obj;

	printf("[.] Bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes object\n");
		return;
	}

	size = PyBytes_Size(p);
	bytes_obj = PyObject_Repr(p);
	bytes = PyBytes_AsString(bytes_obj);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes);
	printf("  first %ld bytes: ", (size < 10) ? size + 1 : 10);

	for (i = 0; i < size && i < 10; i++)
		printf("%02hhx%c", bytes[i], (i == 9 || i == size - 1) ? '\n' : ' ');

	Py_DECREF(bytes_obj);
}

