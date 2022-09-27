import matplotlib.pyplot as plt
import numpy as np
import cv2


def main():
    rgb = plt.imread('erosion_dilation.jpg')

    grayscale = rgb_to_grayscale(rgb)
    binary = grayscale_to_binary(grayscale)

    structureElement = np.ones((3, 3), dtype=np.uint8)
    '''Built in Erosion'''
    erosion = cv2.erode(binary, structureElement, iterations=1)

    '''Custom Erosion'''
    custom_erosion = custom_erode(binary, structureElement)

    '''Built in Dilation'''
    dilation = cv2.dilate(binary, structureElement, iterations=1)

    '''Custom Dilation'''
    custom_dilation = custom_dilate(binary, structureElement)

    '''Built in Opening'''
    opening = cv2.dilate(erosion, structureElement, iterations=1)

    '''Custom Opening'''
    custom_opening = custom_dilate(custom_erosion, structureElement)

    '''Built in Closing'''
    closing = cv2.erode(dilation, structureElement, iterations=1)

    '''Custom Closing'''
    custom_closing = custom_erode(custom_dilation, structureElement)

    img_set = [binary, erosion,
               custom_erosion, dilation, custom_dilation, opening, custom_opening, closing, custom_closing]
    title_set = ['Binary',
                 'Built Erosion', 'Custom Erosion', 'Built Dilation', 'Custom Dilation', 'Built Opening', 'Custom Opening', 'Built Closing', 'Custom Closing']

    plot_img(img_set, title_set)


def count_one(kernel):
    row, col = kernel.shape
    cnt = 0

    for i in range(row):
        for j in range(col):
            if kernel[i, j] > 0:
                cnt += 1
    return cnt


def padding(img, kernel):
    row, col = img.shape
    k_r, k_c = kernel.shape

    new_row = row + k_r - 1
    new_col = col + k_c - 1

    zero_padding = np.zeros((new_row, new_col), dtype=np.uint8)
    r, c = int(k_r/2), int(k_c/2)

    zero_padding[r:r+row, c:c+col] = img

    return zero_padding


def custom_erode(img, kernel):
    row, col = img.shape
    k_r, k_c = kernel.shape

    zero_padding = padding(img, kernel)
    kernel_ones = count_one(kernel)

    result = np.zeros((row, col), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            mat = zero_padding[i:i+k_r, j:j+k_c]
            mat_ones = count_one(np.multiply(mat, kernel))

            if kernel_ones == mat_ones:
                result[i, j] = 1
    return result


def custom_dilate(img, kernel):
    row, col = img.shape
    k_r, k_c = kernel.shape

    zero_padding = padding(img, kernel)
    result = np.zeros((row, col), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            mat = zero_padding[i:i+k_r, j:j+k_c]
            mat_ones = count_one(np.multiply(mat, kernel))

            if mat_ones > 0:
                result[i, j] = 1

    return result


def plot_img(img_set, title_set):
    n = len(img_set)
    plt.figure(figsize=(15, 15))

    for i in range(n):
        plt.subplot(3, 3, i+1)
        plt.title(title_set[i])

        ch = len(img_set[i].shape)
        if ch == 3:
            plt.imshow(img_set[i])
        else:
            plt.imshow(img_set[i], cmap='gray')

    plt.show()


def rgb_to_grayscale(rgb):
    red, green, blue = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    grayscale = red * 0.2989 + green * 0.5087 + blue * 0.1140
    grayscale = grayscale.astype(int)

    return grayscale


def grayscale_to_binary(grayscale):
    row, col = grayscale.shape
    threshold = 127

    custom_binary = np.zeros((row, col), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            if grayscale[i, j] >= threshold:
                custom_binary[i, j] = 1

    return custom_binary


if __name__ == '__main__':
    main()
