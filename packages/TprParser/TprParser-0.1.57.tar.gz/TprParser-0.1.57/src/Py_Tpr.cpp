#ifndef _DEBUG

#    include <cinttypes> // toupper

#    include "numpy/arrayobject.h"
#    include "Python.h"
#    include "Reader.h"

#    define xstr(x) #x
#    define tostr(x) xstr(x)
#    define xcat(x, y) x##y
#    define cat(x, y) xcat(x, y)

#    define RAW_MODULE_NAME TprParser_ // use name "TprParser_"
#    define MODULE_NAME tostr(RAW_MODULE_NAME)
#    define PYINIT_FUNC cat(PyInit_, RAW_MODULE_NAME)

//< For Python API, I use NULL instead of nullptr

// A macro for simply writing, executed a function and return ret with ... parameters
#    define TRY_THROW_EXCEPTION_FROM_OBJ(funcname, ret, ...)                                         \
        do                                                                                           \
        {                                                                                            \
            TprReader* reader = static_cast<TprReader*>(PyCapsule_GetPointer(capsule, MODULE_NAME)); \
            if (!reader)                                                                             \
            {                                                                                        \
                PyErr_SetString(PyExc_RuntimeError, "Invalid capsule object");                       \
                return NULL;                                                                         \
            }                                                                                        \
            try                                                                                      \
            {                                                                                        \
                ret = reader->funcname(__VA_ARGS__);                                                 \
            }                                                                                        \
            catch (const std::exception& e)                                                          \
            {                                                                                        \
                PyErr_SetString(PyExc_RuntimeError, e.what());                                       \
                return NULL;                                                                         \
            }                                                                                        \
        } while (0)


// free
static void destory_tpr(PyObject* obj)
{
    delete (TprReader*)PyCapsule_GetPointer(obj, MODULE_NAME);
}

static PyObject* reader_new(PyObject* self, PyObject* args)
{
    const char* fname       = NULL;
    PyObject*   bGRO_obj    = Py_False;
    PyObject*   bMol2_obj   = Py_False;
    PyObject*   bCharge_obj = Py_False;

    if (!PyArg_ParseTuple(args, "s|OOO", &fname, &bGRO_obj, &bMol2_obj, &bCharge_obj))
    {
        return NULL;
    }

    bool bGRO    = PyObject_IsTrue(bGRO_obj);
    bool bMol2   = PyObject_IsTrue(bMol2_obj);
    bool bCharge = PyObject_IsTrue(bCharge_obj);

    TprReader* reader = NULL;
    try
    {
        reader = new TprReader(fname, bGRO, bMol2, bCharge);
    }
    catch (const std::exception& e)
    {
        PyErr_SetString(PyExc_RuntimeError, e.what());
        return NULL;
    }
    return PyCapsule_New(reader, MODULE_NAME, destory_tpr);
}

static PyObject* set_nsteps(PyObject* self, PyObject* args)
{
    PyObject* capsule = NULL;
    int64_t   nsteps;
    if (!PyArg_ParseTuple(args, "OL", &capsule, &nsteps)) { return NULL; }

    int ret;
    TRY_THROW_EXCEPTION_FROM_OBJ(set_nsteps, ret, nsteps);

    Py_RETURN_TRUE;
}

static PyObject* set_dt(PyObject* self, PyObject* args)
{
    PyObject* capsule = NULL;
    double    dt      = 0.0;
    if (!PyArg_ParseTuple(args, "Od", &capsule, &dt)) { return NULL; }

    int ret;
    TRY_THROW_EXCEPTION_FROM_OBJ(set_dt, ret, dt);

    Py_RETURN_TRUE;
}

