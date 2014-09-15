
import PIL
import math


class Imaging():

    def __init__(self):
        pass

    def acquire(self, im):
        pass

    @staticmethod
    def compare(self, im1, im2):
        """Calculate the root-mean-square difference between two images"""

        self.diff = PIL.ImageChops.difference(im1, im2)
        self.h = self.diff.histogram()
        self.sq = (value*((idx%256)**2) for idx, value in enumerate(self.h))
        self.sum_of_squares = sum(self.sq)
        self.rms = math.sqrt(self.sum_of_squares/float(im1.size[0] * im1.size[1]))
        return self.rms