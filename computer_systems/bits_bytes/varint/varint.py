import struct

def encode(n):
  encoded = []

  while n > 0:
    bit_group = n & 0x7f

    bit_group |= 0x80
    
    encoded.append(bit_group)

    n >>= 7
    
  encoded[-1] ^= 0x80

  return bytes(encoded)


def decode(varint):
  decoded = 0

  for byte in varint[::-1]:
    decoded <<= 7

    decoded |= (byte & 0x7f)

  return decoded


if __name__ == '__main__':
  cases = (
    ('1.uint64', b'\x01'),
    ('150.uint64', b'\x96\x01'),
    ('maxint.uint64', b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01'),
  )

  for fname, expectation in cases:
    with open(fname, 'rb') as f:
      n = struct.unpack('>Q', f.read())[0]
      assert encode(n) == expectation
      assert decode(encode(n)) == n
  print("OK")
