# 存放各种自定义异常


class ConfigReadError(Exception):
    """配置文件读取错误异常"""

    def __init__(self, message: str, file_path: str):
        self.message = message
        self.file_path = file_path
        super().__init__(self._format_message())

    def _format_message(self) -> str:
        return f"{self.message} (file_path: {self.file_path})"

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.__module__ = "builtins"


class FileNotFoundError(ConfigReadError):
    pass


class TOMLReadError(ConfigReadError):
    pass


class ENVReadError(ConfigReadError):
    pass

class EnvVarError(Exception):
    """环境变量错误异常"""

    def __init__(self, message: str, env_key: str):
        self.message = message
        self.env_key = env_key
        super().__init__(self._format_message())

    def _format_message(self) -> str:
        return f"{self.message} (env_key: {self.env_key})"

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.__module__ = "builtins"

class EnvVarNotFoundError(EnvVarError):
    pass
