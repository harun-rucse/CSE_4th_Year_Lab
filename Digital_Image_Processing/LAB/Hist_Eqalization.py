import matplotlib.pyplot as plt
import numpy as np
import cv2
import math


def main():
    rgb = cv2.imread('lena.jpg')
    print(rgb.shape)
    grayscale = rgb_to_grayscale(rgb)

    result = hist_equal(grayscale)

    img_set = [grayscale, result]
    title_set = ['Original Image', 'Eqalize Image']

    plot_img(img_set, title_set)


def hist_equal(img):
    row, col = img.shape
    img_1d = img.reshape(-1)
    num_of_pixels = np.zeros((256,), dtype=int)

    for i in range(len(img_1d)):
        num_of_pixels[img_1d[i]] += 1

    equalization = []

    for i in range(256):
        pdf = num_of_pixels[i]/np.sum(num_of_pixels)

        if i == 0:
            cdf = pdf
        else:
            cdf = cdf + pdf

        equalization.append(math.ceil(cdf * 256))

    result = np.zeros((row, col), dtype=np.uint8)
    for i in range(row):
        for j in range(col):
            result[i, j] = equalization[img[i, j]]

    return result


def rgb_to_grayscale(rgb):
    red, green, blue = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]

    graysclae = red * 0.2989 + green * 0.5870 + blue * 0.1140
    graysclae = graysclae.astype(int)

    return graysclae


def plot_img(img_set, title_set):
    n = len(img_set)
    plt.figure(figsize=(15, 15))
    plot_number = 1

    for i in range(n):
        plt.subplot(2, 2, plot_number)
        plt.title(title_set[i])
        plt.imshow(img_set[i], cmap='gray')

        plt.subplot(2, 2, plot_number+1)
        plt.title(title_set[i] + ' Histogram')
        plt.hist(img_set[i].ravel(), 256, [0, 256])
        plt.xlabel('Intensity')
        plt.ylabel('Number of pixels')

        plot_number += 2

    plt.show()


if __name__ == '__main__':
    main()
