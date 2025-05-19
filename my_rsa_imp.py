import random


def euclidean_gcd(a, b):
    while b != 0:
        old_a=a
        a=b
        b=old_a%b
    return a



def extended_euclidean_algorithm(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    counter=0

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s + quotient * s
        old_t, t = t, old_t + quotient * t
        counter += 1

    gcd=old_r
    x = old_s
    y = old_t
    if counter%2==1:
        x=(-1)*x
    else:
        y=(-1)*y

    return gcd, x, y



def mod_exp(base, exponent, modulus):
    result = 1
    base =base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent =exponent // 2

    return result



def is_strong_pseudoprime(n, a):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d = d // 2
        s = s + 1

    t = mod_exp(a, d, n)
    if t == 1:
        return True
    for _ in range(s):
        if t == n - 1:
            return True
        t = (t * t) % n
    return False


def is_prime(n, k=5):  # k = number of iterations (higher = more accuracy)
    if n in (2, 3):
        return True
    if n <= 1 or n % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(2, n - 1)
        if not is_strong_pseudoprime(n, a):
            return False
    return True


def CRT(c, d, p, q):
    c1 = mod_exp(c, d % (p-1), p)
    c2 = mod_exp(c, d % (q-1), q)
    M = p * q
    M1 = M // p
    M2 = M // q
    gcd, y1, y2 = extended_euclidean_algorithm(M1, M2)
    m = (c1 * M1 * y1 + c2 * M2 * y2) % M
    if m < 0:
        m += M
    return m



def generate_large_prime(bits=8):
    lower = 2**(bits - 1)
    upper = 2**bits - 1
    while True:
        n = random.randint(lower, upper)
        if is_prime(n):
            return n


# RSA Key Generation
def generate_keys(bits=8):
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    while p == q:
        q = generate_large_prime(bits)


    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose public exponent e
    e = 65537  # Common choice, but for representative use, use e=2
    while euclidean_gcd(e, phi) != 1:
        e = random.randrange(3, phi, 2)

    # Compute private exponent d
    _, _, y = extended_euclidean_algorithm(phi, e)
    d = y % phi
    if d < 0:
        d += phi

    public_key = (e, n)
    private_key = (d, n)
    crt_params = (d, p, q)

    return public_key, private_key, crt_params


# RSA Encryption
def encrypt(message, public_key):
    e, n = public_key
    return mod_exp(message, e, n)

# RSA Decryption (CRT Optimized)
def decrypt(ciphertext, crt_params):
    d, p, q = crt_params
    return CRT(ciphertext, d, p, q)


def raw_sign(message_int, crt_params):
    if message_int >= crt_params[1] * crt_params[2]:
        raise ValueError("Message too large for modulus")
    return decrypt(message_int, crt_params)

def raw_verify(signature, message_int, public_key):
    e, n = public_key
    decrypted_message = encrypt(signature, public_key)
    return decrypted_message == message_int



if __name__ == '__main__':
    print("Ex_Euc_Alg: 10368,5")
    print(extended_euclidean_algorithm(10368,5),"\n")

    print("Mod_Exp: ")
    print(mod_exp(2, 69, 1105),"\n")  # Output: 24

    print("Crt")
    # CRT Example usage
    c = 1727
    d = 727
    p = 83
    q = 67
    result = CRT(c, d, p, q)
    print(result,"\n")


    print("-------------------------\nTest full RSA:\n-------------------------\n")

    message = 14
    public_key, private_key, crt_params = generate_keys(bits=8)

    #public_key, private_key, crt_params = (19, 943),(139,943),(139,41,23)
    # Public key: (19, 943)
    # Private key: (139, 943)
    # Encrypted message: 79
    # Decrypted message: 14
    print("Message:", message)
    print("Public key:", public_key)
    print("Private key:", private_key)

    encrypted = encrypt(message, public_key)
    print("Encrypted message:", encrypted)

    decrypted = decrypt(encrypted, crt_params)
    print("Decrypted message:", decrypted)

    print("-------------------------\nTest Dig Sign\n-------------------------\n")

    public_key, private_key, crt_params = generate_keys(bits=256)

    # Convert message to integer directly (vulnerable to manipulation)
    message = "No hash"
    message_int = int.from_bytes(message.encode('utf-8'), byteorder='big')

    signature = raw_sign(message_int, crt_params)
    is_valid = raw_verify(signature, message_int, public_key)

    print(f"Original Message: {message}")
    print(f"Message as Integer: {message_int}")
    print(f"Signature: {signature}")
    print(f"Signature Valid: {is_valid}")


