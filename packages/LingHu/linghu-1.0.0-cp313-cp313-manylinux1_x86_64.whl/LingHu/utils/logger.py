import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from typing import Optional, Union, Dict, Any
from threading import Lock


class LoggerManager:
    """
    日志管理器 - 单例模式，管理全局日志配置
    """
    
    _instance = None
    _lock = Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._logger: Optional[logging.Logger] = None
            self._config = {
                'log_dir': None,
                'log_filename': None,
                'log_level': logging.INFO,
                'max_file_size': 10 * 1024 * 1024,  # 10MB
                'backup_count': 5,
                'console_output': True,
                'file_output': True,
                'format_string': '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
                'date_format': '%Y-%m-%d %H:%M:%S'
            }
            self._initialized = True
    
    def configure(self, **kwargs):
        """
        配置日志系统
        
        Args:
            log_dir: 日志文件目录
            log_filename: 日志文件名
            log_level: 日志级别
            max_file_size: 单个日志文件最大大小
            backup_count: 保留的备份文件数量
            console_output: 是否输出到控制台
            file_output: 是否输出到文件
            format_string: 日志格式字符串
            date_format: 日期格式字符串
        """
        # 验证日志级别
        if 'log_level' in kwargs:
            log_level = kwargs['log_level']
            if isinstance(log_level, str):
                level_map = {
                    'DEBUG': logging.DEBUG,
                    'INFO': logging.INFO,
                    'WARNING': logging.WARNING,
                    'ERROR': logging.ERROR,
                    'CRITICAL': logging.CRITICAL
                }
                kwargs['log_level'] = level_map.get(log_level.upper(), logging.INFO)
            elif not isinstance(log_level, int):
                kwargs['log_level'] = logging.INFO
        
        self._config.update(kwargs)
        
        # 如果日志器已存在，重新配置
        if self._logger is not None:
            self._reconfigure_logger()
    
    def _reconfigure_logger(self):
        """重新配置日志器"""
        if self._logger is not None:
            # 移除所有处理器
            for handler in self._logger.handlers[:]:
                self._logger.removeHandler(handler)
                handler.close()
            
            # 重新设置日志器
            self._setup_logger()
    
    def _setup_logger(self):
        """设置日志器"""
        try:
            # 创建日志器
            self._logger = logging.getLogger("LingHuLogger")
            self._logger.setLevel(self._config['log_level'])
            
            # 避免重复添加handler
            if not self._logger.handlers:
                # 创建格式化器
                formatter = logging.Formatter(
                    self._config['format_string'],
                    datefmt=self._config['date_format']
                )
                
                # 文件处理器
                if self._config['file_output']:
                    log_dir = self._config['log_dir'] or os.path.join(os.getcwd(), "logs")
                    log_filename = self._config['log_filename'] or f"linghu_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
                    
                    # 创建日志目录
                    os.makedirs(log_dir, exist_ok=True)
                    
                    # 日志文件完整路径
                    log_file_path = os.path.join(log_dir, log_filename)
                    
                    # 文件处理器（支持轮转）
                    file_handler = RotatingFileHandler(
                        filename=log_file_path,
                        maxBytes=self._config['max_file_size'],
                        backupCount=self._config['backup_count'],
                        encoding='utf-8'
                    )
                    file_handler.setLevel(self._config['log_level'])
                    file_handler.setFormatter(formatter)
                    self._logger.addHandler(file_handler)
                    
                    # 保存日志文件路径
                    self._log_file_path = log_file_path
                
                # 控制台处理器
                if self._config['console_output']:
                    console_handler = logging.StreamHandler(sys.stdout)
                    console_handler.setLevel(self._config['log_level'])
                    console_handler.setFormatter(formatter)
                    self._logger.addHandler(console_handler)
                
                # 输出初始化信息
                if hasattr(self, '_log_file_path'):
                    self._logger.info(f"日志系统初始化完成 - 日志文件: {self._log_file_path}")
        except Exception as e:
            # 如果设置失败，至少确保有一个控制台输出
            if self._logger is None:
                self._logger = logging.getLogger("LingHuLogger")
                self._logger.setLevel(logging.INFO)
                console_handler = logging.StreamHandler(sys.stdout)
                console_handler.setLevel(logging.INFO)
                formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                console_handler.setFormatter(formatter)
                self._logger.addHandler(console_handler)
                self._logger.error(f"日志系统初始化失败: {e}")
    
    def get_logger(self) -> logging.Logger:
        """获取日志器实例"""
        if self._logger is None:
            self._setup_logger()
        # 确保总是返回一个有效的日志器实例
        if self._logger is None:
            # 如果_setup_logger失败，创建一个基本的控制台日志器
            self._logger = logging.getLogger("LingHuLoggerFallback")
            self._logger.setLevel(logging.INFO)
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(formatter)
            self._logger.addHandler(console_handler)
            self._logger.error("日志系统初始化失败，使用备用日志器")
        return self._logger
    
    def get_config(self) -> Dict[str, Any]:
        """获取当前配置"""
        return self._config.copy()
    
    def get_log_file_path(self) -> Optional[str]:
        """获取当前日志文件路径"""
        return getattr(self, '_log_file_path', None)


