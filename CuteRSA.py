from random import randint
from typing import List, Tuple


class CuteRSA:
    def __init__(self) -> None:
        self._cuteKeys = {"Public Key": Tuple, "Private Key": Tuple}
        self._generateKeys()

    def _loadListOfPrimes(self) -> List[int]:
        list_of_primes: List[int] = []
        file_lines = open("prime_numbers.txt", "r").readlines()
        for line in file_lines:
            tmp_line = line.split("\t")
            for number in tmp_line:
                list_of_primes.append(int(number))
            #
        #
        return list_of_primes

    #

    def _modInv(self, e: int, totient: int) -> int:
        e = e % totient
        for x in range(1, totient):
            if (e * x) % totient == 1:
                return x
            #
        #
        return 1

    #

    def _generateKeys(self) -> None:
        # selecting p and q
        list_of_primes = self._loadListOfPrimes()
        p: int = list_of_primes[randint(0, len(list_of_primes)) - 1]
        q: int = list_of_primes[randint(0, len(list_of_primes)) - 1]

        # ensures that p and q are different prime numbers
        while p == q:
            p: int = list_of_primes[randint(0, len(list_of_primes)) - 1]
        #

        # n is released as part of the public key.
        n: int = p * q

        totient: int = (p - 1) * (q - 1)

        # choosing 'e', ​​where 1 < 'e' < totient and gcd = 1
        e: int = 0
        do: bool = True
        while do:
            e = list_of_primes[randint(0, len(list_of_primes)) - 1]
            if (totient % e) != 0 and e < totient:
                do = False
            #
        #

        # d is the modular multiplicative inverse of e modulo totient
        d: int = self._modInv(e, totient)

        self._cuteKeys["Public Key"] = (n, e)
        self._cuteKeys["Private Key"] = (n, d)

        print(f"Public Key: {self._cuteKeys['Public Key']}\n")
        print(f"Private Key: {self._cuteKeys['Private Key']}\n")

    #

    def cute_encrypt(self, message: str) -> List[int]:
        encrypted_message: List[int] = []
        for character in message:
            encrypted_message.append(
                pow(
                    ord(character),
                    self._cuteKeys["Public Key"][1],
                    self._cuteKeys["Public Key"][0],
                )
            )
        #
        return encrypted_message

    #

    def cute_decrypt(self, message_encr: List[int]) -> str:
        decrypted_message: List[char] = [
            chr(
                pow(
                    character,
                    self._cuteKeys["Private Key"][1],
                    self._cuteKeys["Public Key"][0],
                )
            )
            for character in message_encr
        ]
        return "".join(decrypted_message)


if __name__ == "__main__":
    rsa = CuteRSA()
    encrypted_message = rsa.cute_encrypt("Computing")
    print(f"Encrypted Message: {encrypted_message}\n")

    decrypted_message = rsa.cute_decrypt(encrypted_message)
    print(f"Decrypted Message: {decrypted_message}\n")
