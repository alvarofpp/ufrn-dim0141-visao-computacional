import cv2
from utils import Parse
from hough import Draw, Hough, Plot


parse = Parse()

# Image
shapes = cv2.imread(parse.filename)
# Plot.show(shapes, 'Original Image')

# Edges
shapes_grayscale = cv2.cvtColor(shapes, cv2.COLOR_RGB2GRAY)
shapes_blurred = cv2.GaussianBlur(shapes_grayscale, (5, 5), 1.5)
canny_edges = cv2.Canny(shapes_blurred, 100, 200)
# Plot.show(canny_edges, 'Canny Edges')

# Lines
accumulator, rhos, thetas = Hough.accumulator(canny_edges, **parse.get_valid_parameters())
#Plot.accumulator(accumulator)
lines = Hough.detector(accumulator, **parse.get_valid_parameters('detector'))
Draw.lines(shapes, lines, rhos, thetas)

# Show
Plot.show(shapes, 'Hough Transform')
