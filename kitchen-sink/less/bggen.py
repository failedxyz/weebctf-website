from PIL import Image

im = Image.new("RGB", (40, 40), "white")

for x in range(40):
	for y in range(40):
		if (x + y) % 10 in [9, 0, 1]:
			im.putpixel((x, y), (255, 214, 203))
		else:
			im.putpixel((x, y), (255, 229, 183))

im.save("bg.jpg", "JPEG")