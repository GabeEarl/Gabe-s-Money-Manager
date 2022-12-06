import tkinter as tk

root = tk.Tk()
root.geometry("1000x1000")

Inp1 = []
Inp2 = []
Inp2 = tk.IntVar

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






def open_win():
    num1 = 0
    perc1 = 0
    perc2 = 0
    perc3 = 0

    def save_percent():
        num1 = float(e1.get())

        perc1 = float(invests.get())
        perc1 = (perc1 / 100)
        perc1 = (num1 * perc1)
        invest1.config(text=(round(perc1, 2)))

        perc2 = float(saves.get())
        perc2 = (perc2 / 100)
        perc2 = (num1 * perc2)
        save1.config(text=(round(perc2, 2)))

        perc3 = float(spends.get())
        perc3 = (perc3 / 100)
        perc3 = (num1 * perc3)
        spend1.config(text=(round(perc3, 2)))





    new= tk.Toplevel(root)
    new.geometry("1000x1000")

    canvas = tk.Canvas(new, bg='#68F088')
    canvas.place(relwidth=1, relheight=1)

    frame = tk.Frame(new, bg="#22B835")
    frame.place(relwidth=0.95, relheight=0.95, relx=0.025, rely=0.025)

    new.title("New Window")

    Calc = tk.Button(frame, text='Calculate', font=font2, command=save_percent)
    Calc.grid(column=0, row=13, padx=10, pady=10)

    Title = tk.Label(frame, text='Savings Calculator', font=font1, )
    Title.grid(column=1, row=0, padx=10, pady=10)

    Labels = tk.Label(frame, text='Please enter investment percentages: ', font=font2)
    Labels.grid(column=0, row= 2, padx=10, pady=10)

    #Credit = tk.Label(frame, text='Enter amount of credit card debt', font=font2)
    #Credit.grid(column=0, row= 3, padx=10, pady=10)
    #Credits = tk.Entry(frame, font=('Arial', 14),)
    #Credits.grid(column=1, row=3, padx=10, pady=10)\

    earn_Label = tk.Label(frame, text='Enter monthly savings: ', font=font2)
    earn_Label.grid(column=0, row=1, padx=10, pady=10)
    e1 = tk.Entry(frame, font=('Arial', 14), )
    e1.grid(column=1, row=1, padx=10, pady=10)

    invest = tk.Label(frame, text='Percentage to invest in Index 500: ', font=font2)
    invest.grid(column=0, row= 4, padx=10, pady=10)
    invests = tk.Entry(frame, font=('Arial', 14),)
    invests.grid(column=1, row=4, padx=10, pady=10)
    invest1 = tk.Label(frame, text='', font=font2)
    invest1.grid(column=2, row= 4, padx=10, pady=10)

    save = tk.Label(frame, text='Percentage to put in savings: ', font=font2)
    save.grid(column=0, row= 5, padx=10, pady=10)
    saves = tk.Entry(frame, font=('Arial', 14),)
    saves.grid(column=1, row=5, padx=10, pady=10)
    save1 = tk.Label(frame, text='', font=font2)
    save1.grid(column=2, row= 5, padx=10, pady=10)

    spend = tk.Label(frame, text='Percentage for spending money: ', font=font2)
    spend.grid(column=0, row= 6, padx=10, pady=10)
    spends = tk.Entry(frame, font=('Arial', 14),)
    spends.grid(column=1, row=6, padx=10, pady=10)
    spend1 = tk.Label(frame, text='', font=font2)
    spend1.grid(column=2, row= 6, padx=10, pady=10)




# function for taking the for loop entry data and subtracting monthly earnings from
# tried to do input validation but can only get it to work for the last entry
def total_Expense():
    total = 0
    for entries in Inp1:
        #print(int(entries.get()))
        inval(entries.get())
        total = total + int(entries.get())
        total_num.config(text=total)
        leftover = int(e1.get()) - total
        gross_num.config(text=leftover)

def inval(z):
        try:
            int(z)
        except:
            total_num.config(text='Non number detected')
            gross_num.config(text='Non number detected')
            return


 #total2 = inval(entries.get())
        #total = total + total2
        #total_num.config(text=total)



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

#invalid_num = tk.Label(frame,text='Input Valid: ', font=font2)
#invalid_num.grid(column=0,row=12, padx=10, pady=10)
#invalid_num1 = tk.Label(frame,text='', font=font2)
#invalid_num1.grid(column=1,row=12, padx=10, pady=10)

# Button to calculate everything
Calc = tk.Button(frame, text='Calculate', font=font2, command = total_Expense)
Calc.grid(column=0, row=13, padx=10, pady=10)

nope = tk.Button(frame, text='Open savings calculator', font=font2, command=lambda:[open_win(),])
nope.grid(column=1, row=14, padx=10, pady=10)

root.mainloop()