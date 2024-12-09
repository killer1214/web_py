import tkinter as tk

class LabeledEntry:
    def __init__(self, master, label_text):
        self.frame = tk.Frame(master)
        self.label = tk.Label(self.frame, text=label_text)
        self.label.pack(side=tk.LEFT, padx=5, pady=5)
        self.entry = tk.Entry(self.frame)
        self.entry.pack(side=tk.RIGHT, padx=5, pady=5)
        self.frame.pack()

    def get_text(self):
        return self.entry.get()

    @classmethod
    def create(cls, master, label_text):
        """创建一个新的 LabeledEntry 实例"""
        return cls(master, label_text) 