# -*- coding: utf-8 -*-
'''
@File    :   BaseDefaultServer.py
@Time    :   2025/06/10 10:36:03
@Author  :   LX
@Version :   1.0.0
@Desc    :   None
'''


class BaseBrowser:
  # 或者更明确地定义方法签名

    def __init__(self, log = None):
        if log is not None:
            self.log = log

    def get_view_kwargs(self, app , kwargs={}):
        # 实现内容
        return kwargs


    def view(self, app , kwargs):
        # 实现内容
        pass


