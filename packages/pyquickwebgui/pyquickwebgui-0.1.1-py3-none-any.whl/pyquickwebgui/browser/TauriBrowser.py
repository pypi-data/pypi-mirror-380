# -*- coding: utf-8 -*-
'''
@File    :   DefaultServerFlask.py
@Time    :   2025/06/10 10:36:03
@Author  :   LX
@Version :   1.0.0
@Desc    :   None
'''

from traceback import print_tb
from .BaseBrowser  import BaseBrowser



class TauriBrowser(BaseBrowser):

    def get_view_kwargs(self, app, kwargs):
        return {"app": kwargs["app"], "port": kwargs["port"]}

 
    def view(self, app, kwargs):
        print("TauriBrowser.view server_kwargs:{}".format(server_kwargs))
