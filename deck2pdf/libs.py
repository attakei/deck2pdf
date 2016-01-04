# -*- coding:utf8 -*-
import os
import hashlib


def gen_md5(filepath):
    if not os.path.exists(filepath):
        raise Exception()
    hash_ = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_.update(chunk)
    return hash_.hexdigest()
