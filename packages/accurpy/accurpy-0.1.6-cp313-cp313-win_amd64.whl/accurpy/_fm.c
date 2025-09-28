// src/accurpy/_fm.c
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <math.h>
#include <stdint.h>
#include <stddef.h>

#ifndef HAVE_FMA
#  if defined(__STDC_VERSION__) && (__STDC_VERSION__ >= 199901L)
#    define HAVE_FMA 1
#  endif
#endif
#ifndef HAVE_FMA
#  if defined(_MSC_VER)
#    pragma function(fma)
#  endif
static inline double fma(double a, double b, double c){ return a*b + c; }
#endif

static inline int nint_tieeven(double x){
#if defined(_MSC_VER)
    double r = nearbyint(x);
    return (int)r;
#else
    return (int)lrint(x);
#endif
}

static PyObject* alloc_double_bytearray(size_t n){
    PyObject* ba = PyByteArray_FromStringAndSize(NULL, (Py_ssize_t)(n * sizeof(double)));
    if (!ba) return NULL;
    return ba;
}

/* ---------------------- Double-double helpers ---------------------- */

typedef struct { double hi, lo; } dd;
static const double SPLITTER = 134217729.0; /* 2^27+1 */
static const double LN2_HI = 6.93147180369123816490e-01;
static const double LN2_LO = 1.90821492927058770002e-10;
static const double INV_LN2 = 1.44269504088896340736;
static const double EXP_COEFFS[41] = {
    1.00000000000000000000e+00,
    1.00000000000000000000e+00,
    5.00000000000000000000e-01,
    1.66666666666666657415e-01,
    4.16666666666666643537e-02,
    8.33333333333333321769e-03,
    1.38888888888888894189e-03,
    1.98412698412698412526e-04,
    2.48015873015873015658e-05,
    2.75573192239858925110e-06,
    2.75573192239858935697e-07,
    2.50521083854417202239e-08,
    2.08767569878681001866e-09,
    1.60590438368216159258e-10,
    1.14707455977297261229e-11,
    7.64716373181981741526e-13,
    4.77947733238738588453e-14,
    2.81145725434552099254e-15,
    1.56192069685862277363e-16,
    8.22063524662433103628e-18,
    4.11031762331216532555e-19,
    1.95729410633912625952e-20,
    8.89679139245057407789e-22,
    3.86817017063068412615e-23,
    1.61173757109611838590e-24,
    6.44695028438447358950e-26,
    2.47959626322479758961e-27,
    9.18368986379554712643e-29,
    3.27988923706983845963e-30,
    1.13099628864477180713e-31,
    3.76998762881590606938e-33,
    1.21612504155351810759e-34,
    3.80039075485474408621e-36,
    1.15163356207719508905e-37,
    3.38715753552116179633e-39,
    9.67759295863189067186e-41,
    2.68822026628663633314e-42,
    7.26546017915307135902e-44,
    1.91196320504028195296e-45,
    4.90246975651354351900e-47,
    1.22561743912838584936e-48
};

