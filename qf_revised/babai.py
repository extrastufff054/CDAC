import numpy as np
from scipy.linalg import qr

def gram_schmidt(basis):
    """ Compute the Gram-Schmidt orthogonalization of the basis """
    n = len(basis)
    m = len(basis[0])
    B_star = np.zeros((n, m))
    mu = np.zeros((n, n))

    for i in range(n):
        B_star[i] = basis[i]
        for j in range(i):
            mu[i][j] = np.dot(basis[i], B_star[j]) / np.dot(B_star[j], B_star[j])
            B_star[i] -= mu[i][j] * B_star[j]
    
    return B_star, mu

def babais_algorithm(lattice_basis, target_vector):
    """
    Implements Babai's Nearest Plane Algorithm to find an approximate solution to the Closest Vector Problem (CVP).
    :param lattice_basis: The basis of the lattice (as a 2D list or array).
    :param target_vector: The target vector to find the closest lattice point to (as a list or array).
    :return: An approximate solution to the CVP (as a list or array).
    """
    # Perform QR decomposition using scipy
    B = np.array(lattice_basis)
    Q, R = qr(B)
    B_star = np.array(Q.T)

    approx_vector = np.copy(target_vector)
    for i in reversed(range(len(B))):
        c = round(np.dot(approx_vector, B_star[i]) / np.dot(B_star[i], B_star[i]))
        approx_vector -= c * B_star[i]

    closest_vector = target_vector - approx_vector
    return closest_vector  # Returning the closest lattice point

# Example usage
if __name__ == "__main__":
    lattice_basis = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    target_vector = np.array([1.2, 3.4, 5.6])
    result = babais_algorithm(lattice_basis, target_vector)
    print("Approximate solution:", result)