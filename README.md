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
```