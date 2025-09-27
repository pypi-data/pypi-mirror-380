"""
LingHu - 智能化工具包
"""

from .utils.logger import (
    get_logger, 
    setup_logging, 
    configure_logging,
    get_logging_config,
    get_log_file_path,
    debug, 
    info, 
    warning, 
    error, 
    critical, 
    exception
)
from .utils.base import Base
from .modules.login import Login, 登录模块
__version__ = "1.0.0"
__author__ = "LingHu Team"

