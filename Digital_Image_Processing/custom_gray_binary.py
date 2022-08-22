import matplotlib.pyplot as plt
import cv2
import numpy as np


def main():
    rgb = plt.imread('rose.jpg')

    ''' RGB to Grayscale '''
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)

    ''' Grayscale to Binary '''
    _, binary = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)

    ''' Extract red, green and blue channel form RGB '''
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]

    ''' RGB to Custom Grayscale '''
    custom_grayscale = r * 0.2989 + g * 0.5870 + b * 0.1140
    custom_grayscale = custom_grayscale.astype(int)

    ''' Grayscale to Custom Binary '''
    row, col = custom_grayscale.shape
    custom_binary = np.zeros((row, col), dtype=np.uint8)

    threshold = 127
    for i in range(row):
        for j in range(col):
            if custom_grayscale[i, j] >= threshold:
                custom_binary[i, j] = 255
            else:
                custom_binary[i, j] = 0

    img_set = [rgb, grayscale, custom_grayscale, binary, custom_binary]
    title_set = ['RGB', 'Built-in grayscale',
                 'Custom grayscale', 'Built-in Binary', 'Custom Binary']
    plot_img(img_set, title_set)


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
