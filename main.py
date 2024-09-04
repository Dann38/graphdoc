import cv2
from tesseract_reader.image_reader import ImageReader
from tesseract_reader.tesseract_reader import TesseractReader, TesseractReaderConfig
from image_processor import ImageProcessor


def get_bboxes(path_img):
    reader_img = ImageReader()
    config = TesseractReaderConfig(lang="rus")
    reader = TesseractReader(config)

    img = reader_img.read(path_img)
    bboxes, text = reader.read(img)
    return img, bboxes, text


if __name__ == "__main__":
    inp, out = 'example_image/img_1.jpeg', 'output_image_with_bboxes.jpeg'
    img, bboxes, text = get_bboxes(inp)

    processor = ImageProcessor()

    img_with_bboxes = processor.draw_bboxes(img, bboxes)

    cv2.imwrite(out, img_with_bboxes)
    print(f"Изображение сохранено в {out}")
