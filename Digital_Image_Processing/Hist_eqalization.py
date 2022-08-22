import matplotlib.pyplot as plt
import cv2
import numpy as np
import math


def main():
    rgb = cv2.imread('image.jpg')

    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]

    grayscale = r * 0.2989 + g * 0.5870 + b * 0.1140
    # grayscale = cv2.resize(grayscale, (300, 300))
    grayscale = grayscale.astype(int)

    result = hist_equal(grayscale)

    plt.figure(figsize=(15, 15))
    plt.subplot(1, 2, 1)
    plt.title('Old')
    plt.imshow(rgb, cmap='gray')

    plt.subplot(1, 2, 2)
    plt.title('Equalize')
    plt.imshow(result, cmap='gray')

    plt.show()


def hist_equal(img):
    row, col = img.shape
    num_of_pixels = []
    pdf = []
    cdf = []
    multi = []
    equalization = []

    for val in range(256):
        cnt = 0
        for i in range(row):
            for j in range(col):
                if img[i, j] == val:
                    cnt = cnt + 1
        num_of_pixels.append(cnt)

    for i in range(256):
        pdf.append(num_of_pixels[i]/np.sum(num_of_pixels))

    for i in range(256):
        if i == 0:
            cdf.append(pdf[i])
        else:
            cdf.append(cdf[i-1] + pdf[i])

    for i in range(256):
        multi.append(cdf[i] * 255)

    for i in range(256):
        equalization.append(math.ceil(multi[i]))

    equalize_img = np.zeros((row, col), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            equalize_img[i, j] = equalization[img[i, j]]

    return equalize_img


if __name__ == '__main__':
    main()
