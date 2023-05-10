with open("./cases", "rb") as f:

  for line in f.readlines():

    truncate = line[0]
    txt = line[1:-1]

    if truncate >= len(txt):
      print(txt.decode('utf-8'))
      continue

    pointer = 1

    bytes_to_print = bytearray()

    while True:
      if pointer > truncate:
        break

      codepoint = (line[pointer] & 0x80) >> 7

      if codepoint == 0:
        bytes_to_print.append(line[pointer])
        pointer += 1
      
      if codepoint == 1:
        length = (line[pointer] & 0xf0) >> 4
        size = 0

        match length:
          case 15:
            size = 4
          case 14:
            size = 3
          case 12:
            size = 2 

        if pointer + size <= truncate:
          bytes_to_print += bytearray(line[pointer: pointer + size])
          pointer += size
        else:
          break

    print(bytes_to_print.decode('utf-8'))
