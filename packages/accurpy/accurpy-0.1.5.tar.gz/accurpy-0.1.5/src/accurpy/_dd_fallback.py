# -*- coding: utf-8 -*-
# Python DD fallback (STRICT) – new approach without u-map

import math
from math import copysign, fabs, ldexp, sqrt

_SPLITTER = 134217729.0  # 2^27 + 1

def _two_sum(a: float, b: float):
    s = a + b
    bb = s - a
    err = (a - (s - bb)) + (b - bb)
    return s, err

def _quick_two_sum(a: float, b: float):
    s = a + b
    return s, b - (s - a)

def _split(a: float):
    c = _SPLITTER * a
    a_hi = c - (c - a)
    a_lo = a - a_hi
    return a_hi, a_lo

def _two_prod(a: float, b: float):
    p = a * b
    a_hi, a_lo = _split(a)
    b_hi, b_lo = _split(b)
    err = ((a_hi * b_hi - p) + a_hi * b_lo + a_lo * b_hi) + a_lo * b_lo
    return p, err

def _dd_normalize(hi: float, lo: float):
    s, e = _two_sum(hi, lo)
    return s, e

def _dd_add_dd(a_hi, a_lo, b_hi, b_lo):
    s, e = _two_sum(a_hi, b_hi)
    t, f = _two_sum(a_lo, b_lo)
    e, e2 = _quick_two_sum(e, t)
    s, e3 = _quick_two_sum(s, e)
    lo = e2 + f + e3
    hi, lo2 = _quick_two_sum(s, lo)
    return hi, lo2

def _dd_add_d(a_hi, a_lo, c):
    s, e = _two_sum(a_hi, c)
    return _dd_normalize(s, a_lo + e)

def _dd_sub_dd(a_hi, a_lo, b_hi, b_lo):
    return _dd_add_dd(a_hi, a_lo, -b_hi, -b_lo)

def _dd_mul_d(a_hi, a_lo, x):
    p, pe = _two_prod(a_hi, x)
    q = a_lo * x
    s, se = _two_sum(pe, q)
    hi, lo = _two_sum(p, s)
    return _dd_normalize(hi, lo + se)

def _dd_mul_dd(a_hi, a_lo, b_hi, b_lo):
    p, pe = _two_prod(a_hi, b_hi)
    pe += a_hi * b_lo + a_lo * b_hi
    hi, lo = _quick_two_sum(p, pe)
    return hi, lo

def _dd_div_two_corrections(a_hi, a_lo, b_hi, b_lo):
    q1 = a_hi / b_hi
    p1, p2 = _two_prod(q1, b_hi)
    p2 += q1 * b_lo
    r1h, r1l = _dd_sub_dd(a_hi, a_lo, p1, p2)
    q2 = (r1h + r1l) / b_hi
    qh, ql = _quick_two_sum(q1, q2)
    p1, p2 = _two_prod(qh, b_hi)
    p2 += qh * b_lo
    r2h, r2l = _dd_sub_dd(a_hi, a_lo, p1, p2)
    q3 = (r2h + r2l) / b_hi
    qh, ql = _quick_two_sum(qh, q3)
    return qh, ql

def _dd_div_d(a_hi, a_lo, d):
    q1 = a_hi / d
    t_hi, t_lo = _dd_mul_d(d, 0.0, q1)
    r_hi, r_lo = _dd_sub_dd(a_hi, a_lo, t_hi, t_lo)
    q2 = (r_hi + r_lo) / d
    return _dd_add_d(q1, 0.0, q2)

def _dd_ldexp(a_hi, a_lo, n):
    return _dd_normalize(ldexp(a_hi, n), ldexp(a_lo, n))

def _dd_to_double_rn(hi, lo):
    s, _ = _two_sum(hi, lo)
    return s

def _dd_pow2(h, l):
    return _dd_mul_dd(h, l, h, l)

def _dd_pow3(h, l):
    a, b = _dd_mul_dd(h, l, h, l)
    return _dd_mul_dd(a, b, h, l)

def _dd_cbrt(v):
    y = v ** (1.0/3.0)
    yh, yl = y, 0.0
    for _ in range(2):
        y3h, y3l = _dd_pow3(yh, yl)
        rh, rl = _dd_sub_dd(y3h, y3l, v, 0.0)
        y2h, y2l = _dd_pow2(yh, yl)
        dh, dl = _dd_add_dd(y2h, y2l, y2h, y2l)
        dh, dl = _dd_add_dd(dh, dl, y2h, y2l)  # 3*y^2
        d1h, d1l = _dd_div_two_corrections(rh, rl, dh, dl)
        yh, yl = _dd_sub_dd(yh, yl, d1h, d1l)
    return yh, yl

