import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for c in plaintext:
        if c.isalpha():
            if chr(ord(c) + shift).isalpha():
                ciphertext += chr(ord(c) + shift)
            else:
                ciphertext += chr(ord(c) + shift - 26)
        else:
            ciphertext += c
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            if chr(ord(c) - shift).isalpha():
                plaintext += chr(ord(c) - shift)
            else:
                plaintext += chr(ord(c) - shift + 26)
        else:
            plaintext += c
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    best_shift = 0
    plaintext = ""
    while best_shift < 26:
        plaintext = ""
        for c in ciphertext:
            if c.isalpha():
                if chr(ord(c) - best_shift).isalpha():
                    plaintext += chr(ord(c) - best_shift)
                else:
                    plaintext += chr(ord(c) - best_shift + 26)
            else:
                plaintext += c
        if plaintext in dictionary:
            break
        else:
            best_shift += 1
    return best_shift
