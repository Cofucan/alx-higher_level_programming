#include <stdio.h>
#include <stdlib.h>
#include "/usr/include/python3.4/Python.h"

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
void print_hexn(const char *str, int n);

/**
 * print_python_bytes - Print information about a Python list object
 * @p: Python object to be processed.
 * 
 * Return: Nothing.
*/

void print_python_list(PyObject *p)
{
    int l, list_len;
    PyObject *item;
    PyListObject *py_copy = (PyListObject *)p;

    printf("[*] Python list info\n");

    /* Check if the provided object is a valid list object */
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    /* Get the length of the list */
    list_len = PyList_GET_SIZE(p);

    printf("[*] Size of the Python List = %d\n", list_len);
    printf("[*] Allocated = %d\n", (int)py_copy->allocated);

    /* Iterate over each element in the list */
    for (l = 0; l < list_len; l++)
    {
        item = PyList_GET_ITEM(p, l);

        /* Print the type name of the element */
        printf("Element %d: %s\n", l, item->ob_type->tp_name);

        /* Check if the element is a bytes object and print its information */
        if (PyBytes_Check(item))
            print_python_bytes(item);

        /* Check if the element is a float object and print its information */
        else if (PyFloat_Check(item))
            print_python_float(item);
    }

    fflush(stdout);
}

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: Python object to be processed.
 * 
 * Return: Nothing.
*/

void print_python_bytes(PyObject *p)
{
    PyBytesObject *py_copy = (PyBytesObject *)p;
    int n_bytes, py_copy_size = 0;

    printf("[.] bytes object info\n");

    /* Check if the provided object is a valid bytes object */
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    /* Get the size of the bytes object */
    py_copy_size = PyBytes_Size(p);
    n_bytes = py_copy_size + 1;

    /* Limit the number of bytes to print to a maximum of 10 */
    if (n_bytes >= 10)
        n_bytes = 10;

    /* Print information about the bytes object */
    printf("  size: %d\n", py_copy_size);
    printf("  trying string: %s\n", py_copy->ob_sval);
    printf("  first %d bytes: ", n_bytes);

    /* Print the hexadecimal representation of the bytes */
    print_hexn(py_copy->ob_sval, n_bytes);
    printf("\n");

    fflush(stdout);
}

/**
 * print_python_bytes - Print information about a Python float object
 * @p: Python object to be processed.
 * 
 * Return: Nothing.
*/

void print_python_float(PyObject *p)
{
    PyFloatObject *py_copy = (PyFloatObject *)p;
    char *num_str = NULL;

    printf("[.] float object info\n");

    /* Check if the provided object is a valid float object */
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    /* Store the number as a string and print */
	num_str = PyOS_double_to_string(py_copy->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", num_str);
	PyMem_Free(num_str);

    fflush(stdout);
}

/**
 * print_hexn - Prints n chars of a string in hex format
 * @str: String to be printed.
 * @n: Number of characters to print.
 * 
 * Return: Nothing.
*/

void print_hexn(const char *str, int n)
{
	int c = 0;

	while (c < (n - 1))
    {
		printf("%02x ", (unsigned char) str[c]);
        c++;
    }

    /* Print the last character without a space */
	printf("%02x", str[c]);
    fflush(stdout);
}
