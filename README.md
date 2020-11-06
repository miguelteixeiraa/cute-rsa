# cute-rsa

A simple RSA implementation. Quickly developed as a work in a college subject.


**To test:**
```python
# -*- coding: utf-8 -*-
from CuteRSA import CuteRSA

rsa = CuteRSA()

encrypted_message = rsa.cute_encrypt("Computing")
print(f"Encrypted Message: {encrypted_message}\n")

decrypted_message = rsa.cute_decrypt(encrypted_message)
print(f"Decrypted Message: {decrypted_message}\n")


# to test homomorphic multiplicative operations

encr_number_one = rsa.cute_encrypt(46)
encr_number_two = rsa.cute_encrypt(43)

encr_h_mult = rsa.cute_mult(encr_number_one, encr_number_two)

decrypted_message = rsa.cute_decrypt(encr_h_mult, "number_operations")

print(
    f"It seems that we have an homomorphic result! The result of our operation is: {decrypted_message}"
)

```
