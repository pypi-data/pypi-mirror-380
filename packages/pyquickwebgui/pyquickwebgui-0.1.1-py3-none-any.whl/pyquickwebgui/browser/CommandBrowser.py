# -*- coding: utf-8 -*-
'''
@File    :   DefaultServerFlask.py
@Time    :   2025/06/10 10:36:03
@Author  :   LX
@Version :   1.0.0
@Desc    :   None
'''

from datetime import time
from multiprocessing import Process
import multiprocessing
import os
import platform
import shutil
import subprocess
from threading import Thread
from typing import Union

from ..config import QuickConfig
from .BaseBrowser  import BaseBrowser
from typing import Any, Callable, Dict, List, Union


class CommandBrowser(BaseBrowser):


    linux_browser_paths = [
        r"/usr/bin/google-chrome",
        r"/usr/bin/microsoft-edge",
        r"/usr/bin/brave-browser",
        r"/usr/bin/chromium",
        # Web browsers installed via flatpak portals
        r"/run/host/usr/bin/google-chrome",
        r"/run/host/usr/bin/microsoft-edge",
        r"/run/host/usr/bin/brave-browser",
        r"/run/host/usr/bin/chromium",
        # Web browsers installed via snap
        r"/snap/bin/chromium",
        r"/snap/bin/brave-browser",
        r"/snap/bin/google-chrome",
        r"/snap/bin/microsoft-edge",
    ]

    mac_browser_paths = [
        r"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        r"/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
        r"/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    ]
    # 操作系统
    OPERATING_SYSTEM = platform.system().lower()
    windows_browser_paths = [
        #优先 启动 chrome
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
    ]

    def get_browser_command(self,app):
        # https://peter.sh/experiments/chromium-command-line-switches/
        # https://www.cnblogs.com/Ghsoft/p/18359891

        browser_path = app.browser_path or self.browser_path
        if not browser_path:
            raise ValueError("未找到有效的浏览器路径")


        flags = [
            self.browser_path,
            # 用户数据（设置、缓存等）的位置
            f"--user-data-dir={app.profile_dir}",
            # 不遵守同源策略。关闭web安全检查 允许跨域请求
            # "--disable-web-security",
            # 新窗口
            "--new-window",
            # 启动时不检查是否为默认浏览器
            "--no-default-browser-check",
            "--allow-insecure-localhost",
            "--no-first-run",
            "--disable-sync",
            # https 页面允许从 http 链接引用 javascript/css/plug-ins
            "--allow-running-insecure-content",
            # 启动隐身无痕模式
            # "--incognito",
            #设置语言为英语_美国
            #"--lang=en_US",
            # 禁用沙盒
            # "--no-sandbox",
            # 启用自助服务终端模式 全屏
            # "--kiosk",
            #隐藏所有消息中心通知弹出窗口
            "--suppress-message-center-popups",
            # 本地开发调试的话，需要忽略证书错误
            # 设置允许访问本地文件
            "--args --allow-file-access-from-files",
            # "--test-type",
            #禁用桌面通知，在 Windows 中桌面通知默认是启用的。
            "--disable-desktop-notifications",
            # 禁用ssl证书检查
            # "--ignore-certificate-errors-spki-list",
            # 在离线插页式广告上禁用恐龙复活节彩蛋。
            "--disable-dinosaur-easter-egg",
            # 禁用插件
            "--disable-plugins",
            # 禁用java
            "--disable-java",
            # 禁用同步
            "--disable-sync",
            # 禁用内部的Flash Player
            "--disable-internal-flash",
            # 禁用同步应用程序
            "--disable-sync-apps",
            # 禁用同步自动填充
            "--disable-sync-autofill",
            # 禁用弹出拦截
            "--disable-popup-blocking",
            # 仅使用信任的插件
            "--trusted-plugins",
            # 禁用翻译
            "--disable-translate",
            "--disable-features=Translate",
        ]

        if app.debug:
            flags.extend(["--auto-open-devtools-for-tabs"])

        # if app.frameless:
        #     flags.extend(["--headless=new"])

        # if app.frameless:
        #     # 启动时不建立窗口
        #     flags.extend(["--disable-desktop-notifications"])


        if app.width and app.height and app.app_mode:
            flags.extend([f"--window-size={app.width},{app.height}"])
        elif app.fullscreen:
            flags.extend(["--start-maximized"])

        if app.extra_flags:
            flags = flags + app.extra_flags

        if app.app_mode:
            flags.append(f"--app={app.url}")
        else:
            flags.extend(["--guest", app.url])

        # 确保所有参数都是字符串
        valid_commands = []
        for cmd in flags:
            if cmd is None:
                self.log.warning("跳过无效的None命令参数")
                continue
            valid_commands.append(str(cmd))

        return valid_commands
    def get_browser_path_for_os(self, os_name: str) -> str:
        """根据操作系统名称获取浏览器路径"""
        dispatch_map = {
            "windows": lambda: self.find_browser_in_paths(self.windows_browser_paths),
            "linux": lambda: self.find_browser_in_paths(self.linux_browser_paths),
            "darwin": lambda: self.find_browser_in_paths(self.mac_browser_paths),
        }
        func = dispatch_map.get(os_name)
        path = func() if func else None

        func = dispatch_map.get(os_name)
        path = func() if func else None

        if path:
            self.log.info(f"找到浏览器路径: {path}")
        else:
            self.log.warning(f"在 {os_name} 系统上未找到兼容的浏览器")

        return path

    def find_browser_in_paths(self,browser_paths: List[str]):

        compatible_browser_path = None
        for path in browser_paths:

            if not os.path.exists(path):
                continue

            if compatible_browser_path is None:
                compatible_browser_path = path

            # if self.DEFAULT_BROWSER in path:
            #     return path

        return compatible_browser_path
    def get_view_kwargs( self, kwargs={}):
        return {"app":  kwargs["app"], "port": kwargs["port"]}


    def view(self, app , kwargs):
        try:

            # 如果未指定浏览器路径，则尝试根据操作系统获取默认浏览器路径
            self.browser_path = app.browser_path  or self.get_browser_path_for_os(self.OPERATING_SYSTEM)

            # 验证浏览器路径
            self.log.debug(f"使用的浏览器路径: {self.browser_path}")

            if not self.browser_path:
                self.log.error("找不到兼容的浏览器，请手动指定浏览器路径")
                return

            # 如果未指定浏览器命令，则调用方法生成默认的浏览器命令
            self.browser_command = app.browser_command  or self.get_browser_command(app)


            self.kwargs = kwargs
            self.show_browser = Thread(target=self.start_browser, args=(app,self.kwargs,))

            if self.show_browser:
                self.show_browser.start()

        except KeyboardInterrupt as e:
            self.__keyboard_interrupt = True
            self.log.error(":{}".format(e) , exc_info = True )


    def start_browser(self,app , server_process: Union[Thread, Process]):
        """
        启动浏览器进程。

        Args:
            server_process (Union[Thread, Process]): 服务器进程或线程对象。
        """
        self.log.info("==========>start_browser Quick version:{}".format(self.browser_command))
        # self.log.info("Command:{}".format(" ".join(self.browser_command)))

        # if app.OPERATING_SYSTEM == "darwin":
        #     multiprocessing.set_start_method("fork")




        app.config.FLASKWEBGUI_BROWSER_PROCESS = subprocess.Popen(self.browser_command)
        self.browser_pid = app.config.FLASKWEBGUI_BROWSER_PROCESS.pid
        app.config.FLASKWEBGUI_BROWSER_PROCESS.wait()


        if self.browser_path is None:
            while self.__keyboard_interrupt is False:
                time.sleep(1)

        if isinstance(server_process, Process):
            if self.on_shutdown is not None:
                self.on_shutdown()
            self.browser_pid = None
            shutil.rmtree(self.profile_dir, ignore_errors=True)

            if self.stray is False:
                print("server_process.kill.")
                server_process.kill()
        else:
            if app.on_shutdown is not None:
                app.on_shutdown()
            self.browser_pid = None
            #shutil.rmtree(self.profile_dir, ignore_errors=True)

            # if self.stray is False:
            #     print("QuickConfig.kill_port.")
            #     QuickConfig.kill_port(self.port)


