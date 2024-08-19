import subprocess
import pyperclip
import tkinter as tk

def get_disk_serial():
    cmd = ["wmic", "diskdrive", "get", "SerialNumber"]
    output = subprocess.check_output(cmd, shell=True).decode().split('\n')[1].strip()
    return output

def copy_to_clipboard():
    serial_number = get_disk_serial()
    pyperclip.copy(serial_number)
    print("复制成功！你的 HWID 是", serial_number)

# 创建 GUI 窗口
window = tk.Tk()
window.title("HWID 获取工具")

# 添加标签
label = tk.Label(window, text="点击按钮获取磁盘序列号并复制到剪贴板")
label.pack()

# 添加按钮
button = tk.Button(window, text="获取 HWID", command=copy_to_clipboard)
button.pack()

# 运行 GUI
window.mainloop()
