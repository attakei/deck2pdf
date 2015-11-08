# -*- coding:utf8 -*-
"""
"""
from __future__ import unicode_literals
import os
from . import errors

__author__ = 'attakei'


def resolve_path(path):
    if path.startswith('http://'):
        return path
    elif path.startswith('https://'):
        return path
    real_path = os.path.abspath(path)
    if not os.path.exists(real_path):
        raise errors.ResourceNotFound()
    return 'file://{}'.format(real_path)


class WebResource(object):
    """Capture target web-resource

    """
    def __init__(self, path):
        """

        :param path:
        :type path: str or unicode
        :return:
        """
        self.url = resolve_path(path)

    @property
    def is_local(self):
        return self.url.startswith('file://')
