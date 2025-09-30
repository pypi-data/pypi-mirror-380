"""High-level utilities for manipulating multivariate polynomials that appear in
normal-form and centre-manifold calculations of the spatial circular
restricted three-body problem.

This module provides comprehensive polynomial operations for the circular
restricted three-body problem, optimized for performance using Numba JIT
compilation and parallel processing.
"""

import numpy as np
from numba import njit, prange
from numba.typed import List

from hiten.algorithms.polynomial.algebra import (_get_degree, _poly_clean,
                                                  _poly_diff, _poly_evaluate,
                                                  _poly_integrate, _poly_mul,
                                                  _poly_poisson)
from hiten.algorithms.polynomial.base import (_decode_multiindex,
                                               _encode_multiindex, _make_poly)
from hiten.algorithms.utils.config import FASTMATH, N_VARS


@njit(fastmath=FASTMATH, cache=False)
def _polynomial_zero_list(max_deg: int, psi) -> List[np.ndarray]:
    """
    Create a list of zero polynomial coefficient arrays up to a maximum degree.
    
    Parameters
    ----------
    max_deg : int
        Maximum degree of the polynomials to create
    psi : numpy.ndarray
        Combinatorial table from :func:`~hiten.algorithms.polynomial.base._init_index_tables`
        
    Returns
    -------
    List[numpy.ndarray]
        A list of length max_deg+1 where the i-th element contains an array of zeros
        representing the homogeneous part of degree i
        
    Notes
    -----
    This function is used to initialize polynomial lists. The structure
    of the returned list is such that the index corresponds to the degree,
    and each element is an array of zeros with the appropriate size for 
    that degree's coefficients.
    """
    lst = List()
    for d in range(max_deg + 1):
        lst.append(_make_poly(d, psi))
    return lst

@njit(fastmath=FASTMATH, cache=False)
def _polynomial_variable(idx: int, max_deg: int, psi, clmo, encode_dict_list) -> List[np.ndarray]:
    """
    Create a polynomial representing a single variable.
    
    Parameters
    ----------
    idx : int
        Index of the variable (0 to N_VARS-1)
    max_deg : int
        Maximum degree to allocate for the polynomial
    psi : numpy.ndarray
        Combinatorial table from :func:`~hiten.algorithms.polynomial.base._init_index_tables`
    clmo : numba.typed.List
        List of arrays containing packed multi-indices
    encode_dict_list : numba.typed.List
        List of dictionaries mapping packed multi-indices to their positions
        
    Returns
    -------
    List[numpy.ndarray]
        A list representing the polynomial for the variable x_idx,
        with arrays for degrees 0 to max_deg
        
    Notes
    -----
    The result is a polynomial with a single non-zero coefficient
    corresponding to the monomial x_idx.
    """
    poly_result = _polynomial_zero_list(max_deg, psi)
    k = np.zeros(N_VARS, dtype=np.int64)
    k[idx] = 1
    if 1 < len(poly_result) and poly_result[1].size > 0:
        encoded_idx = _encode_multiindex(k, 1, encode_dict_list)
        if 0 <= encoded_idx < poly_result[1].shape[0]:
            poly_result[1][encoded_idx] = 1.0
    return poly_result

@njit(fastmath=FASTMATH, cache=False)
def _polynomial_variables_list(max_deg: int, psi, clmo, encode_dict_list) -> List[List[np.ndarray]]:
    """
    Create a list of polynomials for each variable in the hiten.system.
    
    Parameters
    ----------
    max_deg : int
        Maximum degree to allocate for each polynomial
    psi : numpy.ndarray
        Combinatorial table from :func:`~hiten.algorithms.polynomial.base._init_index_tables`
    clmo : numba.typed.List
        List of arrays containing packed multi-indices
    encode_dict_list : numba.typed.List
        List of dictionaries mapping packed multi-indices to their positions
        
    Returns
    -------
    List[List[numpy.ndarray]]
        A list of length N_VARS where each element is a polynomial 
        representing one of the system variables
        
    Notes
    -----
    This function creates polynomials for all variables in the system
    (typically position and momentum variables in a Hamiltonian system).
    """
    var_polys = List()
    for var_idx in range(6):
        var_polys.append(_polynomial_variable(var_idx, max_deg, psi, clmo, encode_dict_list))
    return var_polys

