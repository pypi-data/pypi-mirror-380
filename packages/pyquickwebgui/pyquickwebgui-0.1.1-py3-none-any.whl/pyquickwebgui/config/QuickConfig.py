# -*- coding: utf-8 -*-
'''
@File    :   QuickConfig.py
@Time    :   2025/06/10 16:46:15
@Author  :   LX
@Version :   1.0.0
@Desc    :   配置类
'''


from typing import Any, Callable, Dict, List, Union
import webbrowser
from enum import Enum
import platform
import socketserver
import psutil
import signal
import os

from ..servers.BaseDefaultServer import BaseDefaultServer
from ..servers.DefaultServerDjango import DefaultServerDjango
from ..servers.DefaultServerFastApi import DefaultServerFastApi
from ..servers.DefaultServerFlask import DefaultServerFlask
from ..servers.DefaultServerFlaskSocketIO import DefaultServerFlaskSocketIO
from ..servers.DefaultServerWebpy import DefaultServerWebpy


from ..browser.BaseBrowser import BaseBrowser
from ..browser.CommandBrowser import CommandBrowser
from ..browser.TauriBrowser import TauriBrowser
from ..browser.WebviewBrowser import WebviewBrowser



class Browser_type_enum(Enum):
    """_summary_
    浏览器类型枚举
    :param Enum: _description_
    :type Enum: _type_
    """
    # 命令行启动浏览器
    COMMAND = "command"
    # webview 启动浏览器
    WEBVIEW = "webview"
    # tauri 启动浏览器
    TAURI = "tauri"

class Server_type_enum(Enum):
    """_summary_
    服务器枚举
    :param Enum: _description_
    :type Enum: _type_
    """
    #"fastapi"
    FASTAPI =  "fastapi"
    FLASK =  "flask"
    FLASK_SOCKETIO = "flask_socketio"
    DJANGO = "django"
    WEBPY = "webpy"



class QuickConfig:

    # 版本号
    version = "0.0.5"

    FLASKWEBGUI_USED_PORT = None
    FLASKWEBGUI_BROWSER_PROCESS = None

 
    # 操作系统
    OPERATING_SYSTEM = platform.system().lower()

    PY = "python3" if OPERATING_SYSTEM in ["linux", "darwin"] else "python"

    ROOTPLUGINS_DIR = "rootplugins"

    BASE_PLUGIN_CLASS_NAME = "BasePlugin".lower()

    PLUGIN_CLASS_NAME = "plugin"
    # 插件目录
    PLUGINS_DIR = "plugins"




    # 服务 调度器
    webserver_dispacher: Dict[str, BaseDefaultServer] = {
        Server_type_enum.FASTAPI.value : DefaultServerFastApi,
        Server_type_enum.FLASK.value : DefaultServerFlask,
        Server_type_enum.FLASK_SOCKETIO.value : DefaultServerFlaskSocketIO,
        Server_type_enum.DJANGO.value : DefaultServerDjango,
        Server_type_enum.WEBPY.value : DefaultServerWebpy,
    }

    # 浏览器 调度器
    browser_dispacher: Dict[str, BaseBrowser] = {
        Browser_type_enum.COMMAND.value : CommandBrowser,
        Browser_type_enum.WEBVIEW.value : WebviewBrowser,
        Browser_type_enum.TAURI.value : TauriBrowser,
    }

    @staticmethod
    def get_free_port():
        with socketserver.TCPServer(("localhost", 0), None) as s:
            free_port = s.server_address[1]
        return free_port

    @staticmethod
    def kill_port(port: int):
        for proc in psutil.process_iter():
            try:
                for conns in proc.net_connections(kind="inet"):
                    if conns.laddr.port == port:
                        proc.send_signal(signal.SIGTERM)
            except psutil.AccessDenied:
                continue

 
    