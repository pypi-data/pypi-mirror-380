class BasePlugin:
    """
    插件基类
    """
    def register(self , app):
        raise NotImplementedError("插件必须实现 register 方法")
    def run(self, app):
        raise NotImplementedError("插件必须实现 run 方法")

