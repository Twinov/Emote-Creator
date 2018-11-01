# Emote-Creator
A python script that takes an image and resizes it for use as a Discord emote.

This project requires the python Wand library to be installed (can be done through pip) and also needs ImageMagick to be on the the user's computer.

To use, clone the repository and type 

`python EmoteResizer.py [image to be made into an emote] [output filename]`

The output file will be a 128x128 pixel png that will be ready to be put into a server.

It is expected that the file is already cropped before this tool is used on it. This script is only meant to remove whitespace and maximize the size of the emote given its dimensions.
