#include <stdio.h>
#include <stdlib.h>
#include "listobject.h"

/**
 * print_python_list_info - function that prints basic info about Python list
 * @p: pointer to Python Object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	printf("*] Size of the Python List = %d\n", p->Py_SIZE);
}
