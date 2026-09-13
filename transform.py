from math import atan2, cos, sin, tau

from mat import Mat
from vec import Vec

VEC_LOCATION_KEYS = {"x", "y", "u"}
MAT_LOCATION_KEYS = (VEC_LOCATION_KEYS,) * 2
MAT_LOCATION_IDENTITY_3 = Mat(MAT_LOCATION_KEYS, {(k, k): 1 for k in VEC_LOCATION_KEYS})

VEC_COLOR_KEYS = {"r", "g", "b"}
MAT_COLOR_KEYS = (VEC_COLOR_KEYS,) * 2
MAT_COLOR_IDENTITY_3 = Mat(MAT_COLOR_KEYS, {(k, k): 1 for k in VEC_COLOR_KEYS})


def vec_approx_equal(u, v, e=2**-8):
    assert isinstance(u, Vec)
    assert isinstance(v, Vec)
    assert u.D == v.D
    uk = u.f.keys()
    vk = v.f.keys()
    uvk = uk | vk
    return all(abs(u[k] - v[k]) < e for k in uvk)


def mat_approx_equal(A, B, e=2**-8):
    assert isinstance(A, Mat)
    assert isinstance(B, Mat)
    assert A.D == B.D
    uk = A.f.keys()
    vk = B.f.keys()
    uvk = uk | vk
    return all(abs(A[k] - B[k]) < e for k in uvk)


def clone_mat(M):
    return Mat(M.D, M.f.copy())


def identity():
    """
    >>> v = Vec({'x','y','u'}, {'x':5,'y':7,'u':1})
    >>> M = identity()
    >>> M*v == v
    True
    >>> v*M == v
    True
    """
    return clone_mat(MAT_LOCATION_IDENTITY_3)


def translation(alpha, beta):
    """
    >>> v = Vec({'x','y','u'}, {'x':5,'y':7,'u':1})
    >>> M = translation(1, 2)
    >>> M*v == Vec({'x','y','u'}, {'x':6,'y':9,'u':1})
    True
    """
    M = identity()
    M["x", "u"] = alpha
    M["y", "u"] = beta
    return M


def scale(alpha, beta):
    """
    >>> v = Vec({'x','y','u'}, {'x':5,'y':7,'u':1})
    >>> M = scale(2, 3)
    >>> M*v == Vec({'x','y','u'}, {'x':10,'y':21,'u':1})
    True
    """
    return Mat(
        MAT_LOCATION_KEYS,
        {
            ("x", "x"): alpha,
            ("y", "y"): beta,
            ("u", "u"): 1,
        },
    )


def rotation(theta):
    """
    >>> v = Vec({'x','y','u'}, {'x':5,'y':7,'u':1})
    >>> M = rotation(tau / 4)
    >>> vec_approx_equal(M*v, Vec({'x','y','u'}, {'x':-7,'y':5,'u':1}))
    True
    """
    return Mat(
        MAT_LOCATION_KEYS,
        {
            ("x", "x"): cos(theta),
            ("x", "y"): -sin(theta),
            ("y", "x"): sin(theta),
            ("y", "y"): cos(theta),
            ("u", "u"): 1,
        },
    )


def rotation_about(theta, x, y):
    """
    >>> v = Vec({'x','y','u'}, {'x':5,'y':7,'u':1})
    >>> M = rotation_about(tau / 4, 1, 2)
    >>> vec_approx_equal(M*v, Vec({'x','y','u'}, {'x':1-(7-2),'y':2+(5-1),'u':1}))
    True
    """
    return translation(x, y) * rotation(theta) * translation(-x, -y)


def reflect_y():
    return scale(1, -1)


def reflect_x():
    return scale(-1, 1)


def scale_color(r, g, b):
    return Mat(
        MAT_COLOR_KEYS,
        {
            ("r", "r"): r,
            ("g", "g"): g,
            ("b", "b"): b,
        },
    )


def grayscale():
    return Mat(
        MAT_COLOR_KEYS,
        {
            ("r", "r"): 77 / 256,
            ("r", "g"): 151 / 256,
            ("r", "b"): 28 / 256,
            ("g", "r"): 77 / 256,
            ("g", "g"): 151 / 256,
            ("g", "b"): 28 / 256,
            ("b", "r"): 77 / 256,
            ("b", "g"): 151 / 256,
            ("b", "b"): 28 / 256,
        },
    )


def reflect_about(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dt = atan2(dy, dx)
    return (
        translation(dx, dy)
        * rotation(dt)
        * reflect_y()
        * rotation(-dt)
        * translation(-dx, -dy)
    )
