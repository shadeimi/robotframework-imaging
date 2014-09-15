
from PIL import ImageChops, Image
import math
from Selenium2Library import Selenium2Library


class Imaging(Selenium2Library):

    def __init__(self):
        super(Selenium2Library, self).__init__()
        self.a = None

    def capture_page_screenshot_by_selector(self, im, selector):
        """
        :param im: Image file
        :param selector: CSS selector
        :return: Boolean Value
        """

        pass

    def compare(self, im1, im2, threshold):
        """
        :param im1: PIL.Image instance
        :param im2: PIL.Image instance
        :param threshold: Compare threshold value
        :return: Boolean value
        """

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