import cv2
import numpy as np


class Draw:

    # drawing the lines from the Hough Accumulatorlines using OpevCV cv2.line
    @staticmethod
    def lines(img, indicies, rhos, thetas):
        for i in range(len(indicies)):
            # print("indicies", indicies[i])
            rho = rhos[indicies[i][0]]
            theta = thetas[indicies[i][1]]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            # print(rho, theta)
            # print(a, b)
            # print(x0, y0)
            # these are then scaled so that the lines go off the edges of the image
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))

            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
