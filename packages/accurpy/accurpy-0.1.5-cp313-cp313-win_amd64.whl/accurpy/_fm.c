
// src/accurpy/_fm.c
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <math.h>
#include <stdint.h>
#include <stddef.h>
#include <string.h>

#ifndef M_PI
#define M_PI 3.141592653589793238462643383279502884
#endif

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

/* ---------------------- Double-double core (STRICT) ---------------------- */

typedef struct { double hi, lo; } dd;
static const dd DD_HALF = {0.5, 0.0};
static const double SPLITTER = 134217729.0; /* 2^27+1 */

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
static inline dd dd_add_dd(dd A, dd B){
    double s, e; two_sum(A.hi, B.hi, &s, &e);
    double t, f; two_sum(A.lo, B.lo, &t, &f);
    double e_new, e2; quick_two_sum(e, t, &e_new, &e2);
    double s_new, e3; quick_two_sum(s, e_new, &s_new, &e3);
    double lo = e2 + f + e3;
    double hi, lo2; quick_two_sum(s_new, lo, &hi, &lo2);
    dd r = {hi, lo2};
    return r;
}
static inline dd dd_add_d(dd A, double c){
    double s, e; two_sum(A.hi, c, &s, &e);
    return dd_norm(s, A.lo + e);
}
static inline dd dd_sub_dd(dd A, dd B){
    dd nB = { -B.hi, -B.lo };
    return dd_add_dd(A, nB);
}
static inline dd dd_mul_d_strict(dd A, double x){
    double p, pe; two_prod(A.hi, x, &p, &pe);
    double q = A.lo * x;
    double s, se; two_sum(pe, q, &s, &se);
    double hi, lo; two_sum(p, s, &hi, &lo);
    return dd_norm(hi, lo + se);
}
static inline dd dd_mul_dd_strict(dd A, dd B){
    double p, pe; two_prod(A.hi, B.hi, &p, &pe);
    pe += A.hi * B.lo + A.lo * B.hi;
    double hi, lo; two_sum(p, pe, &hi, &lo);
    return dd_norm(hi, lo);
}
static inline dd dd_div_two_corrections_strict(dd A, dd B){
    double q1 = A.hi / B.hi;
    double p1, p2; two_prod(q1, B.hi, &p1, &p2);
    p2 += q1 * B.lo;
    dd r1 = dd_sub_dd(A, (dd){p1, p2});
    double q2 = (r1.hi + r1.lo) / B.hi;
    double qh, ql; quick_two_sum(q1, q2, &qh, &ql);
    two_prod(qh, B.hi, &p1, &p2);
    p2 += qh * B.lo;
    dd r2 = dd_sub_dd(A, (dd){p1, p2});
    double q3 = (r2.hi + r2.lo) / B.hi;
    quick_two_sum(qh, q3, &qh, &ql);
    dd r = {qh, ql};
    return r;
}
static inline dd dd_div_d_strict(dd A, double d){
    double q1 = A.hi / d;
    dd t = dd_mul_d_strict((dd){d, 0.0}, q1);
    dd r = dd_sub_dd(A, t);
    double q2 = (r.hi + r.lo) / d;
    return dd_add_d((dd){q1, 0.0}, q2);
}
static inline dd dd_ldexp_strict(dd A, int n){
    return dd_norm(ldexp(A.hi, n), ldexp(A.lo, n));
}
static inline double dd_to_double_rn(dd A){
    double s, e; two_sum(A.hi, A.lo, &s, &e);
    (void)e; return s;
}
static inline dd dd_sqrt_one_step(double a){
    double y = sqrt(a);
    dd ydd = (dd){ y, 0.0 };
    dd ay  = dd_div_two_corrections_strict((dd){a, 0.0}, ydd);
    dd s   = dd_add_dd(ydd, ay);
    return dd_mul_dd_strict(s, DD_HALF);
}
static inline double cbrt_seed(double x){
    double ax = x < 0 ? -x : x;
    double y = pow(ax, 1.0/3.0);
    return x < 0 ? -y : y;
}
static inline dd dd_pow2(dd a){
    return dd_mul_dd_strict(a, a);
}

static inline dd dd_pow3(dd a){
    dd a2 = dd_mul_dd_strict(a, a);
    return dd_mul_dd_strict(a2, a);
}

static inline dd dd_cbrt(dd a){
    double y0 = cbrt_seed(a.hi);
    dd y = (dd){ y0, 0.0 };
    for (int i=0;i<2;i++){
        dd y3 = dd_pow3(y);
        dd num = dd_sub_dd(y3, a);
        dd y2 = dd_pow2(y);
        dd den = dd_add_dd(dd_add_dd(y2, y2), y2);  // 3*y^2
        dd corr = dd_div_two_corrections_strict(num, den);
        y = dd_sub_dd(y, corr);
    }
    return y;
}

