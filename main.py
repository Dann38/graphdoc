from tesseract_reader.image_reader import ImageReader
from tesseract_reader.tesseract_reader import TesseractReader, TesseractReaderConfig
reader_img = ImageReader()
config = TesseractReaderConfig(lang="rus")
reader = TesseractReader(config)

img = reader_img.read('example_image/img_1.jpeg')
bboxes = reader.read(img)
print(bboxes)