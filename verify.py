from bitcoin.rpc import RawProxy
import hashlib
import bitcoin.core
import binascii

def swap32(x):
    return (((x << 24) & 0xFF000000) |
        ((x <<  8) & 0x00FF0000) |
        ((x >>  8) & 0x0000FF00) |
        ((x >> 24) & 0x000000FF))
        
def swap(x):
    ba = bytearray.fromhex(x)
    ba.reverse()
    return ''.join(format(n, '02x') for n in ba)

def convert_int32(x):
    return format(swap32(x), '#010x')[2:]

p = RawProxy()

blockid = str(raw_input("Enter block ID: "))

header = p.getblockheader(blockid)

version = convert_int32(header['version'])
previousBlock = swap(header['previousblockhash'])
merkleRoot = swap(header['merkleroot'])
time = convert_int32(header['time'])
bits = swap(header['bits'])
nonce = convert_int32(header['nonce'])

header_hex = version + previousBlock + merkleRoot + time + bits + nonce
header_bin = header_hex.decode('hex')
hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()

final_hash = swap(hash.encode('hex_codec'))

print(final_hash)

if (blockid == final_hash):
    print("Block is valid")
else:
    print("Block is not valid!")
