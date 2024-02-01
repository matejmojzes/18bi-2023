from PIL import Image

try:
    img = Image.open('/Users/stepan/Desktop/BI/github/IMG_2488.png')
    img.show()
except IOError:
    print("Error: Cannot open the image.")