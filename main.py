import cv2
from tesseract_reader.image_reader import ImageReader
from tesseract_reader.tesseract_reader import TesseractReader, TesseractReaderConfig
from image_processor import ImageProcessor


def get_bboxes():
    reader_img = ImageReader()
    config = TesseractReaderConfig(lang="rus")
    reader = TesseractReader(config)

    img = reader_img.read('example_image/img_1.jpeg')
    bboxes, text = reader.read(img)
    return img, bboxes


if __name__ == "__main__":
    img, bboxes = get_bboxes()

    processor = ImageProcessor()

    img_with_bboxes = processor.draw_bboxes(img, bboxes)

    output_path = 'output_image_with_bboxes.jpeg'
    cv2.imwrite(output_path, img_with_bboxes)
    print(f"Изображение сохранено в {output_path}")
