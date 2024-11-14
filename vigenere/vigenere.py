# Letter frequencies in standard English sentences
alphabet_freqs = [0.0817, 0.0149, 0.0278, 0.0425, 0.1270, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0403, 0.0241, 0.0675, 0.0751, 0.0193, 0.0009, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007]

def lowest_local_max(array):
    lowest_max = float('inf')
    for i in range(1, len(array) - 1):
        if array[i] > array[i - 1] and array[i] > array[i + 1] and array[i] > 0.06:
            lowest_max = min(lowest_max, array[i])
            break
    return lowest_max

def get_key_length(cipher):
    cosets = []
    for i in range(100):
        cosets.append([cipher[i::length] for length in range(1, len(cipher))])
    # get index of coincidence for each coset
    
    matrix_of_ics = []
    for i in range(len(cosets)):
        ics_of_k_lengths = []
        for j in range(len(cosets[i])):
            ic = 0
            for char in range(26):
                ic += (cosets[i][j].count(chr(65 + char))/len(cosets[i][j]))**2
            ics_of_k_lengths.append(ic)
        matrix_of_ics.append(ics_of_k_lengths)
    
    # get average ic for each key length
    col_avgs = []
    for col in range(len(matrix_of_ics) - 1):
        col_sum = sum(row[col] for row in matrix_of_ics)
        col_avgs.append(col_sum/(len(matrix_of_ics)))
    key_len = col_avgs.index(lowest_local_max(col_avgs)) + 1
    return key_len
    
def get_key(cipher, key_len, alphabet_freqs):
    # compartmentalize the cipher
    sub_ciphers = []
    for i in range(key_len):
        sub_cipher = []
        for char in range(len(cipher)):
            if char%key_len == i:
                sub_cipher.append(cipher[char])
        sub_ciphers.append(''.join(sub_cipher))
    
    k = ''
    for i in range(len(sub_ciphers)):
        ics = []
        for shift in range(26):
            ic = 0
            for char in range(26):
                ic += alphabet_freqs[char]*sub_ciphers[i].count(chr((char + shift)%26 + 65))/len(sub_ciphers[i])
            ics.append(ic)
        k += chr(65 + ics.index(max(ics)))
    return k

def decrypt(cipher, key):
    decrypted = []
    for char in range(0, len(cipher), len(key)):
        for k in range(len(key)):
            if char + k >= len(cipher):
                break
            decrypted.append(chr(65 + (ord(cipher[char + k]) - ord(key[k]))%26))
    return ''.join(decrypted)

def decrypt_vigenere(text):
    #with open('cipher.txt', 'r') as file:
    #    file_contents = file.read()
    text = text.replace('\n', '')
    key_len = get_key_length(text)
    key = get_key(text, key_len, alphabet_freqs)
    decrypted = decrypt(text, key)
    #return key, key_len, decrypted
    return decrypted
