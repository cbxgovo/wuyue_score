import pyautogui
import time
import os
import logging

# 设定关键词
keywords = [
    "经济全球化", 
    "作用强劲动力", 
    "多边主义", 
    "合作共赢", 
    "国际关系民主化", 
    "人类命运共同体"
]

# 设置日志配置
log_file = "task_log.txt"
logging.basicConfig(level=logging.INFO,  # 设置日志级别为INFO
                    format='%(asctime)s - %(levelname)s - %(message)s', 
                    handlers=[logging.FileHandler(log_file, 'w', encoding='utf-8'),
                              logging.StreamHandler()])

# 读取文件内容
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        logging.error(f"文件 {file_path} 未找到。")
        return ""
    except Exception as e:
        logging.error(f"读取文件时发生错误: {e}")
        return ""

# 计算分数
def calculate_score(text):
    # 计算字符个数
    char_count = len(text)
    
    # 统计出现的关键词个数
    keyword_count = sum(1 for keyword in keywords if keyword in text)
    logging.info(f"关键词个数：{keyword_count}, 字符数：{char_count}")
    
    # 根据 keyword_count 和 char_count 判断 score
    if keyword_count == 0:
        if char_count <= 10:
            return 0
        elif 10 < char_count <= 50:
            return 1
        elif 50 < char_count <= 100:
            return 2
        elif 100 < char_count <= 250:
            return 3
        else:
            return 4

    elif 1 <= keyword_count <= 2:
        if char_count <= 150:
            return 3
        elif 150 < char_count <= 280:
            return 4
        else:
            return 5

    elif keyword_count == 3:
        if char_count <= 200:
            return 4
        elif 200 < char_count <= 250:
            return 5
        else:
            return 6

    elif keyword_count > 3:
        if char_count <= 200:
            return 5
        elif 200 < char_count <= 300:
            return 6
        else:
            return 7

def main():
    # 文件路径
    file_path = r'D:\d_downloads\Chrome_Download\image.txt'
    
    # 首先执行浏览器任务栏位置的点击一次
    pyautogui.click(x=708, y=1053)
    logging.info("执行浏览器任务栏位置的点击一次。")

    # 之后的任务在循环中执行3次
    for _ in range(400):
        logging.info("----------------起始----------------------")
        
        # 试题截屏位置
        pyautogui.click(x=866, y=639) 
        time.sleep(1)

        # 模拟按下 F1 键
        pyautogui.press('f1')  # 按 F1 键 Snipaste快捷键截屏

        # 模拟双击指定坐标位置 复制图片到剪切板
        pyautogui.doubleClick(x=866, y=639)
        time.sleep(1)

        # 浏览器任务栏位置
        pyautogui.click(x=399, y=18)  # 白描浏览器栏目
        time.sleep(1)
        pyautogui.click(x=866, y=639)  # 点击试题
        time.sleep(1)

        # 模拟按下 Ctrl+V（粘贴）
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        # 点击识别按钮
        pyautogui.click(x=379, y=440)  # 点击“识别”
        time.sleep(5)  # 等待OCR识别结果

        # 点击识别窗口
        pyautogui.click(x=348, y=378)  # 点击识别窗口
        time.sleep(1)

        # 点击导出txt按钮
        pyautogui.click(x=1682, y=990)  # 导出txt
        time.sleep(1)

        # 刷新
        pyautogui.click(x=89, y=61)  # 刷新
        time.sleep(2) 
        pyautogui.click(x=1030, y=190)  # 重新加载

        # 读取文件内容
        text = read_file(file_path)
        if text:
            logging.info(f"文件内容: {text}")
            
            # 计算分数
            score = calculate_score(text)
            logging.info(f"计算得到的分数为: {score}")
        else:
            logging.warning("没有读取到文件内容。")
            score = 3

        # 删除文件
        os.remove(file_path)
        logging.info(f"文件 {file_path} 已成功删除。")

        time.sleep(1)
        pyautogui.click(x=169, y=18)  # 第一个标签栏切换
        time.sleep(1)
        pyautogui.click(x=1746, y=464)  # 分数空
        time.sleep(1)

        # 调用函数模拟按键
        pyautogui.press(str(score))
        time.sleep(1)
        pyautogui.click(x=1711, y=506)  # 提交
        time.sleep(1)

        logging.info("--------------截至------------------------")

# 执行主程序
if __name__ == "__main__":
    main()
