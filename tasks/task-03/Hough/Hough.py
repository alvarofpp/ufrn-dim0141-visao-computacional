import numpy as np


class Hough:

    @staticmethod
    def lines_accumulator(img, rho_resolution=1, theta_resolution=1):
        ''' A function for creating a Hough Accumulator for lines in an image. '''
        height, width = img.shape  # we need heigth and width to calculate the diag
        img_diagonal = np.ceil(np.sqrt(height ** 2 + width ** 2))  # a**2 + b**2 = c**2
        rhos = np.arange(-img_diagonal, img_diagonal + 1, rho_resolution)
        thetas = np.deg2rad(np.arange(-90, 90, theta_resolution))

        # create the empty Hough Accumulator with dimensions equal to the size of
        # rhos and thetas
        accumulator = np.zeros((len(rhos), len(thetas)), dtype=np.uint64)
        y_idxs, x_idxs = np.nonzero(img)  # find all edge (nonzero) pixel indexes

        for i in range(len(x_idxs)):  # cycle through edge points
            x = x_idxs[i]
            y = y_idxs[i]

            for j in range(len(thetas)):  # cycle through thetas and calc rho
                rho = int((x * np.cos(thetas[j]) +
                           y * np.sin(thetas[j])) + img_diagonal)
                accumulator[rho, j] += 1

        return accumulator, rhos, thetas

    @staticmethod
    def find_peaks(accumulator, num_peaks, threshold=0, nhood_size=3):
        indicies = []
        accumulator_copy = np.copy(accumulator)
        for i in range(num_peaks):
            idx = np.argmax(accumulator_copy)  # find argmax in flattened array
            accumulator_copy_idx = np.unravel_index(idx, accumulator_copy.shape)  # remap to shape of H
            indicies.append(accumulator_copy_idx)

            # surpess indicies in neighborhood
            idx_y, idx_x = accumulator_copy_idx  # first separate x, y indexes from argmax(H)
            # if idx_x is too close to the edges choose appropriate values
            if (idx_x - (nhood_size / 2)) < 0:
                min_x = 0
            else:
                min_x = idx_x - (nhood_size / 2)
            if ((idx_x + (nhood_size / 2) + 1) > accumulator.shape[1]):
                max_x = accumulator.shape[1]
            else:
                max_x = idx_x + (nhood_size / 2) + 1

            # if idx_y is too close to the edges choose appropriate values
            if (idx_y - (nhood_size / 2)) < 0:
                min_y = 0
            else:
                min_y = idx_y - (nhood_size / 2)
            if ((idx_y + (nhood_size / 2) + 1) > accumulator.shape[0]):
                max_y = accumulator.shape[0]
            else:
                max_y = idx_y + (nhood_size / 2) + 1

            # bound each index by the neighborhood size and set all values to 0
            for x in range(int(min_x), int(max_x)):
                for y in range(int(min_y), int(max_y)):
                    # remove neighborhoods in accumulator_copy
                    accumulator_copy[y, x] = 0

                    # highlight peaks in original H
                    if (x == int(min_x) or x == (int(max_x) - 1)):
                        accumulator[y, x] = 255
                    if (y == int(min_y) or y == (int(max_y) - 1)):
                        accumulator[y, x] = 255

        # return the indicies and the original Hough space with selected points
        return indicies, accumulator
