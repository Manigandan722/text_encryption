def caesar_encrypt(plaintext, key, lang):
    if lang == 'en':
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif lang == 'tr':
        alphabet = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    else:
        raise ValueError('Invalid language option')

    ciphertext = ""
    for char in plaintext.upper():
        if char in alphabet:
            shifted_char = alphabet[(alphabet.index(char) + key) % len(alphabet)]
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, key, lang):
    if lang == "tr":
        alphabet = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    else:  # default to English alphabet if lang is not "tr"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = ""
    for char in ciphertext.upper():
        if char in alphabet:
            shifted_char = alphabet[(alphabet.index(char) - key) % len(alphabet)]
            plaintext += shifted_char
        else:
            plaintext += char
    return plaintext
