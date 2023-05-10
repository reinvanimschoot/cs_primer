import struct

SIGN = 0b0
EXP = 0b11111111111
INF = 0b1

M_LEN_MASK = 0b00000111

def conceal(m):
    f = SIGN
    f = (f << 11) | EXP
    f = (f << 1) | INF

    m_len = len(m.encode('utf-8'))

    assert m_len <= 6

    f = (f << 3) | m_len

    for c in m:
        f = (f << 8) | ord(c)

    f <<= ((6 - m_len) * 8)

    return struct.unpack('>d', struct.pack('>Q',f))[0]

def extract(n):
    x = struct.pack('>d', n)

    m_len = x[1] & M_LEN_MASK

    return x[2: 2 + m_len].decode('utf-8')