@njit(fastmath=FASTMATH, cache=False)
def _polynomial_add_inplace(poly_p: List[np.ndarray], poly_q: List[np.ndarray], scale=1.0, max_deg: int = -1):
    """
    Add or subtract one polynomial to/from another in-place.
    
    Parameters
    ----------
    poly_p : List[numpy.ndarray]
        Destination polynomial, modified in-place
    poly_q : List[numpy.ndarray]
        Source polynomial to add to the destination
    scale : float, optional
        Scaling factor for the source polynomial, default is 1.0
    max_deg : int, optional
        Maximum degree to consider, default is -1 (all degrees)
        
    Returns
    -------
    None
        The destination polynomial 'poly_p' is modified in-place
        
    Notes
    -----
    If scale=1.0, computes poly_p += poly_q
    If scale=-1.0, computes poly_p -= poly_q
    Otherwise, computes poly_p += scale * poly_q
    
    The operation is performed element-wise for each degree up to min(max_deg, len(poly_p), len(poly_q))
    """
    if max_deg == -1:
        loop_limit = min(len(poly_p), len(poly_q))
    else:
        loop_limit = min(max_deg + 1, len(poly_p), len(poly_q))

    for d in range(loop_limit):
        if poly_p[d].size == 0 or poly_q[d].size == 0:
            continue
        if scale == 1.0:
            poly_p[d] += poly_q[d]
        elif scale == -1.0:
            poly_p[d] -= poly_q[d]
        else:
            poly_p[d] += scale * poly_q[d]

@njit(fastmath=FASTMATH, cache=False)
def _polynomial_multiply(poly_p: List[np.ndarray], poly_q: List[np.ndarray], max_deg: int, psi, clmo, encode_dict_list) -> List[np.ndarray]:
    """
    Multiply two polynomials.
    
    Parameters
    ----------
    poly_p : List[numpy.ndarray]
        First polynomial
    poly_q : List[numpy.ndarray]
        Second polynomial
    max_deg : int
        Maximum degree for the result
    psi : numpy.ndarray
        Combinatorial table from :func:`~hiten.algorithms.polynomial.base._init_index_tables`
    clmo : numba.typed.List
        List of arrays containing packed multi-indices
    encode_dict_list : numba.typed.List
        List of dictionaries mapping packed multi-indices to their positions
        
    Returns
    -------
    List[numpy.ndarray]
        Product polynomial poly_r = poly_p * poly_q, with homogeneous parts up to max_deg
        
    Notes
    -----
    The multiplication is done by multiplying each homogeneous part of poly_p
    with each homogeneous part of poly_q, and accumulating the results in the
    appropriate degree of the output polynomial.
    """
    poly_r = _polynomial_zero_list(max_deg, psi)
    for d1 in range(max_deg + 1):
        if d1 >= len(poly_p) or not np.any(poly_p[d1]):
            continue
        for d2 in range(max_deg + 1 - d1):
            if d2 >= len(poly_q) or not np.any(poly_q[d2]):
                continue
            res_deg = d1 + d2
            prod = _poly_mul(poly_p[d1], d1, poly_q[d2], d2, psi, clmo, encode_dict_list)
            if prod.shape == poly_r[res_deg].shape:
                poly_r[res_deg] += prod
            elif prod.size == poly_r[res_deg].size:
                poly_r[res_deg] += prod.reshape(poly_r[res_deg].shape)
    return poly_r

