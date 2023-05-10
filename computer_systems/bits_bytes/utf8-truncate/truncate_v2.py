import sys

def truncate(s, n):
  if n >= len(s):
    return s
  
  while n > 0 and (s[n] & 0xc0) == 0x80:
    n -= 1
  
  return s[:n]

with open("./cases", "rb") as f:
  while True:
    line = f.readline()

    if len(line) == 0:
      break

    n = line [0]
    s = line[1:-1]

    res = truncate(n, s)

    sys.stdout.buffer.write(res + b'\n')

