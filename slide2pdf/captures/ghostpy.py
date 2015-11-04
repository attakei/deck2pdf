# -*- coding:utf8 -*-
"""slide2pdf capturing engine by Shost.py

"""
from . import CaptureEngine as AbstractEngine
from .. import count_slide_from_dom
import os
import logging
from ghost import Ghost


Logger = logging.getLogger(__file__)


class CaptureEngine(AbstractEngine):
    def __init__(self, url):
        super(CaptureEngine, self).__init__(url)
        self._url = 'file://' + self._url

    def start(self):
        self._ghost = Ghost()
        self._session = self._ghost.start()
        self._session.set_viewport_size(1135, 740)

    def end(self):
        self._session.exit()

    def _calc_slide_num(self):
        self._session.open(self._url)
        return int(self._session.evaluate('slidedeck.slides.length')[0])        

    def capture_page(self, slide_idx, is_last=False):
        FILENAME = os.path.join(self.save_dir, "screen_{}.png".format(slide_idx))
        curSlide = int(self._session.evaluate('slidedeck.curSlide_')[0])
        while not is_last and slide_idx >= curSlide:
            self._session.evaluate('slidedeck.nextSlide();')
            curSlide = int(self._session.evaluate('slidedeck.curSlide_')[0])
        # Get Screen Shot
        self._session.evaluate('slidedeck.prevSlide();')
        self._session.sleep(1.5)
        self._session.capture_to(FILENAME)
        self._slide_captures.append(FILENAME)
    
    def capture_all(self):
        self.start()
        slides = self._calc_slide_num()
        Logger.debug('{} slides'.format(slides))
        self._session.evaluate('for (var idx = slidedeck.curSlide_; idx > 0; idx--) { slidedeck.prevSlide();}')
        
        for slide_idx in range(slides):
            is_last = (slide_idx == slides - 1)
            self.capture_page(slide_idx, is_last)
        self.end()
