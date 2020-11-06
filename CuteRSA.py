# -*- coding: utf-8 -*-
from random import randint
from typing import List, Tuple, Any
from collections.abc import Iterable

# from binascii import unhexlify


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

    def cute_mult(self, encr_element_one, encr_element_two) -> List[Any]:
        return [encr_element_one[0] * encr_element_two[0]]

    def cute_encrypt(self, message: Any) -> List[Any]:
        encrypted_message: List[int] = []

        plainMessage: List[int] = []
        if not isinstance(message, Iterable):
            plainMessage.append(message)
        else:
            plainMessage = message

        for pl_element in plainMessage:
            if type(pl_element) != str:
                encr_element = pow(
                    pl_element,
                    self._cuteKeys["Public Key"][1],
                    self._cuteKeys["Public Key"][0],
                )
                encrypted_message.append(encr_element)
            #
            elif type(pl_element) == str:
                encr_element = pow(
                    ord(character),
                    self._cuteKeys["Public Key"][1],
                    self._cuteKeys["Public Key"][0],
                )
                encrypted_message.append(encr_element)
            #
        #
        return encrypted_message

    #

    def cute_decrypt(self, message_encr: List[int], decr_type) -> Any:
        decrypted_message: List[Any] = list()

        if decr_type == "number_operations":
            for encr_element in message_encr:
                decrypted_message.append(
                    pow(
                        encr_element,
                        self._cuteKeys["Private Key"][1],
                        self._cuteKeys["Public Key"][0],
                    )
                )
            #
            return decrypted_message
        #
        elif decr_type == "str_operations":
            for encr_element in message_encr:
                decrypted_message.append(
                    chr(
                        pow(
                            encr_element,
                            self._cuteKeys["Private Key"][1],
                            self._cuteKeys["Public Key"][0],
                        )
                    )
                )
            #
            return "".join(decrypted_message)
        #
        return False


#


if __name__ == "__main__":
    rsa = CuteRSA()

    encr_number_one = rsa.cute_encrypt(46)
    encr_number_two = rsa.cute_encrypt(43)

    encr_h_mult = rsa.cute_mult(encr_number_one, encr_number_two)

    decrypted_message = rsa.cute_decrypt(encr_h_mult, "number_operations")

    print(
        f"It seems that we have an homomorphic result! The result of our operation is: {decrypted_message}"
    )
