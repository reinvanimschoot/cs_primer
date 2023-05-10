import sys
import tty

fd = sys.stdin.fileno()
old = tty.tcgetattr(fd)

tty.setcbreak(fd)

try:
  while(True):
    key = sys.stdin.read(1)

    ascii = ord(key)

    if ascii in range(ord("1"), ord("9")):
      beeps = ascii - ord("0")

      for _ in range(beeps):
        sys.stdout.buffer.write(b'\x07')
        sys.stdout.flush()

except KeyboardInterrupt:
  tty.tcsetattr(fd, tty.TCSAFLUSH, old) 
finally:
  tty.tcsetattr(fd, tty.TCSAFLUSH, old) 
