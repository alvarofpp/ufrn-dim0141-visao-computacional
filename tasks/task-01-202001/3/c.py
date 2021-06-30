import cv2


# Imagens originais
img_a = cv2.imread('resized/php_logo.png')
img_b = cv2.imread('resized/python_logo.png')

# Blend
img_blending = cv2.addWeighted(img_a, 0.5, img_b, 0.5, 0.0)

# Show
cv2.imshow('img-blending', img_blending)
cv2.waitKey(0)
cv2.destroyAllWindows()
