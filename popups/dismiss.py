#!/usr/bin/python
# encoding=utf-8

"""
@Author  :  Lijiawei
@Date    :  2022/2/9 2:40 下午
@Desc    :  dismiss line.
"""

from airtest.core.api import *
from popups.settings import Settings as UT
from loguru import logger


def popup(tpl=UT.TPL_DIR, timeout=5, devices=None):
    """
    General pop-up processing!
    :param devices: Current device uri
    :param tpl: Image template flies path
    :param timeout: timeout Default 5 seconds
    :return: Click pop-up event
    """
    if UT.ENABLE:
        auto_setup(__file__, devices=str(devices).split(','))
        ST.FIND_TIMEOUT_TMP = timeout

        if tpl:
            images_path = tpl
        else:
            if UT.SYS:
                if UT.iOS:
                    images_path = str(__file__).replace('dismiss.py', 'tpl/sys/ios')
                else:
                    images_path = str(__file__).replace('dismiss.py', 'tpl/sys/android')
            else:
                images_path = str(__file__).replace('dismiss.py', 'tpl/app')

        try:
            images = sorted([tpl for tpl in os.listdir(images_path) if str(tpl).endswith('png')])
            logger.info(f'Try to find template pictures: {images}')
            for s in range(UT.LOOP):
                for img in images:
                    logger.info(f'Try to find tpl: {img}')
                    pos = exists(Template(r"{}/{}".format(images_path, img)))
                    if pos:
                        touch(pos)
        except FileNotFoundError as E:
            logger.warning(f'Picture template path does not exist: {images_path}')
            logger.error(f'{E}')
