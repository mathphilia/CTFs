import json

with open('output.txt') as f:
    c = json.loads(f.read()[4:])
    print(c)

N = gcd(21 ^ 0x101 - c[-6], 42 ^ 0x101 - c[-7])
PR.<x> = PolynomialRing(Zmod(N))

poly1 = (2 * x + 1) ^ 0x101 - c[0]
poly2 = x ^ 0x101 - c[1]

while 1 < poly1.degree():
    if poly1.degree() < poly2.degree():
        poly1, poly2 = poly2, poly1
    else:
        k = poly1.coefficients()[-1] / poly2.coefficients()[-1]
        poly1 -= k * poly2 * x ^ (poly1.degree() - poly2.degree())

m = int(-poly1.coefficients()[0] / poly1.coefficients()[1] * 2 + 1)
print(m.to_bytes((m.bit_length() + 7)//8, 'big'))
