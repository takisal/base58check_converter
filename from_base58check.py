import bitcoin
import sys

x = sys.argv[1]
print(bitcoin.encode_privkey(x,'wif')+"\n")

print(bitcoin.encode_privkey(x,'wif_compressed')+"\n")
