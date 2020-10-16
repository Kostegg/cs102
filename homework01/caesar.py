import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a757f48... Реализована функция is_prime(n)
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
<<<<<<< HEAD
=======
>>>>>>> 49424cf... Убран лишний код и переименована функция взломщика обратно в caesar_breaker
    ciphertext = ""
    for c in plaintext:
        if c.isalpha():
<<<<<<< HEAD
            if "a" <= c <= "z":
                ciphertext += chr(ord("a") + (ord(c) - ord("a") + shift) % 26)
                """
=======
    ciphertext = ""
    for c in plaintext:
        if c.isalpha():
            if 'a' <= c <= 'z':
               ciphertext += chr(ord('a') + (ord(c) - ord('a') + shift) % 26)
               """
>>>>>>> a757f48... Реализована функция is_prime(n)
                    ord(c) - ord('a') - номер буквы в алфавите
                    + shift - сдвигаем
                    %26 - берем по модулю размера алфавита 
                     (ord(c) - ord('a') + shift) % 26 - номер итогового символа

               """
<<<<<<< HEAD
            else:
                ciphertext += chr(ord("A") + (ord(c) - ord("A") + shift) % 26)
=======
            if chr(ord(c) + shift).isalpha():
                ciphertext += chr(ord(c) + shift)
            else:
                ciphertext += chr(ord(c) + shift - 26)
>>>>>>> 374337a... Реализована шифровка и расшифровка
=======
            else:
               ciphertext += chr(ord('A') + (ord(c) - ord('A') + shift) % 26)
>>>>>>> a757f48... Реализована функция is_prime(n)
        else:
            ciphertext += c
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a757f48... Реализована функция is_prime(n)
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
<<<<<<< HEAD
=======
>>>>>>> 49424cf... Убран лишний код и переименована функция взломщика обратно в caesar_breaker
    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
<<<<<<< HEAD
<<<<<<< HEAD
            if "a" <= c <= "z":
                plaintext += chr(ord("a") + (ord(c) - ord("a") + 26 - shift) % 26)
            else:
                plaintext += chr(ord("A") + (ord(c) - ord("A") + 26 - shift) % 26)
=======
            if chr(ord(c) + - shift).isalpha():
=======
            if chr(ord(c) - shift).isalpha():
>>>>>>> 2dd9b35... Реализована функция caesar_breaker_brute_force
                plaintext += chr(ord(c) - shift)
            else:
                plaintext += chr(ord(c) - shift + 26)
>>>>>>> 374337a... Реализована шифровка и расшифровка
=======
    plaintext = ""
    for c in ciphertext:
        if c.isalpha():            
            if 'a' <= c <= 'z':
                plaintext += chr(ord('a') + (ord(c) - ord('a') + 26 - shift) % 26)
            else:
                plaintext += chr(ord('A') + (ord(c) - ord('A') + 26 - shift) % 26)
>>>>>>> a757f48... Реализована функция is_prime(n)
        else:
            plaintext += c
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
<<<<<<< HEAD
<<<<<<< HEAD
    """
<<<<<<< HEAD
=======
    Brute force breaking a Caesar cipher.
>>>>>>> 2dd9b35... Реализована функция caesar_breaker_brute_force
=======
    """
>>>>>>> a757f48... Реализована функция is_prime(n)
    >>> d = {"python", "java", "ruby"}
    >>> caesar_breaker_brute_force("python", d)
    0
    >>> caesar_breaker_brute_force("sbwkrq", d)
    3
    """
<<<<<<< HEAD
=======
>>>>>>> 49424cf... Убран лишний код и переименована функция взломщика обратно в caesar_breaker
=======
>>>>>>> a757f48... Реализована функция is_prime(n)
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
