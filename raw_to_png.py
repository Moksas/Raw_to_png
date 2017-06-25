import _imaging #using the PIL library ,use the programe after insall the library
import Image 
rawData = open("1.raw",'rb').read()
imgSize = (500,360)
# Use the PIL raw decoder to read the data.
# the 'F;16' informs the raw decoder that we are reading 
# a little endian, unsigned integer 16 bit data.
img = Image.fromstring('RGB', imgSize, rawData, 'raw', 'RGB')
img.save("1.png")
