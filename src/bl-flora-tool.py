import struct
import os
import argparse

# for explanation see 'playground.py'
HEADER_LEN = 12
NAME_PREFILL_LEN = 3
DATA_LEN = 84
DATA_X_OFFSET = 52
DATA_Y_OFFSET = 56


def offset_entry_data(data, x_offset: float, y_offset: float):
  x = struct.unpack('f', data[DATA_X_OFFSET:DATA_X_OFFSET+4])[0]
  y = struct.unpack('f', data[DATA_Y_OFFSET:DATA_Y_OFFSET+4])[0]

  data_offset = bytearray(data)
  data_offset[DATA_X_OFFSET:DATA_X_OFFSET+4] = struct.pack('f', x + x_offset)
  data_offset[DATA_Y_OFFSET:DATA_Y_OFFSET+4] = struct.pack('f', y + y_offset)
  return data_offset


def offset_entry(f_in, f_out, x_offset: float, y_offset: float):
  firstByte = f_in.read(1)
  if firstByte == b'':
    return False
  name_len = struct.unpack('!B', firstByte)[0]

  name_prefill = f_in.read(NAME_PREFILL_LEN)
  name = f_in.read(name_len)
  data = f_in.read(DATA_LEN)

  data_offset = offset_entry_data(data, x_offset, y_offset)

  f_out.write(firstByte + name_prefill + name + data_offset)
  return True


def offset_flora(filename_in: str, filename_out: str, x_offset: float, y_offset: float):
  num_entries = 0
  with open(filename_in, 'rb') as f_in:
    with open(filename_out, 'wb') as f_out:
      header = f_in.read(HEADER_LEN)
      f_out.write(header)
      while offset_entry(f_in, f_out, x_offset, y_offset):
        num_entries += 1
        if (num_entries % 1000) == 0:
          print(f'{num_entries}', end='\r')

  print(f'Flora entries offset: {num_entries}')
  print(f'Input filesize:  {os.stat(filename_in).st_size}B ({filename_in})')
  print(f'Output filesize: {os.stat(filename_out).st_size}B ({filename_out})')


def main():
  parser = argparse.ArgumentParser(
    description="""Offset flora of "Mount & Blade II: Bannerlord" scenes saved in "flora.bin".
If successful, the output filesize will be equal to the input filesize.""",
  )
  parser.add_argument('file_in', type=str, help='input file, usually "flora.bin" or similar')
  parser.add_argument('file_out', type=str, help='output file')
  parser.add_argument('x_offset', type=float, help='offset x-coordinates by this amount')
  parser.add_argument('y_offset', type=float, help='offset y-coordinates by this amount')

  args = parser.parse_args()
  offset_flora(args.file_in, args.file_out, args.x_offset, args.y_offset)


if __name__ == '__main__':
  main()
