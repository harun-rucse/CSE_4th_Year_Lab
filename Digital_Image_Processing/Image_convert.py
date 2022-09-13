from PIL import Image

'''Convert JPEG to PNG'''
img = Image.open("input.jpeg")
img.save("output.png")

'''Convert PNG to JPEG'''
img = Image.open("input.png")
img.save("output.jpeg")
