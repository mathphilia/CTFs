# coding: utf-8
from Crypto.Util.number import getPrime, inverse, getRandomRange
import math
from secret import flag


def lcm(a, b):
    return (a * b) // math.gcd(a, b)


class Cryptosystem:
    def __init__(self, bits):
        p = getPrime(bits // 2)
        while True:
            q = getPrime(bits // 2)
            if p != q:
                break
        n = p * q
        λ = lcm(p - 1, q - 1)
        while True:
            g = getRandomRange(2, n * n)
            μ = inverse((pow(g, λ, n * n) - 1) // n % n, n)
            if μ is not None:
                break
        self.secret_key = (λ, μ)
        self.public_key = (n, g)

    def encrypt(self, plain):
        n, g = self.public_key
        nn = n * n
        assert(0 <= plain < n)
        while(True):
            r = getRandomRange(2, n)
            if(math.gcd(r, n) == 1):
                break
        return (pow(g, plain, nn) * pow(r, n, nn)) % nn

    def decrypt(self, crypto):
        n, _ = self.public_key
        λ, μ = self.secret_key
        return ((pow(crypto, λ, n * n) - 1) // n * μ) % n


class OnlinePoll:
    def __init__(self):
        self.cryptosystem = Cryptosystem(bits=1024)
        self.votes = self.cryptosystem.encrypt(100)

    def vote(self, crypto):
        n, _ = self.cryptosystem.public_key
        nn = n * n

        if(crypto * self.votes % nn == 0):
            return -1

        self.votes = crypto * self.votes % nn

    def result(self):
        ret = self.cryptosystem.decrypt(self.votes)
        return ret


def main():
    onlinepoll = OnlinePoll()
    n, g = onlinepoll.cryptosystem.public_key
    one = onlinepoll.cryptosystem.encrypt(1)
    zero = onlinepoll.cryptosystem.encrypt(0)

    print("Welcome to OnlinePoll System")
    print("public keys...")
    print(f"n = {n}")
    print(f"g = {g}")
    print("")
    while True:
        print("Enter one if you agree and zero otherwise.")
        print(f"one = {one}")
        print(f"zero = {zero}")
        vote = int(input(">"))
        err = onlinepoll.vote(vote)

        if(err == -1):
            print("illegal input.")
            continue

        print("Election Results...")
        result = onlinepoll.result()
        print(f"Approve: {result}")
        if(result != 0):
            print("He won this vote.")
            print("Thank you for voting.")
        else:
            print("He lose this vote.")
            print("Thanks for your cooperation.")
            print(f"{flag}")
        break


if __name__ == "__main__":
    main()
