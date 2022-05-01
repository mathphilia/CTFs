# coding: utf-8
import os
from Crypto.Util.number import getPrime, bytes_to_long

from secret import flag


def encrypt(plain, N, e):
    return pow(plain, e, N)


def decrypt(enc, p, q, e):
    phi = (p-1) * (q-1)
    d = pow(e, -1, phi)
    return pow(enc, d, p * q)


def generate_question(N, e):
    question1 = bytes_to_long(os.urandom(16))
    question2 = bytes_to_long(os.urandom(16))
    question3 = question1 * question2

    return [encrypt(question1, N, e), encrypt(question2, N, e)], encrypt(question3, N, e)


def main():
    p = getPrime(512)
    q = getPrime(512)
    N = p * q
    e = 0x10001

    print("Welcome to Happy App")
    print(f"N = {N}")
    print(f"e = {e}")
    while True:
        q, correct = generate_question(N, e)
        print(f"encrypt(a) = {q[0]}")
        print(f"encrypt(b) = {q[1]}")
        print("What is a × b encrypted")

        answer = int(input("> "))
        if(correct == answer):
            print(flag)
        else:
            print("Noooooo")
        break
    return


if __name__ == "__main__":
    main()
