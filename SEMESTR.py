import datetime #импортируем библиотеку datetime для обработки времени и даты
import calendar #импортируем библиотеку calendar для работы с днями недели
import os #ввел данную библиотеку для использования команды очистки консоли
from tkinter import * 
from tkinter.ttk import Radiobutton  
from tkinter import messagebox

#Переменные базовых констант, за начало берется трариф брокера ВТБ "Мой Онлайн"
ndfl_13 = 0.13
ndfl_35 = 0.35
KomBrok = 0.0005
KomBir = 0.0001

#Параметры маржинальной торговли
KomLong = 0.000461 #занять деньги в рублях («длинная» позиция) — 16,8% годовых (ВТБ)
KomShort = 0.00036 #занять ценные бумаги («короткая» позиция) — 13,0% годовых (ВТБ)

def par():
    global ndfl_13, ndfl_35, KomBrok, KomBir, KomLong, KomShort
    new = Toplevel(window)
    new.title('Параметры констант')
    new.geometry('300x300')
    
    Label(new, text='Ставка НДФЛ-13: 13%', padx=10, pady=10).grid(row=0,column=0)
    Label(new, text='Ставка НДФЛ-35: 35%', padx=10, pady=10).grid(row=1,column=0)

def clicked_bonds():
    messagebox.showinfo('Облигации', 'Вы выбрали облигации')
    

def clicked_stocks():
    messagebox.showinfo('Акции', 'Вы выбрали акции')
    
def clicked_founds():
    messagebox.showinfo('Фонды', 'Вы выбрали фонды')
    
window = Tk()  
window.title("Мой инвестиционный портфель 1.0 (release 01.12.2020)")  
window.geometry('270x30')
menu = Menu(window)  
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Новый')  
new_item.add_separator()  
new_item.add_command(label='Параметры констант', command = par)  
menu.add_cascade(label='Файл', menu=new_item)  
window.config(menu=menu)    
Bonds = Radiobutton(window, text='Облигация', value=1, command = clicked_bonds)  
Stocks = Radiobutton(window, text='Акция', value=2, command = clicked_stocks)  
Founds = Radiobutton(window, text='ETF/ПИФ (Фонды)', value=3, command = clicked_founds)  
Bonds.grid(column=0, row=0)  
Stocks.grid(column=2, row=0)  
Founds.grid(column=4, row=0)  

window.mainloop()