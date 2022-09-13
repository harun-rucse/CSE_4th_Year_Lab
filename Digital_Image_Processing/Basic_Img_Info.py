import matplotlib.pyplot as plt
import numpy as np


def main():
    rgb = plt.imread('rose.jpg')

    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    grayscale = r * 0.2989 + g * 0.5870 + b * 0.1140

    row, col = grayscale.shape
    binary = np.zeros((row, col), dtype=np.uint8)

    threshold = 127
    for i in range(row):
        for j in range(col):
            if grayscale[i, j] >= threshold:
                binary[i, j] = 255

    img_set = [rgb, r, g, b, grayscale, binary]
    title_set = ['RGB', 'Red', 'Green', 'Blue', 'Grayscale', 'Binary']
    cmap_set = ['', 'Reds', 'Greens', 'Blues', 'gray', 'binary']

    plot_img(img_set, title_set, cmap_set)


def plot_img(img_set, title_set, cmap_set):
    n = len(img_set)
    plt.figure(figsize=(15, 15))

    for i in range(n):
        plt.subplot(2, 3, i+1)
        plt.title(title_set[i])

        ch = len(img_set[i].shape)
        if ch == 3:
            plt.imshow(img_set[i])
        else:
            plt.imshow(img_set[i], cmap=cmap_set[i])

    plt.show()


if __name__ == '__main__':
    main()
