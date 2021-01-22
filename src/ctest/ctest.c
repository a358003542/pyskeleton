#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

static PyObject *
ctest_hello(PyObject *self, PyObject *args) {
    char *str;

    /* Parse arguments */
    if(!PyArg_ParseTuple(args, "s", &str)) {
        return NULL;
    }

    printf(str);

    return Py_None;
}

static PyMethodDef CtestMethods[] = {
    {"hello", ctest_hello, METH_VARARGS, "a simple say hello function."},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef ctestmodule = {
    PyModuleDef_HEAD_INIT,
    "ctest",
    "a simple python module writing in c",
    -1,
    CtestMethods
};

PyMODINIT_FUNC PyInit_ctest(void) {
    return PyModule_Create(&ctestmodule);
}