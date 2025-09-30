import numpy as np
from sympy import symbols, matrices, Expr, Poly
from scipy import optimize, linalg

# Matrix B from eq. (7)
CONSTRAINT_MATRIX = np.array([
    [0, 0, 0, -2],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [-2, 0, 0, 0]
])

def compute_moments(z_data: np.ndarray) -> np.ndarray:
    """
    Calculate the moments as defined in eq. 6.
    """
    # Split out data into x (real), y (imag), and z (x**2 + y**2)
    x = z_data.real
    y = z_data.imag
    z = x*x + y*y
    n = np.shape(z_data)[0] # Length of data.

    # Calculate the sums over x,y,z
    m_x = np.sum(x) # Simple sums
    m_y = np.sum(y)
    m_z = np.sum(z)

    # Calculate the moments, as sum over the element-wise products
    m_xx = np.sum(x*x)
    m_yy = np.sum(y*y)
    m_zz = np.sum(z*z)
    m_xy = np.sum(x * y)
    m_xz = np.sum(x * z)
    m_yz = np.sum(y * z)

    # Build the moment matrix
    return np.array([
        [m_zz, m_xz, m_yz, m_z],
        [m_xz, m_xx, m_xy, m_x],
        [m_yz, m_xy, m_yy, m_y],
        [m_z,  m_x,  m_y,  n]
    ])

def fit_circle_algebraic(z_data: np.ndarray):
    """
    Fit a circle in the complex plane using a algebraic method.

    Stable against noise, can be used to get very good start parameters for iterative fit.
    """
    # Build the characteristic polynomial and solve it.
    x = symbols('x')
    M = compute_moments(z_data)
    polynomial: Poly = matrices.det(M - x * CONSTRAINT_MATRIX).as_poly()
    assert polynomial
    derivative = polynomial.diff(x)
    x0, infodict, ier, mesg = optimize.fsolve(polynomial.eval, 0., fprime=derivative.eval)

    # Retrieve the corresponding EV
    U, s, Vt = np.linalg.svd(M - x0 * CONSTRAINT_MATRIX)
    A_vec = Vt[np.argmin(s), :]

    # Calculate center position and radius
    x_c = -A_vec[1]/(2 * A_vec[0])
    y_c = -A_vec[2]/(2 * A_vec[0])
    radius = np.sqrt(A_vec[1]*A_vec[1] + A_vec[2] * A_vec[2] - 4 * A_vec[0] * A_vec[3]) / 2 * np.abs(A_vec[0])
    return x_c, y_c, radius