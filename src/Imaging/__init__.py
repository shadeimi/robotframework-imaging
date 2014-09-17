
import os
from Selenium2Library import Selenium2Library
from engines.pil_engine import ImageDiff
from contextlib import contextmanager
from PIL import Image
from warnings import warn


class Imaging(Selenium2Library):

    def __init__(self, engine='rms_engine'):
        super(Selenium2Library, self).__init__()
        try:
            self.engineName = engine
            self.module = __import__('engines.%s' % self.engineName, fromlist=['Engine'])
            self.engine = getattr(self.module, 'Engine')
        except ImportError:
            print "Wrong Engine submitted"
            exit(-1)

    def capture_page_screenshot_by_selector(self):
        pass

    def compare_page_screenshot(self, file, baseline_file, threshold=0):
        return self.engine.assertSameFiles(self.engine(), file, baseline_file, threshold)


if __name__ == "__main__":
    image = Imaging(engine="perceptualdiff_engine")
    print image.compare_page_screenshot('1.png', '2.png', 70)