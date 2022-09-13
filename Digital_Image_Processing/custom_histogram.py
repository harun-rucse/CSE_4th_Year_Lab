import matplotlib.pyplot as plt
import numpy as np


def main():
    rgb = plt.imread('rose.jpg')
    grayscale = rgb_to_grayscale(rgb)

    plot_hist(grayscale)


def rgb_to_grayscale(rgb):
    red, green, blue = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]

    graysclae = red * 0.2989 + green * 0.5870 + blue * 0.1140
    graysclae = graysclae.astype(int)

    return graysclae


def custom_hist(img):
    img = img.reshape(-1)
    num_of_pixels = np.zeros((256,), dtype=int)

    for i in range(len(img)):
        num_of_pixels[img[i]] += 1

    return [num_of_pixels, range(256)]


def plot_hist(img):
    plt.figure(figsize=(15, 15))

    plt.subplot(1, 2, 1)
    plt.title('Built-in Histogram')
    plt.xlabel('Intensity')
    plt.ylabel('Number of Pixels')
    plt.hist(img.ravel(), 256, [0, 256])

    plt.subplot(1, 2, 2)
    plt.title('CUstom Histogram')
    plt.xlabel('Intensity')
    plt.ylabel('Number of Pixels')
    num_of_pixels, intensity = custom_hist(img)
    plt.bar(intensity, num_of_pixels, width=1.01)

    plt.show()


if __name__ == '__main__':
    main()
