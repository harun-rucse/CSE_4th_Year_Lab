import matplotlib.pyplot as plt
import cv2
import numpy as np
import random


def main():
    grayscale = cv2.imread('noisy.png', 0)
    grayscale2 = cv2.imread('noisy.png', 0)

    noisy_img = add_noise(grayscale2)

    '''Custom Median filter'''
    row, col = grayscale.shape
    kernel_size = 3

    result = np.zeros((row, col), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            result[i, j] = np.median(
                noisy_img[i:i+kernel_size, j:j+kernel_size])

    img_set = [grayscale, noisy_img, result]
    title_set = ['Grayscale', 'Noisy Image', 'Remove noise']

    plot_img(img_set, title_set)


def add_noise(img):
    row, col = img.shape
    number_of_pixels = random.randint(700, 10000)

    for i in range(number_of_pixels):
        x_coord = random.randint(0, row-1)
        y_coord = random.randint(0, col-1)

        img[x_coord, y_coord] = 255

    number_of_pixels = random.randint(700, 10000)

    for i in range(number_of_pixels):
        x_coord = random.randint(0, row-1)
        y_coord = random.randint(0, col-1)

        img[x_coord, y_coord] = 0

    return img


def plot_img(img_set, title_set):
    n = len(img_set)
    plt.figure(figsize=(20, 20))

    for i in range(n):
        plt.subplot(2, 3, i+1)
        plt.title(title_set[i])

        ch = len(img_set[i].shape)
        if ch == 3:
            plt.imshow(img_set[i])
        else:
            plt.imshow(img_set[i], cmap='gray')

    plt.show()


if __name__ == '__main__':
    main()