# 全局日志管理器实例
_logger_manager = LoggerManager()


class Logger:
    """
    公开的日志类 - 提供用户友好的接口
    """
    
    def __init__(self, 
                 log_dir: Optional[str] = None, 
                 log_filename: Optional[str] = None,
                 log_level: Union[int, str] = logging.INFO,
                 max_file_size: int = 10 * 1024 * 1024,
                 backup_count: int = 5,
                 console_output: bool = True,
                 file_output: bool = True):
        """
        初始化日志器（用户接口）
        
        Args:
            log_dir: 日志文件目录，如果为None则使用全局配置
            log_filename: 日志文件名，如果为None则使用全局配置
            log_level: 日志级别，如果为None则使用全局配置
            max_file_size: 单个日志文件最大大小
            backup_count: 保留的备份文件数量
            console_output: 是否输出到控制台
            file_output: 是否输出到文件
        """
        # 验证日志级别
        if isinstance(log_level, str):
            level_map = {
                'DEBUG': logging.DEBUG,
                'INFO': logging.INFO,
                'WARNING': logging.WARNING,
                'ERROR': logging.ERROR,
                'CRITICAL': logging.CRITICAL
            }
            log_level = level_map.get(log_level.upper(), logging.INFO)
        elif not isinstance(log_level, int):
            log_level = logging.INFO
        
        # 如果用户提供了配置，更新全局配置
        config = {}
        if log_dir is not None:
            config['log_dir'] = log_dir
        if log_filename is not None:
            config['log_filename'] = log_filename
        if log_level is not None:
            config['log_level'] = log_level
        if max_file_size != 10 * 1024 * 1024:
            config['max_file_size'] = max_file_size
        if backup_count != 5:
            config['backup_count'] = backup_count
        if console_output is not None:
            config['console_output'] = console_output
        if file_output is not None:
            config['file_output'] = file_output
        
        if config:
            _logger_manager.configure(**config)
        
        # 获取内部日志器
        self._logger: logging.Logger = _logger_manager.get_logger()
    
    def debug(self, message: str, *args, **kwargs):
        """调试级别日志"""
        self._logger.debug(message, *args, **kwargs)
    
    def info(self, message: str, *args, **kwargs):
        """信息级别日志"""
        self._logger.info(message, *args, **kwargs)
    
    def warning(self, message: str, *args, **kwargs):
        """警告级别日志"""
        self._logger.warning(message, *args, **kwargs)
    
    def error(self, message: str, *args, **kwargs):
        """错误级别日志"""
        self._logger.error(message, *args, **kwargs)
    
    def critical(self, message: str, *args, **kwargs):
        """严重错误级别日志"""
        self._logger.critical(message, *args, **kwargs)
    
    def exception(self, message: str, *args, **kwargs):
        """异常级别日志（包含异常信息）"""
        self._logger.exception(message, *args, **kwargs)
    
    def set_level(self, level: Union[int, str]):
        """设置日志级别"""
        _logger_manager.configure(log_level=level)
    
    def get_log_file_path(self) -> Optional[str]:
        """获取当前日志文件路径"""
        return _logger_manager.get_log_file_path()


# ============================================================================
# 内部使用接口 - 简单直接
# ============================================================================

def _get_internal_logger() -> logging.Logger:
    """获取内部日志器"""
    return _logger_manager.get_logger()


def _debug(message: str, *args, **kwargs):
    """内部调试日志"""
    try:
        _get_internal_logger().debug(message, *args, **kwargs)
    except Exception as e:
        print(f"日志记录失败: {e}")


def _info(message: str, *args, **kwargs):
    """内部信息日志"""
    try:
        _get_internal_logger().info(message, *args, **kwargs)
    except Exception as e:
        print(f"日志记录失败: {e}")


def _warning(message: str, *args, **kwargs):
    """内部警告日志"""
    try:
        _get_internal_logger().warning(message, *args, **kwargs)
    except Exception as e:
        print(f"日志记录失败: {e}")


def _error(message: str, *args, **kwargs):
    """内部错误日志"""
    try:
        _get_internal_logger().error(message, *args, **kwargs)
    except Exception as e:
        print(f"日志记录失败: {e}")


def _critical(message: str, *args, **kwargs):
    """内部严重错误日志"""
    try:
        _get_internal_logger().critical(message, *args, **kwargs)
    except Exception as e:
        print(f"日志记录失败: {e}")


def _exception(message: str, *args, **kwargs):
    """内部异常日志"""
    try:
        _get_internal_logger().exception(message, *args, **kwargs)
    except Exception as e:
        print(f"日志记录失败: {e}")


