# import random
# import math

# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# def is_prime(n):
#     if n <= 1 or n % 2 == 0:
#         return False
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# def generate_keypair(p, q):
#     if not (is_prime(p) and is_prime(q)):
#         raise ValueError('Both numbers must be prime.')
#     elif p == q:
#         raise ValueError('p and q cannot be equal.')
#     n = p * q
#     phi = (p-1) * (q-1)
#     e = random.randrange(1, phi)
#     g = gcd(e, phi)
#     while g != 1:
#         e = random.randrange(1, phi)
#         g = gcd(e, phi)
#     d = pow(e, -1, phi)
#     return ((e, n), (d, n))

# def encrypt(plaintext, public_key):
#     key, n = public_key
#     cipher = [(ord(char) ** key) % n for char in plaintext]
#     return cipher

# def decrypt(ciphertext, private_key):
#     key, n = private_key
#     plain = [chr((char ** key) % n) for char in ciphertext]
#     return ''.join(plain)

# if __name__ == '__main__':
#     p = int(input("Enter a prime number (17, 19, 23, etc): "))
#     q = int(input("Enter another prime number (not equal to the first one): "))
#     public, private = generate_keypair(p, q)
#     print("Your public key is ", public, " and your private key is ", private)
#     message = input("Enter a message to encrypt with your public key: ")
#     encrypted_msg = encrypt(message, public)
#     print("Your encrypted message is: ")
#     print(''.join(map(lambda x: str(x), encrypted_msg)))
#     print("Decrypting message with private key ", private, " . . .")
#     print("Your message is:")
#     print(decrypt(encrypted_msg, private))


import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inv(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def generate_key_pair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(1, phi)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi)
    d = mod_inv(e, phi)
    return (e, n), (d, n)

def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [(ord(char) ** e) % n for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plaintext)

if __name__ == "__main__":
    p = 17
    q = 23
    public_key, private_key = generate_key_pair(p, q)
    plaintext = "Hello World!"
    ciphertext = encrypt(public_key, plaintext)
    decrypted_text = decrypt(private_key, ciphertext)
    print(f"Original Text: {plaintext}")
    print(f"Encrypted Text: {ciphertext}")
    print(f"Decrypted Text: {decrypted_text}")