from tkinter import *

# Create a window
root = Tk()
root.geometry("600x600")
root.title('Currency Converter')
root.configure(background='#3E464A')

Label(root, text='CURRENCY CONVERTER', font='arial 13 bold', fg='white', bg='#3A323A').pack()

my_num = DoubleVar()  # Changed IntVar to DoubleVar to handle decimal numbers
Label(root, text='Enter amount in Dollars', font='arial 20 bold', fg='#3190C7', bg='#3A323A').pack()
Entry(root, width=20, textvariable=my_num).pack()

result_label = Label(root, text='', font='arial 20 bold', fg='white', bg='#5D5863')
result_label.pack(padx=10)


def convert_rand():
    try:
        here = my_num.get()
        final = here * 15.41
        result_label.config(text=('R ' + str(final)), fg='red')
    except:
        result_label.config(text='Invalid input', fg='red')


def convert_ero():
    try:
        here = my_num.get()
        final = here * 0.8411
        result_label.config(text=('EUR ' + str(final)), fg='#84F22F')
    except:
        result_label.config(text='Invalid input', fg='red')


def convert_nzd():
    try:
        here = my_num.get()
        final = here * 1.442
        result_label.config(text=('NZD ' + str(final)), fg='white')
    except:
        result_label.config(text='Invalid input', fg='red')


def convert_jpy():
    try:
        here = my_num.get()
        final = here * 103.75
        result_label.config(text=('JPY ' + str(final)), fg='green')
    except:
        result_label.config(text='Invalid input', fg='red')


Button(root, text='Convert to Rands', width=12, bg='#5087A0', command=convert_rand).pack()
Button(root, text='Convert to EURO', width=12, bg='#5087A0', command=convert_ero).pack()
Button(root, text='Convert to NZD', width=12, bg='#5087A0', command=convert_nzd).pack()
Button(root, text='Convert to JPY', width=12, bg='#5087A0', command=convert_jpy).pack()


# Function for clearing the Entry field
def clear():
    my_num.set(0)
    result_label.config(text=' ')


def exit_app():
    root.destroy()


Button(root, text='Clear', bg='red', fg='blue', command=clear).pack(pady=5)
Button(root, text='Exit', bg='red', fg='blue', command=exit_app).pack(pady=5)

root.mainloop()
