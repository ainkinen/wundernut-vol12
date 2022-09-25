def rot5_decrypt(encrypted: str, /) -> str:
    rot5 = ''.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'FGHIJKLMNOPQRSTUVWXYZABCDE')  # Ceasar cipher with a shift of 5
    return encrypted.translate(rot5)
