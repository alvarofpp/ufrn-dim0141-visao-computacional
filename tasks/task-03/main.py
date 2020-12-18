import cv2
from Hough import Draw, Hough, Plot

# Image
shapes = cv2.imread('images/test_01.png')
# Plot.show(shapes, 'Original Image')

# Edges
shapes_grayscale = cv2.cvtColor(shapes, cv2.COLOR_RGB2GRAY)
shapes_blurred = cv2.GaussianBlur(shapes_grayscale, (5, 5), 1.5)
canny_edges = cv2.Canny(shapes_blurred, 100, 200)
# Plot.show(canny_edges, 'Canny Edges')

# run hough_ on the shapes canny_edges image
accumulator, rhos, thetas = Hough.lines_accumulator(canny_edges)
indicies, accumulator = Hough.find_peaks(accumulator, 5, nhood_size=11)
# Plot.accumulator(accumulator)
Draw.lines(shapes, indicies, rhos, thetas)

# Show image with manual Hough Transform Lines
Plot.show(shapes, 'Major Lines: Manual Hough Transform')
