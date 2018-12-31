from pystrich.datamatrix import DataMatrixEncoder
from PIL import Image
from PIL import ImageDraw

encoder = DataMatrixEncoder("This is a DataMatrix.12345678901234567890123456789012345678901234567890123457889012345678901234567890")
encoder.save('DataMatrix.jpg')
DataMatrix = Image.open('DataMatrix.jpg')
img = Image.new( 'RGB', (400,250), "blue") # Create a new black image

new_width  = 120
new_height = new_width * DataMatrix.height / DataMatrix.width
print(new_height)
DataMatrix = DataMatrix.resize((new_width, int(new_height)), Image.ANTIALIAS)

image_copy = img.copy()
position = ((image_copy.width - DataMatrix.width), (image_copy.height - DataMatrix.height))
image_copy.paste(DataMatrix, position)
image_copy.save('pasted_image.jpg')
image_copy.show()