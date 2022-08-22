import matplotlib.pyplot as plt
import cv2
import numpy as np


def main():
    '''	Load an RGB image.	'''
    img_path = "rose.jpg"
    rgb = plt.imread(img_path)

    '''	Convert the RGB image into grayscale image.	'''
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    height, width = grayscale.shape

    ''' Generate a binary mask. '''
    mask = np.zeros((height, width), dtype=np.uint8)
    for i in range(500, 1500):
        for j in range(800, 2000):
            mask[i, j] = 1

    ''' Apply a binary mask on a grayscale image. '''
    result = np.zeros((height, width), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            if mask[i, j] == 1:
                result[i, j] = grayscale[i, j]

    img_set = [grayscale, mask, result]
    title_set = ['Grayscale Image', 'Binary Mask', 'After Mask']
    plot_img(img_set, title_set)


def plot_img(img_set, title_set):
    n = len(img_set)
    plt.figure(figsize=(12, 12))

    for i in range(n):
        plt.subplot(1, 3, i + 1)
        plt.imshow(img_set[i], cmap='gray')
        plt.title(title_set[i])

    plt.savefig('Binary_mask.png')
    plt.show()


if __name__ == '__main__':
    main()
