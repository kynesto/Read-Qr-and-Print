from pystrich.datamatrix import DataMatrixEncoder
from PIL import Image
from PIL import ImageDraw

class Matrix():
    def create(self, text, length=127):
        self.dm = DataMatrixEncoder(text)

    def merge(self, image, widthQr=120):
        self.dm.save('DataMatrix.bmp')
        DataMatrix = Image.open('DataMatrix.bmp')

        new_height = widthQr * DataMatrix.height / DataMatrix.width
        DataMatrix = DataMatrix.resize((widthQr, int(new_height)), Image.ANTIALIAS)
        position = ((image.width - DataMatrix.width), (image.height - DataMatrix.height))
        image.paste(DataMatrix, position)
        # image.show()
        return image
