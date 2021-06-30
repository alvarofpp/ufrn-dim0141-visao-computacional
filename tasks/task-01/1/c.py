import sys
import cv2


def main(args):
    if len(args) != 2:
        print("A quantidade de argumentos é inválido. "
              + "Por favor, digite os dois argumentos necessários (os dois são caminhos para imagens)")
        exit(1)

    # Imagens originais
    img_a = cv2.imread(args[0])
    img_b = cv2.imread(args[1])

    if img_a.shape[0] != img_b.shape[0] or img_a.shape[1] != img_b.shape[1]:
        print("As duas imagens possuem tamanhos diferentes")
        exit(1)

    # Blend
    img_blending = cv2.addWeighted(img_a, 0.5, img_b, 0.5, 0.0)

    # Show
    cv2.imshow('img-blending', img_blending)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main(sys.argv[1:])
