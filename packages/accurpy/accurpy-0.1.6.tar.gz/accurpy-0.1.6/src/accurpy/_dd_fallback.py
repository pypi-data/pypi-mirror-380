# -*- coding: utf-8 -*-
"""Python double-double fallback implementation."""

import math

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


def _dd_add(a_hi, a_lo, b_hi, b_lo):
    s, e = _two_sum(a_hi, b_hi)
    t, f = _two_sum(a_lo, b_lo)
    e, e2 = _quick_two_sum(e, t)
    s, e3 = _quick_two_sum(s, e)
    lo = e2 + f + e3
    hi, lo2 = _quick_two_sum(s, lo)
    return hi, lo2


def _dd_sub(a_hi, a_lo, b_hi, b_lo):
    return _dd_add(a_hi, a_lo, -b_hi, -b_lo)


def _dd_mul(a_hi, a_lo, b_hi, b_lo):
    p, err = _two_prod(a_hi, b_hi)
    err += a_hi * b_lo + a_lo * b_hi
    hi, lo = _quick_two_sum(p, err)
    return hi, lo


def _dd_div_two_corrections(a_hi, a_lo, b_hi, b_lo):
    q1 = a_hi / b_hi
    p1, p2 = _two_prod(q1, b_hi)
    p2 += q1 * b_lo
    r1h, r1l = _dd_sub(a_hi, a_lo, p1, p2)
    q2 = (r1h + r1l) / b_hi
    qh, ql = _quick_two_sum(q1, q2)
    p1, p2 = _two_prod(qh, b_hi)
    p2 += qh * b_lo
    r2h, r2l = _dd_sub(a_hi, a_lo, p1, p2)
    q3 = (r2h + r2l) / b_hi
    qh, ql = _quick_two_sum(qh, q3)
    return qh, ql


def _dd_pow2(h, l):
    return _dd_mul(h, l, h, l)


def _dd_pow3(h, l):
    a, b = _dd_mul(h, l, h, l)
    return _dd_mul(a, b, h, l)


def _dd_cbrt_dd(a_hi, a_lo):
    y = a_hi ** (1.0 / 3.0)
    yh, yl = y, 0.0
    for _ in range(3):
        y3h, y3l = _dd_pow3(yh, yl)
        rh, rl = _dd_sub(y3h, y3l, a_hi, a_lo)
        y2h, y2l = _dd_pow2(yh, yl)
        dh, dl = _dd_add(y2h, y2l, y2h, y2l)
        dh, dl = _dd_add(dh, dl, y2h, y2l)  # 3*y^2
        d1h, d1l = _dd_div_two_corrections(rh, rl, dh, dl)
        yh, yl = _dd_sub(yh, yl, d1h, d1l)
    return yh, yl


def _dd_sqrt(a_hi, a_lo):
    y = math.sqrt(a_hi)
    yh, yl = y, 0.0
    for _ in range(3):
        invh, invl = _dd_div_two_corrections(a_hi, a_lo, yh, yl)
        tmp_h, tmp_l = _dd_add(yh, yl, invh, invl)
        yh, yl = _dd_mul(0.5, 0.0, tmp_h, tmp_l)
    return yh, yl


def _dd_horner(coeffs, xh, xl):
    rh, rl = coeffs[-1]
    for k in range(len(coeffs) - 2, -1, -1):
        ph, pl = _dd_mul(rh, rl, xh, xl)
        ah, al = coeffs[k]
        rh, rl = _dd_add(ph, pl, ah, al)
    return rh, rl


def _dd_ldexp(a_hi, a_lo, k):
    return _dd_mul(a_hi, a_lo, math.ldexp(1.0, k), 0.0)


LN2_HI = 6.93147180369123816490e-01
LN2_LO = 1.90821492927058770002e-10
INV_LN2 = 1.4426950408889634073599246810018921


def _dd_exp_minus_small_horner(rh, rl, terms=40):
    coeffs = [1.0]
    c = 1.0
    for k in range(1, terms + 1):
        c /= k
        coeffs.append(c)
    eh, el = coeffs[terms], 0.0
    for k in range(terms - 1, -1, -1):
        ph, pl = _dd_mul(eh, el, -rh, -rl)
        eh, el = _dd_add(ph, pl, coeffs[k], 0.0)
    return eh, el


def _dd_exp_neg(x: float):
    m = int(round(x * INV_LN2))
    mh, ml = _split(float(m))
    t1h, t1l = _dd_mul(mh, ml, LN2_HI, 0.0)
    t2h, t2l = _dd_mul(mh, ml, LN2_LO, 0.0)
    th, tl = _dd_add(t1h, t1l, t2h, t2l)
    rh, rl = _dd_sub(x, 0.0, th, tl)
    eh, el = _dd_exp_minus_small_horner(rh, rl, terms=40)
    return _dd_ldexp(eh, el, -m)


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


def _core_dd(x: float):
    x = float(x)
    xh, xl = _split(x)
    denh, denl = _dd_add(1.0, 0.0, xh, xl)
    invh, invl = _dd_div_two_corrections(1.0, 0.0, denh, denl)
    t3h, t3l = _dd_sub(1.0, 0.0, invh, invl)
    th, tl = _dd_cbrt_dd(t3h, t3l)
    t2h, t2l = _dd_pow2(th, tl)
    sqh, sql = _dd_sqrt(invh, invl)
    sh, sl = _dd_div_two_corrections(t2h, t2l, sqh, sql)
    Ph, Pl = _dd_horner(P_t_dd_pairs, th, tl)
    Qh, Ql = _dd_horner(Q_t_dd_pairs, th, tl)
    Rh, Rl = _dd_div_two_corrections(Ph, Pl, Qh, Ql)
    return _dd_div_two_corrections(Rh, Rl, sh, sl)


def syncF(x: float, skip_exp: bool = False) -> float:
    Ah, Al = _core_dd(x)
    xh, xl = _split(float(x))
    Bh, Bl = _dd_mul(Ah, Al, xh, xl)
    if skip_exp:
        hi, lo = _quick_two_sum(Bh, Bl)
        return float(hi)
    Eh, El = _dd_exp_neg(float(x))
    Yh, Yl = _dd_mul(Bh, Bl, Eh, El)
    hi, lo = _quick_two_sum(Yh, Yl)
    return float(hi)