static inline void two_sum(double a, double b, double* s, double* e){
    double sum = a + b;
    double bb = sum - a;
    double err = (a - (sum - bb)) + (b - bb);
    *s = sum; *e = err;
}
static inline void quick_two_sum(double a, double b, double* s, double* e){
    double sum = a + b;
    double err = b - (sum - a);
    *s = sum; *e = err;
}
static inline void split(double a, double* hi, double* lo){
    double c = SPLITTER * a;
    double ahi = c - (c - a);
    double alo = a - ahi;
    *hi = ahi; *lo = alo;
}
static inline void two_prod(double a, double b, double* p, double* e){
    double prod = a * b;
    double a_hi, a_lo, b_hi, b_lo;
    split(a, &a_hi, &a_lo);
    split(b, &b_hi, &b_lo);
    double err = ((a_hi * b_hi - prod) + a_hi * b_lo + a_lo * b_hi) + a_lo * b_lo;
    *p = prod; *e = err;
}
static inline dd dd_norm(double hi, double lo){
    double s, e; two_sum(hi, lo, &s, &e);
    dd r = {s, e}; return r;
}
static inline dd dd_make(double hi, double lo){
    return dd_norm(hi, lo);
}
static inline dd dd_add(dd A, dd B){
    double s, e; two_sum(A.hi, B.hi, &s, &e);
    double t, f; two_sum(A.lo, B.lo, &t, &f);
    double e_new, e2; quick_two_sum(e, t, &e_new, &e2);
    double s_new, e3; quick_two_sum(s, e_new, &s_new, &e3);
    double lo = e2 + f + e3;
    double hi, lo2; quick_two_sum(s_new, lo, &hi, &lo2);
    return dd_make(hi, lo2);
}
static inline dd dd_sub(dd A, dd B){
    dd nB = { -B.hi, -B.lo };
    return dd_add(A, nB);
}
static inline dd dd_mul(dd A, dd B){
    double p, pe; two_prod(A.hi, B.hi, &p, &pe);
    pe += A.hi * B.lo + A.lo * B.hi;
    double hi, lo; quick_two_sum(p, pe, &hi, &lo);
    return dd_make(hi, lo);
}
static inline dd dd_mul_d(dd A, double x){
    double p, pe; two_prod(A.hi, x, &p, &pe);
    double q = A.lo * x;
    double s, se; two_sum(pe, q, &s, &se);
    double hi, lo; two_sum(p, s, &hi, &lo);
    return dd_make(hi, lo + se);
}
static inline dd dd_div(dd A, dd B){
    double q1 = A.hi / B.hi;
    double p1, p2; two_prod(q1, B.hi, &p1, &p2);
    p2 += q1 * B.lo;
    dd r1 = dd_sub(A, (dd){p1, p2});
    double q2 = (r1.hi + r1.lo) / B.hi;
    double qh, ql; quick_two_sum(q1, q2, &qh, &ql);
    two_prod(qh, B.hi, &p1, &p2);
    p2 += qh * B.lo;
    dd r2 = dd_sub(A, (dd){p1, p2});
    double q3 = (r2.hi + r2.lo) / B.hi;
    quick_two_sum(qh, q3, &qh, &ql);
    return dd_make(qh, ql);
}
static inline dd dd_pow2(dd A){
    return dd_mul(A, A);
}
static inline dd dd_pow3(dd A){
    return dd_mul(dd_mul(A, A), A);
}
static inline dd dd_cbrt(dd A){
    double y0 = cbrt(A.hi);
    dd y = {y0, 0.0};
    for (int i=0;i<3;i++){
        dd y3 = dd_pow3(y);
        dd r  = dd_sub(y3, A);
        dd y2 = dd_pow2(y);
        dd d  = dd_add(dd_add(y2, y2), y2); /* 3*y^2 */
        dd corr = dd_div(r, d);
        y = dd_sub(y, corr);
    }
    return y;
}
static inline dd dd_sqrt(dd A){
    double y0 = sqrt(A.hi);
    dd y = {y0, 0.0};
    for (int i=0;i<3;i++){
        dd inv = dd_div(A, y);
        dd sum = dd_add(y, inv);
        y = dd_mul_d(sum, 0.5);
    }
    return y;
}
static inline dd dd_ldexp(dd A, int k){
    double factor = ldexp(1.0, k);
    return dd_make(A.hi * factor, A.lo * factor);
}
static inline dd dd_exp_minus_small(dd R, int terms){
    dd e = {EXP_COEFFS[terms], 0.0};
    for (int k = terms - 1; k >= 0; --k){
        dd prod = dd_mul(e, (dd){-R.hi, -R.lo});
        e = dd_add(prod, (dd){EXP_COEFFS[k], 0.0});
    }
    return e;
}
static inline dd dd_exp_neg(double x){
    if (x > 745.0){
        dd zero = {0.0, 0.0};
        return zero;
    }
    int m = nint_tieeven(x * INV_LN2);
    double mh, ml; split((double)m, &mh, &ml);
    dd md = {mh, ml};
    dd t1 = dd_mul(md, (dd){LN2_HI, 0.0});
    dd t2 = dd_mul(md, (dd){LN2_LO, 0.0});
    dd t  = dd_add(t1, t2);
    dd r  = dd_sub((dd){x, 0.0}, t);
    dd e  = dd_exp_minus_small(r, 40);
    return dd_ldexp(e, -m);
}
static inline dd dd_from_split(double x){
    double xh, xl; split(x, &xh, &xl);
    dd r = {xh, xl};
    return r;
}

