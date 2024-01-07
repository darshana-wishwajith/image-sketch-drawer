from sketchpy import canvas

def image_drawing(image, scale) :
    pencil = canvas.sketch_from_svg(image, scale)
    pencil.draw()

image = input("Image :")
scale = int(input("Scale :"))

image_drawing(image, scale)