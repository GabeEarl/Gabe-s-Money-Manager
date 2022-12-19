from tkinter import *

#root window
root = Tk()
root.title('Money Manager')
root.configure(bg='#0F2830')
root.state('zoomed')


# Smaller window for color offset
frame = Frame(root, bg="#014751")
frame.place(relwidth=0.95, relheight=0.95, relx=0.025, rely=0.025)

#fonts
font1 = ('Arial', 22)
font2 = ('Arial', 18)
boldf = ('Arial bold', 22, )






# function to open new window
# function containing all of the code for the Savings calculator window
def savings_calc_win():
    num1 = 0
    perc1 = 0
    perc2 = 0
    perc3 = 0
    cc1 = 0
    # function to calculate percentages
    def save_percent():
        try:
            num1 = float(e1.get()) #taking the inputs from entry fields and putting them in variables
            cc1 = float(cc.get())
            perc1 = float(invests.get())
            perc2 = float(saves.get())
            perc3 = float(spends.get())
            num_too_high = perc1 + perc2 + perc3 #num_too_high to check if percentages are above 100
            if num_too_high > 100:
                invest1.config(text='Over 100%')
                save1.config(text='Over 100%')
                spend1.config(text='Over 100%')
                savings_display.config(text='Over 100%')
                error_window_over100()
            else:
                if num1<0 or perc1<0 or perc2<0 or perc3<0 or cc1<0: #input validation for positive numbers
                    invest1.config(text='Enter a positive number')
                    save1.config(text='Enter a positive number')
                    spend1.config(text='Enter a positive number')
                    savings_display.config(text='Enter a positive number')
                    error_window_nonpos()

                else: # function that turn numbers into percentages and then uses said percentages to calculate how much of the savings will be put into each investment
                    perc1 = (perc1 / 100)
                    perc1 = (num1 * perc1)
                    invest_amount_month = str((round(perc1, 2)))
                    invest1.config(text=('$',invest_amount_month))

                    perc2 = (perc2 / 100)
                    perc2 = (num1 * perc2)
                    #invest_amount_month = str((round(perc2, 2)))
                    save1.config(text=('$',str((round(perc2, 2)))))

                    perc3 = (perc3 / 100)
                    perc3 = (num1 * perc3)
                    spend1.config(text=('$',str((round(perc3, 2)))))

                    savings_Num = num1 - (perc1 + perc2 + perc3)
                    savings_display.config(text=('$', str((round(savings_Num, 2)))))
                    credit_Payoff()

        except ValueError: #input validation to make sure numbers are entered
            invest1.config(text='Enter number')
            save1.config(text='Enter number')
            spend1.config(text='Enter number')
            savings_display.config(text='Enter number')
            error_window_nonnum()

    def credit_Payoff(): # function for the calculation of how long the debt will take to pay off
        mon_savings = float(e1.get())
        cc2 = float(cc.get())
        debt_num = float(saves.get())
        debt_num = (debt_num / 100)
        debt_num = (mon_savings * debt_num)
        debt_month = cc2/debt_num
        if debt_month == 0:
            credit_paytime_num.config(text=' no debt!')
        else:
            credit_paytime_num.config(text=(str((round(debt_month, 2))), 'months'))

    def investment(): # function to calculate how much the investment would be worth after x number of years
        perc1 = float(invests.get())
        num1 = float(e1.get())
        y = float(invest_years.get())
        perc1 = (perc1 / 100)
        perc1 = (num1 * perc1)
        invest_amount_month = str((round(perc1, 2)))
        P = perc1 * 12
        FV = P * (((1 + ((9 / 100.0) / 1)) ** (1 * y))) # formula to calculate the investment after x years
        invest_final = str((round(FV, 2)))
        Labels2.config(text=(f'If you invest ${invest_amount_month} a month for the next year.\n  It will be worth ${invest_final},\n after {y} years.'))

    def error_window_over100(): # function to display the error message for if the percentages entered add up to over 100% in a new window
        er_win = Toplevel(root)
        er_win.geometry('600x400')
        canvas = Canvas(er_win, bg='#0F2830')
        canvas.place(relwidth=1, relheight=1)
        over_100 = Label(er_win, text='The percentages entered add up to over 100%', font=font2, bg='#00D37F', fg='black')
        over_100.pack(side=TOP)
        over_100.place(relx=0.5, rely=0.5, anchor=CENTER)
        back_Button = Button(er_win, text='Quit', font=font2, command=er_win.destroy, bg='#D2C4FB')
        back_Button.pack(side=BOTTOM)
        back_Button.place(relx=0.5, rely=0.7, anchor=CENTER)

    def error_window_nonpos(): # function to display the error message for a negative number being entered in a new window
        er_win = Toplevel(root)
        er_win.geometry('600x400')
        canvas = Canvas(er_win, bg='#0F2830')
        canvas.place(relwidth=1, relheight=1)
        over_100 = Label(er_win, text='The value entered is negative\n please enter a positive', font=font2, bg='#00D37F', fg='black')
        over_100.pack(side=TOP)
        over_100.place(relx=0.5, rely=0.5, anchor=CENTER)
        back_Button = Button(er_win, text='Quit', font=font2, command=er_win.destroy, bg='#D2C4FB')
        back_Button.pack(side=BOTTOM)
        back_Button.place(relx=0.5, rely=0.7, anchor=CENTER)

    def error_window_nonnum(): # function to display the error message for a non number being entered in a new window
        er_win = Toplevel(root)
        er_win.geometry('600x400')
        canvas = Canvas(er_win, bg='#0F2830')
        canvas.place(relwidth=1, relheight=1)
        over_100 = Label(er_win, text='The value entered was not a number\n please enter a number', font=font2, bg='#00D37F', fg='black')
        over_100.pack(side=TOP)
        over_100.place(relx=0.5, rely=0.5, anchor=CENTER)
        back_Button = Button(er_win, text='Quit', font=font2, command=er_win.destroy, bg='#D2C4FB')
        back_Button.pack(side=BOTTOM)
        back_Button.place(relx=0.5, rely=0.7, anchor=CENTER)






    # new window
    new= Toplevel(root)
    new.state('zoomed')

    # background for new window
    canvas = Canvas(new, bg='#0F2830')
    canvas.place(relwidth=1, relheight=1)

    # frame for new window
    frame = Frame(new, bg="#014751", )
    frame.place(relwidth=0.95, relheight=0.95, relx=0.025, rely=0.025)

    # frame for the right side of the page
    frame2= Frame(new,bg='#0F2830')
    frame2.place(relwidth=0.4, relheight=0.95, relx=0.575, rely=0.025, )

    # Label for the top of the right side of the screen
    Title_right = Label(frame2, text='Spending', font=boldf, bg='#FFEEB4', )
    Title_right.grid(column=1, row=0, padx=10, pady=10, sticky='w')

    # Label and entry for the amount of years for the user to invest
    Labels3 = Label(frame2, text='Enter amount of years to invest:', font=font2, bg='#00D37F', fg='black')
    Labels3.grid(column=0, row=1, padx=10, pady=10, sticky='w')
    invest_years = Entry(frame2, font=('Arial', 14), bg='#AFF8C8')
    invest_years.grid(column=1, row=1, padx=10, pady=10)

    # Label to display the outcome from the investment
    Labels2 = Label(frame2, text='', font=font2, bg='#0F2830', fg='white')
    Labels2.place(relx=0.5, rely=0.4, anchor=CENTER)


    new.title("Savings Calculator")

    # button to call the percentages function
    Calc = Button(frame, text='Calculate', font=font2, command=save_percent, bg='#D2C4FB')
    Calc.grid(column=0, row=13, padx=10, pady=10, sticky='e')

    # Button on the right
    Calc2 = Button(frame2, text='Calculate', font=font2, command=investment, bg='#D2C4FB')
    Calc2.grid(column=0, row=13, padx=10, pady=10, sticky='e')


    # Button to exit window
    back_Button = Button(frame, text='Quit', font=font2, command=new.destroy, bg='#D2C4FB')
    back_Button.grid(column=1, row=13, padx=10, pady=10)

    # Main label at top of page
    Title = Label(frame, text='Savings Calculator', font=font1, bg='#FFEEB4' )
    Title.grid(column=1, row=0, padx=10, pady=10)

    # Prompt for what the user should enter
    Labels = Label(frame, text='Enter percentages:', font=font2, bg='#00D37F')
    Labels.grid(column=0, row= 3, padx=10, pady=10, sticky='e')

    #Label and entry for totlal savings
    earn_Label = Label(frame, text='Enter monthly savings:', font=font2, bg='#00D37F')
    earn_Label.grid(column=0, row=1, padx=10, pady=10, sticky='e')
    e1 = Entry(frame, font=('Arial', 14), bg= '#AFF8C8')
    e1.grid(column=1, row=1, padx=10, pady=10)

    # Label and entry field to enter how much debt the user has
    cc_Label = Label(frame, text='Enter Debt:', font=font2, bg='#00D37F')
    cc_Label.grid(column=0, row=2, padx=10, pady=10, sticky='e')
    cc = Entry(frame, font=('Arial', 14), bg= '#AFF8C8')
    cc.grid(column=1, row=2, padx=10, pady=10)

    #Label and entry for percentage to invest in stock market
    invest = Label(frame, text='Percentage to invest in S&P 500:', font=font2,  bg='#0F2830', fg = 'white')
    invest.grid(column=0, row= 4, padx=10, pady=10, sticky='w')
    invests = Entry(frame, font=('Arial', 14), bg='#AFF8C8')
    invests.grid(column=1, row=4, padx=10, pady=10)
    invest1 = Label(frame, text='', font=font2, bg='#AFF8C8')
    invest1.grid(column=2, row= 4, padx=10, pady=10)

    #Label and entry for percentage to put in savings account
    save = Label(frame, text='Percentage to pay off Debt:', font=font2,  bg='#0F2830', fg = 'white')
    save.grid(column=0, row= 5, padx=10, pady=10, sticky='w')
    saves = Entry(frame, font=('Arial', 14), bg='#AFF8C8')
    saves.grid(column=1, row=5, padx=10, pady=10)
    save1 = Label(frame, text='', font=font2, bg='#AFF8C8')
    save1.grid(column=2, row= 5, padx=10, pady=10)

    #Label and entry for perncentage to keep as spending money
    spend = Label(frame, text='Percentage for spending money:', font=font2, bg='#0F2830', fg = 'white')
    spend.grid(column=0, row= 6, padx=10, pady=10, sticky='w')
    spends = Entry(frame, font=('Arial', 14), bg='#AFF8C8')
    spends.grid(column=1, row=6, padx=10, pady=10)
    spend1 = Label(frame, text='', font=font2, bg='#AFF8C8')
    spend1.grid(column=2, row= 6, padx=10, pady=10)

    # Label to tell the user that any left over percentage will be put into savings
    savings = Label(frame, text='Leftovers will be put in savings:', font=font2, bg='#0F2830', fg = 'white')
    savings.grid(column=0, row= 7, padx=10, pady=10, sticky='w')
    savings_display = Label(frame, text='', font=font2, bg='#AFF8C8', )
    savings_display.grid(column=2, row= 7, padx=10, pady=10)

    # Label to display how many months are left until the debt gets paid off
    credit_paytime = Label(frame, text=('Months until debt is payed:'), font=font2, bg='#0F2830', fg = 'white')
    credit_paytime.grid(column=0, row= 8, padx=10, pady=10, sticky='w')
    credit_paytime_num = Label(frame, text='', font=font2, bg='#AFF8C8', )
    credit_paytime_num.grid(column=1, row= 8, padx=10, pady=10)










