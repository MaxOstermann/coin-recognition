from PIL import Image


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb


def get_middle_color(image_path):
    image = Image.open(image_path)

    w, h = image.size
    rr, gg, bb, hh = 0, 0, 0, 0

    for x in range(w):
        for y in range(h):
            r, g, b = image.getpixel((x, y))
            rr += r
            gg += g
            hh += h

    cnt = w * h
    return rgb_to_hex((rr // cnt, gg // cnt, hh // cnt))
