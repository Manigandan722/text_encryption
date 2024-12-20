def atbash_cipher(text, mode, lang):
    if lang == 'tr':
        alphabet = 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
    else:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if mode == 'encrypt':
        result = ''
        for char in text:
            if char.isalpha():
                if char.isupper():
                    result += alphabet[25 - alphabet.index(char)]
                else:
                    result += alphabet[25 - alphabet.index(char.upper())].lower()
            else:
                result += char
        return result
    else:
        return atbash_cipher(text, 'encrypt', lang)
