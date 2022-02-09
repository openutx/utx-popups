#!/usr/bin/python
# encoding=utf-8

"""
@Author  :  Lijiawei
@Date    :  2022/2/9 2:40 下午
@Desc    :  dismiss line.
"""

from airtest.core.api import *
from popup.settings import Settings as ST


def popup(tpl=ST.TPL_DIR, timeout=5, devices=None, enable=ST.ENABLE):
    """
    General pop-up processing!
    :param enable: Open or not
    :param devices: Current device uri
    :param tpl: Image template flies path
    :param timeout: timeout Default 5 seconds
    :return: Click pop-up event
    """
    if enable:
        auto_setup(__file__, devices=str(devices).split(','))
        ST.FIND_TIMEOUT_TMP = timeout
        ST.THRESHOLD = 0.7

        if tpl:
            images_path = tpl
            images = os.listdir(images_path)
        else:
            images_path = os.path.join(os.getcwd(), 'img')
            images = os.listdir(images_path)

        print(images)
        for img in images:
            pos = exists(Template(r"{}/{}".format(images_path, img)))
            if pos:
                touch(pos)
