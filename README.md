# packSigner
A tool to sign the textures in Minecraft resource packs

This tool takes a message of your choice, and encodes it into the textures of a resource pack so that you can tell when they have been stolen.

The message is added in 2 separate ways:
- Metadata
- Pixel Encoding

# Metatata
This method adds the message to the metadata of the textures. 

With the metadata, there is no character limit (within reason).

With this method it easy to view the message, but also easy to remove. To view the metadata message, you can either use the provided checker tool, or open the image in notepad.

# Pixel Encoding
This method encodes the message into the physical pixels of the texture by making minor adjustments to the colours. The end result looks almost identical to the input where you will not be able to see a difference without using a colour picker.

Since this method is distructive to the original textures, a copy of the pack is made and edited instead of the original.

With pixel encoding, there is a character limit based on the texture resolution. Here are some examples of the character limits:

- 8x8: 20
- 16x16: 92
- 32x32: 379
- 64x64: 1530

If the provided message is too long for the texture resolution, the end is automatically trimmed off.

With this method it is hard to view the message, and also harder to remove it. To view the pixel encoded message, you have to use the provided checker tool.