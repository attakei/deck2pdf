# -*- coding:utf8 -*-
"""deck2pdf capturing engine by Shost.py

"""
from . import CaptureEngine as AbstractEngine
import os
import logging
from ghost import Ghost


Logger = logging.getLogger(__file__)


class CaptureEngine(AbstractEngine):
    def start(self):
        super(CaptureEngine, self).start()
        self._ghost = Ghost()

    def end(self):
        self._ghost.exit()

    def _calc_slide_num(self):
        session = self._ghost.start()
        session.open(self.url)
        slides = int(session.evaluate('slidedeck.slides.length')[0])
        session.exit()
        return slides

    def capture_page(self, slide_idx):
        FILENAME = os.path.join(self.save_dir, "screen_{}.png".format(slide_idx))
        url = '{}#{}'.format(self.url, slide_idx+1)
        session = self._ghost.start()
        session.set_viewport_size(1135, 740)
        session.open(url)
        session.sleep(2)
        session.capture_to(FILENAME)
        session.exit()
        self._slide_captures.append(FILENAME)

    def capture_all(self):
        self.start()
        slides = self._calc_slide_num()
        Logger.debug('{} slides'.format(slides))

        for slide_idx in range(slides):
            self.capture_page(slide_idx)
        self.end()
