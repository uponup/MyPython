import sys
import json
import base64
from Crypto.Cipher import AES # pycryptodome

KEY = "Emoji_JingNCK567"

def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)

def main(input_file):
    with open(input_file, 'r') as f:
        tokens = {}
        for line in f:
            strs = line.split(',')
            tokens[strs[0].strip()] = strs[1].strip()
        tokensStr = json.dumps(tokens)
        aes = AES.new(add_to_16(KEY), AES.MODE_ECB)
        encrypted_text = str(base64.encodebytes(aes.encrypt(add_to_16(tokensStr))), encoding='utf-8').replace('\n', '')
        print(encrypted_text)

        with open('tokens.en', 'w') as wf:
            wf.write(encrypted_text)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('params error...')
        print('python txt2tokens.py Scanner_jq2ngnhfdse8.txt')
    else:
        main(sys.argv[1])
        print('complete ok!!!')