//< get vector from given object, return NULL if failed
static inline PyObject* get_vector_float(PyObject* vec_obj, std::vector<float>& vec)
{
    if (PyArray_Check(vec_obj))
    {
        // numpy to C array
        PyArrayObject* arr = (PyArrayObject*)(vec_obj);

        // compare dtype
        if (PyArray_TYPE(arr) != NPY_FLOAT32)
        {
            PyErr_SetString(PyExc_RuntimeError, "Python API Only support np.float32 array");
            return NULL;
        }

        npy_intp* dims = PyArray_DIMS(arr);
        int       ndim = PyArray_NDIM(arr);
        if (ndim != 1)
        {
            PyErr_SetString(PyExc_RuntimeError, "Input numpy dimension is not equal 1");
            return NULL;
        }
        float* data = (float*)PyArray_DATA(arr);
        vec.assign(data, data + dims[0]);
    }
    // if is list
    else if (PyList_Check(vec_obj))
    {
        Py_ssize_t size = PyList_Size(vec_obj);
        for (Py_ssize_t i = 0; i < size; i++)
        {
            PyObject* item = PyList_GetItem(vec_obj, i);
            // if (!PyFloat_Check(item))
            //{
            //	PyErr_SetString(PyExc_RuntimeError, "List must be float type");
            //	return NULL;
            // }
            double value = PyFloat_AsDouble(item);
            if (PyErr_Occurred())
            {
                PyErr_SetString(PyExc_RuntimeError,
                                "Some value of input vector can not be converted");
                return NULL;
            }
            vec.push_back((float)(value)); // double to float
        }
    }
    else
    {
        PyErr_SetString(PyExc_RuntimeError, "Input vector must be numpy array or list");
        return NULL;
    }
    // check array size
    if (vec.empty())
    {
        PyErr_SetString(PyExc_RuntimeError, "Empty input vector");
        return NULL;
    }

    return vec_obj;
}


static PyObject* set_pressure(PyObject* self, PyObject* args, PyObject* kwargs)
{
    PyObject*   capsule = NULL;
    const char* epc     = NULL;
    const char* epct    = NULL;
    float       tau_p;
    PyObject*   ref_p    = NULL;
    PyObject*   compress = NULL;
    PyObject*   deform   = NULL;

    static const char* keywords[] = {
        "capsule", "epc", "epct", "tau_p", "ref_p", "compress", "deform", NULL};
    if (!PyArg_ParseTupleAndKeywords(
            args, kwargs, "OssfOOO", (char**)keywords, &capsule, &epc, &epct, &tau_p, &ref_p, &compress, &deform))
    {
        return NULL;
    }

    // get pressure
    std::vector<float> vec_press;
    if (!get_vector_float(ref_p, vec_press)) return NULL;

    // get compress
    std::vector<float> vec_compress;
    if (!get_vector_float(compress, vec_compress)) return NULL;

    // get deform
    std::vector<float> vec_deform;
    if (!get_vector_float(deform, vec_deform)) return NULL;

    int ret;
    TRY_THROW_EXCEPTION_FROM_OBJ(set_pressure, ret, epc, epct, tau_p, vec_press, vec_compress, vec_deform);

    Py_RETURN_TRUE;
}

static PyObject* set_temperature(PyObject* self, PyObject* args, PyObject* kwargs)
{
    PyObject*   capsule = NULL;
    const char* etc     = NULL;
    PyObject*   ref_t   = NULL;
    PyObject*   tau_t   = NULL;

    static const char* keywords[] = {"capsule", "etc", "tau_t", "ref_t", NULL};
    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "OsOO", (char**)keywords, &capsule, &etc, &tau_t, &ref_t))
    {
        return NULL;
    }

    // get tau_t
    std::vector<float> vec_tau;
    if (!get_vector_float(tau_t, vec_tau)) return NULL;

    // get ref_t
    std::vector<float> vec_t;
    if (!get_vector_float(ref_t, vec_t)) return NULL;

    int ret;
    TRY_THROW_EXCEPTION_FROM_OBJ(set_temperature, ret, etc, vec_tau, vec_t);

    Py_RETURN_TRUE;
}

// set integer props in mdp
static PyObject* set_mdp_integer(PyObject* self, PyObject* args)
{
    PyObject*   capsule = NULL;
    const char* prop    = NULL;
    int         val     = 0;

    if (!PyArg_ParseTuple(args, "Osi", &capsule, &prop, &val)) { return NULL; }

    int ret;
    TRY_THROW_EXCEPTION_FROM_OBJ(set_mdp_integer, ret, prop, val);

    Py_RETURN_TRUE;
}

