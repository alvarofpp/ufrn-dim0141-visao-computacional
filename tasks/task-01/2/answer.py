import sys
import cv2


def main(args):
    if len(args) < 1:
        print("A quantidade de argumentos é inválido.")
        exit(1)

    # Imagens
    images = [cv2.imread(filename) for filename in args]
    result = cv2.fastNlMeansDenoisingMulti(images, 2, 5)

    # Flip horizontal
    cv2.imshow('Denoising', result)

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main(sys.argv[1:])
