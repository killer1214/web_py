import tkinter as tk
from widgets.input_widgets import LabeledEntry  # 导入新类
import configparser  # 导入配置解析器

class InputApp:
    def __init__(self, master):
        self.master = master
        self.master.title("版本修改demo")
        self.master.geometry("600x400")  # 设置窗口大小

        self.entries = []  # 存储 LabeledEntry 实例

        # 创建输入框和提交按钮的框架
        self.left_frame = tk.Frame(master)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10)  # 左侧框架

        # 添加初始的 LabeledEntry 示例
        self.add_labeled_entry("姓名:", "name")
        self.add_labeled_entry("年龄:", "age")
        self.add_labeled_entry("等级:", "level")

        # 创建显示框
        self.output_text = tk.Text(master, height=20, width=40)
        self.output_text.grid(row=0, column=1, padx=10, pady=10)  # 右侧显示框

        # 创建提交按钮
        self.submit_button = tk.Button(master, text="确认", command=self.submit_data)
        self.submit_button.grid(row=1, column=0, columnspan=2, pady=10)  # 按钮跨越两列，放在下方

    def add_labeled_entry(self, label_text, config_key):
        """添加一个新的 LabeledEntry 实例"""
        labeled_entry = LabeledEntry.create(self.left_frame, label_text)  # 使用新类创建输入框
        labeled_entry.config_key = config_key  # 将对应的配置键存储在实例中
        self.entries.append(labeled_entry)  # 将实例添加到列表中

    def submit_data(self):
        """处理用户输入的文本并显示在显示框中"""
        self.output_text.delete(1.0, tk.END)  # 清空显示框
        
        # 读取配置文件
        config = configparser.ConfigParser()
        config.read('config/config.ini')

        # 更新配置文件中的内容
        for entry in self.entries:
            user_input = entry.get_text()  # 使用新类的方法获取文本
            if hasattr(entry, 'config_key') and entry.config_key in config['version']:
                config['version'][entry.config_key] = user_input  # 更新配置

        # 写入更新后的配置文件
        with open('config/config.ini', 'w') as configfile:
            config.write(configfile)

        # 在显示框中显示成功信息
        self.output_text.insert(tk.END, "Success!\n")  # 显示成功信息

# 运行主程序
if __name__ == "__main__":
    root = tk.Tk()
    app = InputApp(root)
    root.mainloop() 