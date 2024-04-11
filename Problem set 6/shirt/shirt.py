import sys
import os
from PIL import Image, ImageOps

extensions = ['.png' , '.jpg' , '.jpeg']

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')

if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

else:

    root_ext_input = os.path.splitext(sys.argv[1])
    root_ext_output = os.path.splitext(sys.argv[2])

    if root_ext_input[1] not in extensions:
        sys.exit('Invalid input')

    elif root_ext_output[1] not in extensions:
        sys.exit('Invalid output')

    else:

        if root_ext_input[1] != root_ext_output[1]:
            sys.exit('Input and output have different extensions')

        else:
            try:
                shirt = Image.open("shirt.png")
                shirt_size = shirt.size
                image = Image.open(sys.argv[1])
                cropped_image = ImageOps.fit(image, shirt_size)
                #only providing size in order to use default value of method bleed and centering
                cropped_image.paste(shirt, shirt)
                #first shirt represents the image to overlay
                #second shirt represents a “mask” indicating which pixels in photo to update.
                cropped_image.save(sys.argv[2])

            except FileNotFoundError:
                sys.exit('Input does not exist')
