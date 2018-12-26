
# typedString = input()

# print(typedString)



from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("MARBLES.BMP")
pixels = img.load() # Create the pixel map

font = ImageFont.truetype("arial.ttf", 15)

ImageDraw.Draw(img).text(
    (100, 100),  # Coordinates
    'Hello world!',  # Text
    (0, 0, 0),  # Color
      font=font
)

img.show()