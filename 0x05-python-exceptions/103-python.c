#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: Pointer to PyObject.
 */
void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *obj;

    printf("[*] Python list info\n");

    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        obj = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
    }
}

/**
 * print_python_bytes - Prints basic info about Python bytes.
 * @p: Pointer to PyObject.
 */
void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first %ld bytes:", size + 1 > 10 ? 10 : size + 1);
    str = PyBytes_AsString(p);
    for (i = 0; i < size + 1 && i < 10; i++)
        printf(" %02hhx", str[i]);
    printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float.
 * @p: Pointer to PyObject.
 */
void print_python_float(PyObject *p) {
    double d;
    char *str;

    printf("[.] float object info\n");

    if (!PyFloat_Check(p)) {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    d = ((PyFloatObject *)p)->ob_fval;
    str = PyOS_double_to_string(d, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", str);
}
