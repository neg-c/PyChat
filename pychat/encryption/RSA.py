import math
import rsa


class RSA:
    @staticmethod
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        return RSA.gcd(b, a % b)

    @staticmethod
    def generate_keypair():
        private_key, public_key = rsa.newkeys(1024)
        return public_key, private_key

    @staticmethod
    def encrypt(pk, plaintext):
        ciphertext = rsa.encrypt(plaintext.encode('utf-8'), pk)
        return ciphertext

    @staticmethod
    def decrypt(pk, ciphertext):
        plaintext, _ = rsa.decrypt(ciphertext, pk).decode('utf-8')
        return plaintext
