def affine_cipher(text, a, b, mode, lang):
    # Convert text to uppercase and remove spaces
    text = text.upper().replace(" ", "")
    if lang == 'en':
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif lang == 'tr':
        alphabet = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    else:
        raise ValueError('Invalid language option')

    result = ""

    # Calculate modular multiplicative inverse of 'a' modulo 26
    def mod_inverse(a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    # Determine if encryption or decryption mode
    if mode == 'encrypt':
        # Encrypt mode: E(x) = (a*x + b) mod 26
        for char in text:
            if char in alphabet:
                # Encrypt the character using the affine cipher formula
                char_index = alphabet.index(char)
                encrypted_index = (a * char_index + b) % len(alphabet)
                encrypted_char = alphabet[encrypted_index]
                result += encrypted_char
            else:
                # If character is not in the alphabet, append as is
                result += char
    elif mode == 'decrypt':
        # Decrypt mode: D(y) = a^(-1)(y - b) mod 26
        mod_inv = mod_inverse(a, len(alphabet))
        if mod_inv is None:
            raise ValueError("Invalid key: 'a' is not invertible")
        for char in text:
            if char in alphabet:
                # Decrypt the character using the affine cipher formula
                char_index = alphabet.index(char)
                decrypted_index = (mod_inv * (char_index - b)) % len(alphabet)
                decrypted_char = alphabet[decrypted_index]
                result += decrypted_char
            else:
                # If character is not in the alphabet, append as is
                result += char
    else:
        raise ValueError("Invalid mode: must be 'encrypt' or 'decrypt'")

    # Return result
    return result