static inline dd dd_sqrt(dd a){
    double y0 = sqrt(a.hi);
    dd y = (dd){ y0, 0.0 };
    for (int i=0;i<2;i++){
        dd inv = dd_div_two_corrections_strict(a, y);
        dd sum = dd_add_dd(y, inv);
        y = dd_mul_dd_strict(sum, DD_HALF);
    }
    return y;
}

/* ---------------------- Double-double (OPT path) ---------------------- */

static inline dd dd_add_dd_opt(dd A, dd B){
    return dd_add_dd(A,B);
}
static inline dd dd_add_d_opt(dd A, double c){
    return dd_add_d(A,c);
}
static inline dd dd_mul_dd_opt(dd A, dd B){
    double p1 = A.hi * B.hi;
    double p2 = fma(A.hi, B.hi, -p1);
    p2 += A.hi * B.lo + A.lo * B.hi;
    double s1 = p1 + p2;
    double s2 = p2 - (s1 - p1);
    return dd_norm(s1, s2);
}
static inline dd dd_mul_d_opt(dd A, double x){
    double p1 = A.hi * x;
    double p2 = fma(A.hi, x, -p1);
    p2 += A.lo * x;
    double s1 = p1 + p2;
    double s2 = p2 - (s1 - p1);
    return dd_norm(s1, s2);
}
static inline dd dd_div_dd_opt(dd A, dd B){
    double q1 = A.hi / B.hi;
    dd t = dd_mul_d_opt(B, q1);
    dd r = dd_sub_dd(A, t);
    double q2 = (r.hi + r.lo) / B.hi;
    double s1 = q1 + q2;
    double s2 = q2 - (s1 - q1);
    return dd_norm(s1, s2);
}
static inline dd dd_div_d_opt(dd A, double d){
    double q1 = A.hi / d;
    dd t = (dd){ q1 * d, 0.0 };
    dd r = dd_sub_dd(A, t);
    double q2 = (r.hi + r.lo) / d;
    double s1 = q1 + q2;
    double s2 = q2 - (s1 - q1);
    return dd_norm(s1, s2);
}
static inline dd dd_ldexp_opt(dd A, int n){
    return dd_norm(ldexp(A.hi, n), ldexp(A.lo, n));
}
static inline dd dd_cbrt_one_step(dd a){
    double y0 = cbrt(a.hi);
    dd y = (dd){ y0, 0.0 };
    dd y2 = dd_mul_dd_opt(y,y);
    dd y3 = dd_mul_dd_opt(y2,y);
    dd num = dd_sub_dd(y3, a);
    dd den = dd_mul_d_opt(y2, 3.0);
    dd corr = dd_div_dd_opt(num, den);
    y = dd_sub_dd(y, corr);
    return y;
}

/* ---------------------- Coefficients ---------------------- */

