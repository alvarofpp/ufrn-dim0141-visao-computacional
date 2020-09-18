import sys
import cv2
import numpy as np


def increase_brightness(img, value):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #hsv[:, :, 2] += value

    for x in range(0, len(hsv)):
        for y in range(0, len(hsv[0])):
            new_color = hsv[x, y][2] + value
            hsv[x, y][2] = 255 if new_color > 255 else new_color

    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

def main(args):
    if len(args) != 5 and False:
        print("A quantidade de argumentos é inválido.")
        exit(1)

    # Imagem original
    filename = args[0]
    img = cv2.imread(filename)
    new_img = cv2.add(img, np.array([500.0]))

    #cv2.imshow('RGB', np.concatenate((img, increase_brightness(img, 5000)), axis=1))
    cv2.imshow('RGB', np.concatenate((increase_brightness(img, 50), new_img), axis=1))
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main(sys.argv[1:])
