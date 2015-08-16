import random
import math
from PIL import Image, ImageMode


# constants
tex_width = 1024
tex_height = 1024
deg_to_rad = math.pi / 180

# load new image
img = Image.new ("RGB", (tex_width, tex_height), (0, 0, 0))
img_pixels = img.load ()

# for each pixels..
for x in range(img.size[0]):
	for y in range(img.size[1]):

		# Set tangent, bitangent, normal
		t = 5 + math.cos(y * 1.5 * deg_to_rad) + math.sin(x * deg_to_rad)
		b = 5 + math.sin(x * 1.5 * deg_to_rad) + math.cos(y * deg_to_rad)
		n = 10

		# get magnitude
		magnitude = math.sqrt(t * t + b * b + n * n)

		# normalize t, b, n
		t = int ((t / magnitude) * 256) + 1 / 2
		b = int ((b / magnitude) * 256) + 1 / 2
		n = int ((n / magnitude) * 256) + 1 / 2

		# set pixel
		img_pixels[x, y] = (t, b, n)

img.save ("TestNormal.png")

