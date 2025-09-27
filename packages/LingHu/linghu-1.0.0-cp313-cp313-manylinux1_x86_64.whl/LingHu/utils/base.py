
from LingHu.utils.logger import _info, _error, _debug


class Base:
    """
    操作结果处理的基础类
    
    该类提供了一个通用的框架，用于处理各种操作的结果和状态。作为其他功能类的基类，
    它定义了统一的操作结果处理模式，包括返回值存储、状态判断和结果描述。
    
    主要功能：
    - 统一管理操作返回值（ret属性）
    - 提供操作成功/失败状态判断（bool属性）
    - 生成操作结果的文本描述（text属性）
    - 提供通用的结果处理方法（user_login、execute_function、drive_device等）
    
    核心属性：
        ret (Any): 存储操作返回值，可以是None、整数、字符串等类型
        bool (bool): 操作状态标志，True表示成功，False表示失败
        text (str): 操作结果描述信息，会根据操作结果动态更新
    
    使用方法：
        1. 继承Base类创建具体的功能类
        2. 在子类中实现具体的操作逻辑
        3. 调用相应的结果处理方法（如user_login、execute_function等）
        4. 通过value()方法获取返回值，通过bool和text属性获取状态和描述
    
    示例：
        class MyOperation(Base):
            def perform_operation(self):
                # 执行具体操作
                self.ret = some_function()
                self.user_login()  # 处理登录结果
                
        op = MyOperation()
        op.perform_operation()
        print(op.value())    # 获取返回值
        print(op.bool)       # 获取状态
        print(op.text)       # 获取描述
    """
    def __init__(self):
        """
        初始化Base类的实例属性
        
        该方法为Base类实例设置初始状态，初始化三个核心属性：
        - ret: 用于存储操作返回值
        - bool: 用于表示操作是否成功
        - text: 用于存储操作结果的描述信息
        
        这些属性会在后续的操作方法（如user_login、execute_function、drive_device等）
        中被更新，用于记录操作的状态和结果信息。
        
        Attributes:
            ret (Any): 操作返回值，初始为None，在操作执行后被设置为具体的返回结果
            bool (bool): 操作状态标志，初始为False，成功时设为True，失败时保持False
            text (str): 操作结果描述，初始为空字符串，操作后会添加成功/失败信息
        """
        self.ret = None
        self.bool = False
        self.text = ""
    def value(self):
        """
        获取操作返回值
        
        返回当前操作的结果值，该值通常由具体的操作方法（如user_login、execute_function等）设置。
        可能是整数、字符串或其他类型，取决于具体的操作结果。
        
        Returns:
            Any: 操作的返回值，可能是None、整数、字符串等类型
        """
        return self.ret
