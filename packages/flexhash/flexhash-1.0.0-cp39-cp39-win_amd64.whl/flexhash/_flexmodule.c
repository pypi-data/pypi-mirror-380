#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdint.h>
#include "flex.h" // declares flex_hash(...)  // NOLINT

// Python: flexhash.hash(data: bytes) -> bytes[32]
static PyObject *py_flex_hash(PyObject *self, PyObject *args)
{
    const uint8_t *in_buf = NULL;
    Py_ssize_t in_len = 0;
    if (!PyArg_ParseTuple(args, "y#", &in_buf, &in_len))
    {
        return NULL;
    }

    uint8_t out[32];
    // flex_hash ignores 'len' internally for size=80 first round and then 64,
    // but we pass the input length to match the signature.
    flex_hash((const char *)in_buf, (char *)out, (uint32_t)in_len);

    return PyBytes_FromStringAndSize((const char *)out, 32);
}

static PyMethodDef Methods[] = {
    {"hash", py_flex_hash, METH_VARARGS, "Compute Kylacoin Flex digest"},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef Module = {
    PyModuleDef_HEAD_INIT,
    "_flexhash",
    "Kylacoin Flex hash (C extension)",
    -1,
    Methods};

PyMODINIT_FUNC PyInit__flexhash(void) { return PyModule_Create(&Module); }
