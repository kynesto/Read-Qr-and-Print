from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

class ImageGen():

    def blank(self):
        self.img = Image.new( 'RGB', (400,250), "white") # Create a new black image

    def WriteTo(self, position, text, font="arial.ttf", size=18):
        font = ImageFont.truetype(font, size)
        ImageDraw.Draw(self.img).text(
        position,  # Coordinates
        text,  # Text
        (0, 0, 0),  # Color
        font=font
        )
    
    def get(self):
        return self.img