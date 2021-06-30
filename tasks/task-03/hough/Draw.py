import cv2
import numpy as np


class Draw:

    @staticmethod
    def lines(image, lines, rhos, thetas):
        edge_height, edge_width = image.shape[:2]
        edge_height_half, edge_width_half = edge_height / 2, edge_width / 2

        for line in lines:
            y, x = line
            rho = rhos[y]
            theta = thetas[x]
            a = np.cos(np.deg2rad(theta))
            b = np.sin(np.deg2rad(theta))
            x0 = (a * rho) + edge_width_half
            y0 = (b * rho) + edge_height_half
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
