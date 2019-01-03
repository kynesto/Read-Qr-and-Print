from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

class ImageGen():

    def blank(self):
        self.img = Image.new( 'RGB', (800,500), "white") # Create a new black image

    def WriteTo(self, position, text, font="cour.ttf", size=38):
        font = ImageFont.truetype(font, size)
        ImageDraw.Draw(self.img).text(
        position,  # Coordinates
        text,  # Text
        (0, 0, 0),  # Color
        font=font
        )
    
    def get(self):
        return self.img