@njit(fastmath=FASTMATH, cache=False)
def _polynomial_power(poly_p: List[np.ndarray], k: int, max_deg: int, psi, clmo, encode_dict_list) -> List[np.ndarray]:
    """
    Raise a polynomial to a power using binary exponentiation.
    
    Parameters
    ----------
    poly_p : List[numpy.ndarray]
        Base polynomial
    k : int
        Exponent (non-negative integer)
    max_deg : int
        Maximum degree for the result
    psi : numpy.ndarray
        Combinatorial table from :func:`~hiten.algorithms.polynomial.base._init_index_tables`
    clmo : numba.typed.List
        List of arrays containing packed multi-indices
    encode_dict_list : numba.typed.List
        List of dictionaries mapping packed multi-indices to their positions
        
    Returns
    -------
    List[numpy.ndarray]
        Result polynomial poly_r = poly_p^k, with homogeneous parts up to max_deg
        
    Notes
    -----
    This function uses the binary exponentiation algorithm to compute poly_p^k
    efficiently in O(log k) multiplications.
    
    For k=0, the result is the constant polynomial 1.
    """
    if k == 0:
        poly_result = _polynomial_zero_list(max_deg, psi)
        if max_deg >= 0 and len(poly_result) > 0 and poly_result[0].size > 0:
            poly_result[0][0] = 1.0 + 0.0j
        return poly_result

    poly_result = _polynomial_zero_list(max_deg, psi)
    if max_deg >= 0 and len(poly_result) > 0 and poly_result[0].size > 0:
        poly_result[0][0] = 1.0 + 0.0j

    active_base = List()
    for arr_idx in range(len(poly_p)):
        active_base.append(poly_p[arr_idx].copy())
        
    exponent = k
    while exponent > 0:
        if exponent % 2 == 1:
            poly_result = _polynomial_multiply(poly_result, active_base, max_deg, psi, clmo, encode_dict_list)
        
        if exponent > 1 :
            active_base = _polynomial_multiply(active_base, active_base, max_deg, psi, clmo, encode_dict_list)
        exponent //= 2
    return poly_result

@njit(fastmath=FASTMATH, cache=False)
def _polynomial_poisson_bracket(poly_p: List[np.ndarray], poly_q: List[np.ndarray], max_deg: int, psi, clmo, encode_dict_list) -> List[np.ndarray]:
    """
    Compute the Poisson bracket of two polynomials.
    
    Parameters
    ----------
    poly_p : List[numpy.ndarray]
        First polynomial
    poly_q : List[numpy.ndarray]
        Second polynomial
    max_deg : int
        Maximum degree for the result
    psi : numpy.ndarray
        Combinatorial table from :func:`~hiten.algorithms.polynomial.base._init_index_tables`
    clmo : numba.typed.List
        List of arrays containing packed multi-indices
    encode_dict_list : numba.typed.List
        List of dictionaries mapping packed multi-indices to their positions
        
    Returns
    -------
    List[numpy.ndarray]
        Poisson bracket {poly_p, poly_q}, with homogeneous parts up to max_deg
        
    Notes
    -----
    The Poisson bracket {poly_p, poly_q} is computed by combining the Poisson brackets
    of each homogeneous part of poly_p with each homogeneous part of poly_q.
    
    The degree of the Poisson bracket of terms of degrees d1 and d2
    is d1 + d2 - 2.
    """
    poly_r = _polynomial_zero_list(max_deg, psi)
    for d1 in range(len(poly_p)):
        if not np.any(poly_p[d1]):
            continue
        for d2 in range(len(poly_q)):
            if not np.any(poly_q[d2]):
                continue

            res_deg = d1 + d2 - 2

            if res_deg < 0 or res_deg > max_deg:
                continue
            
            term_coeffs = _poly_poisson(poly_p[d1], d1, poly_q[d2], d2, psi, clmo, encode_dict_list)
            if term_coeffs.shape == poly_r[res_deg].shape:
                poly_r[res_deg] += term_coeffs
            elif term_coeffs.size == poly_r[res_deg].size and poly_r[res_deg].size > 0:
                poly_r[res_deg] += term_coeffs.reshape(poly_r[res_deg].shape)
    return poly_r

@njit(fastmath=FASTMATH, cache=False)
def _polynomial_clean(poly_p: List[np.ndarray], tol: float) -> List[np.ndarray]:
    """
    Create a new polynomial with small coefficients set to zero.
    
    Parameters
    ----------
    poly_p : List[numpy.ndarray]
        Input polynomial
    tol : float
        Tolerance threshold; coefficients with |value| <= tol will be set to zero
        
    Returns
    -------
    List[numpy.ndarray]
        A new polynomial with small coefficients set to zero
        
    Notes
    -----
    This function creates a copy of the input polynomial with all coefficients
    having absolute value less than or equal to the tolerance set to zero.
    """
    # Initialize a Numba Typed List with the correct item type
    # The item type is complex128 1D array, matching the elements of polys.
    cleaned_list = List.empty_list(np.complex128[::1])
    for p_arr in poly_p:
        out_arr = np.empty_like(p_arr)
        _poly_clean(p_arr, tol, out_arr)
        cleaned_list.append(out_arr)
    return cleaned_list