// get integer props in mdp
static PyObject* get_mdp_integer(PyObject* self, PyObject* args)
{
    PyObject*   capsule = NULL;
    const char* prop    = NULL;

    if (!PyArg_ParseTuple(args, "Os", &capsule, &prop)) { return NULL; }

    int ret = -1;
    TRY_THROW_EXCEPTION_FROM_OBJ(get_mdp_integer, ret, prop);

    return Py_BuildValue("i", ret);
}

static PyObject* get_xvf(PyObject* self, PyObject* args)
{
    PyObject*   capsule = NULL;
    const char* type    = NULL;

    // get object handle
    if (!PyArg_ParseTuple(args, "Os", &capsule, &type)) { return NULL; }

    std::vector<float> vec;
    TRY_THROW_EXCEPTION_FROM_OBJ(get_xvf, vec, type);

    // coords to python list
    PyObject* list = PyList_New(vec.size());
    if (!list)
    {
        PyErr_SetString(PyExc_RuntimeError, "Can not new list for vector");
        return NULL;
    }
    Py_ssize_t i = 0;
    for (const auto& it : vec)
    {
        PyObject* value = PyFloat_FromDouble(static_cast<double>(it));
        if (!value)
        {
            PyErr_SetString(PyExc_RuntimeError, "Can not convert vector to list");
            Py_DECREF(list); // free list
            return NULL;
        }
        PyList_SET_ITEM(list, i++, value);
    }

    return list;
}


// get resid, atomtype number, atomic number
static PyObject* get_ivector(PyObject* self, PyObject* args)
{
    PyObject*   capsule = NULL;
    const char* type    = NULL;

    // get object handle
    if (!PyArg_ParseTuple(args, "Os", &capsule, &type)) { return NULL; }

    std::vector<int> vec;
    TRY_THROW_EXCEPTION_FROM_OBJ(get_ivector, vec, type);

    // ivector to python list
    PyObject* list = PyList_New(vec.size());
    if (!list)
    {
        PyErr_SetString(PyExc_RuntimeError, "Can not new list for ivector");
        return NULL;
    }
    Py_ssize_t i = 0;
    for (const auto& it : vec)
    {
        PyObject* value = PyLong_FromLong(static_cast<long>(it));
        if (!value)
        {
            PyErr_SetString(PyExc_RuntimeError, "Can not convert ivector to list");
            Py_DECREF(list); // free list
            return NULL;
        }
        PyList_SET_ITEM(list, i++, value);
    }

    return list;
}


// get precision of tpr
static PyObject* get_prec(PyObject* self, PyObject* args)
{
    PyObject* capsule = NULL;

    if (!PyArg_ParseTuple(args, "O", &capsule)) { return NULL; }

    int prec = 4;
    TRY_THROW_EXCEPTION_FROM_OBJ(get_precision, prec);

    return Py_BuildValue("i", prec);
}

// get resname or atomname
static PyObject* get_name(PyObject* self, PyObject* args)
{
    PyObject*   capsule = NULL;
    const char* type    = NULL;

    if (!PyArg_ParseTuple(args, "Os", &capsule, &type)) { return NULL; }

    // get vector of name
    std::vector<std::string> vec;
    TRY_THROW_EXCEPTION_FROM_OBJ(get_name, vec, type);

    if (vec.empty())
    {
        PyErr_SetString(PyExc_RuntimeError, "Can not find vector in tpr");
        return NULL;
    }

    // coords to python list
    PyObject* list = PyList_New(vec.size());
    if (!list)
    {
        PyErr_SetString(PyExc_RuntimeError, "Can not new list for vector");
        return NULL;
    }
    Py_ssize_t i = 0;
    for (const auto& it : vec)
    {
        // const char * to python string obj
        PyObject* value = PyUnicode_FromString(it.c_str());
        if (!value)
        {
            PyErr_SetString(PyExc_RuntimeError, "Can not convert vector to list");
            Py_DECREF(list); // free list
            return NULL;
        }
        PyList_SET_ITEM(list, i++, value);
    }

    return list;
}


