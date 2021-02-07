import tkinter as tk
window = tk.Tk()
window.title("scale test")
window.geometry('500x500')
maxS = 100
def print_selection(v):      #v是传入s表单的选择值
    intA = int(v)
    labelA.config(text = 'a = ' + v)
    labelB.config(text = "b = " + str(maxS - intA))
    labelC.config(text = "b - a = " + str(maxS - 2 * intA))
    labelD.config(text = "b * a = " + str(intA * (maxS - intA)))

s = tk.Scale(window, label='最值问题演示：a + b = ' + str(maxS), from_=1, to=maxS, orient=tk.HORIZONTAL, length=5 * maxS, showvalue=1, tickinterval=9, resolution=1, command=print_selection)
'''
设置一个尺度表单，
orient是方向(HORIZONTAL是横向)，
showvalue是实时显示选中的值（布尔型，0就是false），
tickinterval是表单划分尺度,
resolution是精度（1是精确到整数）
'''
s.pack()

labelA = tk.Label(window, bg='yellow', width=20, height=2, text='empty')
labelA.pack()
labelB = tk.Label(window, bg='yellow', width=20, height=2, text='empty')
labelB.pack()
labelC = tk.Label(window, bg='yellow', width=20, height=2, text='empty')
labelC.pack()
labelD = tk.Label(window, bg='yellow', width=20, height=2, text='empty')
labelD.pack()
window.mainloop()