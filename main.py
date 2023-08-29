import csv
import subprocess
import tkinter as tk
from ttkbootstrap import Style
from tkinter import Canvas

style = Style(theme='yeti')


with open(r"D:\KEAL\Desktop\pytools\saplogon.csv", "r") as f:
    reader = csv.DictReader(f, delimiter="\t")
    data = [row for row in reader]

# 创建主窗口
root = style.master
root.title("选择你要登录的系统:")
root.configure(bg=style.colors.get("white"))
# root.geometry("800x600")

# 创建画布并添加背景图
canvas = Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)
bg_image = tk.PhotoImage(file=r"D:\KEAL\Desktop\pytools\backpic.png")
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# 创建多个按钮，每个按钮对应数据表中的一行数据
i=0
for row in data:
    # button = tk.Button( root, text=row["Name"], padx=10, pady=5, width=30, underline=False,
    #                     command=lambda r=row: show_data( r ) )
    button = tk.Button(root, text=row["Name"], width=30, bg=style.colors.get("primary"), 
                    fg=style.colors.get("white"), font=("TkDefaultFont", 15), 
                    command=lambda r=row: show_data(r),
                    highlightthickness=0,    # Remove border when not selected
                    bd=0,   # Remove border to achieve rounded corner
                    relief=tk.RIDGE,    # Add relief to create a raised button effect
                    borderwidth=5,    # Increase borderwidth to make button bigger
                    )
    # button.pack(pady=5)
    button.place( x=250, y=40 + i * 40 )
    i+=1
def show_data(row):
    path = r"C:\Program Files\SAP\FrontEnd\SapGui\sapshcut.exe"
    conn = "-user={} -pw={} -language=1 -SYSTEM={} -CLIENT={} -sysname={} -maxgui" \
        .format(row["Account"], row["Password"], row["System"], row["Client"], row["Sysname"])
    subprocess.Popen(path + " " + conn)

# 进入主循环
root.mainloop()