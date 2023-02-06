# public keys G and P
P = 23 # A prime number P is taken
G = 9 # A primitve root for P, G is taken

print("The Value of P is :", P)
print("The Value of G is :", G)

a = 4 # Alice will choose the private key a
print("The Private Key a for Alice is :", a)

x = int(pow(G,a,P)) # gets the generated key

b = 3 # Bob will choose the private key b
print("The Private Key b for Bob is :", b)

y = int(pow(G,b,P)) # gets the generated key

ka = int(pow(y,a,P)) # Secret key for Alice
kb = int(pow(x,b,P)) # Secret key for Bob

print("Secret key for the Alice is :", ka)
print("Secret Key for the Bob is :", kb)