@njit(fastmath=FASTMATH, cache=False)
def _polynomial_degree(poly_p: List[np.ndarray]) -> int:
    """
    Get the degree of a polynomial represented as a list of homogeneous parts.

    The degree is the highest index d for which poly_p[d] contains non-zero coefficients.

    Parameters
    ----------
    poly_p : List[np.ndarray]
        A list where poly_p[d] is a NumPy array of coefficients for the
        homogeneous part of degree d.

    Returns
    -------
    int
        The degree of the polynomial. Returns -1 if the polynomial is zero.
    """
    for d in range(len(poly_p) - 1, -1, -1):
        # Check if any element in the coefficient array for degree d is non-zero
        if np.any(poly_p[d]):
            return d
    return -1 # All parts are zero or poly_p is empty

@njit(fastmath=FASTMATH, cache=False)
def _polynomial_total_degree(poly_p: List[np.ndarray], psi) -> int:
    """
    Get the total degree of a polynomial using the _get_degree kernel function.
    
    This function uses the _get_degree kernel to verify the degree of each 
    homogeneous part by checking the coefficient array size, then finds 
    the highest degree with non-zero coefficients.
    
    Parameters
    ----------
    poly_p : List[numpy.ndarray]
        A list where poly_p[d] is a NumPy array of coefficients for the
        homogeneous part of degree d.
    psi : numpy.ndarray
        Combinatorial table from :func:`~hiten.algorithms.polynomial.base._init_index_tables`
        
    Returns
    -------
    int
        The total degree of the polynomial. Returns -1 if the polynomial is zero.
        
    Notes
    -----
    This function provides an alternative to _polynomial_degree() by using the 
    _get_degree kernel function to determine the degree of each homogeneous part
    based on coefficient array size rather than relying on array indexing.
    """
    max_degree_found = -1
    
    for d in range(len(poly_p)):
        coeffs_d = poly_p[d]
        
        # Skip empty coefficient arrays
        if coeffs_d.size == 0:
            continue
            
        # Use _get_degree to verify this array represents degree d
        actual_degree = _get_degree(coeffs_d, psi)
        
        # Check consistency: the degree determined by _get_degree should match the index
        if actual_degree != d:
            # If inconsistent, we might have a malformed polynomial structure
            continue
            
        # Check if this degree has non-zero coefficients
        if np.any(coeffs_d):
            max_degree_found = max(max_degree_found, actual_degree)
    
    return max_degree_found

@njit(fastmath=FASTMATH, cache=False)
def _polynomial_differentiate(
    poly_p: List[np.ndarray], 
    var_idx: int, 
    max_deg: int, 
    psi_table: np.ndarray, 
    clmo_table: List[np.ndarray],
    derivative_psi_table: np.ndarray,
    derivative_clmo_table: List[np.ndarray],
    encode_dict_list: List
):
    """
    Compute the partial derivative of a polynomial with respect to a variable.
    
    Parameters
    ----------
    poly_p : List[numpy.ndarray]
        Input polynomial
    var_idx : int
        Index of the variable to differentiate with respect to (0 to N_VARS-1)
    max_deg : int
        Maximum degree of the input polynomial
    psi_table : numpy.ndarray
        Combinatorial table for the input polynomial
    clmo_table : List[numpy.ndarray]
        List of arrays containing packed multi-indices for the input polynomial
    derivative_psi_table : numpy.ndarray
        Combinatorial table for the derivative polynomial
    derivative_clmo_table : List[numpy.ndarray]
        List of arrays containing packed multi-indices for the derivative polynomial
    encode_dict_list : List
        List of dictionaries mapping packed multi-indices to their positions
        
    Returns
    -------
    (List[numpy.ndarray], int)
        A tuple containing:
        - The derivative polynomial
        - The maximum degree of the derivative polynomial
        
    Notes
    -----
    The derivative of a term of degree d is a term of degree d-1.
    The maximum degree of the derivative is max_deg-1 (or 0 if max_deg=0).
    """
    derivative_max_deg = max_deg - 1
    if derivative_max_deg < 0:
        derivative_max_deg = 0

    derivative_coeffs_list = _polynomial_zero_list(derivative_max_deg, derivative_psi_table)

    for d_orig in range(1, max_deg + 1):
        d_res = d_orig - 1 
        
        if d_res <= derivative_max_deg:
            if d_orig < len(poly_p) and np.any(poly_p[d_orig]):
                term_diff_coeffs = _poly_diff(
                    poly_p[d_orig], 
                    var_idx, 
                    d_orig, 
                    psi_table, 
                    clmo_table,
                    encode_dict_list
                )
                
                if d_res < len(derivative_coeffs_list) and derivative_coeffs_list[d_res].shape[0] == term_diff_coeffs.shape[0]:
                    derivative_coeffs_list[d_res] = term_diff_coeffs

    return derivative_coeffs_list, derivative_max_deg

