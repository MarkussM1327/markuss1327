import os
os.system('cls')
# Encoding mapping
encoding_map = {
    'a': 'aaa ', 'b': 'aab ', 'c': 'abc ', 'd': 'abb ', 'e': 'aca ',
    'f': 'acc ', 'g': 'baa ', 'h': 'bab ', 'i': 'bca ', 'j': 'bcc ',
    'k': 'caa ', 'l': 'cab ', 'm': 'cbc ', 'n': 'cba ', 'o': 'ccb ',
    'p': 'cca ', 'q': 'cbb ', 'r': 'bbb ', 's': 'bbc ', 't': 'bba ',
    'u': 'bab ', 'v': 'bcb ', 'w': 'bca ', 'x': 'cca ', 'y': 'cab ',
    'z': 'ccc '
}

# Reverse mapping for decoding
decoding_map = {v: k for k, v in encoding_map.items()}

def encode(text):
    return ''.join([encoding_map[char] if char in encoding_map else char for char in text.lower()])

def decode(encoded_text):
    # Decoding every 3 characters at a time
    return ''.join([decoding_map[encoded_text[i:i+3]] if encoded_text[i:i+3] in decoding_map else encoded_text[i:i+3] for i in range(0, len(encoded_text), 3)])

# Example usage
message = input('Enter something: ')
encoded_message = encode(message)
print("Encoded:", encoded_message)

# To demonstrate decoding as well:
decoded_message = decode(encoded_message)




