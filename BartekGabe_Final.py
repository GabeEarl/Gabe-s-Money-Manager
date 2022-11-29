import tkinter as tk
import os

root = tk.Tk()

font1 = ('Arial', 22)
font2 = ('Arial', 18)

canvas = tk.Canvas(root, height=800, width=800, bg='#68F088')
canvas.pack()

frame = tk.Frame(root, bg="#22B835")
frame.place(relwidth=0.95, relheight=0.95, relx=0.025, rely=0.025)

Title = tk.Label(frame, text='Money Manager', font=font1, )
Title.grid(column=1,row=0, padx=10, pady=10)

Weekly = tk.Label(frame,text='Enter monthly earnings: ', font=font2)
Weekly.grid(column=0, row=1, padx=10, pady=10)
e1 = tk.Entry(frame, font=('Arial', 14),)
e1.grid(column=1, row=1, padx=10, pady=10)

Rent = tk.Label(frame,text='Enter monthly rent including utilities: ', font=font2)
Rent.grid(column=0, row=2, padx=10, pady=10)
e2 = tk.Entry(frame, font=('Arial', 14),)
e2.grid(column=1, row=2, padx=10, pady=10)

carIns = tk.Label(frame,text='Enter monthly car and health insurance: ', font=font2)
carIns.grid(column=0, row=3, padx=10, pady=10)
e3 = tk.Entry(frame, font=('Arial', 14),)
e3.grid(column=1, row=3, padx=10, pady=10)

Gas = tk.Label(frame,text='Enter price of gas each month: ', font=font2)
Gas.grid(column=0, row=4, padx=10, pady=10)
e4 = tk.Entry(frame, font=('Arial', 14),)
e4.grid(column=1, row=4, padx=10, pady=10)

Grocery = tk.Label(frame,text='Grocery expenses each month: ', font=font2)
Grocery.grid(column=0, row=5, padx=10, pady=10)
e5 = tk.Entry(frame, font=('Arial', 14),)
e5.grid(column=1, row=5, padx=10, pady=10)

Phone = tk.Label(frame,text='Phone bill each month: ', font=font2)
Phone.grid(column=0, row=6, padx=10, pady=10)
e6 = tk.Entry(frame, font=('Arial', 14),)
e6.grid(column=1, row=6, padx=10, pady=10)

Pet = tk.Label(frame,text='Pet expenses each month: ', font=font2)
Pet.grid(column=0, row=7, padx=10, pady=10)
e7 = tk.Entry(frame, font=('Arial', 14),)
e7.grid(column=1, row=7, padx=10, pady=10)

Sub = tk.Label(frame,text='Monthly Subscriptions: ', font=font2)
Sub.grid(column=0, row=8, padx=10, pady=10)
e8 = tk.Entry(frame, font=('Arial', 14),)
e8.grid(column=1, row=8, padx=10, pady=10)

CC = tk.Label(frame,text='Monthly credit card payment: ', font=font2)
CC.grid(column=0, row=9, padx=10, pady=10)
e9 = tk.Entry(frame, font=('Arial', 14),)
e9.grid(column=1, row=9, padx=10, pady=10)

afterExp = tk.Label(frame,text='Total after expenses: ', font=font2)
afterExp.grid(column=0, row=10, padx=10, pady=10)
expNum = tk.Label(frame,text='', font=font2)
expNum.grid(column=1, row=10, padx=10, pady=10)

root.mainloop()