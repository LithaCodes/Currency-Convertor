from tkinter import *

# Create a window
root = Tk()
root.geometry("600x600")
root.title('Weather App')
root.configure(background='#3E464A')

heading = Label(root, text='CURRENCY CONVERTER', font='arial 13 bold', fg='white', bg='#3A323A').pack()

my_num = IntVar()
entry_box = Label(root, text='Enter amount in Dollars', font='arial 20 bold', fg='#3190C7', bg='#3A323A').pack()
entry_box = Entry(root, width=20, textvariable=my_num).pack()


def convert_rand():
    here = my_num.get()
    final = here * 15.41
    lab = Label(root, text=('R ' + str(final)), font='arial 20 bold', fg='red', bg='#5D5863').pack(padx=10)


btn1 = Button(root, text='Convert to Rands', width=12, bg='#5087A0', command=convert_rand).pack()


def convert_uro():
    here = my_num.get()
    final = here * 0.8411
    lab = Label(root, text=('EUR ' + str(final)), font='arial 20 bold', fg='#84F22F', bg='#5D5863').pack()


btn1 = Button(root, text='Convert to EURO', width=12, bg='#5087A0', command=convert_uro).pack()


def convert_nzd():
    here = my_num.get()
    final = here * 1.442
    lab = Label(root, text=('NZD ' + str(final)), font='arial 20 bold', fg='white', bg='#5D5863').pack()


btn1 = Button(root, text='Convert to NZD', width=12, bg='#5087A0', command=convert_nzd).pack()


def convert_jpy():
    here = my_num.get()
    final = here * 103.75
    lab = Label(root, text=('JPY ' + str(final)), font='arial 20 bold', fg='green', bg='#5D5863').pack(padx=20)


btn1 = Button(root, text='Convert to EURO', width=12, bg='#5087A0', command=convert_jpy).pack()


# Function for clearing the Entry field
def clear():
    entry_box.delete(0, END)


btn2 = Button(root, text='Clear', bg='red', fg='blue', command=clear).place(x=450, y=300)
root.mainloop()