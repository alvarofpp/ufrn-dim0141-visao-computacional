import sys
import cv2
import numpy as np


def median(image, dimension):
    matrix = tuple([[1 for j in range(dimension)] for i in range(dimension)])
    print("matrix", matrix)
    kernel = np.array(matrix, np.float32)
    # grab the image dimensions
    height = image.shape[0]
    width = image.shape[1]

    for row in range(height):
        for col in range(width):
            image[row, col] = 255 if image[row, col] >= 100 else 0

    return image


def main(args):
    if len(args) != 1:
        print("A quantidade de argumentos é inválido.")
        exit(1)

    # Imagem original
    filename = args[0]
    img = cv2.imread(filename)

    img = img[::2, ::2]  # Diminui a imagem
    print(img.shape, type(img))

    cv2.imwrite('test.jpg', median(img, 3))


if __name__ == "__main__":
    main(sys.argv[1:])