# function that houses all of the code for the money manager window
def money_manager_win():
    Inp1 = []
    Inp2 = []
    perc_inp = []

    # function for taking the for loop entry data and subtracting monthly earnings from
    # tried to do input validation but can only get it to work for the last entry
    def total_Expense():
        total = 0
        for entries in Inp1: # for loop to iterate through the list of entries
            inval(entries.get())
            br = float(entries.get())
            if br < 0: # input validation to test if entries are positive and displays message and opens a window telling the user
                total_num.config(text='Enter a positive number')
                gross_num.config(text='Enter a positive number')
                error_window_negnum()
                break
            else:
                total = total + float(entries.get()) # adds the entry to the total of expenses
                leftover = float(e1.get()) - total # takes total earnings minus the total of expenses
                str(round(total, 2))
                str(round(leftover, 2))
                total_num.config(text=('$', str(total))) # changes label to show total expenses
                gross_num.config(text=('$', str(leftover))) # changes label to show left over earnings
        percentage_spent(float(total))

    def error_window_negnum(): # error window to display the error message when a negative number is entered
        er_win = Toplevel(root)
        er_win.geometry('600x400')
        canvas = Canvas(er_win, bg='#0F2830')
        canvas.place(relwidth=1, relheight=1)
        over_100 = Label(er_win, text='There was a negative number entered\n Please enter a positive number', font=font2, bg='#00D37F', fg='black')
        over_100.pack(side=TOP)
        over_100.place(relx=0.5, rely=0.5, anchor=CENTER)
        back_Button = Button(er_win, text='Quit', font=font2, command=er_win.destroy, bg='#D2C4FB')
        back_Button.pack(side=BOTTOM)
        back_Button.place(relx=0.5, rely=0.7, anchor=CENTER)

    def inval(z): # function to test that the value entered is a number, if it is then the previous function continues, if not it displays an error
        try:
            float(z)
        except:
            total_num.config(text='Enter a number')
            gross_num.config(text='Enter a number')
            error_window_nonnum1()
            return

    def error_window_nonnum1(): # function to open a new window to display the error message for a non number being entered
        er_win = Toplevel(root)
        er_win.geometry('600x400')
        canvas = Canvas(er_win, bg='#0F2830')
        canvas.place(relwidth=1, relheight=1)
        over_100 = Label(er_win, text='There was an empty space or non number entered\n Please enter a number or 0 if no number is needed', font=font2, bg='#00D37F', fg='black')
        over_100.pack(side=TOP)
        over_100.place(relx=0.5, rely=0.5, anchor=CENTER)
        back_Button = Button(er_win, text='Quit', font=font2, command=er_win.destroy, bg='#D2C4FB')
        back_Button.pack(side=BOTTOM)
        back_Button.place(relx=0.5, rely=0.7, anchor=CENTER)

    def percentage_spent(total): # function for calculating what percentage of each expense is based on total expenses
        perc_inp = []
        for entries in Inp1: # for loop to find the percentages for expenses
            cent = float(entries.get())
            pp = (cent/total) * 100
            perc_inp.append(round(pp, 2)) # appends the percent to the end of a list
        for i in range(len(perc_inp)): # for loop the length of the list of percentages that loops through and display the corresponding percentage
            indivi_perc = Label(frame2, text=(perc_inp[i], '%'), font=font2, bg='#AFF8C8')
            indivi_perc.grid(column=1, row=i + 2, padx=10, pady=10)

    # new window
    new= Toplevel(root)
    new.state('zoomed')

    # background for new window
    canvas = Canvas(new, bg='#0F2830')
    canvas.place(relwidth=1, relheight=1)

    # frame for new window
    frame = Frame(new, bg="#014751")
    frame.place(relwidth=0.5, relheight=0.95, relx=0.025, rely=0.025, )
    # frame for the right side of the window
    frame2= Frame(new,bg='#0F2830')
    frame2.place(relwidth=0.4, relheight=0.95, relx=0.575, rely=0.025, )

    new.title("Money Manager")

    # Main label at top of page
    Title = Label(frame, text='Money Manager', font=boldf, bg= '#FFEEB4',)
    Title.grid(column=1, row=0, padx=10, pady=10)
    # Label for the top of the right side of the page
    Title_right = Label(frame2, text='Spending', font=boldf, bg='#FFEEB4', )
    Title_right.grid(column=1, row=0, padx=10, pady=10)
    #Label to display the spending percentages
    spend_Label = Label(frame2, text='Spending by percentage: ', font=font2, bg='#00D37F')
    spend_Label.grid(column=0, row=1, padx=10, pady=10, sticky='e')
    # List of prompts to use in the for loop to create the labels
    prompts = ('Enter monthly rent including utilities: ',
               'Enter monthly car and health insurance: ', 'Enter price of gas each month: ',
               'Grocery expenses each month: ', 'Phone bill each month: ',
               'Pet expenses each month: ', 'Monthly Subscriptions: ')
    # List of prompts to use for the labels on the right side of the page
    prompts2 = ('Rent and Utilities: ',
               'Car and Health insurance: ', 'Gas: ',
               'Groceries: ', 'Phone biil: ',
               'Pets: ', 'Subscriptions: ')


    # for loop for labels and corresponding entry areas
    for i in range(len(prompts)):
        Labels = Label(frame, text=prompts[i], font=font2,bg = '#0F2830', fg = 'white')
        Labels.grid(column=0, row=i + 2, padx=10, pady=10, sticky='w')
        Inputs = Entry(frame, font=('Arial', 14), bg='#AFF8C8')
        Inputs.grid(column=1, row=i + 2, padx=10, pady=10)
        Inp1.append(Inputs)
    # for loop for labels on the right side of the page
    for i in range(len(prompts2)):
        Labels2 = Label(frame2, text=prompts2[i], font=font2, bg = '#0F2830', fg = 'white')
        Labels2.grid(column=0, row=i + 2, padx=10, pady=10, sticky='w')

    # label and entry for the income since it is used differently in the function
    earn_Label = Label(frame, text='Enter monthly earnings: ', font=font2, bg='#00D37F', )
    earn_Label.grid(column=0, row=1, padx=10, pady=10, sticky='e')
    e1 = Entry(frame, font=('Arial', 14), bg='#AFF8C8')
    e1.grid(column=1, row=1, padx=10, pady=10)

    # Label to show all the expenses for the month
    total_Label = Label(frame, text='Total monthly expenses: ', font=font2, bg='#00D37F', )
    total_Label.grid(column=0, row=10, padx=10, pady=10, sticky='e')
    total_num = Label(frame, text='0', font=font2, bg='#AFF8C8')
    total_num.grid(column=1, row=10, padx=10, pady=10)


    # Label to show the income after expenses have been taken out
    gross_Label = Label(frame, text='Monthly income after expenses: ', font=font2, bg='#00D37F',)
    gross_Label.grid(column=0, row=11, padx=10, pady=10, sticky='e')
    gross_num = Label(frame, text='0', font=font2, bg='#AFF8C8')
    gross_num.grid(column=1, row=11, padx=10, pady=10)

    # Button to calculate everything
    Calc = Button(frame, text='Calculate', font=font2, command=total_Expense, bg='#D2C4FB')
    Calc.grid(column=0, row=13, padx=10, pady=10)

    # Button to exit window
    back_Button = Button(frame, text='Quit', font=font2, command=new.destroy, bg='#D2C4FB')
    back_Button.grid(column=1, row=13, padx=10, pady=10)





