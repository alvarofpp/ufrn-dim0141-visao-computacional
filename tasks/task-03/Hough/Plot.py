import cv2
import matplotlib.pyplot as plt


class Plot:
    @staticmethod
    def accumulator(image, plot_title='Hough Accumulator Plot'):
        fig = plt.figure(figsize=(10, 10))
        fig.canvas.set_window_title(plot_title)

        plt.imshow(image, cmap='jet')
        plt.xlabel('Theta Direction'), plt.ylabel('Rho Direction')
        plt.tight_layout()
        plt.show()

    @staticmethod
    def show(image, plot_title='Image'):
        cv2.imshow(plot_title, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
