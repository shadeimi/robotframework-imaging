
from PIL import Image, ImageChops
from base import EngineBase
import math


class Engine(EngineBase):

    def assertSameFiles(self, output_file, baseline_file, threshold=1):

        im1 = Image.open(output_file)
        im2 = Image.open(baseline_file)

        if not threshold:
            width, height = im1.size
            threshold = int(width * height * threshold)

        diff = ImageChops.difference(im1, im2)
        h = diff.histogram()
        sq = (value*((idx%256)**2) for idx, value in enumerate(h))
        sum_of_squares = sum(sq)
        rms = math.sqrt(sum_of_squares/float(im1.size[0] * im1.size[1]))
        return '%s' % True if rms < threshold else False
