import struct

file = open("./teapot.bmp", 'rb')
new_file = open("rotate.bmp", "wb")

data = file.read()
offset = data[10]

new_file.write(data[0:offset])

width = struct.unpack('<i', data[18:22])[0]
height = struct.unpack('<i',data[22:26])[0]

bits_per_pixel = struct.unpack('<h', data[28:30])[0]

bytes_per_pixel = int(bits_per_pixel / 8)

for h in range(height):
  for w in range(width):
    value = offset + (((w * height) + ((width - 1) - h )) * bytes_per_pixel)

    new_file.write(data[value:value + bytes_per_pixel])


print("OK")