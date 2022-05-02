from tkinter import *

# create window
window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=50)

# text labels
label1 = Label(text="Miles")
label2 = Label(text="is equal to")
label3 = Label(text="Km")
label4 = Label(text=0)

# label positioning
label1.grid(column=2, row=0)
label2.grid(column=0, row=1)
label3.grid(column=2, row=1)
label4.grid(column=1, row=1)

# entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)


# button function, gets input from entry and converts it using formula, rounds to 2 places
def calc_to_kilo():
    label4.config(text=round(float(miles_input.get()) * 1.609344, 2))


# button
button = Button(text="Calculate", command=calc_to_kilo)
button.grid(column=1, row=2)

window.mainloop()