img = PhotoImage(file='savingsnew.png') # initializing the images to use on main menu
img2 = PhotoImage(file='calculator1.png')



# all the labels and buttons for the main menu
# Money manager button on main screen that is an image
money_manage_button = Button(root, text='Money Manager', image=img2, command=money_manager_win, font='none 32 bold',  bg= '#AFF8C8', fg='black',height=350, width=380)
money_manage_button.place(relx=0.35, rely=0.45, anchor=CENTER)
# Money manager text button above the image
money_manage_button1 = Button(root, text='Money Manager', command=money_manager_win, font='none 31 bold', bg='#FFEEB4', fg='black', width=15)
money_manage_button1.place(relx=0.35, rely=0.25, anchor=CENTER)

# Savings calculator button with text above the image
savings_calc_button = Button(root, text='Savings Calculator', image = img, command=savings_calc_win,font='none 32 bold', bg= '#AFF8C8', fg='black', height=350, width=380)
savings_calc_button.place(relx=0.65, rely=0.45, anchor=CENTER)

# Savings calculator button that is an image
savings_calc_button1 = Button(root, text='Savings Calculator', command=savings_calc_win,font='none 31 bold', bg='#FFEEB4', fg='black',width=15)
savings_calc_button1.place(relx=0.65, rely=0.25, anchor=CENTER)

# label to display the text on the bottom of the main menu
explain = Label(root, text='Money Manager to calculate expenses for the month\n\nSavings Calculator to figure out what to do with leftover savings', font=font1, bg='#0F2830', fg='white', width=50, )
explain.place(relx=.5, rely=.8, anchor=CENTER)

# button to quit the main menu
back_Button = Button(frame, text='Quit', font=font2, command=root.destroy, bg='#D2C4FB')
back_Button.place(relx=.5, rely=.6, anchor=CENTER)

#run window
root.mainloop()