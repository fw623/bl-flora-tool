# Bannerlord Flora Tool
This is a tool which edits painted flora of a Mount & Blade II: Bannerlord scene.

That is the flora placed by "Paint Flora" which is saved to `flora.bin`.

It was initially develop with the Bannerlord version `1.8.0`, but I expect it to work for scenes of practically all versions.

## Features
Current functionality is limited to moving all flora by a given offset.

## Usage
1. Download `bl-flora-tool.py` from the releases.
2. Have `python3` installed.
3. Backup your scene's `flora.bin`!
4. Execute according to the help message:
```
$ python3 bl-flora-tool.py -h
usage: bl-flora-tool.py [-h] file_in file_out x_offset y_offset

Offset flora of "Mount & Blade II: Bannerlord" scenes saved in "flora.bin". If
successful, the output filesize will be equal to the input filesize.

positional arguments:
  file_in     input file, usually "flora.bin" or similar
  file_out    output file
  x_offset    offset x-coordinates by this amount
  y_offset    offset y-coordinates by this amount

optional arguments:
  -h, --help  show this help message and exit
```
5. Load your scene with the updated flora.

### Example
The following example will move the flora defined in `flora.bin` by `0` in the x-axis and by `+333.33` in the y-axis.
```
$ python3 bl-flora-tool.py flora.bin flora_moved.bin 0 333.33
```
