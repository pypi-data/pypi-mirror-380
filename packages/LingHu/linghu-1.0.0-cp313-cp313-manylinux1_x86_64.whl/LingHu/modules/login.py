from typing import Self
# 第三方库导入
import HD.HD登录 as hd # pylint: disable=import-error

# 第一方库导入
from LingHu.utils.base import Base
class Login(Base):
    """
    登录类
    """
    def __init__(self, username:str, password:str, dll_path:str, appname: str = "", lparam: str = "", autoupdate: bool = False,
              showmanship: bool = False):
        """
        初始化登录类
        
        :param username: 用户名
        :param password: 密码
        :param dll_path: DLL路径
        :param appname: 应用名称
        :param lparam: 登录参数
        :param autoupdate: 是否自动更新
        :param showmanship: 是否显示manship
        """
        super().__init__()
        self.username: str = username
        self.password: str = password
        self.dll_path: str = dll_path
        self.appname: str = appname
        self.lparam: str = lparam
        self.autoupdate: bool = autoupdate
        self.showmanship: bool = showmanship
        self._login:bool = False 
    def set_dll_path(self) -> Self:
        """
        设置DLL路径
        
        :return: Self
        """
        hd.HD_Path(self.dll_path)
        return self
    
    def login(self)  -> Self:
        """
        执行登录操作
        :return: Self
        """
        self.text = "登录"
        self.ret = hd.HD登录_登录(self.username, self.password, self.appname, self.lparam, self.autoupdate, self.showmanship)
        self.user_login()
        self._login = self.bool
        return self

    def get_last_login_fyi(self) -> Self:
        """
        获取最近登录时候的点数
        
        :return: Self
        """
        if self._login:
            self.text = "获取最近登录点数"
            self.ret = hd.HD登录_获取最近登录点数()
            self.execute_function()
        return self

    def get_last_login_time(self) -> Self:
        """
        获取最近登录时间戳
        
        :return: Self
        """
        if self._login:
            self.text = "获取最近登录时间"
            self.ret = hd.HD登录_获取最近登录时间()
            self.execute_function()
        return self

    def get_current_fyi(self) -> Self:
        """
        获取当前点数
        
        :return: Self
        """
        if self._login:
            self.text = "获取当前点数"
            self.ret = hd.HD登录_获取点数()
            self.execute_function()
        return self

    def get_max_open_num(self) -> Self:
        """
        获取当前最大打开窗口数
        
        :return: Self
        """
        if self._login:
            self.text = "获取最大多开数"
            self.ret = hd.HD登录_获取最大多开数()
            self.execute_function()
        return self

    def get_version(self) -> Self:
        """
        获取当前插件版本号
        
        :return: Self
        """
        if self._login:
            self.text = "获取版本号"
            self.ret = hd.HD登录_获取版本号()
            self.execute_function()
        return self
    
class 登录模块(Base):
    """
    登录模块封装类（中文函数名版本）
    
    """
    
    def __init__(self, 用户名:str, 密码:str, dll路径:str, 应用名称: str = "", 应用参数: str = "", 自动更新: bool = False,
              显示消息框: bool = False):
        """
        初始化登录类
        
        :param 用户名: 登录用户名
        :param 密码: 登录密码
        :param dll路径: HD登录DLL文件路径
        :param 应用名称: 应用名称，用于自动更新识别
        :param 应用参数: 应用启动参数，用于自动更新
        :param 自动更新: 是否启用自动更新功能
        :param 显示消息框: 是否显示操作消息框
        """
        super().__init__()
        self.用户名: str = 用户名
        self.密码: str = 密码
        self.dll路径: str = dll路径
        self.应用名称: str = 应用名称
        self.应用参数: str = 应用参数
        self.自动更新: bool = 自动更新
        self.显示消息框: bool = 显示消息框
        self._login:bool = False
    def 设置dll路径(self) -> Self:
        """
        设置DLL文件路径
        
        加载HD登录所需的DLL文件，为后续操作做准备。
        
        :return: Self 返回实例本身，支持链式调用
        """
        hd.HD_Path(self.dll路径)
        return self
    
    def 登录(self) -> Self:
        """
        执行用户登录操作
        
        使用提供的用户名、密码和应用信息进行HD登录验证。
        登录结果会自动处理并更新状态信息。
        
        :return: Self 返回实例本身，支持链式调用
        """
        self.ret = hd.HD登录_登录(self.用户名, self.密码, self.应用名称, self.应用参数, self.自动更新, self.显示消息框)
        self.user_login()
        self._login = self.bool
        return self

    def 获取最近登录点数(self) -> Self:
        """
        获取最近登录时的点数信息
        
        查询并获取最近一次成功登录时的点数数据。
        
        :return: Self 返回实例本身，支持链式调用
        """
        if self._login:
            self.text = "获取最近登录点数"
            self.ret = hd.HD登录_获取最近登录点数()
            self.execute_function()
        return self

    def 获取最近登录时间(self) -> Self:
        """
        获取最近登录时间戳
        
        查询并获取最近一次成功登录的时间戳信息。
        
        :return: Self 返回实例本身，支持链式调用
        """
        if self._login:
            self.text = "获取最近登录时间"
            self.ret = hd.HD登录_获取最近登录时间()
            self.execute_function()
        return self

    def 获取当前点数(self) -> Self:
        """
        获取当前账户点数
        
        查询并获取当前账户的可用点数信息。
        
        :return: Self 返回实例本身，支持链式调用
        """
        if self._login:
            self.text = "获取当前点数"
            self.ret = hd.HD登录_获取点数()
            self.execute_function()
        return self

    def 获取最大多开数(self) -> Self:
        """
        获取最大多开数量
        
        查询当前账户支持的最大同时打开窗口数量。
        
        :return: Self 返回实例本身，支持链式调用
        """
        if self._login:
            self.text = "获取最大多开数"
            self.ret = hd.HD登录_获取最大多开数()
            self.execute_function()
        return self

    def 获取版本号(self) -> Self:
        """
        获取插件版本号
        
        查询当前HD登录插件的版本信息。
        
        :return: Self 返回实例本身，支持链式调用
        """
        if self._login:
            self.text = "获取版本号"
            self.ret = hd.HD登录_获取版本号()
            self.execute_function()
        return self
    
