from collections.abc import Container as _Container
from time import sleep as _sleep
from typing import Any as _Any, List as _List
from warnings import warn as _warn
__doc__ = """
    字节跳动系列 / ByteDance Series
    支持字符串、容器 / Supports strings and containers
    你甚至还可以设置延迟是毫秒还是秒 / You can even set the delay to milliseconds or seconds
    字节跳动，也就是类似打字机的效果 / ByteDance, which is similar to a typewriter
    """
__all__ = (
    "str_byte_dance",
    "bd",
    "sbd",
    "container_byte_dance",
    "cbd"
)
__version__ = "1.2.0"

def str_byte_dance(content: _Any, speed: int|float = 30, /, ms_mode: bool = True) -> None:
    """
    :note: 别看我只是一个简简单单的STR类型，实际我支持所有 / Don't be fooled by the simple STR type - I actually support all types
    :param Any content: 内容，建议为str类型 / Content, str type is recommended
    :param int|float speed: 打印速度，默认30 / Printing speed, default 30
    :param bool ms_mode: 是否设置为毫秒模式，默认True / Whether to set millisecond mode, default True
    :note: 参数均为位置参数，除了ms_mode，ms_mode关闭时建议同时修改speed / All parameters are positional except ms_mode; it's recommended to modify speed when ms_mode is disabled
    :return: None: 仅限打印内容 / Only for printing content
    :raises TypeError: speed强制，必须为int或float类型，否则报错 / speed is mandatory, must be int or float type, otherwise an error is raised
    :raises ValueError: speed必须≥0，否则报错 / speed must be ≥ 0, otherwise an error is raised
    :warning: speed不能为0，否则警告提醒你 / speed cannot be 0, otherwise a warning is issued
    :warning: ms_mode为布尔值，建议传入bool类型 / ms_mode should be a boolean value, it's recommended to pass bool type
    """
    if not isinstance(speed, (int, float)):
        raise TypeError(f"不合适的参数类型：{type(speed).__name__}\n请确保它的参数类型为：int 或 float\nInappropriate parameter type: {type(speed).__name__}\nPlease ensure it is int or float type")
    if speed < 0:
        raise ValueError(f"不合适的范围：{speed}，你必须得确保它大于等于0以上\nInappropriate range: {speed}\nPlease ensure it is greater than or equal to 0")
    if speed == 0:
        _warn("speed数值为0时你干脆直接使用print算了！\nWhen speed is 0, you might as well use print directly!", UserWarning, stacklevel=2)
    if not isinstance(ms_mode, bool):
        _warn(f"ms_mode建议为布尔值，不然可能偏离预想，结果你的输入却是{type(ms_mode).__name__}类型\nms_mode is recommended to be boolean, otherwise results may deviate from expectations. Your input is {type(ms_mode).__name__} type", UserWarning, stacklevel=2)
        ms_mode = bool(ms_mode)
    content = str(content)
    if ms_mode:
        speed /= 1000
    for i in content:
        print(end = i, flush = True)
        _sleep(speed)
    print()

def bd(c: _Any, s: int|float = 30, /, m: bool = True) -> None:
    """
    :note: 这是一个名称简化的str_byte_dance函数 / This is a simplified-named version of str_byte_dance
    :param Any c: 简化版content / Simplified content
    :param int|float s: 简化版speed，默认为30 / Simplified speed, default 30
    :param bool m: 简化版ms_mode，默认为True / Simplified ms_mode, default True
    :note: 具体内容请看被简化的函数 / For details, refer to the original function
    :return: None: 与原函数机制一致 / Consistent with the original function mechanism
    :raises TypeError: 与原函数机制一致 / Consistent with the original function mechanism
    :raises ValueError: 与原函数机制一致 / Consistent with the original function mechanism
    :warning: 与原函数机制一致 / Consistent with the original function mechanism
    """
    str_byte_dance(c, s, m)

def sbd(c: _Any, s: int|float = 30, /, m: bool = True) -> None:
    """
    :note: 这是一个名称简化的str_byte_dance函数 / This is a simplified-named version of str_byte_dance
    :param Any c: 简化版content / Simplified content
    :param int|float s: 简化版speed，默认为30 / Simplified speed, default 30
    :param bool m: 简化版ms_mode，默认True / Simplified ms_mode, default True
    :note: 具体内容请看被简化的函数 / For details, refer to the original function
    :return: None: 与原函数机制一致 / Consistent with the original function mechanism
    :raises TypeError: 与原函数机制一致 / Consistent with the original function mechanism
    :raises ValueError: 与原函数机制一致 / Consistent with the original function mechanism
    :warning: 与原函数机制一致 / Consistent with the original function mechanism
    """
    bd(c, s)

