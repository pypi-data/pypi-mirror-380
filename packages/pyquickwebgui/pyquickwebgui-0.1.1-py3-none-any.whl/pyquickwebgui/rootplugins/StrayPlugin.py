
from pyquickwebgui.rootplugins.BasePlugin import BasePlugin



class StrayPlugin(BasePlugin):

    def __init__(self):
        super().__init__()


    def register(self , app):
        pass
    def run(self , app):
        """
        创建并运行系统托盘图标。
        """
        import pystray
        from PIL import Image

        # 定义托盘图标
        if app.stray.get('icon') is None and len(app.stray.get('img', "")) > 0:
            app.stray['icon'] = Image.open(app.stray.get('img'))
        else:
            # 默认白色
            app.stray['icon'] = Image.new('RGB', (64, 64), 'white')

        # 定义托盘图标被点击时的响应函数
        def on_activate(icon, item):
            """处理托盘图标点击事件"""
            _call =  app.stray.get('menu_click_show', lambda:  print("托盘图标被点击") )
            _call()
        def on_menu_click(icon, item):
            """处理菜单项点击事件"""
            if str(item) == "Show":
                print("显示功能被触发")
                _call =  app.stray.get('menu_click_show',app.show_browser)
                _call()
            elif str(item) == "Exit":
                _call =  app.stray.get('menu_click_exit',app.close_application)
                _call()

        # 创建一个系统托盘对象
        default_menu = (
            pystray.MenuItem("Show", lambda icon, item: on_menu_click(icon, item)),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem("Exit", lambda icon, item: on_menu_click(icon, item)),
        )

        pystray.Icon(
            name=app.stray.get('name', ""),
            icon=app.stray.get('icon', ""),
            title=app.stray.get('title', ""),
            menu=app.stray.get('menu', default_menu),
            activate=app.stray.get('activate', on_activate)
        ).run()

if __name__ == "__main__":
    log =  StrayPlugin()
    # 测试日志
    log.logger.debug("这是一个调试信息")
    log.logger.info("这是一个普通信息")
    log.logger.warning("这是一个警告信息")
    log.logger.error("这是一个错误信息")
    log.logger.critical("这是一个严重错误信息")