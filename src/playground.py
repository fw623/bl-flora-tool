import struct

f = open("flora.bin", "rb")

# meanings:
#   name_len ... length of name
#   fill     ... likely padding, possibly flags as some contain individual 1-bits
#   b        ... idk what these are, but b3=-b2 and b4=b1
#   a        ... was always the same sequence in test sample (ffff 7f7f)
#   d        ... don't know
#   x/y      ... coordinates
#   rest     ... rest of the element
def parse_entry():
  firstByte = f.read(1)
  if firstByte == b'':
    return False

  name_len = struct.unpack('!B', firstByte)[0]
  fill1 = f.read(3)
  name = f.read(name_len).decode('ascii')
  fill2 = f.read(4)
  b1 = struct.unpack('f', f.read(4))[0]
  b2 = struct.unpack('f', f.read(4))[0]
  fill3 = f.read(4)
  a1 = f.read(4)
  b3 = struct.unpack('f', f.read(4))[0]
  b4 = struct.unpack('f', f.read(4))[0]
  fill4 = f.read(4) # with some flag
  a2 = f.read(4)
  fill5 = f.read(4) # with some flag
  fill6 = f.read(4)
  d = struct.unpack('f', f.read(4))[0]
  fill7 = f.read(4)
  x = struct.unpack('f', f.read(4))[0]
  y = struct.unpack('f', f.read(4))[0]
  rest = f.read(24)

  print(name_len, name.ljust(32), x, y)
  return True


def parse_flora():
  header = f.read(12)
  i = 0
  while parse_entry():
    i = i + 1
    print(i)

parse_flora()
