from tkinter import *

icon = './icon.ico'


def two_way_zeroing(c1, c2):
    probability_sum = 1 / c1 + 1 / c2
    margin = probability_sum - 1
    c1_new = c1 * (1 + margin)
    c2_new = c2 * (1 + margin)
    call_result_window_2(margin, c1_new, c2_new)

    
def three_way_zeroing(c1, c2, c3):
    probability_sum = 1 / c1 + 1 / c2 + 1 / c3
    margin = probability_sum - 1
    c1_new = c1 * (1 + margin)
    c2_new = c2 * (1 + margin)
    c3_new = c3 * (1 + margin)
    call_result_window_3(margin, c1_new, c2_new, c3_new)


def call_result_window_2(margin, c1_new, c2_new):
    result_window = Toplevel()
    result_window.title('Результат')
    result_window.iconbitmap(icon)
    lbl1 = Label(result_window, text='Маржа БК: ' + str(format(margin * 100, '.1f')) + '%')
    lbl2 = Label(result_window, text='Исправленные коэффициенты:  ' + str(format(c1_new, '.2f')) + '  ' + str(format(c2_new, '.2f')))
    lbl3 = Label(result_window, text='Новая маржа: ' + str(format(abs((1 / c1_new + 1 / c2_new) - 1) * 100, '.1f')) + '%')
    btn = Button(result_window, text='OK', width=20, command=lambda: result_window.destroy())
    lbl1.pack(pady=10)
    lbl2.pack(pady=10)
    lbl3.pack(pady=10)
    btn.pack(pady=10)
    
    
def call_result_window_3(margin, c1_new, c2_new, c3_new):
    result_window = Toplevel()
    result_window.title('Результат')
    result_window.iconbitmap(icon)
    lbl1 = Label(result_window, text='Маржа БК: ' + str(format(margin * 100, '.1f')) + '%')
    lbl2 = Label(result_window, text='Исправленные коэффициенты:  ' + str(format(c1_new, '.2f')) + '  ' + str(format(c2_new, '.2f')) + '  ' + str(format(c3_new, '.2f')))
    lbl3 = Label(result_window, text='Новая маржа: ' + str(format(abs((1 / c1_new + 1 / c2_new + 1 / c3_new) - 1) * 100, '.1f')) + '%')
    btn = Button(result_window, text='OK', width=20, command=lambda: result_window.destroy())
    lbl1.pack(pady=10)
    lbl2.pack(pady=10)
    lbl3.pack(pady=10)
    btn.pack(pady=10)


def two_way_button_action():
    two_way_window = Toplevel()
    two_way_window.title('Ввод коэффициентов')
    two_way_window.geometry('300x150')
    two_way_window.iconbitmap(icon)
    lbl = Label(two_way_window, text='Введите коэффициенты')
    frame = Frame(two_way_window)
    entry1 = Entry(frame, width=10, justify='center')
    entry2 = Entry(frame, width=10, justify='center')
    btn = Button(two_way_window, text='Пересчитать коэффициенты', command=lambda: two_way_zeroing(float(entry1.get()), float(entry2.get())))
    lbl.pack(side=TOP, pady=15)
    frame.pack()
    entry1.pack(side=LEFT, padx=20, pady=10)
    entry2.pack(side=RIGHT, padx=20, pady=10)
    btn.pack(side=BOTTOM, pady=10)
    two_way_window.mainloop()
    
    
def three_way_button_action():
    three_way_window = Toplevel()
    three_way_window.title('Ввод коэффициентов')
    three_way_window.geometry('300x150')
    three_way_window.iconbitmap(icon)
    lbl = Label(three_way_window, text='Введите коэффициенты')
    frame = Frame(three_way_window)
    entry1 = Entry(frame, width=10, justify='center')
    entry2 = Entry(frame, width=10, justify='center')
    entry3 = Entry(frame, width=10, justify='center')
    btn = Button(three_way_window, text='Пересчитать коэффициенты', command=lambda: three_way_zeroing(float(entry1.get()), float(entry2.get()), float(entry3.get())))
    lbl.pack(side=TOP, pady=15)
    frame.pack()
    entry1.pack(side=LEFT, padx=20, pady=10)
    entry2.pack(side=LEFT, padx=20, pady=10)
    entry3.pack(side=RIGHT, padx=20, pady=10)
    btn.pack(side=BOTTOM, pady=10)
    three_way_window.mainloop()
    

def main():
    root = Tk()  
    root.title('Обнуление маржи')
    root.geometry('300x100')
    root.iconbitmap(icon)
    lbl = Label(root, text='Выберите вид cобытия')  
    btn1 = Button(root, text='2 исхода (12)', command=two_way_button_action)
    btn2 = Button(root, text='3 исхода (1X2)', command=three_way_button_action) 
    lbl.pack(side=TOP, pady=10)  
    btn1.pack(side=LEFT, padx=30, pady=10)
    btn2.pack(side=RIGHT, padx=30, pady=10)  
    root.mainloop()


if __name__ == '__main__':
    main()