@njit(fastmath=FASTMATH, cache=False)
def _polynomial_jacobian(
    poly_p: List[np.ndarray],
    max_deg: int,
    psi_table: np.ndarray,
    clmo_table: List[np.ndarray],
    encode_dict_list: List
) -> List[List[np.ndarray]]:
    """
    Compute the Jacobian matrix of a polynomial.
    
    Parameters
    ----------
    poly_p : List[np.ndarray]
        Input polynomial
    max_deg : int
        Maximum degree of the input polynomial
    psi_table : numpy.ndarray
        Combinatorial table from :func:`~hiten.algorithms.polynomial.base._init_index_tables`
    clmo_table : List[numpy.ndarray]
        List of arrays containing packed multi-indices
    encode_dict_list : List
        List of dictionaries mapping packed multi-indices to their positions
        
    Returns
    -------
    List[List[numpy.ndarray]]
        A list of length N_VARS where each element is the partial derivative
        of the input polynomial with respect to one variable
        
    Notes
    -----
    This function computes all partial derivatives of the input polynomial
    with respect to each of the N_VARS variables in the hiten.system.
    """
    jacobian_list = List.empty_list(List.empty_list(np.complex128[::1])) # Typed list for list of polynomials

    for i in prange(N_VARS): # Iterate over all variables
        derivative_poly_coeffs, _ = _polynomial_differentiate(
            poly_p=poly_p,
            var_idx=i,
            max_deg=max_deg,
            psi_table=psi_table,
            clmo_table=clmo_table,
            derivative_psi_table=psi_table,  # Use original psi table for derivative
            derivative_clmo_table=clmo_table, # Use original clmo table for derivative
            encode_dict_list=encode_dict_list
        )
        jacobian_list.append(derivative_poly_coeffs)
    
    return jacobian_list

@njit(fastmath=FASTMATH, cache=False)
def _polynomial_evaluate(
    poly_p: List[np.ndarray], 
    point: np.ndarray, 
    clmo: List[np.ndarray] # Typically _CLMO_GLOBAL
) -> np.complex128:
    """
    Evaluate a polynomial at a specific point.
    
    Parameters
    ----------
    poly_p : List[numpy.ndarray]
        Polynomial to evaluate
    point : numpy.ndarray
        Array of length N_VARS containing the values of variables
        where the polynomial should be evaluated
    clmo : List[np.ndarray]
        List of arrays containing packed multi-indices
        
    Returns
    -------
    numpy.complex128
        The value of the polynomial at the specified point
        
    Notes
    -----
    This function evaluates the polynomial by summing the evaluations
    of all its homogeneous parts.
    """
    total_value = 0.0 + 0.0j
    for degree in range(len(poly_p)):
        coeffs_d = poly_p[degree]
        if coeffs_d.shape[0] > 0: # Check if there are coefficients for this degree
            total_value += _poly_evaluate(coeffs_d, degree, point, clmo)
    return total_value

