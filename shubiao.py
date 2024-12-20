

import pyautogui

# 模拟点击屏幕上的 (x, y) 坐标位置
pyautogui.click(x=500, y=500)


import pyautogui

# 获取当前鼠标位置
x, y = pyautogui.position()
print(f"当前鼠标位置: ({x}, {y})")


import pyautogui
import time

# 打开浏览器并最大化窗口，假设浏览器位于屏幕中心
# 模拟点击浏览器的刷新按钮位置（此位置为例，实际需要根据屏幕分辨率调整）
pyautogui.click(x=500, y=100)  # 假设刷新按钮的坐标是 (500, 100)

# 你也可以在点击之前让程序暂停一会，等待浏览器加载
time.sleep(2)  # 等待2秒


import pyautogui

# 模拟双击指定坐标位置
pyautogui.doubleClick(x=500, y=500)


import pyautogui
import time

# 模拟按下 F1 键
pyautogui.press('f1')  # 按 F1 键

# 等待 1 秒
time.sleep(1)

# 模拟按下 Ctrl+C（复制）
pyautogui.hotkey('ctrl', 'c')

# 等待 1 秒
time.sleep(1)

# 模拟按下 Ctrl+V（粘贴）
pyautogui.hotkey('ctrl', 'v')

