# utilities - Windows-OS specific utilities

"""
Module provides various routines to deal with application windows.
NOTE: Windows platform only


Example / doctest:
```
>>> import utils_mystuff_windows
>>> print(find_window_ctypes("Excel"))
>>> print(find_window_win32gui("Excel"))
>>> print(find_window_ctypes("Access"))
>>> print(find_window_win32gui("Access"))

```
"""


# ruff and mypy per file settings
#
# empty lines
# ruff: noqa: E302, E303
# naming conventions
# ruff: noqa: N801, N802, N803, N806, N812, N813, N815, N816, N818, N999
# others
# ruff: noqa: E501, F403, F405, F841, S605
#
# disable mypy errors
# mypy: disable-error-code = name-defined

# fmt: off



from typing import Any

import os
from ctypes import *
import win32gui

import time



# find windows from title

# variant using ctypes
# http://makble.com/how-to-find-window-with-wildcard-in-python-and-win32gui
def find_window_ctypes(title: str) -> Any:
    """
    find_window_ctypes - find windows from title, variant using ctypes

    Args:
        title (str): window title

    Returns:
        Union[str, bool]: title if found, False otherwise
    """

    titles = []

    def foreach_window_gettitle(hwnd, lParam):
        if windll.user32.IsWindowVisible(hwnd):
            length = windll.user32.GetWindowTextLengthW(hwnd)
            classname = create_unicode_buffer(100 + 1)
            windll.user32.GetClassNameW(hwnd, classname, 100 + 1)
            buff = create_unicode_buffer(length + 1)
            windll.user32.GetWindowTextW(hwnd, buff, length + 1)
            titles.append((hwnd, buff.value.encode(), classname.value, windll.user32.IsIconic(hwnd)))
        return True

    def refresh_wins() -> Any:
        titles: list[str] = []
        windll.user32.EnumWindows(WINFUNCTYPE(c_bool, c_int, POINTER(c_int))(foreach_window_gettitle), 0)

    refresh_wins()
    for item in titles:
        if title in str(item[1]):
            return item[0]

    return False

# variant using win32gui
def find_window_win32gui(title: str) -> Any:
    """
    find_window_ctypes - find windows from title, variant using win32gui

    Args:
        title (str): window title

    Returns:
        Union[str, bool]: title if found, False otherwise
    """

    titles = []

    def foreach_window_gettitle(hwnd, lParam):
        if win32gui.IsWindowVisible(hwnd):
            classname = win32gui.GetClassName(hwnd)
            title = win32gui.GetWindowText(hwnd)
            titles.append((hwnd, title, classname, win32gui.IsIconic(hwnd)))
        return True

    def refresh_wins():
        titles = []
        win32gui.EnumWindows(foreach_window_gettitle, 0)

    refresh_wins()
    for item in titles:
        if title in str(item[1]):
            return item[0]

    return False


# close window / application depending on title

WM_CLOSE = 0x0010

# variant using ctypes
def close_app_windowtitle_ctypes(title: str) -> None:
    """
    close_app_windowtitle_ctypes - close window / application depending on title, variant using ctypes

    Args:
        title (str): window title
    """

    hwnd = find_window_ctypes(title)
    if hwnd:
        windll.user32.SendMessageA(hwnd, WM_CLOSE, 0, 0)
        time.sleep(0.1)

# variant using win32gui
def close_app_windowtitle_win32gui(title: str) -> None:
    """
    close_app_windowtitle_win32gui - close window / application depending on title, variant using win32gui

    Args:
        title (str): window title
    """

    hwnd = find_window_win32gui(title)
    if hwnd:
        win32gui.SendMessage(hwnd, WM_CLOSE, 0, 0)
        time.sleep(0.1)

# variant using taskkill
# https://stackoverflow.com/questions/52203803/wildcard-in-taskkill-windowtitle
# note:
# - execution is pretty slow
# - watch out % vs %% in direct entry vs cmd-files
def close_app_windowtitle_taskkill(title: str) -> None:
    """
    close_app_windowtitle_taskkill - close window / application depending on title, variant using taskkill

    Args:
        title (str): window title
    """

    # os.system("taskkill /F /FI 'WINDOWTITLE eq {title}*'")   # wildcard not allowed at beginning of title
    os.system(f"for /f \"tokens=2 delims=,\" %a in ('tasklist /v /fo:csv /nh ^| findstr /r \"{title}\"') do taskkill /pid %a")
    time.sleep(0.1)

# callpoint
def close_app_windowtitle(title: str) -> None:
    """
    close_app_windowtitle - close window / application depending on title

    Args:
        title (str): window title
    """
    close_app_windowtitle_win32gui(title)


# wait for open window (overcome delay in asynchronuous processing subprocess.Popen)

# variant using ctypes
def wait_for_window_ctypes(title: str, timeout: int = 5, wait: float = 0.25) -> None:
    """
    wait_for_window_ctypes - wait for close window (overcome delay in asynchronous processing subprocess.Popen)

    Args:
        title (str): _description_
        timeout (int, optional): timeout time. Defaults to 5.
        wait (float, optional): wait time. Defaults to 0.25.
    """
    starttime = time.time()
    while time.time() < starttime + timeout:
        hwnd = find_window_ctypes(title)
        if hwnd:
            return
        else:
            time.sleep(wait)
    return

# variant using win32gui
def wait_for_window_win32gui(title: str, timeout: int = 5, wait: float = 0.25) -> None:
    """
    wait_for_window_win32gui - wait for close window (overcome delay in asynchronous processing subprocess.Popen)

    Args:
        title (str): _description_
        timeout (int, optional): timeout time. Defaults to 5.
        wait (float, optional): wait time. Defaults to 0.25.
    """

    starttime = time.time()
    while time.time() < starttime + timeout:
        hwnd = find_window_win32gui(title)
        if hwnd:
            return
        else:
            time.sleep(wait)
    return

# callpoint
def wait_for_window(title: str, timeout: int = 5, wait: float = 0.25) -> None:
    """
    wait_for_window - wait for close window (overcome delay in asynchronous processing subprocess.Popen)

    Args:
        title (str): _description_
        timeout (int, optional): timeout time. Defaults to 5.
        wait (float, optional): wait time. Defaults to 0.25.
    """
    wait_for_window_win32gui(title, timeout, wait)
