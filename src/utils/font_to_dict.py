import pygame

pygame.init()


def clip(set, pos, size):
    clip_rect = pygame.Rect(pos, size)
    set.set_clip(clip_rect)
    img = set.subsurface(set.get_clip())

    return img


def clip_font_to_dict(font_set, order, separator_color=(255, 0, 0, 255)):
    characters = {}
    character_wd = 0
    idx = 0

    # Loop over every top pixel in the given fontset
    for x in range(font_set.get_width()):
        pixel = font_set.get_at((x, 0))

        # A separator has found
        if pixel == separator_color:
            # Get letter image
            img = clip(
                font_set,
                (x - character_wd, 0),
                (character_wd, font_set.get_height())
            )

            # Append letter image to chracters dictionary
            characters[order[idx]] = img

            # Update variables
            character_wd = 0
            idx += 1
        else:
            # Update variables
            character_wd += 1

    # Return
    return characters
