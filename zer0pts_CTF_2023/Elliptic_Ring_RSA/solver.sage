import collections, math, random, re, string


##### copy from source code (q.sage) #####
class EllipticRingElement:
	point = None
	def __init__(self, point):
		self.point = point
	
	def __add__(self, other):
		if self.point == dict():
			return other
		if other.point == dict():
			return self
		res = self.point.copy()
		for k in other.point.keys():
			if k in res:
				res[k] += other.point[k]
				if res[k] == 0:
					res.pop(k)
			else:
				res[k] = other.point[k]
				if res[k] == 0:
					res.pop(k)
		return EllipticRingElement(res)
	
	def __mul__(self, other):
		if self.point == dict() or other.point == dict():
			return self.point()
		res = dict()
		for k1 in other.point.keys():
			for k2 in self.point.keys():
				E = k1 + k2
				k = other.point[k1] * self.point[k2]
				if E in res:
					res[E] += k
					if res[E] == 0:
						res.pop(E)
				else:
					res[E] = k
					if res[E] == 0:
						res.pop(E)
		return EllipticRingElement(res)
	
	def __repr__(self):
		st = ""
		for k in self.point.keys():
			st += f"{self.point[k]}*({k[0]}, {k[1]}) + "
		return st[:-3]
##### copy from source code (q.sage) #####


def read_tuple(string):
    return tuple(map(int, string.strip()[1:-1].split(',')))

def partition(n, maximum):
    # return partitions of n i.e. sequences a_0, a_2, ..., a_k
    # (k: length of `maximum`) with sum equal to n.
    # a_i is no greater than i-th element of `maximum`.
    if maximum == []:
        return [[]]
    result = []
    for i in range(min(n, maximum[0]) + 1):
        result += [[i] + p for p in partition(n - i, maximum[1:])]
    return result

def ER2polynomial(ER_element):
    isomorphism = {generator * i: x ** i for i in range(order_E)}
    return sum(coeff * isomorphism[point] for point, coeff in ER_element.point.items())

def polynomial2ER(polynomial):
    isomorphism = {x ** i: generator * i for i in range(order_E)}
    coeffs = list(polynomial)
    point = {}
    for i, coeff in enumerate(coeffs):
        if coeff != 0:
            point[isomorphism[x ** i]] = coeff
    return EllipticRingElement(point)

def decode(ER_element):
    return bytes(ER_element.point[point] for point in sorted(ER_element.point))


with open('output.txt') as f:
    output = f.read()

p = int(re.findall(r'p: \d+', output)[0].split()[-1])
a = int(re.findall(r'a: \d+', output)[0].split()[-1])
b = int(re.findall(r'b: \d+', output)[0].split()[-1])
e = int(re.findall(r'e: \d+', output)[0].split()[-1])

Fp = GF(p)
E = EllipticCurve(Fp, [a, b])
order_E = E.order()
generator = E.gens()[0]

C_str = re.findall(r'C: .+', output)[0][3:]
C_dict = dict()
for elem in C_str.split('+'):
    xy = read_tuple(elem.split('*')[1])
    point = E.point(xy) if xy != (0, 1) else E(0)
    C_dict[point] = Fp(elem.split('*')[0])
C = EllipticRingElement(C_dict)

PR.<x> = PolynomialRing(Fp)
factorization = (x ** order_E - 1).factor()
degree = collections.Counter(factor[0].degree() for factor in factorization)
order_KE = 0
for par in partition(sum(degree.values()), list(degree.values())):
    elements = p ** (order_E - sum(i * _par for i, _par in zip(degree, par)))
    subsets = math.prod(math.comb(i, _par) for i, _par in zip(degree.values(), par))
    order_KE += (-1) ** sum(par) * elements * subsets

d = pow(e, -1, order_KE)
M = polynomial2ER(pow(ER2polynomial(C), d, x ** order_E - 1))
message = decode(M)
print(re.findall(r'zer0pts\{[\x20-\x7e]+\}', message.decode()))