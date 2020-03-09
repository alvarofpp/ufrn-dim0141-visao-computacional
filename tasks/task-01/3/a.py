import cv2


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


# Imagem original
filename = 'imagem.jpg'
img = cv2.imread(filename)

# RGB - Red
cv2.imshow('R-RGB', OnlyChannel.to_red(img))
# RGB - Blue
cv2.imshow('B-RGB', OnlyChannel.to_blue(img))
# RGB - Green
cv2.imshow('G-RGB', OnlyChannel.to_green(img))

cv2.waitKey(0)
cv2.destroyAllWindows()
