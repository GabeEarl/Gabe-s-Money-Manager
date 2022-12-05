import tkinter as tk

root = tk.Tk()
root.geometry("1000x1000")

Inp1 = []
Inp2 = []

font1 = ('Arial', 22)
font2 = ('Arial', 18)

# Window that holds everything
canvas = tk.Canvas(root, bg='#68F088')
canvas.place(relwidth=1,relheight=1)

# Smaller window for color offset
frame = tk.Frame(root, bg="#22B835")
frame.place(relwidth=0.95, relheight=0.95, relx=0.025, rely=0.025)

# Applications name
Title = tk.Label(frame, text='Money Manager', font=font1, )
Title.grid(column=1,row=0, padx=10, pady=10)

# function for taking the for loop entry data and subtracting monthly earnings from
# tried to do input validation but can only get it to work for the last entry
def total_Expense():
    total = 0
    cnun = 0
    for entries in Inp1:
        try:
            int(entries.get())
            total = total + int(entries.get())
            total_num.config(text=total)
        except ValueError:
            total_num.config(text='Not a number')
    try:
        int(entries.get())
        leftover = int(e1.get()) - total
        gross_num.config(text=leftover)
    except ValueError:
        total_num.config(text='Not a number')

# prompts for the for loop to display as labels
prompts = ('Enter monthly rent including utilities: ',
           'Enter monthly car and health insurance: ', 'Enter price of gas each month: ',
           'Grocery expenses each month: ', 'Phone bill each month: ',
           'Pet expenses each month: ', 'Monthly Subscriptions: ',
           'Monthly credit card payment: ')

# for loop for labels and corresponding entry areas
for i in range(len(prompts)):
    Labels = tk.Label(frame, text=prompts[i], font=font2)
    Labels.grid(column=0, row= i +2, padx=10, pady=10)
    Inputs = tk.Entry(frame, font=('Arial', 14),)
    Inputs.grid(column=1, row=i+2, padx=10, pady=10)
    Inp1.append(Inputs)

# label and entry for the income since it is used differently in the function
earn_Label = tk.Label(frame,text='Enter monthly earnings: ', font=font2)
earn_Label.grid(column=0,row=1, padx=10, pady=10)
e1 = tk.Entry(frame, font=('Arial', 14),)
e1.grid(column=1, row=1, padx=10, pady=10)

# Label to show all the expenses for the month
total_Label = tk.Label(frame,text='Total monthly expenses: ', font=font2)
total_Label.grid(column=0,row=10, padx=10, pady=10)
total_num = tk.Label(frame,text='', font=font2,)
total_num.grid(column=1,row=10, padx=10, pady=10)

# Label to show the income after expenses have been taken out
gross_Label = tk.Label(frame,text='Monthly income after expenses: ', font=font2)
gross_Label.grid(column=0,row=11, padx=10, pady=10)
gross_num = tk.Label(frame,text='', font=font2)
gross_num.grid(column=1,row=11, padx=10, pady=10)

# Button to calculate everything
Calc = tk.Button(frame, text='Calculate', font=font2, command=total_Expense)
Calc.grid(column=0, row=12, padx=10, pady=10)

root.mainloop()