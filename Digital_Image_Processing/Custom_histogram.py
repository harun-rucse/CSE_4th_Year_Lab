import matplotlib.pyplot as plt
import cv2


def main():
    rgb = plt.imread('rose.jpg')

    ''' RGB to Grayscale '''
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    resize_img = cv2.resize(grayscale, (200, 200))

    plt.figure(figsize=(15, 15))

    ''' Built-in Histogram '''
    plt.subplot(1, 2, 1)
    plt.hist(resize_img.ravel(), 256, [0, 256])
    plt.title('Built-in Histogram')
    plt.xlabel('Intensity')
    plt.ylabel('Number of Pixels')

    ''' Custom Histogram '''
    row, col = resize_img.shape
    intensity = range(256)
    num_of_pixels = []

    for val in range(256):
        cnt = 0

        for i in range(row):
            for j in range(col):
                if resize_img[i, j] == val:
                    cnt = cnt + 1
        num_of_pixels.append(cnt)

    plt.subplot(1, 2, 2)
    plt.title('Custom Histogram')
    plt.xlabel('Intensity')
    plt.ylabel('Number of Pixels')
    plt.stem(intensity, num_of_pixels, markerfmt='')

    plt.show()


if __name__ == '__main__':
    main()