# ============================================================================
# 公开用户接口 - 功能完整
# ============================================================================

def get_logger(log_dir: Optional[str] = None, 
               log_filename: Optional[str] = None,
               log_level: Union[int, str] = logging.INFO,
               max_file_size: int = 10 * 1024 * 1024,
               backup_count: int = 5,
               console_output: bool = True,
               file_output: bool = True) -> Logger:
    """
    获取日志器实例（用户接口）
    
    Args:
        log_dir: 日志文件目录
        log_filename: 日志文件名
        log_level: 日志级别
        max_file_size: 单个日志文件最大大小
        backup_count: 保留的备份文件数量
        console_output: 是否输出到控制台
        file_output: 是否输出到文件
        
    Returns:
        Logger: 日志器实例
    """
    return Logger(
        log_dir=log_dir,
        log_filename=log_filename,
        log_level=log_level,
        max_file_size=max_file_size,
        backup_count=backup_count,
        console_output=console_output,
        file_output=file_output
    )


def setup_logging(log_dir: Optional[str] = None, 
                  log_filename: Optional[str] = None,
                  log_level: Union[int, str] = logging.INFO,
                  max_file_size: int = 10 * 1024 * 1024,
                  backup_count: int = 5,
                  console_output: bool = True,
                  file_output: bool = True):
    """
    设置全局日志配置（用户接口）
    
    Args:
        log_dir: 日志文件目录
        log_filename: 日志文件名
        log_level: 日志级别
        max_file_size: 单个日志文件最大大小
        backup_count: 保留的备份文件数量
        console_output: 是否输出到控制台
        file_output: 是否输出到文件
    """
    _logger_manager.configure(
        log_dir=log_dir,
        log_filename=log_filename,
        log_level=log_level,
        max_file_size=max_file_size,
        backup_count=backup_count,
        console_output=console_output,
        file_output=file_output
    )


def configure_logging(**kwargs):
    """
    配置日志系统（高级用户接口）
    
    Args:
        **kwargs: 配置参数
    """
    _logger_manager.configure(**kwargs)


def get_logging_config() -> Dict[str, Any]:
    """
    获取当前日志配置（用户接口）
    
    Returns:
        Dict[str, Any]: 当前配置
    """
    return _logger_manager.get_config()


def get_log_file_path() -> Optional[str]:
    """
    获取当前日志文件路径（用户接口）
    
    Returns:
        Optional[str]: 日志文件路径
    """
    return _logger_manager.get_log_file_path()


# ============================================================================
# 快捷函数 - 用户接口
# ============================================================================

def debug(message: str, *args, **kwargs):
    """快捷调试日志"""
    try:
        get_logger().debug(message, *args, **kwargs)
    except Exception as e:
        print(f"日志记录失败: {e}")


def info(message: str, *args, **kwargs):
    """快捷信息日志"""
    try:
        get_logger().info(message, *args, **kwargs)
    except Exception as e:
        print(f"日志记录失败: {e}")


def warning(message: str, *args, **kwargs):
    """快捷警告日志"""
    try:
        get_logger().warning(message, *args, **kwargs)
    except Exception as e:
        print(f"日志记录失败: {e}")


def error(message: str, *args, **kwargs):
    """快捷错误日志"""
    try:
        get_logger().error(message, *args, **kwargs)
    except Exception as e:
        print(f"日志记录失败: {e}")


def critical(message: str, *args, **kwargs):
    """快捷严重错误日志"""
    try:
        get_logger().critical(message, *args, **kwargs)
    except Exception as e:
        print(f"日志记录失败: {e}")


def exception(message: str, *args, **kwargs):
    """快捷异常日志"""
    try:
        get_logger().exception(message, *args, **kwargs)
    except Exception as e:
        print(f"日志记录失败: {e}")


if __name__ == "__main__":
    # 测试代码
    print("=== 测试日志模块 ===")
    
    # 测试内部接口
    print("\n1. 测试内部接口:")
    _info("内部信息日志")
    _error("内部错误日志")
    
    # 测试用户接口
    print("\n2. 测试用户接口:")
    logger = get_logger(
        log_dir="./test_logs",
        log_filename="test.log",
        log_level=logging.DEBUG
    )
    
    logger.debug("用户调试信息")
    logger.info("用户信息")
    logger.warning("用户警告")
    logger.error("用户错误")
    
    # 测试快捷函数
    print("\n3. 测试快捷函数:")
    info("快捷函数信息")
    error("快捷函数错误")
    
    # 测试配置功能
    print("\n4. 测试配置功能:")
    config = get_logging_config()
    print(f"当前配置: {config}")
    
    log_path = get_log_file_path()
    print(f"日志文件路径: {log_path}")
    
    print("\n=== 测试完成 ===")