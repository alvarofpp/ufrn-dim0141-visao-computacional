import sys
import cv2
import numpy as np


class OnlyChannel:
    """Classe responsável por realizar a seleção dos canais de cores da imagem."""
    CHANNEL_RED = 2  # Valor do canal de cor vermelho
    CHANNEL_GREEN = 1  # Valor do canal de cor verde
    CHANNEL_BLUE = 0  # Valor do canal de cor azul

    @staticmethod
    def to_red(img):
        """Seta como zero os canais azul e verde, restando apenas o canal vermelho da imagem."""
        img_red = img.copy()
        img_red[:, :, OnlyChannel.CHANNEL_BLUE] = 0
        img_red[:, :, OnlyChannel.CHANNEL_GREEN] = 0

        return img_red

    @staticmethod
    def to_green(img):
        """Seta como zero os canais azul e vermelho, restando apenas o canal verde da imagem."""
        img_green = img.copy()
        img_green[:, :, OnlyChannel.CHANNEL_BLUE] = 0
        img_green[:, :, OnlyChannel.CHANNEL_RED] = 0

        return img_green

    @staticmethod
    def to_blue(img):
        """Seta como zero os canais verde e vermelho, restando apenas o canal azul da imagem."""
        img_blue = img.copy()
        img_blue[:, :, OnlyChannel.CHANNEL_GREEN] = 0
        img_blue[:, :, OnlyChannel.CHANNEL_RED] = 0

        return img_blue


def main(args):
    if len(args) != 1:
        print("A quantidade de argumentos é inválido. "
              + "Por favor, digite um único argumento (caminho da imagem de entrada)")
        exit(1)

    # Imagem original
    filename = args[0]
    img = cv2.imread(filename)

    images = (
        OnlyChannel.to_red(img),
        OnlyChannel.to_green(img),
        OnlyChannel.to_blue(img)
    )
    cv2.imshow('RGB', np.concatenate(images, axis=1))
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main(sys.argv[1:])
