
import tkinter
from tkinter import filedialog
import os

def file_select():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Выберите файл', filetypes=(('Текстовый файл', '.txt'),
                                                                                            ('Все файлы', '*')))
    text['text'] = text['text'] + filename
    os.startfile(filename)

window = tkinter.Tk()
window.title('Проводник')
window.geometry('450x150+500+300')
window.resizable(False, False)
window.configure(background='silver')
window.attributes('-toolwindow', True)
window.attributes('-alpha', 0.8)
text = tkinter.Label(window, text='Файл: ', height=5, width=65, background='gray', foreground='white')
text.grid(column=1, row=1)
button_select = tkinter.Button(window, text='Выбрать файл', width=20, height=3, background='gray', foreground='white',
                            command=file_select)
button_select.grid(column=1, row=2, pady=5)
window.mainloop()