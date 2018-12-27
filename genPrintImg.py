from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# img = Image.open("MARBLES.BMP")
# pixels = img.load() # Create the pixel map

# font = ImageFont.truetype("arial.ttf", 15)

# ImageDraw.Draw(img).text(
#     (500, 100),  # Coordinates
#     'Hello world!',  # Text
#     (0, 0, 0),  # Color
#       font=font
# )

# img.show()

class ImageGen():

    def blank(self):
        self.img = Image.new( 'RGB', (400,250), "white") # Create a new black image

    def WriteTo(self, position, text, size=10):
        font = ImageFont.truetype("arial.ttf", size)
        ImageDraw.Draw(self.img).text(
        position,  # Coordinates
        text,  # Text
        (0, 0, 0),  # Color
        font=font
        )
        
    # def WriteTo(self, Customer, LabelMat, MaterialNr, LabelDrw, DrawingNr):
    #     font = ImageFont.truetype("arial.ttf", 8)
    #     ImageDraw.Draw(self.img).text(
    #     (5,100),  # Coordinates
    #     Customer,  # Text
    #     (0, 0, 0),  # Color
    #     font=font
    #     )
    #     ImageDraw.Draw(self.img).text((5,130), LabelMat+" "+MaterialNr, (0, 0, 0), font=font )

    #     self.img.show()