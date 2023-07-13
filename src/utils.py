import numpy as np

def approximate_x0(x0 : float) -> tuple[bool, bool, bool]:
    """
    N(a) = ( a1, a2, a3 ) @ ( 2^-1, 2^-2, 2^-3) , a = ( a1, a2, a3) belongs to {0, 1}^3

    find a that best approximate x0 i.e min(N(a) - x0)**2)

    params: 
        x0 (float) : number to approximate

    returns:
        a (tuple[bool, bool, bool]) : boolean tuple minimize | N(a) - x0 |
    """

    N = lambda a : a @ np.array([1/2, 1/4, 1/8])
    C = lambda a : abs( N(a) - x0 )

    A = np.array([list(format(i, '03b')) for i in range(8)], dtype=int)
    cost = [ C(a) for a in A ] 
    a = A[np.argmin(cost)]

    print("x0 : ", x0)
    print("a : ", a)
    print("N(a) : ", N(a))
    print("C(a) : ", C(a))
    
    return a


def approximate_x1(x1 : float) -> tuple[bool, bool, bool, bool]:
    """
    M(b) = ( b0, b1, b2, b3 ) @ ( 2^-2, 2^-3, 2^-4, 0) , b = ( b0, b1, b2, b3) belongs to {0, 1}^4

    find a that best approximate x1 i.e min(M(b) - x1)**2)

    params: 
        x1 (float) : number to approximate

    returns:
        b (tuple[bool, bool, bool, bool]) : boolean tuple minimize | M(b) - x1 |
    """

    M = lambda b : b @ np.array([1/4, 1/8, 1/16, 0])
    C = lambda b : abs( M(b) - x1 )

    B = np.array([list(format(i, '04b')) for i in range(16)], dtype=int)
    cost = [ C(b) for b in B ] 
    b = B[np.argmin(cost)]

    print("x1 : ", x1)
    print("b : ", b)
    print("M(b) : ", M(b))
    print("C(b) : ", C(b))
    
    return b


a = approximate_x0(0.234)
b = approximate_x1(0.0324)