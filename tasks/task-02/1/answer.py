import sys
import cv2
import numpy as np


def main(args):
    if len(args) != 5:
        print("A quantidade de argumentos é inválido.")
        exit(1)

    # Imagem original
    filename = args[0]
    img = cv2.imread(filename)

    # Increase the brightness
    increase_brightness_img = cv2.add(img, np.array([float(args[1])]))

    # Draw lines
    width_between_lines = int(args[2])
    line_thickness = int(args[3])
    line_color = (0, 0, 0)
    for i in range(0, increase_brightness_img.shape[0], width_between_lines+line_thickness):
        pt1 = (i, 0)
        pt2 = (i, increase_brightness_img.shape[0] - 1)
        cv2.line(increase_brightness_img, pt1, pt2, line_color, thickness=line_thickness)

    # Result
    cv2.imwrite(args[4], increase_brightness_img)


if __name__ == "__main__":
    main(sys.argv[1:])
