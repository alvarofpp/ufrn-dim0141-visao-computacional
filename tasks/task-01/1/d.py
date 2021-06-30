import sys
import cv2
import numpy as np


def main(args):
    if len(args) != 2:
        print("A quantidade de argumentos é inválido. "
              + "Por favor, digite os dois argumentos necessários (altura e largura)")
        exit(1)

    # Gradient
    height = int(args[0])
    width = int(args[1])
    image = np.zeros((height, width, 1), dtype=np.float)
    image[:, :, 0] = np.tile(np.linspace(0, 255, height), (width, 1)).T

    # Show
    cv2.imshow('img-gradient', np.uint8(image))
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main(sys.argv[1:])