@njit(fastmath=FASTMATH, cache=False)
def _polynomial_integrate(
    poly_p: List[np.ndarray],
    var_idx: int,
    max_deg: int,
    psi_table: np.ndarray,
    clmo_table: List[np.ndarray],
    integral_psi_table: np.ndarray,
    integral_clmo_table: List[np.ndarray],
    encode_dict_list: List
) -> tuple[List[np.ndarray], int]:
    """
    Integrate a polynomial with respect to one variable.
    
    Parameters
    ----------
    poly_p : List[numpy.ndarray]
        Input polynomial
    var_idx : int
        Index of the variable to integrate with respect to (0 to N_VARS-1)
    max_deg : int
        Maximum degree of the input polynomial
    psi_table : numpy.ndarray
        Combinatorial table for the input polynomial
    clmo_table : List[numpy.ndarray]
        List of arrays containing packed multi-indices for the input polynomial
    integral_psi_table : numpy.ndarray
        Combinatorial table for the integral polynomial
    integral_clmo_table : List[numpy.ndarray]
        List of arrays containing packed multi-indices for the integral polynomial
    encode_dict_list : List
        List of dictionaries mapping packed multi-indices to their positions
        
    Returns
    -------
    (List[numpy.ndarray], int)
        A tuple containing:
        - The integral polynomial
        - The maximum degree of the integral polynomial
        
    Notes
    -----
    The integral of a term of degree d is a term of degree d+1.
    The maximum degree of the integral is max_deg+1.
    The integration constant is set to zero.
    """
    integral_max_deg = max_deg + 1
    # Ensure integral_coeffs_list is initialized up to integral_max_deg using integral_psi_table
    integral_coeffs_list = _polynomial_zero_list(integral_max_deg, integral_psi_table)

    for d_orig in range(max_deg + 1): # Iterate through all degrees of original polynomial
        d_res = d_orig + 1 # Degree of the result of integrating this part
        
        # Ensure the resulting degree fits within the pre-allocated list for the integral
        if d_res <= integral_max_deg:
            if d_orig < len(poly_p) and np.any(poly_p[d_orig]):
                term_integral_coeffs = _poly_integrate(
                    poly_p[d_orig],
                    var_idx,
                    d_orig,
                    psi_table,
                    clmo_table,
                    encode_dict_list
                )
                
                # Add the integrated term to the correct degree in the result list
                # The term_integral_coeffs is for degree d_res (i.e., d_orig + 1)
                if d_res < len(integral_coeffs_list) and integral_coeffs_list[d_res].shape[0] == term_integral_coeffs.shape[0]:
                    integral_coeffs_list[d_res] += term_integral_coeffs
                elif d_res < len(integral_coeffs_list) and integral_coeffs_list[d_res].size == term_integral_coeffs.size and term_integral_coeffs.size > 0:
                    integral_coeffs_list[d_res] += term_integral_coeffs.reshape(integral_coeffs_list[d_res].shape)

    return integral_coeffs_list, integral_max_deg


@njit(fastmath=FASTMATH, cache=False)
def _linear_variable_polys(C: np.ndarray, max_deg: int, psi, clmo, encode_dict_list) -> List[np.ndarray]:
    """
    Create polynomials for new variables after a linear transformation.
    
    Parameters
    ----------
    C : numpy.ndarray
        Transformation matrix (6x6) that defines the linear change of variables
    max_deg : int
        Maximum degree for polynomial representations
    psi : numpy.ndarray
        Combinatorial table from :func:`~hiten.algorithms.polynomial.base._init_index_tables`
    clmo : numba.typed.List
        List of arrays containing packed multi-indices
    encode_dict_list : numba.typed.List
        List of dictionaries mapping packed multi-indices to their positions
        
    Returns
    -------
    List[List[numpy.ndarray]]
        List of length 6 where each element is a polynomial representing 
        a transformed variable
        
    Notes
    -----
    This function computes the linear transformation of variables:
    L_i = sum_j C[i,j] * var_j
    where var_j are the original variables and L_i are the transformed variables.
    """
    new_basis = [_polynomial_variable(j, max_deg, psi, clmo, encode_dict_list) for j in range(6)]
    L: List[np.ndarray] = []
    for i in range(6):
        poly_result = _polynomial_zero_list(max_deg, psi)
        for j in range(6):
            if C[i, j] == 0:
                continue
            _polynomial_add_inplace(poly_result, new_basis[j], C[i, j], max_deg)
        L.append(poly_result)
    return L


