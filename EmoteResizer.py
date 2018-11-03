#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Takes an image and makes it compatible for a Discord emote.

This script takes a cropped image and turns it into
the appropriate size for use in a Discord emote, maximizing
the possible size in the 128pxx128px allowed by Discord
"""
__version__ = "1.1"
__author__ = "Marc Hoeltge"

import sys
from wand.image import Image
from wand.display import display

with Image(filename=sys.argv[1]) as img:
    IMAGE_SIDE_LENGTH_PX = 128
    #autocrop the image to get rid of transparent space outlining it
    img.trim()

    #determine if width is the longest side of the image
    width_longest_side = True
    if img.width < img.height:
        width_longest_side = False

    if width_longest_side:
        #find the ratio that the short side will have to be scaled
        scale_ratio = float(IMAGE_SIDE_LENGTH_PX) / img.width
        new_height = int(round(scale_ratio * img.height))

        #crop the image into the smallest size possible
        img.resize(IMAGE_SIDE_LENGTH_PX, new_height)

        #create a new blank image and make a composite with the cropped image
        with Image(width=IMAGE_SIDE_LENGTH_PX, height=IMAGE_SIDE_LENGTH_PX) as newImg:
            top = (IMAGE_SIDE_LENGTH_PX - new_height) / 2
            newImg.composite(img, left=0, top=top)
            newImg.format = "png"
            newImg.save(filename=sys.argv[2])

    #repeat the above code but in terms of the height being the longest side
    else:
        scale_ratio = float(IMAGE_SIDE_LENGTH_PX) / img.height
        new_width = int(round(scale_ratio * img.width))
        img.resize(new_width, IMAGE_SIDE_LENGTH_PX)
        with Image(width=IMAGE_SIDE_LENGTH_PX, height=IMAGE_SIDE_LENGTH_PX) as newImg:
            left = (IMAGE_SIDE_LENGTH_PX - new_width) / 2
            newImg.composite(img, left=left, top=0)
            newImg.format = "png"
            newImg.save(filename=sys.argv[2])



