import matplotlib.pyplot as plt
import cv2
import numpy as np


def main():
    rgb = plt.imread('rose.jpg')

    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    grayscale = r * 0.2989 + g * 0.5870 + b * 0.1140
    # grayscale = grayscale.astype(int)
    # grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    grayscale = cv2.resize(grayscale, (800, 800))

    lap_kernel = np.array([
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]
    ])

    sobel_kernel = np.array([
        [1, 0, -1],
        [2, 0, -1],
        [1, 0, -1]
    ])

    gasuuian_kernel = np.array([
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ])

    lap_effect = cv2.filter2D(grayscale, -1, lap_kernel)
    sobel_effect = cv2.filter2D(grayscale, -1, sobel_kernel)
    gasuuian_effect = cv2.filter2D(grayscale, -1, gasuuian_kernel)

    cus_lap_effect = filter2D(grayscale, lap_kernel)
    cus_sobel_effect = filter2D(grayscale, sobel_kernel)
    cus_gasuuian_effect = filter2D(grayscale, gasuuian_kernel)

    img_set = [rgb, grayscale, lap_effect, cus_lap_effect,
               sobel_effect, cus_sobel_effect, gasuuian_effect, cus_gasuuian_effect]
    title_set = ['RGB', 'Grayscale',
                 'Laplacian', 'Custom Laplacian', 'Sobel', 'Custom Sobel', 'Gasuuian', 'Custom Gasuuian']

    plot_img(img_set, title_set)


def filter2D(img, kernel):
    row, col = img.shape
    k_r, k_c = kernel.shape

    new_row = row + k_r - 1
    new_col = col + k_c - 1

    zero_padding = np.zeros((new_row, new_col), dtype=np.uint8)

    r, c = int(k_r/2), int(k_c/2)
    zero_padding[r:r+row, c:c+col] = img

    conv_img = np.zeros((row, col), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            mat = zero_padding[i:i+k_r, j:j+k_c]

            '''Multipy & Summation'''
            summation = 0
            for m in range(mat.shape[0]):
                for n in range(mat.shape[1]):
                    summation = summation + mat[m, n] * kernel[m, n]

            if summation < 0:
                conv_img[i, j] = 0
            elif summation > 255:
                conv_img[i, j] = 255
            else:
                conv_img[i, j] = summation
    return conv_img


def plot_img(img_set, title_set):
    n = len(img_set)
    plt.figure(figsize=(15, 15))

    for i in range(n):
        plt.subplot(3, 4, i+1)
        plt.title(title_set[i])

        ch = len(img_set[i].shape)
        if ch == 3:
            plt.imshow(img_set[i])
        else:
            plt.imshow(img_set[i], cmap='gray')

    plt.show()


if __name__ == '__main__':
    main()
