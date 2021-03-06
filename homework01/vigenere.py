def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    shift = 0

    keyword = keyword.lower()
    mod = len(keyword)

    for i in range(len(plaintext)):
        c = plaintext[i]
        if c.isalpha():
            shift = ord(keyword[i % mod]) - ord("a")
            if "a" <= c <= "z":
                ciphertext += chr(ord("a") + (ord(c) - ord("a") + shift) % 26)
            else:
                ciphertext += chr(ord("A") + (ord(c) - ord("A") + shift) % 26)
        else:
            ciphertext += c

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    shift = 0

    keyword = keyword.lower()
    mod = len(keyword)

    for i in range(len(ciphertext)):
        c = ciphertext[i]
        if c.isalpha():
            shift = ord(keyword[i % mod]) - ord("a")
            if "a" <= c <= "z":
                plaintext += chr(ord("a") + (ord(c) - ord("a") + 26 - shift) % 26)
            else:
                plaintext += chr(ord("A") + (ord(c) - ord("A") + 26 - shift) % 26)
        else:
            plaintext += c

    return plaintext
