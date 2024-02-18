#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; ++i) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    unsigned char *bytes;
    PyObject *repr;

    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    printf("[.] bytes object info\n");
    printf("  [ERROR] Invalid Bytes Object\n");
    printf("[*] Size: %ld\n", size);
    printf("[*] Trying string: %s\n", PyBytes_AS_STRING(p));

    if (size > 10)
        size = 10;
    else
        printf("  [ERROR] Invalid Bytes Object\n");

    bytes = (unsigned char *)PyBytes_AS_STRING(p);

    printf("[*] first %ld bytes: ", size);
    for (i = 0; i < size; ++i) {
        printf("%02x", bytes[i]);
        if (i < size - 1)
            printf(" ");
    }
    printf("\n");
}