/* ---------------------- Polynomial coefficients ---------------------- */

static const dd P_t_DD[15] = {
    { 49.006995503130668,               2.6545877938485625e-15 },
    { -218.41410920766737,              1.0856846568733741e-14 },
    { 362.15572019910832,              -7.1985096569551803e-15 },
    { -287.01784549731411,             -2.7177451380355053e-14 },
    { 215.98523130006109,               1.0204539667856416e-14 },
    { -319.6747716452013,              -2.7778736419462918e-14 },
    { 309.32151239121913,               8.9310496872961097e-15 },
    { -148.40897297675602,             -2.0126588684790277e-15 },
    { 108.39567849229498,               5.1470902505945303e-15 },
    { -128.42449257242512,              4.8556207335910255e-15 },
    { 52.100194565495109,              -3.2475982522323151e-15 },
    { 27.182961753480562,              -1.3720152019821513e-15 },
    { -30.892684655248317,              5.0108778540871665e-16 },
    { 9.7093787947518475,              -3.8070668395354759e-16 },
    { -1.0247896450913392,             -6.4310147348867232e-17 }
};
static const dd Q_t_DD[15] = {
    { 22.798954001249207,              -8.7539435327308824e-16 },
    { -101.61025335110278,             -1.9701453095933502e-16 },
    { 187.71953802474923,               4.3330943763624294e-15 },
    { -238.26512788345983,             -2.8815577216965332e-15 },
    { 343.5556481123333,              -1.9822532755373412e-14 },
    { -477.34560858918263,             -1.6809221219728182e-14 },
    { 470.65283129188964,               2.7459919707678828e-14 },
    { -373.05370118454533,             -8.3104711850257398e-15 },
    { 317.02298340975608,              -2.5746853032378975e-14 },
    { -243.00366934644182,              3.3888066836802741e-15 },
    { 115.01437798970787,               1.7748765489552955e-17 },
    { -21.962170041737416,              5.5451832856193437e-16 },
    { -3.2054989974651682,              1.5971643636866737e-16 },
    { 1.8582106106285154,               1.0067899399548063e-16 },
    { -0.17650862089298841,             1.2770498362192908e-17 }
};

static inline dd dd_horner(const dd* coeffs, size_t count, dd x){
    dd r = coeffs[count - 1];
    for (size_t k = count - 1; k-- > 0; ){ /* from count-2 down to 0 */
        r = dd_add(dd_mul(r, x), coeffs[k]);
    }
    return r;
}

/* ---------------------- Core approximation ---------------------- */

static inline dd core_mul_x(double x){
    dd one = {1.0, 0.0};
    dd xs = dd_from_split(x);
    dd den = dd_add(one, xs);
    dd inv = dd_div(one, den);
    dd t3  = dd_sub(one, inv);
    dd t   = dd_cbrt(t3);
    dd t2  = dd_pow2(t);
    dd sq  = dd_sqrt(inv);
    dd s   = dd_div(t2, sq);
    dd P   = dd_horner(P_t_DD, 15, t);
    dd Q   = dd_horner(Q_t_DD, 15, t);
    dd R   = dd_div(P, Q);
    dd A   = dd_div(R, s);
    return dd_mul(A, xs);
}

