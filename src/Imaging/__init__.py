
from PIL import ImageChops, Image
import Selenium2Library, math


class Imaging():

    def __init__(self):
        pass

    def acquire_image(self, im):
        Selenium2Library.Selenium2Library.
        pass

    def acquire_image_by_selector(self, im, selector):
        pass

    def compare(self, im1, im2, threshold):
        """Calculate the root-mean-square difference between two images"""

        diff = ImageChops.difference(im1, im2)
        h = diff.histogram()
        sq = (value*((idx%256)**2) for idx, value in enumerate(h))
        sum_of_squares = sum(sq)
        rms = math.sqrt(sum_of_squares/float(im1.size[0] * im1.size[1]))
        return rms < threshold


if __name__ == "__main__":
    image = Imaging()
    a = Image.open('1.png')
    b = Image.open('2.png')
    print image.compare(a, b, 70)