//< get force field paramaters from vector
template<typename T>
static inline PyObject* get_ffparams(int nat, const std::vector<T>& vec)
{
    // coords to python list
    PyObject* list = PyList_New(vec.size());
    if (!list)
    {
        PyErr_SetString(PyExc_RuntimeError, "Can not new list for vector");
        return NULL;
    }

    Py_ssize_t i = 0;
    for (const auto& it : vec)
    {
        //! atom indexs + ffparams
        PyObject* ffparams = PyList_New(nat + 1 + it.ff.size());

        Py_ssize_t count = 0;
        for (Py_ssize_t j = 0; j < nat; j++)
        {
            PyObject* value = PyLong_FromLong(static_cast<long>(it[j]));
            if (!value)
            {
                PyErr_SetString(PyExc_RuntimeError, "Can not convert it[j] to pyobj");
                Py_DECREF(ffparams); // free ids
                Py_DECREF(list);     // free list
                return NULL;
            }
            PyList_SET_ITEM(ffparams, count++, value);
        }

        // append func type
        PyObject* value = PyLong_FromLong(static_cast<long>(it.ifunc));
        if (!value)
        {
            PyErr_SetString(PyExc_RuntimeError, "Can not convert it.ifunc to pyobj");
            Py_DECREF(ffparams); // free ffparams
            Py_DECREF(list);     // free list
            return NULL;
        }
        PyList_SET_ITEM(ffparams, count++, value);

        // append true ff parameters in float for all
        for (size_t k = 0; k < it.ff.size(); k++)
        {
            PyObject* value = PyFloat_FromDouble(static_cast<double>(it.ff[k]));
            if (!value)
            {
                PyErr_SetString(PyExc_RuntimeError, "Can not convert iit.ff[k] to pyobj");
                Py_DECREF(ffparams); // free ffparams
                Py_DECREF(list);     // free list
                return NULL;
            }
            PyList_SET_ITEM(ffparams, count++, value);
        }

        // final obj
        PyList_SET_ITEM(list, i++, ffparams);
    }
    return list;
}

//< get bonds/angles/dihedrals/impropers (1-based index) pair of tpr
static PyObject* get_bonded(PyObject* self, PyObject* args)
{
    PyObject*   capsule = NULL;
    const char* type    = NULL;

    if (!PyArg_ParseTuple(args, "Os", &capsule, &type)) { return NULL; }

    // get vector from handle
    std::vector<Bonded> vec;
    TRY_THROW_EXCEPTION_FROM_OBJ(get_bonded, vec, type);

    // type to releated the number of atoms
    int nat = 2;
    switch (std::toupper(type[0]))
    {
            // bonds
        case 'B':
            nat = 2;
            break;
            // angles
        case 'A':
            nat = 3;
            break;
            // dihedrals/impropers
        case 'D':
        case 'I': nat = 4; break;
        default: break;
    }

    return get_ffparams<Bonded>(nat, vec);
}

//< get pairs (1-based index)/LJ parameters of each atom information from tpr
static PyObject* get_nonbonded(PyObject* self, PyObject* args)
{
    PyObject*   capsule = NULL;
    const char* type    = NULL;

    if (!PyArg_ParseTuple(args, "Os", &capsule, &type)) { return NULL; }

    // get vector from handle
    std::vector<NonBonded> vec;
    TRY_THROW_EXCEPTION_FROM_OBJ(get_nonbonded, vec, type);

    // type to releated the number of atoms
    int nat = 2;
    switch (std::toupper(type[0]))
    {
        case 'P': // pairs
            nat = 2;
            break;
        case 'L': // LJ for each atoms
        case 'T': // LJ for unique atomtype
            nat = 0;
            break;
        default: break;
    }

    return get_ffparams<NonBonded>(nat, vec);
}

//< set atom coords/velocity/force
static PyObject* set_xvf(PyObject* self, PyObject* args, PyObject* kwargs)
{
    PyObject*   capsule = NULL;
    const char* prop    = NULL;
    PyObject*   vec_obj = NULL;

    static const char* keywords[] = {"capsule", "prop", "vec", NULL};
    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "OsO", (char**)keywords, &capsule, &prop, &vec_obj))
    {
        return NULL;
    }

    // get vector from handle
    std::vector<float> vec;
    if (!get_vector_float(vec_obj, vec)) return NULL;

    int ret;
    TRY_THROW_EXCEPTION_FROM_OBJ(set_xvf, ret, prop, vec);

    Py_RETURN_TRUE;
}