static inline double fm_eval(double x, int skip_exp){
    dd base = core_mul_x(x);
    if (skip_exp){
        double hi, lo; quick_two_sum(base.hi, base.lo, &hi, &lo);
        (void)lo;
        return hi;
    }
    dd e = dd_exp_neg(x);
    dd y = dd_mul(base, e);
    double hi, lo; quick_two_sum(y.hi, y.lo, &hi, &lo);
    (void)lo;
    return hi;
}

static inline double fm_skipexp(double x){ return fm_eval(x, 1); }
static inline double fm_with_exp(double x){ return fm_eval(x, 0); }

/* ---------------------- Python wrappers ---------------------- */

static PyObject* py_with_exp(PyObject* self, PyObject* args){
    double x; if(!PyArg_ParseTuple(args,"d",&x)) return NULL;
    return PyFloat_FromDouble(fm_with_exp(x));
}
static PyObject* py_skipexp(PyObject* self, PyObject* args){
    double x; if(!PyArg_ParseTuple(args,"d",&x)) return NULL;
    return PyFloat_FromDouble(fm_skipexp(x));
}

static int parse_inbuf(PyObject* obj, Py_buffer* view){
    int flags = PyBUF_SIMPLE;
    if (PyObject_GetBuffer(obj, view, flags) != 0) return -1;
    if ((view->len % (Py_ssize_t)sizeof(double)) != 0){
        PyErr_SetString(PyExc_ValueError, "input buffer length is not a multiple of 8");
        PyBuffer_Release(view);
        return -1;
    }
    return 0;
}

typedef double (*kernel_t)(double);

static PyObject* run_buf(PyObject* obj, kernel_t fn){
    Py_buffer view;
    if (parse_inbuf(obj, &view) != 0) return NULL;
    size_t n = (size_t)(view.len / (Py_ssize_t)sizeof(double));
    const double* xin = (const double*)view.buf;

    PyObject* ba = alloc_double_bytearray(n);
    if (!ba){ PyBuffer_Release(&view); return NULL; }
    double* out = (double*)PyByteArray_AsString(ba);
    for (size_t i=0;i<n;++i) out[i] = fn(xin[i]);

    PyBuffer_Release(&view);
    return ba;
}

static PyObject* py_with_exp_buf(PyObject* self, PyObject* args){
    PyObject* obj; if(!PyArg_ParseTuple(args,"O",&obj)) return NULL;
    return run_buf(obj, fm_with_exp);
}
static PyObject* py_skipexp_buf(PyObject* self, PyObject* args){
    PyObject* obj; if(!PyArg_ParseTuple(args,"O",&obj)) return NULL;
    return run_buf(obj, fm_skipexp);
}

/* ---------------------- Module def ---------------------- */

static PyMethodDef Methods[] = {
    {"fm_with_exp_strict",     py_with_exp,     METH_VARARGS, "(P/Q)/s * x * exp(-x)"},
    {"fm_skipexp_strict",      py_skipexp,     METH_VARARGS, "(P/Q)/s * x"},
    {"fm_with_exp_opt",        py_with_exp,    METH_VARARGS, "(P/Q)/s * x * exp(-x)"},
    {"fm_skipexp_opt",         py_skipexp,    METH_VARARGS, "(P/Q)/s * x"},
    {"fm_with_exp_strict_buf", py_with_exp_buf, METH_VARARGS, "Array version of fm_with_exp"},
    {"fm_skipexp_strict_buf",  py_skipexp_buf, METH_VARARGS, "Array version of fm_skipexp"},
    {"fm_with_exp_opt_buf",    py_with_exp_buf, METH_VARARGS, "Array version of fm_with_exp"},
    {"fm_skipexp_opt_buf",     py_skipexp_buf, METH_VARARGS, "Array version of fm_skipexp"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef Module = {
    PyModuleDef_HEAD_INIT,
    "_fm",
    "AccurPy FM kernels (double-double, final float64)",
    -1,
    Methods
};

PyMODINIT_FUNC PyInit__fm(void){
    return PyModule_Create(&Module);
}
