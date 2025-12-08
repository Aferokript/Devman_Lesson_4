from PIL import Image

image = Image.open('monro.jpg')
red, green, blue = image.split()
coordinate_left = (50, 0, red.width, red.height)
red_left = red.crop(coordinate_left)
coordinate_middle = (25, 0, red.width - 25, red.height)
red_middle = red.crop(coordinate_middle)
red_blend = Image.blend(red_left, red_middle, 0.5)

coordinate_blue_left = (0, 0, blue.width - 50, blue.height)
blue_left = blue.crop(coordinate_blue_left)
coordinate_blue_middle = (25, 0, blue.width - 25, blue.height)
blue_middle = blue.crop(coordinate_blue_middle)
blue_blend = Image.blend(blue_left, blue_middle, 0.5)

coordinate_green = (25, 0, green.width - 25, green.height)
green_complete = green.crop(coordinate_green)


complete_monro = Image.merge('RGB', (red_blend, green_complete, blue_blend))
complete_monro.save('complete_monro.jpg')