typedef struct { double hi, lo; } ddcoef;
// New t-polynomials (14,14) in double-double (low->high)
static const ddcoef P_t_DD[15] = {
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
static const ddcoef Q_t_DD[15] = {
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

static inline dd dd_from_coef(ddcoef c){ dd r = {c.hi, c.lo}; return r; }

static inline dd dd_horner_ddx(const ddcoef* c, dd x){
    dd r = dd_from_coef(c[14]);
    for (int k = 13; k >= 0; k--){
        dd p = dd_mul_dd_strict(r, x);
        dd a = dd_from_coef(c[k]);
        r = dd_add_dd(p, a);
    }
    return r;
}

/* ---------------------- exp(-x) in DD ---------------------- */

static const double LOG2E = 1.44269504088896340735992468100189214;
static const double LN2_HI = 0.693147180559945309417232121458176568;
static const double LN2_LO = 2.319046813846299558417771099e-17;

static inline dd dd_exp_reduced_strict(dd r){
    static const double INV_FACT[23] = {
      1.0,1.0,5e-1,1.6666666666666667e-1,4.1666666666666667e-2,8.3333333333333333e-3,
      1.3888888888888889e-3,1.9841269841269841e-4,2.4801587301587302e-5,2.7557319223985891e-6,
      2.7557319223985891e-7,2.5052108385441719e-8,2.0876756987868099e-9,1.6059043836821615e-10,
      1.1470745597729725e-11,7.6471637318198165e-13,4.7794773323873853e-14,2.8114572543455208e-15,
      1.5619206968586226e-16,8.2206352466243297e-18,4.1103176233121649e-19,1.9572941063391261e-20,
      8.8967913924505733e-22
    };
    dd val = (dd){ INV_FACT[22], 0.0 };
    for (int k=21;k>=0;--k){
        val = dd_mul_dd_strict(val, r);
        val = dd_add_d(val, INV_FACT[k]);
    }
    return val;
}
static inline dd dd_exp_reduced_opt(dd r){
    static const double INV_FACT[23] = {
      1.0,1.0,5e-1,1.6666666666666667e-1,4.1666666666666667e-2,8.3333333333333333e-3,
      1.3888888888888889e-3,1.9841269841269841e-4,2.4801587301587302e-5,2.7557319223985891e-6,
      2.7557319223985891e-7,2.5052108385441719e-8,2.0876756987868099e-9,1.6059043836821615e-10,
      1.1470745597729725e-11,7.6471637318198165e-13,4.7794773323873853e-14,2.8114572543455208e-15,
      1.5619206968586226e-16,8.2206352466243297e-18,4.1103176233121649e-19,1.9572941063391261e-20,
      8.8967913924505733e-22
    };
    dd val = (dd){ INV_FACT[22], 0.0 };
    for (int k=21;k>=0;--k){
        val = dd_mul_dd_opt(val, r);
        val = dd_add_d_opt(val, INV_FACT[k]);
    }
    return val;
}

static inline dd dd_exp_neg_strict(double x){
    double y = -x;
    int n = nint_tieeven(y * LOG2E);
    dd r = dd_sub_dd((dd){y,0.0}, dd_mul_d_strict((dd){LN2_HI,0.0}, n));
    r = dd_sub_dd(r, dd_mul_d_strict((dd){LN2_LO,0.0}, n));
    dd er = dd_exp_reduced_strict(r);
    return dd_ldexp_strict(er, n);
}
static inline dd dd_exp_neg_opt(double x){
    double y = -x;
    int n = nint_tieeven(y * LOG2E);
    dd r = dd_sub_dd((dd){y,0.0}, dd_mul_d_opt((dd){LN2_HI,0.0}, n));
    r = dd_sub_dd(r, dd_mul_d_opt((dd){LN2_LO,0.0}, n));
    dd er = dd_exp_reduced_opt(r);
    return dd_ldexp_opt(er, n);
}

/* ---------------------- Core map (STRICT / OPT) ---------------------- */

// Core DD: A_old(x) = (P/Q)/s (no u-map)
static inline dd approx_old_R_over_s_dd_strict(double x){
    // t^3 = x/(1+x)
    dd one_plus_x = dd_add_d((dd){x, 0.0}, 1.0);
    dd t3 = dd_div_two_corrections_strict((dd){x, 0.0}, one_plus_x);
    // t = cbrt(t^3)
    dd t = dd_cbrt(t3);
    // s(t) = t^2 / sqrt(1 - t^3)
    dd t2 = dd_pow2(t);
    dd om = dd_sub_dd((dd){1.0, 0.0}, t3);
    dd sq = dd_sqrt(om);
    dd s = dd_div_two_corrections_strict(t2, sq);
    // R(t) = P_t(t)/Q_t(t)
    dd P = dd_horner_ddx(P_t_DD, t);
    dd Q = dd_horner_ddx(Q_t_DD, t);
    dd R = dd_div_two_corrections_strict(P, Q);
    // A_old = (P/Q)/s
    return dd_div_two_corrections_strict(R, s);
}

static inline dd approx_old_R_over_s_dd_opt(double x){
    // t^3 = x/(1+x)
    dd one_plus_x = dd_add_d_opt((dd){x, 0.0}, 1.0);
    dd t3 = dd_div_dd_opt((dd){x, 0.0}, one_plus_x);
    // t = cbrt(t^3)
    dd t = dd_cbrt_one_step(t3);
    // s(t) = t^2 / sqrt(1 - t^3)
    dd t2 = dd_mul_dd_opt(t, t);
    dd om = dd_sub_dd((dd){1.0, 0.0}, t3);
    dd sq = dd_sqrt_one_step(om.hi);
    dd s = dd_div_dd_opt(t2, sq);
    // R(t) = P_t(t)/Q_t(t)
    dd P = dd_horner_ddx(P_t_DD, t);
    dd Q = dd_horner_ddx(Q_t_DD, t);
    dd R = dd_div_dd_opt(P, Q);
    // A_old = (P/Q)/s
    return dd_div_dd_opt(R, s);
}

/* ---------------------- Public kernels ---------------------- */

static inline double fm_with_exp_strict(double x){
    dd core = approx_old_R_over_s_dd_strict(x);
    double base = core.hi + core.lo;
    return base * x * exp(-x);  // may underflow at huge x by definition
}
static inline double fm_skipexp_strict(double x){
    dd core = approx_old_R_over_s_dd_strict(x);
    double base = core.hi + core.lo;
    return base * x;
}
static inline double fm_with_exp_opt(double x){
    dd core = approx_old_R_over_s_dd_opt(x);
    double base = core.hi + core.lo;
    return base * x * exp(-x);  // may underflow at huge x by definition
}
static inline double fm_skipexp_opt(double x){
    dd core = approx_old_R_over_s_dd_opt(x);
    double base = core.hi + core.lo;
    return base * x;
}

/* ---------------------- Python wrappers (scalar) ---------------------- */

static PyObject* py_with_exp_strict(PyObject* self, PyObject* args){
    double x; if(!PyArg_ParseTuple(args,"d",&x)) return NULL;
    return PyFloat_FromDouble(fm_with_exp_strict(x));
}
static PyObject* py_skipexp_strict(PyObject* self, PyObject* args){
    double x; if(!PyArg_ParseTuple(args,"d",&x)) return NULL;
    return PyFloat_FromDouble(fm_skipexp_strict(x));
}
static PyObject* py_with_exp_opt(PyObject* self, PyObject* args){
    double x; if(!PyArg_ParseTuple(args,"d",&x)) return NULL;
    return PyFloat_FromDouble(fm_with_exp_opt(x));
}
static PyObject* py_skipexp_opt(PyObject* self, PyObject* args){
    double x; if(!PyArg_ParseTuple(args,"d",&x)) return NULL;
    return PyFloat_FromDouble(fm_skipexp_opt(x));
}

/* ---------------------- Python wrappers (buffer arrays) ---------------------- */

static int parse_inbuf(PyObject* obj, Py_buffer* view){
    int flags = PyBUF_SIMPLE;
    if(PyObject_GetBuffer(obj, view, flags) != 0) return -1;
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

static PyObject* py_with_exp_strict_buf(PyObject* self, PyObject* args){
    PyObject* obj; if(!PyArg_ParseTuple(args,"O",&obj)) return NULL;
    return run_buf(obj, fm_with_exp_strict);
}
static PyObject* py_skipexp_strict_buf(PyObject* self, PyObject* args){
    PyObject* obj; if(!PyArg_ParseTuple(args,"O",&obj)) return NULL;
    return run_buf(obj, fm_skipexp_strict);
}
static PyObject* py_with_exp_opt_buf(PyObject* self, PyObject* args){
    PyObject* obj; if(!PyArg_ParseTuple(args,"O",&obj)) return NULL;
    return run_buf(obj, fm_with_exp_opt);
}
static PyObject* py_skipexp_opt_buf(PyObject* self, PyObject* args){
    PyObject* obj; if(!PyArg_ParseTuple(args,"O",&obj)) return NULL;
    return run_buf(obj, fm_skipexp_opt);
}

/* ---------------------- Module def ---------------------- */

static PyMethodDef Methods[] = {
    {"fm_with_exp_strict",      py_with_exp_strict,      METH_VARARGS, "STRICT: (P/Q)/s * x * exp(-x)"},
    {"fm_skipexp_strict",       py_skipexp_strict,       METH_VARARGS, "STRICT: (P/Q)/s * x"},
    {"fm_with_exp_opt",         py_with_exp_opt,         METH_VARARGS, "OPT:    (P/Q)/s * x * exp(-x)"},
    {"fm_skipexp_opt",          py_skipexp_opt,          METH_VARARGS, "OPT:    (P/Q)/s * x"},

    {"fm_with_exp_strict_buf",  py_with_exp_strict_buf,  METH_VARARGS, "STRICT array: input buffer of float64, return bytearray of float64"},
    {"fm_skipexp_strict_buf",   py_skipexp_strict_buf,   METH_VARARGS, "STRICT array: input buffer of float64, return bytearray of float64"},
    {"fm_with_exp_opt_buf",     py_with_exp_opt_buf,     METH_VARARGS, "OPT array:    input buffer of float64, return bytearray of float64"},
    {"fm_skipexp_opt_buf",      py_skipexp_opt_buf,      METH_VARARGS, "OPT array:    input buffer of float64, return bytearray of float64"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef Module = {
    PyModuleDef_HEAD_INIT,
    "_fm",
    "AccurPy FM_new kernels (STRICT ≤1 ULP, OPT fast)",
    -1,
    Methods
};

PyMODINIT_FUNC PyInit__fm(void){
    return PyModule_Create(&Module);
}
