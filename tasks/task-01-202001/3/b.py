import cv2


class Flip:
    """Classe responsável por realizar o processo de flip na imagem."""
    FLIP_VERTICAL = 0  # Valor do canal de cor vermelho
    FLIP_HORIZONTAL = 1  # Valor do canal de cor verde
    FLIP_BOTH = -1  # Valor do canal de cor azul

    @staticmethod
    def flip(img, flip_code = FLIP_BOTH):
        """Realiza o processo de flip na imagem."""
        return cv2.flip(img, flip_code)


# Imagem original
filename = 'imagem.jpg'
img = cv2.imread(filename)

# Flip horizontal
cv2.imshow('Flip-Horizontal', Flip.flip(img, Flip.FLIP_HORIZONTAL))

cv2.waitKey(0)
cv2.destroyAllWindows()
