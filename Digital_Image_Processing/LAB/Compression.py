import matplotlib.pyplot as plt
import numpy as np


def main():
    rgb = plt.imread('rose.jpg')
    grayscale = rgb_to_grayscale(rgb)

    img_set = [grayscale]
    title_set = ['Grayscale']

    fft_img = np.fft.fft2(grayscale)
    fft_img_sort = np.sort(np.abs(fft_img.ravel()))

    n = len(fft_img_sort)

    for keep in (0.75, 0.50, 0.1, 0.05, 0.01, 0.001, 0.0001):
        thresh = fft_img_sort[int(np.floor(n * (1-keep)))]
        ind = np.abs(fft_img) > thresh
        allow_pass = fft_img * ind
        ifft_img = np.fft.ifft2(allow_pass).real

        img_set.append(ifft_img)
        title_set.append("Compressed (keep= {}%)".format(keep*100))

    plot_img(img_set, title_set)


def rgb_to_grayscale(rgb):
    red, green, blue = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]

    graysclae = red * 0.2989 + green * 0.5870 + blue * 0.1140
    graysclae = graysclae.astype(int)

    return graysclae


def plot_img(img_set, title_set):
    n = len(img_set)
    plt.figure(figsize=(15, 15))

    for i in range(n):
        plt.subplot(2, 4, i+1)
        plt.title(title_set[i])

        ch = len(img_set[i].shape)
        if ch == 3:
            plt.imshow(img_set[i])
        else:
            plt.imshow(img_set[i], cmap='gray')

    plt.show()


if __name__ == '__main__':
    main()