def _dd_sqrt(ah, al):
    y = sqrt(ah)
    yh, yl = y, 0.0
    for _ in range(2):
        ih, il = _dd_div_two_corrections(ah, al, yh, yl)
        tmp_h, tmp_l = _dd_add_dd(yh, yl, ih, il)
        yh, yl = _dd_mul_dd(0.5, 0.0, tmp_h, tmp_l)
    return yh, yl

def _dd_horner_ddx(coeff_hi_lo, xh, xl):
    rh, rl = coeff_hi_lo[-1]
    for k in range(len(coeff_hi_lo)-2, -1, -1):
        ph, pl = _dd_mul_dd(rh, rl, xh, xl)
        ah, al = coeff_hi_lo[k]
        rh, rl = _dd_add_dd(ph, pl, ah, al)
    return rh, rl

# New t-polynomials (14,14) in double-double (low->high)
P_t_dd_pairs = [
  [49.006995503130668, 2.6545877938485625e-15],
  [-218.41410920766737, 1.0856846568733741e-14],
  [362.15572019910832, -7.1985096569551803e-15],
  [-287.01784549731411, -2.7177451380355053e-14],
  [215.98523130006109, 1.0204539667856416e-14],
  [-319.6747716452013, -2.7778736419462918e-14],
  [309.32151239121913, 8.9310496872961097e-15],
  [-148.40897297675602, -2.0126588684790277e-15],
  [108.39567849229498, 5.1470902505945303e-15],
  [-128.42449257242512, 4.8556207335910255e-15],
  [52.100194565495109, -3.2475982522323151e-15],
  [27.182961753480562, -1.3720152019821513e-15],
  [-30.892684655248317, 5.0108778540871665e-16],
  [9.7093787947518475, -3.8070668395354759e-16],
  [-1.0247896450913392, -6.4310147348867232e-17],
]
Q_t_dd_pairs = [
  [22.798954001249207, -8.7539435327308824e-16],
  [-101.61025335110278, -1.9701453095933502e-16],
  [187.71953802474923, 4.3330943763624294e-15],
  [-238.26512788345983, -2.8815577216965332e-15],
  [343.5556481123333, -1.9822532755373412e-14],
  [-477.34560858918263, -1.6809221219728182e-14],
  [470.65283129188964, 2.7459919707678828e-14],
  [-373.05370118454533, -8.3104711850257398e-15],
  [317.02298340975608, -2.5746853032378975e-14],
  [-243.00366934644182, 3.3888066836802741e-15],
  [115.01437798970787, 1.7748765489552955e-17],
  [-21.962170041737416, 5.5451832856193437e-16],
  [-3.2054989974651682, 1.5971643636866737e-16],
  [1.8582106106285154, 1.0067899399548063e-16],
  [-0.17650862089298841, 1.2770498362192908e-17],
]

# Core DD: A_old(x) = (P/Q)/s (no u-map)
def _approx_old_R_over_s_dd_hi_lo(x):
    x = float(x)
    # t^3 = x/(1+x)
    denh, denl = _dd_add_dd(1.0, 0.0, x, 0.0)
    t3h, t3l = _dd_div_two_corrections(x, 0.0, denh, denl)
    # t = cbrt(t^3)
    th, tl = _dd_cbrt(t3h + t3l)
    # s(t) = t^2 / sqrt(1 - t^3)
    t2h, t2l = _dd_pow2(th, tl)
    omh, oml = _dd_sub_dd(1.0, 0.0, t3h, t3l)
    sqh, sql = _dd_sqrt(omh, oml)
    sh, sl = _dd_div_two_corrections(t2h, t2l, sqh, sql)
    # R(t) = P_t(t)/Q_t(t)
    Ph, Pl = _dd_horner_ddx(P_t_dd_pairs, th, tl)
    Qh, Ql = _dd_horner_ddx(Q_t_dd_pairs, th, tl)
    Rh, Rl = _dd_div_two_corrections(Ph, Pl, Qh, Ql)
    # A_old = (P/Q)/s
    Ah, Al = _dd_div_two_corrections(Rh, Rl, sh, sl)
    return Ah, Al

def syncF(x: float, skip_exp: bool = False) -> float:
    """
    DD pipeline -> float64.
    Uses FM(skip_exp=True)  = A_old(x) * x
         FM(skip_exp=False) = A_old(x) * x * exp(-x)
    """
    Ah, Al = _approx_old_R_over_s_dd_hi_lo(x)
    base = Ah + Al
    if skip_exp:
        return float(base * float(x))
    else:
        return float(base * float(x) * math.exp(-float(x)))  # may underflow at huge x by definition
