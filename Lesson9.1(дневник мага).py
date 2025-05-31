# импортируем нужную библиотеку для работы с оконными приложениями
import tkinter
from tkinter import filedialog



# создание нового файла
def file_new():
    save_or_not = tkinter.Tk()
    save_or_not.geometry("150x70")
    save_or_not.resizable(False, False)
    save_or_not.grid_columnconfigure(0, minsize=75)
    save_or_not.grid_columnconfigure(1, minsize=75)

    saving_label = tkinter.Label(save_or_not, text="Save file?")
    saving_label.grid(columnspan=2)

    def without_saving():
        save_or_not.destroy()
        global text
        text.delete("1.0", tkinter.END)
    
    def saving():
        file_save()
        save_or_not.destroy()
        global text
        text.delete("1.0", tkinter.END)

    yes_button = tkinter.Button(save_or_not, text="Yes", command=saving, width=8)
    no_button = tkinter.Button(save_or_not, text="No", command=without_saving, width=8)
    yes_button.grid(column=0, row=1)
    no_button.grid(column=1, row=1)



# открытие файла
def file_open():
    file_name = filedialog.askopenfilename(
        initialdir="/",
        title="Open file",
        filetypes=(("Text documents", "*.txt"), ("All files", "*.*"))
    )
    if(file_name):
        with open(file_name, 'r') as f:
            text_open = f.read()
        text.delete("1.0", tkinter.END)
        text.insert(tkinter.END, text_open)



# сохранение файла
def file_save():
    file_name = filedialog.asksaveasfilename(
        initialdir="/",
        title="Select file",
        defaultextension="*.txt",
        filetypes=(("Text documents", "*.txt"), ("All files", "*.*"))
    )
    if(file_name):
        with open(file_name, 'w') as f:
            text_save = text.get(1.0, tkinter.END).strip()
            f.write(text_save)



# выход с файла
def file_exit():
    root.destroy()



# дополнительные функции 
def help_function():
    help_window = tkinter.Tk()
    help_window.geometry("300x70")
    help_window.resizable(False, False)

    help_label = tkinter.Label(
        help_window,
        text="Link to instruction\nhttps://www.wikihow.com/Use-Notepad"
    )
    help_label.pack()

    def back():
        help_window.destroy()

    back_button = tkinter.Button(help_window, text="Back", command=back, width=10)
    back_button.pack()



# страница "о нас"
def about():
    about_window = tkinter.Tk()
    about_window.geometry("300x70")
    about_window.resizable(False, False)

    about_label = tkinter.Label(about_window, text="IT STEP\nThanks for using")
    about_label.pack()

    def back():
        about_window.destroy()

    back_button = tkinter.Button(about_window, text="Back", command=back, width=10)
    back_button.pack()



# основные параметры и запуск программы
root = tkinter.Tk()
root.geometry("600x400")
root.title("Magician's Diary")

root.iconbitmap("Note.ico")

root.minsize(200, 100)
root.maxsize(1920, 1080)



# меню
menu = tkinter.Menu(root)
root.config(menu=menu)



# файл меню
file_menu = tkinter.Menu(menu, tearoff=0)
file_menu.add_command(label="New", command=file_new)
file_menu.add_command(label="Open", command=file_open)
file_menu.add_command(label="Save as", command=file_save)
file_menu.add_command(label="Exit", command=file_exit)
menu.add_cascade(label="File", menu=file_menu)



# вспомогательное окно
help_menu = tkinter.Menu(menu, tearoff=0)
help_menu.add_command(label="Help", command=help_function)
help_menu.add_command(label="About", command=about)
menu.add_cascade(label="Help", menu=help_menu)



# редактор текст
text = tkinter.Text(root)
text.pack(expand=tkinter.YES, fill=tkinter.BOTH)



# запустить приложение
root.mainloop()