import random

def mod_pow(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent & 1 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def generate_private_key(modulus):
    return random.randint(2, modulus - 2)

def generate_public_key(private_key, base, modulus):
    return mod_pow(base, private_key, modulus)

def generate_shared_secret(private_key, public_key, modulus):
    return mod_pow(public_key, private_key, modulus)

if __name__ == '__main__':
    modulus = int(input('Enter modulus: '))
    base = int(input('Enter base: '))
    alice_private_key = generate_private_key(modulus)
    bob_private_key = generate_private_key(modulus)
    alice_public_key = generate_public_key(alice_private_key, base, modulus)
    bob_public_key = generate_public_key(bob_private_key, base, modulus)
    alice_shared_secret = generate_shared_secret(alice_private_key, bob_public_key, modulus)
    bob_shared_secret = generate_shared_secret(bob_private_key, alice_public_key, modulus)
    print(f'Alice private key: {alice_private_key}')
    print(f'Bob private key: {bob_private_key}')
    print(f'Alice public key: {alice_public_key}')
    print(f'Bob public key: {bob_public_key}')
    print(f'Alice shared secret: {alice_shared_secret}')
    print(f'Bob shared secret: {bob_shared_secret}')
    if alice_shared_secret == bob_shared_secret:
        print('Shared secrets match')
    else:
        print('Shared secrets do not match')