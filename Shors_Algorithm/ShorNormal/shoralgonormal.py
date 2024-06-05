from math import gcd

def shors_algorithm(N):
    """
    Implements Shor's algorithm to find the factors of a given number N.
    
    Parameters:
    N (int): The number to be factorized.
    
    Returns:
    tuple: A tuple containing the factors of N if they exist, otherwise None.
    """
    # Step 1: Choose a random number 'a' where 1 < a < N
    # For simplicity, we're using a fixed value of 'a'. In practice, 'a' should be chosen randomly.
    a = 2  # You can choose a different 'a' for testing

    # Step 2: Compute the greatest common divisor of 'a' and 'N'
    # If gcd(a, N) > 1, it means 'a' is a factor of 'N'.
    if gcd(a, N) > 1:
        return gcd(a, N)

    # Step 3: Find the period r of the function f(x) = a^x mod N
    # This is done by repeatedly squaring 'a' modulo 'N' until we find a value that repeats.
    r = 1
    found_period = False
    while not found_period:
        if pow(a, r, N) == 1:
            found_period = True
        else:
            r += 1

    # Step 4: Check if r is even and a^(r/2) is not congruent to -1 mod N
    # If these conditions are met, we can factorize N.
    if r % 2 == 0:
        x = pow(a, r // 2, N)
        if x!= 1 and x!= N - 1:
            # Calculate the greatest common divisors of (x + 1) and N, and (x - 1) and N.
            # These are the factors of N.
            p = gcd(x + 1, N)
            q = gcd(x - 1, N)
            return p, q

    # If no factors were found, return None.
    return None

# Test the algorithm with a sample number
N = 21
factors = shors_algorithm(N)
if factors:
    print(f"The factors of {N} are: {factors}")
else:
    print(f"Shor's algorithm failed to find factors for {N}")