@njit(fastmath=FASTMATH)
def _substitute_linear(poly_old: List[np.ndarray], C: np.ndarray, max_deg: int, psi, clmo, encode_dict_list, tol: float = 1e-14) -> List[np.ndarray]:
    """
    Perform variable substitution in a polynomial using a linear transformation.
    
    Parameters
    ----------
    poly_old : List[numpy.ndarray]
        Polynomial in the original variables
    C : numpy.ndarray
        Transformation matrix (6x6) that defines the linear change of variables
    max_deg : int
        Maximum degree for polynomial representations
    psi : numpy.ndarray
        Combinatorial table from :func:`~hiten.algorithms.polynomial.base._init_index_tables`
    clmo : numba.typed.List
        List of arrays containing packed multi-indices
    encode_dict_list : numba.typed.List
        List of dictionaries mapping packed multi-indices to their positions
        
    Returns
    -------
    List[numpy.ndarray]
        Polynomial in the transformed variables
        
    Notes
    -----
    This function substitutes each original variable with its corresponding
    transformation defined by the matrix C. For each term in the original
    polynomial, it computes the product of the transformed variables raised
    to the appropriate power.
    """
    var_polys = _linear_variable_polys(C, max_deg, psi, clmo, encode_dict_list)
    poly_new = _polynomial_zero_list(max_deg, psi)

    for deg in range(max_deg + 1):
        p = poly_old[deg]
        if not p.any():
            continue
        for pos, coeff in enumerate(p):
            if coeff == 0:
                continue
            k = _decode_multiindex(pos, deg, clmo)
            
            # build product  Pi_i  (var_polys[i] ** k_i)
            term = _polynomial_zero_list(max_deg, psi)
            
            # Fix: Preserve the full complex value instead of just the real part
            if len(term) > 0 and term[0].size > 0:
                term[0][0] = coeff
            elif coeff !=0:
                pass
                
            for i_var in range(6):
                if k[i_var] == 0:
                    continue
                pwr = _polynomial_power(var_polys[i_var], k[i_var], max_deg, psi, clmo, encode_dict_list)
                term = _polynomial_multiply(term, pwr, max_deg, psi, clmo, encode_dict_list)
                
            _polynomial_add_inplace(poly_new, term, 1.0, max_deg)

    return _polynomial_clean(poly_new, tol)


@njit(fastmath=FASTMATH, cache=False)
def _linear_affine_variable_polys(C: np.ndarray, shifts: np.ndarray, max_deg: int, psi, clmo, encode_dict_list):
    """Build polynomials for variables after an affine change of variables.

    The transformation implemented is
        L_i = sum_j C[i,j] * x_j + shifts[i]

    Parameters
    ----------
    C : np.ndarray, shape (6,6)
        Linear part of the transformation.
    shifts : np.ndarray, shape (6,)
        Constant offsets added to each new variable.  Use 0 for variables that
        are not shifted.
    max_deg, psi, clmo, encode_dict_list
        Same meaning as in `_linear_variable_polys`.

    Returns
    -------
    List[List[np.ndarray]]
        Polynomials for the six transformed variables.
    """
    # First build the purely linear part
    var_polys = _linear_variable_polys(C, max_deg, psi, clmo, encode_dict_list)

    # Inject constant shifts into the degree-0 component of each variable
    for i in range(6):
        delta = shifts[i]
        if delta == 0:
            continue
        if len(var_polys[i]) > 0 and var_polys[i][0].size > 0:
            var_polys[i][0][0] += delta
    return var_polys


@njit(fastmath=FASTMATH, cache=False)
def _substitute_affine(poly_old: List[np.ndarray], C: np.ndarray, shifts: np.ndarray, max_deg: int, psi, clmo, encode_dict_list, tol: float = 1e-14) -> List[np.ndarray]:
    """Substitute an *affine* change of variables into a polynomial.

    The old variables (x_old) are expressed in terms of the new variables (x) by

        x_old_i = sum_j C[i,j] * x_j + shifts[i]

    This is a thin wrapper around `_substitute_linear`; it first builds the
    variable polynomials that include the constant shifts and then performs the
    same expansion/accumulation loop.
    """
    # Build affine variable polynomials (linear part + constant shifts)
    var_polys = _linear_affine_variable_polys(C, shifts, max_deg, psi, clmo, encode_dict_list)

    poly_new = _polynomial_zero_list(max_deg, psi)

    for deg in range(max_deg + 1):
        p = poly_old[deg]
        if not p.any():
            continue
        for pos, coeff in enumerate(p):
            if coeff == 0:
                continue
            k = _decode_multiindex(pos, deg, clmo)

            # start with the constant coeff
            term = _polynomial_zero_list(max_deg, psi)
            if len(term) > 0 and term[0].size > 0:
                term[0][0] = coeff

            # multiply the required powers of each transformed variable
            for i_var in range(6):
                exp_i = k[i_var]
                if exp_i == 0:
                    continue
                pwr = _polynomial_power(var_polys[i_var], exp_i, max_deg, psi, clmo, encode_dict_list)
                term = _polynomial_multiply(term, pwr, max_deg, psi, clmo, encode_dict_list)

            _polynomial_add_inplace(poly_new, term, 1.0, max_deg)

    # Remove numerical noise
    return _polynomial_clean(poly_new, tol)
