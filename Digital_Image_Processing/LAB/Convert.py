from PIL import Image

img = Image.open('dahlia.jpg')
print(img.format)
img.save('output.png')


img = Image.open('noisy.png')
print(img.format)
img.save('output.jpg')
