from tkinter.filedialog import askdirectory
from png import Reader, write_chunks
from stegano import lsb, tools
from math import floor, log10
from shutil import copytree
from os import walk, path
from tkinter import Tk
from PIL import Image
from sys import exit

message = input("This tool signs the textures in resource packs so that you can easily identify if a texture is stolen.\n\nThe messages are added to the image with both metadata, and encoding it into the pixels. There is no character limit for the metadata, but the encoded one has a limit based on the resolution.\n\nHere are some of the character limits:\n\n8x8:   20\n16x16: 92\n32x32: 379\n64x64: 1530\n\nIf you go over the limit, the end will automatically be trimmed off.\n\n\n\nPlease enter the message to sign the textures with: ")

gui = Tk().withdraw()

directory = askdirectory(title = "Select Pack")
if directory == "":
  exit()

outDirectory = directory + "_signed"

if path.isdir(outDirectory):
  x = 2
  while True:
    newOut = outDirectory + str(x)
    if not path.isdir(newOut):
      outDirectory = newOut
      break
    x += 1

print("\n\nCopying pack...")
copytree(directory, outDirectory)

for subdir, dirs, files in walk(outDirectory):
  for file in files:
    if file.endswith(".png"):
      try:
        filePath = path.join(subdir, file)
        img = Image.open(filePath).convert("RGBA")
        img.save(filePath)
        maxLength = (img.size[0] * img.size[1] * 3) / 8 - 1
        maxLength -= floor(log10(maxLength)) + 2
        maxLength = int(maxLength)
        lsb.hide(filePath, message[:maxLength], auto_convert_rgb = True).save(filePath)
        chunks = list(Reader(filename = filePath).chunks())
        chunks.insert(1, (b"tEXt", bytes(message, "utf-8")))
        with open(filePath, "wb") as out:
          write_chunks(out, chunks)
        print(f"Done {file}")
      except:
        print(f"Skipped {file} as an error occured")

input(f"\nFinished! Output to {outDirectory}")