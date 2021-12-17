from tkinter.filedialog import askdirectory
from os import walk, path
from stegano import lsb
from tkinter import Tk
from png import Reader
from sys import exit

gui = Tk().withdraw()

directory = askdirectory(title = "Select Pack")
if directory == "":
  exit()

for subdir, dirs, files in walk(directory):
  for file in files:
    if file.endswith(".png"):
      print(f"Reading {file}")
      filePath = path.join(subdir, file)
      try:
        chunks = list(Reader(filename = filePath).chunks())
        for item in chunks:
          if item[0] == b"tEXt":
            print(f"\tMetadata: {item[1].decode()}")
      except:
        print(f"\tMetadata: Error occured while reading")
      try:
        print(f"\tEncoded: {lsb.reveal(filePath)}")
      except:
        print(f"\tEncoded: Error occured while reading")
      print("\n")

input("Finished!")