import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
	rgb = plt.imread('flower.jpg')
	
	grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
	_, binary = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)
	
	row, col = grayscale.shape
	
	mask = np.zeros((row, col), dtype=np.uint8)
	
	for i in range(100, 400):
		for j in range(200, 400):
			mask[i,j] = 255
 	
	result = np.zeros((row, col), dtype=np.uint8)
	
	for i in range(row):
		for j in range(col):
			if mask[i,j] == 255:
				result[i,j] = grayscale[i,j]
		
	'''Bit slicing'''
	slice_img1 = np.zeros((row,col), dtype=np.uint8)
	slice_img2 = np.zeros((row,col), dtype=np.uint8)
	slice_img3 = np.zeros((row,col), dtype=np.uint8)
	slice_img4 = np.zeros((row,col), dtype=np.uint8)
	slice_img5 = np.zeros((row,col), dtype=np.uint8)
	slice_img6 = np.zeros((row,col), dtype=np.uint8)
	slice_img7 = np.zeros((row,col), dtype=np.uint8)
	slice_img8 = np.zeros((row,col), dtype=np.uint8)
	
	slice_imgs = [slice_img1, slice_img2, slice_img3, slice_img4, slice_img5, slice_img6, slice_img7, slice_img8]
	bit_operators = [1,2,4,8,16,32,64,128]
	
	for i in range(8):
		for j in range(row):
			for k in range(col):
				slice_imgs[i][j][k] = grayscale[j,k] & bit_operators[i]
	
			
	img_set = [rgb, grayscale, mask, result]
	img_set = img_set + slice_imgs
	title_set = ['RGB', 'Grayscale', 'Mask', 'Result']
	title_set = title_set + ['Slice1', 'Slice2', 'Slice3', 'Slice4', 'Slice5', 'Slice6', 'Slice7', 'Slice8']
	
	plot_img(img_set, title_set)

def plot_img(img_set, title_set):
	n = len(img_set)
	plt.figure(figsize=(15,15))
	
	for i in range(n):
		plt.subplot(3,4,i+1)
		plt.title(title_set[i])
		ch = len(img_set[i].shape)
		
		if ch == 3:
			plt.imshow(img_set[i])
		else:
			plt.imshow(img_set[i], cmap='gray')
	plt.show()

if __name__ == '__main__':
	main()
