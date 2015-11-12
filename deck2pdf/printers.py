# -*- coding:utf8 -*-
"""Print features
"""
from __future__ import unicode_literals

__author__ = 'attakei'


def calc_filled_pagesize(origin, capture):
    """
    """
    origin_ratio = origin[0] / origin[1]
    capture_ratio = float(capture[0]) / float(capture[1])
    pagesize = [0, 0]
    if origin_ratio > capture_ratio:
        pagesize[0] = origin[0] * origin_ratio / capture_ratio
        pagesize[1] = origin[1]
    else:
        pagesize[0] = origin[0]
        pagesize[1] = origin[1] * origin_ratio / capture_ratio
    return pagesize
