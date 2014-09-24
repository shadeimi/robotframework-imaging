
import os
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

    def capture_page_screenshot_by_selector(self):
        """ To be implemented ASAP """
        pass

    def _inject_matchmedia_js(self):
        javascript = """

            /*! matchMedia() polyfill - Test a CSS media type/query in JS. Authors & copyright (c) 2012: Scott Jehl, Paul Irish, Nicholas Zakas, David Knight. Dual MIT/BSD license */

            window.matchMedia || (window.matchMedia = function() {
                "use strict";

                // For browsers that support matchMedium api such as IE 9 and webkit
                var styleMedia = (window.styleMedia || window.media);

                // For those that don't support matchMedium
                if (!styleMedia) {
                    var style       = document.createElement('style'),
                        script      = document.getElementsByTagName('script')[0],
                        info        = null;

                    style.type  = 'text/css';
                    style.id    = 'matchmediajs-test';

                    script.parentNode.insertBefore(style, script);

                    // 'style.currentStyle' is used by IE <= 8 and 'window.getComputedStyle' for all other browsers
                    info = ('getComputedStyle' in window) && window.getComputedStyle(style, null) || style.currentStyle;

                    styleMedia = {
                        matchMedium: function(media) {
                            var text = '@media ' + media + '{ #matchmediajs-test { width: 1px; } }';

                            // 'style.styleSheet' is used by IE <= 8 and 'style.textContent' for all other browsers
                            if (style.styleSheet) {
                                style.styleSheet.cssText = text;
                            } else {
                                style.textContent = text;
                            }

                            // Test if media query is true or false
                            return info.width === '1px';
                        }
                    };
                }

                return function(media) {
                    return {
                        matches: styleMedia.matchMedium(media || 'all'),
                        media: media || 'all'
                    };
                };
            }());
        """

        js = self._get_javascript_to_execute(javascript)
        self._current_browser().execute_script(js)

    def assert_mediaquery_execution_in_page(self, url):
        javascript = """
            window.matchMedia("mediaquery")
        """

        self._inject_matchmedia_js()
        js = self._get_javascript_to_execute(javascript)
        return self._current_browser().execute_script(js)

    def compare_page_screenshot(self, file, baseline_file, threshold=0):
        base_path = self._get_screenshot_paths()
        file = os.path.join(base_path, file)
        baseline_file = os.path.join(base_path, baseline_file)
        return self.engine.assertSameFiles(self.engine(), file, baseline_file, threshold)


if __name__ == "__main__":
    image = Imaging(engine="perceptualdiff_engine")
    print image.compare_page_screenshot('1.png', '2.png', 70)