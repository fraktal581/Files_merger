import pandas as pd
import fileinput
import glob, os
import time
import traceback
import tkinter as tk
from tkinter import *
from tkinter import ttk 
from tkinter import filedialog as fd



start_time = time.time()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title = 'Выберите папку'
        self.geometry('300x150')
        #self.progressbar = ttk.Progressbar(orient='horizontal', length=200, value=len(list_files)).pack(pady=5)
        #self.btn_dir = tk.Button(self, text='Указать путь', command=self.choose_dir_to_open)
        #self.btn_dir.pack(padx=60, pady=10)
        
    def choose_dir_to_open(self):
        files_dir = fd.askdirectory(title='Открыть папку', initialdir="/")
        if files_dir:
            print(files_dir)
            return files_dir
    def chose_dir_to_save(self):
        save_dir = fd.asksaveasfilename(title="Куда сохранить файл?")
        if save_dir:
            print(save_dir)
            
            return save_dir
        
value_var = IntVar()
def compile_new_txt_file(list):

    if list:
        # открываем список файлов 'list_files' и новый файл для записи
        with fileinput.FileInput(files=list_files, encoding='utf-8-sig', mode= "r", errors='ignore') as fr, open(new_file, 'w', encoding='utf-8') as fw:
            
                # построчное чтение данных
            for line in fr:
                try:
                    # запись в файл
                    fw.write(line)
                    
                # Обработчик ошибок при рекодировке
                # если получаем не читаемый символ
                except UnicodeEncodeError as u_ex:
                    # получаем позицию из аргументов объекта ошибки
                    position = u_ex.args[2]
                    # слайсируем строку для получения нечитаемого символа
                    char = line[position:position+1]
                    # производим замену символа
                    # пока просто опускаем, в дальнейшем нужно продумать замену на читаемый аналог
                    n_line = line.replace(char, '')
                    line = n_line
                    # запись в файл
                    fw.write(n_line)

if __name__ == "__main__":
    app = App()
    
    # путь к каталогу текстовых файлов
    path = app.choose_dir_to_open()
    #print(path)
    save_path = app.chose_dir_to_save()
    #print(save_path)
    
    # паттерн поиска файлов по расширению
    pattern = '*.txt'
    
    # переменная-маска для получения списка всех файлов нужного расширения
    global_path = os.path.join(path, pattern)
    #print(global_path)
    #print(type(global_path))
    # список файлов в каталоге
    list_files = glob.glob(global_path)
    
    # расширение нового файла устанавливаем как .all для избежания рекурсии
    new_file = save_path
    compile_new_txt_file(list_files)
    
    end_time = time.time()
    running_time = end_time - start_time
    #print(f"Время выполнения: {running_time}")
    app.mainloop