#     current_function_name = sys._getframe().f_code.co_name



    def user_login(self):
        """
        处理用户登录操作的结果
        
        该方法用于分析和处理用户登录操作的返回结果，根据返回值的类型和数值
        来判断登录是否成功，并更新相应的状态标志和描述信息。
        
        处理逻辑：
        1. None值处理：当ret为None时，表示登录未执行或出现异常，标记为失败
        2. 整数处理：当ret为整数时，>=0表示登录成功，<0表示登录失败
        3. 其他类型：对于非None且非整数的返回值，统一标记为失败
        
        该方法会更新以下实例属性：
        - self.bool: 登录状态，成功为True，失败为False
        - self.text: 登录结果描述，会追加"成功"或"失败"信息
        
        同时会根据结果类型调用相应的日志记录函数：
        - 成功时调用_info()记录信息日志
        - 失败时调用_error()记录错误日志
        - 始终调用_debug()记录调试信息
        
        Note:
            调用此方法前，需要确保self.ret已被设置为登录操作的返回值。
            该方法通常在具体的登录操作执行后调用。
            
        Example:
            login_op = Login()
            login_op.ret = login_function(username, password)  # 执行登录
            login_op.user_login()  # 处理登录结果
            if login_op.bool:
                print("登录成功:", login_op.text)
            else:
                print("登录失败:", login_op.text)
        """
        # 明确处理 None 值
        if self.ret is None:
            self.bool = False
            self.text += "失败"
            _error(self.text)
            _debug("返回值"+ str(self.ret))


        elif isinstance(self.ret, int):
            # 处理数值类型
            if self.ret >= 0:
                self.bool = True
                self.text += "成功"
                _info(self.text)
                _debug("返回值"+ str(self.ret))
            else:
                self.bool = False
                self.text += "失败"                
                _error(self.text)
                _debug("返回值"+ str(self.ret))

        else:
            # 处理其他类型
            self.bool = False
            self.text += "失败: 未知返回值"
            _error(self.text)
            _debug("返回值"+ str(self.ret))

    def execute_function(self):
        """
        处理函数执行操作的结果
        
        该方法用于分析和处理函数执行操作的返回结果，根据返回值的类型和数值
        来判断函数执行是否成功，并更新相应的状态标志和描述信息。
        
        处理逻辑：
        1. None值处理：当ret为None时，表示函数未执行或出现异常，标记为失败
        2. 整数处理：当ret为整数时，>0表示函数执行成功，<=0表示执行失败
        3. 字符串处理：当ret为字符串时，非空字符串表示成功，空字符串表示失败
        4. 其他类型：对于None、整数、字符串之外的其他类型，统一标记为失败
        
        该方法会更新以下实例属性：
        - self.bool: 函数执行状态，成功为True，失败为False
        - self.text: 函数执行结果描述，会追加"成功"或"失败"信息
        
        同时会根据结果类型调用相应的日志记录函数：
        - 成功时调用_info()记录信息日志
        - 失败时调用_error()记录错误日志
        - 始终调用_debug()记录调试信息
        
        Note:
            调用此方法前，需要确保self.ret已被设置为函数执行的返回值。
            该方法通常在具体的函数操作执行后调用。
            
        Example:
            func_op = Base()
            func_op.ret = some_function()  # 执行函数
            func_op.execute_function()  # 处理函数执行结果
            if func_op.bool:
                print("函数执行成功:", func_op.text)
            else:
                print("函数执行失败:", func_op.text)
        """
        # 明确处理 None 值
        if self.ret is None:
            self.bool = False
            self.text += "失败"
            _error(self.text)
            _debug("返回值"+ str(self.ret))


        elif isinstance(self.ret, int):
            # 处理数值类型
            if self.ret > 0:
                self.bool = True
                self.text += "成功"
                _info(self.text)
                _debug("返回值"+ str(self.ret))
            else:
                self.bool = False
                self.text += "失败"
                _error(self.text)
                _debug("返回值"+ str(self.ret)) 
        
        elif isinstance(self.ret, str):
            # 单独处理字符串类型
            if self.ret.strip():  # 检查字符串是否非空
                self.bool = True
                self.text += "成功: " + self.ret
                _info(self.text) 
                _debug("返回值"+ str(self.ret)) 
            else:
                self.bool = False
                self.text += "失败: 空字符串"
                _error(self.text)   
                _debug("返回值"+ str(self.ret)) 
        
        else:
            # 处理其他类型
            self.bool = False
            self.text += "失败: 未知返回值"
            _error(self.text)   
            _debug("返回值"+ str(self.ret)) 

    def drive_device(self):
        """
        处理设备驱动操作的结果
        
        该方法用于分析和处理设备驱动操作的返回结果，根据返回值的类型和数值
        来判断设备操作是否成功，并更新相应的状态标志和描述信息。
        
        处理逻辑：
        1. None值处理：当ret为None时，表示设备操作未执行或出现异常，标记为失败
        2. 整数处理：当ret为整数时，>=0或==-1068表示设备操作成功，其他数值表示失败
           （-1068是一个特殊的成功状态码，可能表示特定的设备操作状态）
        3. 字符串处理：当ret为字符串时，非空字符串表示设备操作成功，空字符串表示失败
        4. 其他类型：对于None、整数、字符串之外的其他类型，统一标记为失败
        
        该方法会更新以下实例属性：
        - self.bool: 设备操作状态，成功为True，失败为False
        - self.text: 设备操作结果描述，会追加"成功"或"失败"信息
        
        同时会根据结果类型调用相应的日志记录函数：
        - 成功时调用_info()记录信息日志
        - 失败时调用_error()记录错误日志
        - 始终调用_debug()记录调试信息
        
        Note:
            调用此方法前，需要确保self.ret已被设置为设备操作的返回值。
            该方法通常在具体的设备操作执行后调用。
            特殊状态码-1068被识别为成功状态，这可能是设备驱动特定的返回码。
            
        Example:
            device_op = Base()
            device_op.ret = drive_device_function()  # 执行设备驱动操作
            device_op.drive_device()  # 处理设备操作结果
            if device_op.bool:
                print("设备操作成功:", device_op.text)
            else:
                print("设备操作失败:", device_op.text)
        """
        # 明确处理 None 值
        if self.ret is None:
            self.bool = False
            self.text += "失败"
            _error(self.text)   
            _debug("返回值"+ str(self.ret)) 


        elif isinstance(self.ret, int):
            # 处理数值类型
            if self.ret >= 0 or self.ret == -1068:
                self.bool = True
                self.text += "成功"
                _info(self.text) 
                _debug("返回值"+ str(self.ret)) 
            else:
                self.bool = False
                self.text += "失败"
                _error(self.text)   
                _debug("返回值"+ str(self.ret)) 
        
        elif isinstance(self.ret, str):
            # 单独处理字符串类型
            if self.ret.strip():  # 检查字符串是否非空
                self.bool = True
                self.text += "成功: " + self.ret
                _info(self.text)   
                _debug("返回值"+ str(self.ret)) 
            else:
                self.bool = False
                self.text += "失败: 空字符串"
                _error(self.text)   
                _debug("返回值"+ str(self.ret)) 
        
        else:
            # 处理其他类型
            self.bool = False
            self.text += "失败: 未知返回值"
            _error(self.text)
            _debug("返回值"+ str(self.ret))