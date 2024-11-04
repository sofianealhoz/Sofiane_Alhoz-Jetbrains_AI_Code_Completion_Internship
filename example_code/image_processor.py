import cv2

class ImageProcessor:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path)
        if self.image is None:
            raise ValueError("Image not found.")

    def convert_to_grayscale(self):
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        return gray_image

    def apply_gaussian_blur(self, kernel_size=(5, 5)):
        blurred_image = cv2.GaussianBlur(self.image, kernel_size, 0)
        return blurred_image

    def resize_image(self, width, height):
        resized_image = cv2.resize(self.image, (width, height))
        return resized_image

# Exemple d'utilisation
processor = ImageProcessor("example.jpg")
gray_image = processor.convert_to_grayscale()
blurred_image = processor.apply_gaussian_blur()
resized_image = processor.resize_image(100, 100)