def container_byte_dance(content: _Container[_Any], speed: int|float = 30, /, ms_mode: bool = True) -> None:
    """
    :note: 这是一个容器迭代方式，通过遍历来打印 / This is a container iteration method, printing through traversal
    :param AnyConNstr content: 一个容器，比如list, tuple（str不建议） / A container, e.g., list, tuple (str is not recommended)
    :param int|float speed: 打印速度，默认为30 / Printing speed, default 30
    :param bool ms_mode: 是否设置为毫秒模式，默认True / Whether to set millisecond mode, default True
    :note: 参数均为位置参数，除了ms_mode，ms_mode关闭时建议同时修改speed / All parameters are positional except ms_mode; it's recommended to modify speed when ms_mode is disabled
    :return: None: 仅限打印内容 / Only for printing content
    :raises TypeError: speed强制，必须为int或float类型，否则报错 / speed is mandatory, must be int or float type, otherwise an error is raised
    :raises TypeError: 强制内容content，必须可迭代，否则报错 / content must be iterable, otherwise an error is raised
    :raises ValueError: speed必须≥0，否则报错 / speed must be ≥ 0, otherwise an error is raised
    :warning: speed不能为0，否则警告提醒你 / speed cannot be 0, otherwise a warning is issued
    :warning: 如果content为Str类型，则发个警告 / If content is str type, a warning is issued
    :warning: ms_mode为布尔值，建议传入bool类型 / ms_mode should be a boolean value, it's recommended to pass bool type
    :note: 处理dict类型时，会先打印key，再打印value / When processing dict type, keys are printed first, then values
    """
    if not isinstance(speed, (int, float)):
        raise TypeError(f"不合适的参数类型：{type(speed).__name__}\n请确保它的参数类型为：int 或 float\nInappropriate parameter type: {type(speed).__name__}\nPlease ensure it is int or float type")
    if speed < 0:
        raise ValueError(f"不合适的范围：{speed}，你必须确保它大于等于0以上\nInappropriate range: {speed}\nPlease ensure it is greater than or equal to 0")
    if speed == 0:
        _warn("数值为0时，你干脆直接使用print算了！\nWhen speed is 0, you might as well use print directly!", UserWarning, stacklevel=2)
    if isinstance(content, str):
        _warn("这里是容器玩的地方，不是Str能来的地方\nThis is for containers, not str type!", UserWarning, stacklevel=2)
    if isinstance(content, dict):
        d: _List[_Any] = []
        e: _List[_Any] = []
        for a, b in content.items():
            d.append(a)
            e.append(b)
        content = d + e
    if not isinstance(ms_mode, bool):
        _warn(f"ms_mode建议为布尔值，不然可能偏离预想，结果你的输入却是{type(ms_mode).__name__}类型\nms_mode is recommended to be boolean, otherwise results may deviate from expectations. Your input is {type(ms_mode).__name__} type", UserWarning, stacklevel=2)
        ms_mode = bool(ms_mode)
    if ms_mode:
        speed /= 1000
    try:
        for i in content:  # type: ignore[attr-defined]
            print(end = i, flush = True)
            _sleep(speed)
        print()
    except TypeError:
        raise TypeError(f"你这迭代对象可真特别呢：{type(content).__name__}\nThis iterable object is quite special: {type(content).__name__}")

def cbd(c: _Container[_Any], s: int|float = 30, /, m: bool = True) -> None:
    """
    :note: 这是一个名称简化的container_byte_dance函数 / This is a simplified-named version of container_byte_dance
    :param Any c: 简化版content / Simplified content
    :param int|float s: 简化版speed，默认为30 / Simplified speed, default 30
    :param bool m: 简化版ms_mode，默认为True / Simplified ms_mode, default True
    :note: 具体内容请看被简化的函数 / For details, refer to the original function
    :return: None: 与原函数机制一致 / Consistent with the original function mechanism
    :raises TypeError: 与原函数机制一致 / Consistent with the original function mechanism
    :raises ValueError: 与原函数机制一致 / Consistent with the original function mechanism
    :warning: 与原函数机制一致 / Consistent with the original function mechanism
    """
    container_byte_dance(c, s, ms_mode = m)

__init__ = bd
