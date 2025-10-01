# 存放各种读取工具
import os
import re
import tomllib
from typing import Any

from .exceptions import EnvVarNotFoundError, FileNotFoundError, TOMLReadError


def read_toml(file_path: str) -> dict:
    """使用tomllib读取TOML文件"""
    if not os.path.exists(file_path):
        raise FileNotFoundError("Can not find TOML file", file_path)
    try:
        with open(file_path, "rb") as f:
            return tomllib.load(f)
    except Exception as e:
        raise TOMLReadError("Failed to read TOML file", file_path) from e


def is_env_var(value: str, ENV_VAR_REGEX: str = r"\$\{([^}]*)\}") -> str | None:
    """使用正则表达式判断是否为${value}格式"""
    match = re.fullmatch(ENV_VAR_REGEX, value)
    if match:
        return match.group(1)
    return None


def get_env_var(env_key: str) -> str | None:
    """使用os读取环境变量"""
    return os.getenv(env_key, None)


def resolve_config(config: dict) -> dict:
    """递归解析配置中的占位符"""

    def _parse_env_spec(env_spec: str) -> tuple[str, str | None]:
        """解析环境变量规格: ${VAR:default} -> (VAR, default)"""
        content = env_spec.strip()
        if ':' in content:
            var_name, default_val = content.split(':', 1)
            return var_name.strip(), default_val.strip()
        return content, None

    def _resolve(value: Any) -> Any:
        if isinstance(value, str):
            env_key = is_env_var(value)
            if env_key:
                var_name, default_val = _parse_env_spec(env_key)
                env_value = get_env_var(var_name)

                # 如果环境变量不存在, 使用默认值
                if env_value is None:
                    if default_val is not None:
                        env_value = default_val
                    else:
                        raise EnvVarNotFoundError("Environment variable not found", var_name)

                return env_value
            return value

        elif isinstance(value, dict):
            return {k: _resolve(v) for k, v in value.items()}
        elif isinstance(value, list):
            return [_resolve(item) for item in value]
        else:
            return value

    return _resolve(config)


def find_toml_path(current_dir: str) -> list[str]:
    """查找当前目录下的toml文件, 返回toml路径列表"""
    if not os.path.exists(current_dir):
        raise FileNotFoundError("Directory not found", current_dir)

    if not os.path.isdir(current_dir):
        raise ValueError(f"Path is not a directory: {current_dir}")

    toml_files = []
    for file in os.listdir(current_dir):
        if file.endswith('.toml'):
            toml_files.append(os.path.join(current_dir, file))

    if toml_files == []:
        raise FileNotFoundError("No TOML file found in directory", current_dir)
    return toml_files


def find_env_path(current_dir: str) -> list[str]:
    """查找当前目录下的env文件, 返回env路径列表"""
    if not os.path.exists(current_dir):
        raise FileNotFoundError("Directory not found", current_dir)

    if not os.path.isdir(current_dir):
        raise ValueError(f"Path is not a directory: {current_dir}")

    env_files = []
    for file in os.listdir(current_dir):
        if file.endswith('.env'):
            env_files.append(os.path.join(current_dir, file))

    if env_files == []:
        raise FileNotFoundError("No .env file found in directory", current_dir)
    return env_files
