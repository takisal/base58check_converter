import bitcoin
import sys

x = sys.argv[1]

def hex_to_base58check(x, compressed):
    if compressed:
        return bitcoin.encode_privkey(x,'wif_compressed')+"\n"
    else:
        return bitcoin.encode_privkey(x,'wif')+"\n"


def main():
    print(hex_to_base58check(sys.argv[1]))
