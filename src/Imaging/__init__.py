
from Selenium2Library import Selenium2Library


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

    def capture_page_screenshot_by_selector(self, im, selector):
        """
        :param im: Image file
        :param selector: CSS selector
        :return: Boolean Value
        """

        pass

    def compare_screenshots(self, im1, im2, threshold):
        """
        :param im1: PIL.Image instance
        :param im2: PIL.Image instance
        :param threshold: Compare threshold value
        :return: Boolean value
        """

        return self.engine.assertSameFiles(self.engine(), im1, im2, threshold)


if __name__ == "__main__":
    image = Imaging(engine="perceptualdiff_engine")
    print image.compare_screenshots('1.png', '2.png', 70)