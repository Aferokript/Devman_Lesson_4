from PIL import Image

image = Image.open('monro.jpg')
red, green, blue = image.split()
coordinate_left = (50, 0, red.width, red.height)
red_left = red.crop(coordinate_left)
coordinate_middle = (25, 0, red.width - 25, red.height)
red_middle = red.crop(coordinate_middle)
red_blend = Image.blend(red_left, red_middle, 0.5)

coordinate_blue_left = (50, 0, blue.width, blue.height)
blue_left = blue.crop(coordinate_blue_left)
coordinate_blue_middle = (25, 0, blue.width - 25, blue.height)
blue_middle = blue.crop(coordinate_blue_middle)
blue_blend = Image.blend(blue_left, blue_middle, 0.5)

coordinate_green_left = (50, 0, green.width, green.height)
green_left = green.crop(coordinate_green_left)
coordinate_green_middle = (25, 0, green.width - 25, green.height)
green_middle = green.crop(coordinate_green_middle)

complete_monro = Image.merge('RGB', (red_blend, blue_blend, green_middle))
complete_monro.thumbnail((80, 80))
complete_monro.save('complete_monro.jpg')