//< get exclusions index (0-based) for each atom
static PyObject* get_exclusions(PyObject* self, PyObject* args)
{
    PyObject* capsule = NULL;

    if (!PyArg_ParseTuple(args, "O", &capsule)) { return NULL; }
    std::vector<std::vector<int>> excls;
    TRY_THROW_EXCEPTION_FROM_OBJ(get_exclusions, excls);

    //! convert 2D vector to python list
    PyObject* list = PyList_New(excls.size());
    if (!list)
    {
        PyErr_SetString(PyExc_RuntimeError, "Can not new list for vector for get_exclusions");
        return NULL;
    }

    for (size_t i = 0; i < excls.size(); i++)
    {
        PyObject* sublist = PyList_New(excls[i].size());
        if (!sublist)
        {
            PyErr_SetString(PyExc_RuntimeError,
                            "Can not sublist list for vector for get_exclusions");
            Py_DECREF(list); // free list
            return NULL;
        }
        for (size_t j = 0; j < excls[i].size(); j++)
        {
            PyObject* value = PyLong_FromLong(static_cast<long>(excls[i][j]));
            if (!value)
            {
                PyErr_SetString(PyExc_RuntimeError, "Can not convert excls[i][j] to pyobj");
                Py_DECREF(sublist); // free sublist
                Py_DECREF(list);    // free list
                return NULL;
            }
            PyList_SET_ITEM(sublist, j, value);
        }

        PyList_SET_ITEM(list, i, sublist);
    }

    return list;
}


static PyMethodDef methods[] = {
    {"load", reader_new, METH_VARARGS, "Create a new TprReader instance"},
    {"set_nsteps", set_nsteps, METH_VARARGS, "Set up nsteps"},
    {"set_dt", set_dt, METH_VARARGS, "Set up dt"},
    {"set_mdp_integer", set_mdp_integer, METH_VARARGS, "Set up int keyword"},
    {"set_xvf",
     (PyCFunction)set_xvf,
     METH_VARARGS | METH_KEYWORDS,
     "Set up atomic coordinates/velocity/force/box/electirc-field"},
    {"set_pressure",
     (PyCFunction)set_pressure,
     METH_VARARGS | METH_KEYWORDS,
     "Set up pressure coupling parts"},
    {"set_temperature",
     (PyCFunction)set_temperature,
     METH_VARARGS | METH_KEYWORDS,
     "Set up temperature coupling parts"},

    {"get_prec", get_prec, METH_VARARGS, "Get precision of tpr, float(4) or double(8)"},
    {"get_mdp_integer", get_mdp_integer, METH_VARARGS, "Get int value of keyword"},
    {"get_name", get_name, METH_VARARGS, "Get resname/atomname/atomtype from tpr"},
    {"get_xvf",
     get_xvf,
     METH_VARARGS,
     "Get coords/velocity/force/charge/mass/box/electirc-field from tpr"},
    {"get_ivector", get_ivector, METH_VARARGS, "Get resid/atomtypenumber/atomicnumber from tpr"},
    {"get_bonded",
     get_bonded,
     METH_VARARGS,
     "Get bonds/angles/dihedrals/impropers (1-based index) forcefield paramaters information from "
     "tpr"},
    {"get_nonbonded",
     get_nonbonded,
     METH_VARARGS,
     "Get pairs (1-based index)/LJ parameters of each atom information from tpr"},
    {"get_exclusions",
     get_exclusions,
     METH_VARARGS,
     "Get global atom exclusion index (0-based) for each atom"},

    {NULL, NULL, 0, NULL}};

static struct PyModuleDef tpr_module = {
    PyModuleDef_HEAD_INIT,
    MODULE_NAME, // m_name
    NULL,        // m_doc
    -1,          // m_size
    methods      // m_methods
};

// TprParser_  module name
PyMODINIT_FUNC PYINIT_FUNC(void)
{
    // if is numpy
    import_array(); // ʹ��numpy��صĺ���ʱ������ȵ������

    return PyModule_Create(&tpr_module);
}

#endif // !_DEBUG
