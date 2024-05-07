from math import gcd

def shors_algorithm(N):
    # Step 1: Choose a random number 'a' where 1 < a < N
    a = 2  # You can choose a different 'a' for testing

    # Step 2: Compute the greatest common divisor of 'a' and 'N'
    if gcd(a, N) > 1:
        return gcd(a, N)

    # Step 3: Find the period r of the function f(x) = a^x mod N
    r = 1
    found_period = False
    while not found_period:
        if pow(a, r, N) == 1:
            found_period = True
        else:
            r += 1

    # Step 4: Check if r is even and a^(r/2) is not congruent to -1 mod N
    if r % 2 == 0:
        x = pow(a, r // 2, N)
        if x != 1 and x != N - 1:
            p = gcd(x + 1, N)
            q = gcd(x - 1, N)
            return p, q

    return None

# Test the algorithm with a sample number
N = 21
factors = shors_algorithm(N)
if factors:
    print(f"The factors of {N} are: {factors}")
else:
    print(f"Shor's algorithm failed to find factors for {N}")
