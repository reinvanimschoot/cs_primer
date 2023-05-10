import struct

file = open("./synflood.pcap", 'rb')

file.read(24)

count = 0
initiated = 0
resolved = 0

while True:
  per_packet_header = file.read(16)

  if len(per_packet_header) == 0:
      break

  count += 1
  _, _, length, untrunc_length = struct.unpack('<IIII', per_packet_header)
  assert length == untrunc_length

  packet = file.read(length)

  version = struct.unpack('<I', packet[:4])[0]
  assert version == 2

  ihl = (packet[4] & 0x0f) << 2

  tcp_segment = packet[(ihl + 4):]

  src, dst, _, _, flags = struct.unpack('!HHIIH', tcp_segment[:14])

  syn = (flags & 0x0002) > 0
  ack = (flags & 0x0010) > 0

  if dst == 80 and syn:
    initiated += 1

  if src == 80 and ack:
    resolved += 1

print("Incoming syn requests: ", initiated)
print("Resolved syn requests: ", resolved)

print("OK")