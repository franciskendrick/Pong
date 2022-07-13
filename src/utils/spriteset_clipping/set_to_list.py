from .clip import clip


def clip_set_to_list_on_xaxis(set, y=0):
    images = []

    # Loop over every top pixel in the given spriteset
    for x in range(set.get_width()):
        pixel = set.get_at((x, y))

        # A sprite has been found
        if pixel == (255, 0, 255, 255):  # magenta pixel
            wd, ht = (0, 0)

            # Find the end of the sprite in the X coordinate
            while True:
                wd += 1
                pixel = set.get_at((x + wd, y))
                if pixel == (0, 255, 255, 255):  # cyan pixel
                    break

            # Find the end of the sprite in the Y coordinate
            while True:
                ht += 1
                pixel = set.get_at((x, ht))
                if pixel == (0, 255, 255, 255):  # cyan pixel
                    break

            # Clip image
            img = clip(
                set, 
                (x + 1, 1),
                (wd - 1, ht - 1)
            )

            # Append to images list
            images.append(img)

    # Unpack the images list if its values is less than one
    [images] = [images] if len(images)> 1 else images
    
    # Return
    return images


def clip_set_to_list_on_yaxis(set, x=0):
    images = []

    # Loop over every left pixel in the given spriteset
    for y in range(set.get_height()):
        pixel = set.get_at((x, y))

        # A sprite has been found
        if pixel == (255, 0, 255, 255):  # magenta
            wd, ht = (0, 0)

            # Find the end of the sprite in the X coordinate
            while True:
                wd += 1
                pixel = set.get_at((wd, y))
                if pixel == (0, 255, 255, 255):  # cyan
                    break

            # Find the end of the sprite in the Y coordinate
            while True:
                ht += 1
                pixel = set.get_at((x, y + ht))
                if pixel == (0, 255, 255, 255):  # cyan
                    break

            # Clip image
            img = clip(
                set,
                (1, y + 1),
                (wd - 1, ht - 1)
            )

            # Append to images list
            images.append(img)

    # Unpack the images list if its values is less than one
    [images] = [images] if len(images)> 1 else images

    # Return
    return images
