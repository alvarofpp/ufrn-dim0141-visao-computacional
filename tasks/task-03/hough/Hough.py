import numpy as np


class Hough:

    @staticmethod
    def accumulator(edge_image, rho=180, theta=180):
        edge_height, edge_width = edge_image.shape[:2]
        edge_height_half, edge_width_half = edge_height / 2, edge_width / 2

        d = np.sqrt(np.square(edge_height) + np.square(edge_width))
        dtheta = 180 / theta
        drho = (2 * d) / rho

        thetas = np.arange(0, 180, step=dtheta)
        rhos = np.arange(-d, d, step=drho)

        cos_thetas = np.cos(np.deg2rad(thetas))
        sin_thetas = np.sin(np.deg2rad(thetas))

        edge_points = np.argwhere(edge_image != 0)
        edge_points = edge_points - np.array([[edge_height_half, edge_width_half]])

        rho_values = np.matmul(edge_points, np.array([sin_thetas, cos_thetas]))

        accumulator, theta_vals, rho_vals = np.histogram2d(
            np.tile(thetas, rho_values.shape[0]),
            rho_values.ravel(),
            bins=[thetas, rhos]
        )
        accumulator = np.transpose(accumulator)

        return accumulator, rhos, thetas

    @staticmethod
    def detector(accumulator, threshold=220, take=None):
        lines = np.argwhere(accumulator > threshold)

        if take is not None:
            lines = lines[0:take]

        return lines
