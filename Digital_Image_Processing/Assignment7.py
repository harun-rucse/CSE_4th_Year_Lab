import matplotlib.pyplot as plt
import numpy as np
import cv2


def main():
    ''' Load a RGB image '''
    rgb = cv2.imread('flower.jpeg')

    ''' Convert RGB to Grayscale '''
    grayscale = rgb_to_grayscale(rgb)

    temp = (grayscale - 50) % 200

    left = temp
    right = temp + 50
    middle = (temp % 150)+50

    img_set = [grayscale, left, right, middle]
    title_set = ['Grayscale', 'Left', 'Right', 'Middle']

    plot_img(img_set, title_set)


def plot_img(img_set, title_set):
    n = len(img_set)
    plt.figure(figsize=(20, 20))
    plot_number = 1

    for i in range(n):
        plt.subplot(4, 2, plot_number)
        plt.title(title_set[i])
        plt.imshow(img_set[i], cmap='gray')

        plt.subplot(4, 2, plot_number+1)
        plt.title(title_set[i] + ' Histogram')
        hist = cv2.calcHist([img_set[i]], [0], None, [256], [0, 256])
        plt.plot(hist, color='blue')

        plot_number += 2

    plt.show()


def rgb_to_grayscale(rgb):
    red, green, blue = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]

    graysclae = red * 0.2989 + green * 0.5870 + blue * 0.1140
    graysclae = graysclae.astype('uint8')

    return graysclae


if __name__ == '__main__':
    main()
