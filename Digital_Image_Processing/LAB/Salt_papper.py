import matplotlib.pyplot as plt
import random
import numpy as np


def main():
    rgb = plt.imread('flower.jpg')

    grayscale = rgb_to_gray(rgb)
    noisy_img = add_noise(grayscale)

    result = median_filter(noisy_img)

    img_set = [rgb, grayscale, noisy_img, result]
    title_set = ['RGB', 'Grayscale', 'Noisy Image', 'Remove Noise']

    plot_img(img_set, title_set)


def median_filter(img):
    row, col = img.shape
    kernel_size = 3

    result = np.zeros((row, col), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            mat = img[i:i+kernel_size, j:j+kernel_size]
            result[i, j] = np.median(mat)

    return result


def add_noise(grayscale):
    img = grayscale.copy()
    row, col = grayscale.shape

    '''Add salt noise'''
    num_of_pixels = random.randint(1000, 5000)
    for i in range(num_of_pixels):
        x_coord = random.randint(0, row-1)
        y_coord = random.randint(0, col-1)

        img[x_coord, y_coord] = 255

    '''Add paper noise'''
    num_of_pixels = random.randint(1000, 5000)
    for i in range(num_of_pixels):
        x_coord = random.randint(0, row-1)
        y_coord = random.randint(0, col-1)

        img[x_coord, y_coord] = 0

    return img


def plot_img(img_set, title_set):
    n = len(img_set)
    plt.figure(figsize=(15, 15))

    for i in range(n):
        plt.subplot(2, 3, i+1)
        plt.title(title_set[i])

        ch = len(img_set[i].shape)
        if ch == 3:
            plt.imshow(img_set[i])
        else:
            plt.imshow(img_set[i], cmap='gray')

    plt.show()


def rgb_to_gray(rgb):
    red, green, blue = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    grayscale = red * 0.2989 + green * 0.5087 + blue * 0.1140
    grayscale = grayscale.astype(int)

    return grayscale


if __name__ == '__main__':
    main()
