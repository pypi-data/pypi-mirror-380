import inspect
from pathlib import Path
from typing import IO

from dotenv import load_dotenv

from .utils import find_env_path, find_toml_path, read_toml, resolve_config


def load_config(
    file_path: str | None = None,
    dotenv_path: str | None = None,
    stream: IO[str] | None = None,
    verbose: bool = False,
    override: bool = False,
    interpolate: bool = True,
    encoding: str | None = "utf-8",
) -> dict:
    """读取配置文件"""

    # 1. 获取调用者脚本所在的目录
    caller_frame = inspect.stack()[1]
    caller_file = caller_frame.filename
    current_dir = Path(caller_file).parent

    # 2. 读取TOML配置文件
    file_path = file_path or find_toml_path(str(current_dir))[0]
    config = read_toml(file_path)

    # 3. 读取.env文件
    dotenv_path = dotenv_path or find_env_path(str(current_dir))[0]
    """感谢python-dotenv库实现了非常成熟且高级的读取env的方法, mua~"""
    load_dotenv(
        dotenv_path=dotenv_path,
        stream=stream,
        verbose=verbose,
        override=override,
        interpolate=interpolate,
        encoding=encoding,
    )

    # 4. 解析配置中的占位符
    config = resolve_config(config)

    return config
