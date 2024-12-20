from flask import Flask, render_template, request
from caesar_cipher import caesar_encrypt, caesar_decrypt
from flask import Flask, render_template, request, jsonify
from atbashCipher import atbash_cipher
from affineCipher import affine_cipher

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/atbash-Cipher')
def atbash_Cipher():
    return render_template('atbashCipher.html')



@app.route('/caesarCipher')
def caesarCipher():
    return render_template('caesarCipher.html')

@app.route('/affineCipher')
def affineCipher():
    return render_template('affineCipher.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    plaintext = request.form['plaintext']
    key = int(request.form['key'])
    lang = request.form['lang']
    ciphertext = caesar_encrypt(plaintext, key, lang)
    return render_template('result.html', plaintext=plaintext, key=key, ciphertext=ciphertext, lang=lang)


@app.route('/decrypt', methods=['POST'])
def decrypt():
    ciphertext = request.form['ciphertext']
    key = int(request.form['key'])
    lang = request.form['lang']
    plaintext = caesar_decrypt(ciphertext, key, lang)
    return render_template('result.html', plaintext=plaintext, key=key, ciphertext=ciphertext, lang=lang)


@app.route('/atbash-Cipher', methods=['GET', 'POST'])
def atbash():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        mode = request.form['mode']
        lang = request.form['lang']
    if lang == 'tr':
        alphabet = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    else:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = atbash_cipher(text, mode, alphabet)
    return render_template('atbashCipher.html', result=result)


# Affine cipher implementation
def affine_cipher(text, a, b, mode, lang):
    # Convert text to uppercase and remove spaces

    text = text.upper().replace(" ", "")

    if lang == 'tr':
        alphabet = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    else:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
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

@app.route('/affine', methods=['POST'])
def affine():
    # Get input data from request
    data = request.form
    text = data.get('text')
    a = int(data.get('a'))
    b = int(data.get('b'))
    mode = data.get('mode')
    lang = data.get('lang')

    # Call affine cipher function
    if mode == 'encrypt':
        ciphertext = affine_cipher(text, a, b, 'encrypt', lang)
        result = {'result': ciphertext}
    elif mode == 'decrypt':
        decrypted_text = affine_cipher(text, a, b, 'decrypt', lang)
        result = {'result': decrypted_text}
    else:
        result = {'error': 'Invalid mode: must be "encrypt" or "decrypt"'}

    # Convert result to JSON and return as response
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')  # Add CORS headers if needed
    return response




if __name__ == '__main__':
    app.run(debug=True)
