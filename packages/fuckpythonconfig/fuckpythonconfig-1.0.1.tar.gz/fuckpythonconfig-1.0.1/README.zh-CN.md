# fuckPythonConfig

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE) [![Python >= 3.11](https://img.shields.io/badge/Python-%3E%3D3.11-3776AB?logo=python&logoColor=white)](#安装) [![Ruff](https://img.shields.io/badge/Lint-Ruff-46A3FF)](https://docs.astral.sh/ruff/)

[English](./README.md) | 简体中文

一个“零样板”的 Python 配置加载器：在你的脚本同级目录自动查找 TOML 配置文件与 .env 文件，支持使用 ${VAR} 与 ${VAR:default} 占位符从环境变量填充配置，递归解析 dict/list，基于 python-dotenv 实现稳定的 .env 行为。

> 目标：在小到中等规模的脚本/服务里，用一行 `load_config()` 即拿到可用配置，而不用再写一堆路径拼接与环境变量处理逻辑。

## 特性

- 自动发现：无需传参，默认在“调用脚本所在目录”查找第一个 .toml 与 .env 文件
- 占位符解析：
  - ${VAR} 直接取环境变量
  - ${VAR:default} 环境变量缺失时使用默认值
  - 递归解析 dict/list，保持结构不变
- 与 .env 兼容：由 python-dotenv 提供解析/合并/覆盖等成熟行为
- 明确的错误：
  - 缺失文件：FileNotFoundError（自定义，信息更友好）
  - 解析失败：TOMLReadError
  - 环境变量缺失：EnvVarNotFoundError（当无默认值时抛出）
- 纯标准库 + 小依赖：仅依赖 python-dotenv

## 安装

环境要求：Python >= 3.11

- 使用 pip

```cmd
pip install fuckpythonconfig
```

- 使用 uv（可选）

```cmd
uv add fuckpythonconfig
```

- 从源码安装

```cmd
pip install git+https://github.com/JGG0sbp66/fuckPythonConfig.git@dev
```

## 快速上手

目录结构（示例）：

```text
your-project/
  app.py           # 你的脚本（调用 load_config()）
  config.toml      # 配置文件
  .env             # 环境变量（开发环境）
```

config.toml：

```toml
[database]
host = "127.0.0.1"
port = 5432
username = "${DB_USER:postgres}"
password = "${DB_PASS}"  # 无默认值，未设置时将抛出 EnvVarNotFoundError
```

.env：

```dotenv
DB_USER=local_user
DB_PASS=secret123
```

app.py：

```python
from fuckpythonconfig import load_config

cfg = load_config()  # 不传参时，自动在 app.py 同级目录查找 .toml 与 .env
print(cfg["database"]["username"])  # => "local_user"
```

显式传参（可选）：

```python
from fuckpythonconfig import load_config

cfg = load_config(
    file_path="./config.toml",   # 指定 TOML 路径
    dotenv_path="./.env",        # 指定 .env 路径
    verbose=True,                 # 透传给 python-dotenv，打印更多加载信息
    override=False,               # 是否覆盖已有环境变量
    interpolate=True,             # 是否允许 .env 中的变量插值
)
```

## 占位符与解析规则

- 语法：
  - ${VAR} → 使用环境变量 VAR 的值
  - ${VAR:default} → 当 VAR 未设置时使用 default 字面量
- 作用域：递归应用于 dict 和 list 中的所有字符串值
- 匹配方式：仅当值“完全等于”占位符格式时才会替换
  - 即 "${VAR}" 可替换；而 "prefix ${VAR}" 或 "${VAR} suffix" 不会替换（当前版本的限制）
- 类型：
  - 被替换的值为字符串（来自环境变量或默认值）
  - 其它非占位符的 TOML 值类型保持不变（int、bool、array 等）
- 未找到变量：若无默认值，抛出 EnvVarNotFoundError

## API 参考

### load_config(

file_path: str | None = None,
dotenv_path: str | None = None,
stream: IO[str] | None = None,
verbose: bool = False,
override: bool = False,
interpolate: bool = True,
encoding: str | None = "utf-8",
) -> dict

作用：

- 读取 TOML → 加载 .env → 递归解析占位符 → 返回合并后的配置 dict

行为细节：

- 未显式传参时，会在“调用者脚本所在目录”中查找第一个 .toml 与 .env 文件
- .env 加载由 python-dotenv 完成，上述参数透传对应能力

可能抛出的异常：

- FileNotFoundError（找不到 .toml/.env 或目录）
- TOMLReadError（TOML 语法或读取失败）
- EnvVarNotFoundError（占位符对应的环境变量缺失且未提供默认值）

## 常见问题与限制

- 仅替换“完全由占位符构成”的字符串，暂不支持在长字符串中进行部分替换
- 当目录下存在多个 .toml/.env 时，load_config 会使用发现列表中的第一个（与文件系统枚举顺序相关）
- Python 版本要求：>= 3.11（因内置 tomllib 从 3.11 起提供）

## 开发与贡献

本仓库使用 Ruff 做格式与静态检查

建议使用 uv（或 venv）创建虚拟环境并安装依赖：

```cmd
uv sync
```

欢迎提交 Issue/PR 改进占位符能力（如局部替换、类型转换、跨文件引用等）。

## 致谢

- python-dotenv 提供了强大稳定的 .env 加载能力

## 许可

MIT License，详见仓库根目录的 `LICENSE` 文件。
