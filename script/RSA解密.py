import gmpy2 as gp

p =  gp.mpz(3)
q =  gp.mpz(11)
e =  gp.mpz(3)
c =  gp.mpz(26)
n = p*q
phi = (p-1) * (q-1)
d = gp.invert(e, phi)
m = pow(c, d, n)
print(m)