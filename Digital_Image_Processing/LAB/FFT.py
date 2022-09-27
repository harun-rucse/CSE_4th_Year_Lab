import matplotlib.pyplot as plt
import numpy as np
import cv2


def main():
    rgb = plt.imread('dahlia.jpg')
    grayscale = rgb_to_grayscale(rgb)

    ft_img = np.fft.fft2(grayscale)
    centered_ft_img = np.fft.fftshift(ft_img)

    magnitude_spectrum = np.log(np.abs(ft_img))
    centered_magnitude_spectrum = np.log(np.abs(centered_ft_img))

    row, col = grayscale.shape
    m, n = row//2, col//2

    black_img = np.zeros((row, col), dtype=np.uint8)
    filter = cv2.circle(black_img, (m, n), 25, (255, 255, 255), -1)

    filter_ft_img = centered_ft_img * filter
    filtered_img = np.abs(np.fft.ifft2(filter_ft_img))

    img_set = [rgb, grayscale, magnitude_spectrum,
               centered_magnitude_spectrum, filter, filtered_img]
    title_set = ['RGB', 'Grayscale', 'FFT',
                 'Centered FFT', 'Filter', 'Filtered Image']

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
